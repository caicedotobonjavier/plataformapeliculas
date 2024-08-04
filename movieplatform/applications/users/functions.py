import random
#
import string
#
import os.path
from email.mime.text import MIMEText

from google.oauth2 import service_account

import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def send_mail_google(codigo, nombre, email):
    creds = None
    # El archivo token.json almacena los tokens de acceso y actualización del usuario, y se crea automáticamente 
    # cuando se completa el flujo de autorización por primera vez
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        service = build('gmail', 'v1', credentials=creds)
            
        new_mail(creds, codigo, nombre, email)
        
    # Si no hay credenciales válidas disponibles, permite que el usuario inicie sesión
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:

            flow = InstalledAppFlow.from_client_secrets_file('credenciales.json', SCOPES)
            
            creds = flow.run_local_server(
                access_type='offline',
                prompt=None,
                login_hint='citasmedicascardiologia@gmail.com'
            )

            with open('token.json', 'w') as token:
                token.write(creds.to_json())
            
            new_mail(creds, codigo, nombre, email)



def new_mail(creds, codigo, nombre, email):
    service = build('gmail', 'v1', credentials=creds)
            
    message = MIMEText(f"""Confirmacion de correo,
        \nCordial saludo usaurio : {nombre}.
        \nSe registro a nuestra plaforma de pelciulas con el correo {email}
        \nSu codigo para activar la cuenta es : {codigo}
        \nUrl de activacion http//.
        \nSaludos.""")
    message['to'] = email
    message['subject'] = 'Activacion de cuenta'
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message')
    except HttpError as error:
        print(F'******** ocurrio un error****: {error}')
        message = None
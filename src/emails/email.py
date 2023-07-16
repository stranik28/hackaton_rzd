import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from celery import Celery
import config as env

celery = Celery("emails", broker=f"redis://@redis:6379/0")

smtp_server = env.SMTP_SERVER
smtp_port = env.SMTP_PORT
smtp_username = env.SMTP_USERNAME
smtp_password = env.SMTP_PASSWORD

@celery.task
def send_notification(to, departure, destenation):

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to
    msg['Subject'] = f'Рекомендуемая цена отклонилась сильно от фактической'

    message = f'Цена на напрваление от {departure} до {destenation} сильно отклонилась, пожалуйста ознакомтесь с отчетом '
    msg.attach(MIMEText(message))

    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(smtp_username, smtp_password)
    smtp_connection.sendmail(
        smtp_username, to, msg.as_string())
    smtp_connection.quit()
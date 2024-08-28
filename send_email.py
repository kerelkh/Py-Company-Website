import os
from dotenv import load_dotenv
import smtplib
import ssl
import certifi

load_dotenv()


def send_email(sender, raw_message, topic):
    host = "smtp.gmail.com"
    port = 465

    email = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    sender = sender.strip()
    topic = topic.strip()
    body_message = f"""
        From: {sender}
        Topic: {topic}
        {raw_message}
    """
    message = f"""\
Subject: New user from {sender}
From: {sender}
{body_message}
"""
    context = ssl.create_default_context(cafile=certifi.where())

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
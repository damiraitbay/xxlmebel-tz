import os
from dotenv import load_dotenv

load_dotenv()

# Значение по умолчанию для Docker Compose
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://postgres:postgres@db:5432/furniture'
)

# SMTP для MailHog (имитация отправки писем)
SMTP_HOST = os.getenv('SMTP_HOST', 'mailhog')
SMTP_PORT = int(os.getenv('SMTP_PORT', '1025'))
MAIL_FROM = os.getenv('MAIL_FROM', 'noreply@xxlmebel.local')
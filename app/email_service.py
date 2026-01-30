"""Имитация отправки email через SMTP (MailHog в dev)."""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import SMTP_HOST, SMTP_PORT, MAIL_FROM


def send_order_confirmation(to_email: str, order_id: int, total_price: float) -> bool:
    """
    Отправляет письмо-подтверждение заказа на указанный email.
    В dev письмо попадает в MailHog (не уходит в интернет).
    """
    subject = f"Подтверждение заказа #{order_id}"
    body = (
        f"Здравствуйте!\n\n"
        f"Ваш заказ №{order_id} принят.\n"
        f"Сумма заказа: {total_price:.2f} ₽\n\n"
        f"Спасибо за заказ!\n"
        f"XXL Мебель"
    )
    return send_email(to_email=to_email, subject=subject, body=body)


def send_email(to_email: str, subject: str, body: str) -> bool:
    """Отправка письма через SMTP (MailHog)."""
    msg = MIMEMultipart()
    msg["From"] = MAIL_FROM
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.sendmail(MAIL_FROM, to_email, msg.as_string())
        return True
    except Exception as e:
        # В dev не падаем — письмо просто не отправится в MailHog
        print(f"SMTP send failed: {e}")
        return False

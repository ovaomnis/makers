from django.core.mail import send_mail

def send_code(email: str, code: str):
    send_mail(
        subject='[Cinema] requested code',
        message=f"""
        Code:
        {code}
        """,
        recipient_list=[email],
        from_email='no-replay@noreplay.com'
    )
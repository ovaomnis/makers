from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    message = f'''
    You successfully created account on our site
    This is you activation code is here:
    {activation_code}
    '''
    send_mail('Account activation [No-Reply]', message, ['test@gmail.com'], [email])

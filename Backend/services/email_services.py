from flask import Mail, Message

mail = Mail()

def send_verification_email(email, token)
text = Message("Email Verification", sender="your_email@gmail.com", recipients=[email])
text.body = "Please click on the link to verify your email: http://127.0.
verification_url = f"http://yourdomain.com/verify-email/{token}"
mail.send(text)

def send_reset_email(email, token)
text = Message(
    "Password Reset", sender="your_email@gmail.com", recipients=[email])
    reset_url = f"http://yourdomain.com/reset-password/{token}"
    msg.body = f"Click the following link to reset your password: {reset_url}"
    mail.send(msg)
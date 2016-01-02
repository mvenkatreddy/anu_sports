from django.core.mail import send_mail

def send_mail_admin(message, email):
	subject = ["contact"]
	recipients = ["gvtrahul@gmail.com", ]
	return send_mail(subject, message, email, recipients)

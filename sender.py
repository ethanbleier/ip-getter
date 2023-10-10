#!/usr/bin/python3

import smtplib
import ip_getter
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(ip_address, to_email):
	from_email = 'ebleier4@gmail.com'
	email_password = 'wqcj rgdk uhga xiee'

	subject = 'working!'
	message = f'ip: {ip_address}'

	msg = MIMEMultipart()
	msg['From'] = from_email
	msg['To'] = to_email
	msg['Subject'] = subject
	msg.attach(MIMEText(message, 'plain'))

	try: 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(from_email, email_password)
		server.sendmail(from_email, to_email, msg.as_string())
		server.quit()
		print('nice.')
	except Exception as e:
		print(f'Error {str(e)}')


if __name__ == "__main__":
	ip_address = ip_getter.get_ip()
	if ip_address:
		to_email = 'ebleier@csumb.edu'
		send_email(ip_address, to_email)
	else:
		print('failed to fetch ip')

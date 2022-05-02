from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = [EMAIL]
MY_PASSWORD = [PASSWORD]
emails = [LIST OF EMAILS]
class EmailSent:
    def send_email(self,body, tomorrow, two_month):
        for email in emails:
            message = MIMEMultipart('alternative')
            message['Subject'] = f'Fligt deals from kiwi.com from {tomorrow.strftime("%d/%m/%Y")} to {two_month.strftime("%d/%m/%Y")}'
            message['From'] =  MY_EMAIL
            message['To'] = email
            html = body
            part2 = MIMEText(html, 'html')
            message.attach(part2)
            server = SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(message['From'], MY_PASSWORD)
            server.sendmail(message['From'], message['To'], message.as_string())
            server.quit()




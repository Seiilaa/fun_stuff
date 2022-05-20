import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import jinja2

EMAIL = 'your email'
PASSWORD = 'email password'


def send_email(n, data_dict, html, receivers):
    # prepare the content
    headline = list(data_dict)[n]
    image = data_dict[list(data_dict)[n]][0]
    description = data_dict[list(data_dict)[n]][1]

    temp = jinja2.Template(html)
    formatted_html = temp.render(headline=headline,
                                 image=image,
                                 description=description)

    # send the email
    sender_email = EMAIL
    password = PASSWORD

    message = MIMEMultipart("alternative")
    message["Subject"] = "🤗Your daily art is here!"
    message["From"] = sender_email
    html_part = MIMEText(formatted_html, "html")
    message.attach(html_part)

    for i in range(len(list(receivers))):  # go through each key index
        receiver_email = receivers[list(receivers)[i]]  # get the email
        message["To"] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

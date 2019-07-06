# # figuring out the email and smtp protocols!!!

# import getpass
# import email, smtplib, ssl
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "jacobdummytestingemail@gmail.com"
# receiver_email = "jacobdummytestingemail@gmail.com"
# password = getpass.getpass(prompt = "Type your password and press enter: ") #GetPass Module blocks vision of the password while typing

# message = MIMEMultipart() #Headings for the email
# message["Subject"] = f"Pool Table Management Information from {today}"
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Bcc"] = receiver_email

# # Create the plain-text and HTML version of your message
# text = f"Here is the file from {today} that has the information on the Pool Tables. Included is information on Total Time and Costs for each table. The file is attached to this email in plain text."
# html = f"<html><body><p>Here is the file from {today} that has the information on the Pool Tables.<br>Included is information on <strong>Total Time</strong> and <strong>Costs</strong> for each table.<br>The file is attached to this email in plain text.</p></body></html>"
# # Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
# part2 = MIMEText(html, "html")
# # Add HTML/plain-text parts to MIMEMultipart message - The email client will try to render the last part first
# message.attach(part1)
# message.attach(part2)

# # Open file in binary mode
# with open(todays_txt, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())

# # Encode file in ASCII characters to send by email  
# encoders.encode_base64(part)

# # Add header as key/value pair to attachment part
# part.add_header("Content-Disposition", f"attachment; filename= {todays_txt}",)

# # Add attachment to message and convert message to string
# message.attach(part)
# text = message.as_string()

# # Create a secure SSL context and send email
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
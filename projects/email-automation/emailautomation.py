import imaplib
import email
import smtplib
from email.message import EmailMessage

# Email credentials
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'

# Connect to the IMAP server and select the inbox
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
mail.select('inbox')

# Search for emails with a specific subject or sender
result, data = mail.search(None, '(UNSEEN)')  # Only fetch unseen emails

for num in data[0].split():
    # Fetch the email data
    result, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Extract name and email
    name = msg['From'].split('<')[0].strip()  # Assuming sender's name is before the email address
    email_address = msg['From'].split('<')[1].replace('>', '').strip()

    # Compose the email with sign-up form
    signup_form = """
    <h1>Welcome to Anytime Fitness!</h1>
    <p>Dear {},</p>
    <p>We're excited to have you join our gym! Please fill out the sign-up form <a href="https://example.com/signup">here</a>.</p>
    <p>Best regards,<br>Your Gym Team</p>
    """.format(name)

    # Send the email
    msg = EmailMessage()
    msg.set_content(signup_form, subtype='html')
    msg['Subject'] = 'Sign-Up Form for Our Gym'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email_address

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# Close the connection
mail.close()
mail.logout()

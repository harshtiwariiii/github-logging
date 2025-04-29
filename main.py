import logging
from logging.handlers import SMTPHandler

# Configure logging to write to a file
logging.basicConfig(filename='app.log', level=logging.INFO)

# Add email handler
mail_handler = SMTPHandler(
    mailhost=('smtp.gmail.com', 587),  # Replace with your SMTP server
    fromaddr='your-email@gmail.com',    # Replace with your email
    toaddrs=['recipient@example.com'],  # Replace with recipient email
    subject='Application Error',
    credentials=('your-email@gmail.com', 'your-app-password'),  # Replace with your email and app password
    secure=()
)
mail_handler.setLevel(logging.ERROR)

# Get the root logger and add the email handler
logger = logging.getLogger()
logger.addHandler(mail_handler)

def main():
    logging.info("Script started.")
    try:
        x = 10 / 10  # This will raise ZeroDivisionError
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        raise

if __name__ == "__main__":  # Fixed the typo in __main__
    main()
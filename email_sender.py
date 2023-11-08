# import os 
# import smtpd
# from email.message import EmailMessage
# from email.utils import formataddr
# from pathlib import Path 
# from dotenv import load_dotenv

# PORT = 587
# EMAIL_SERVER = "smtp-mail.outlook.com"

# # Enviroment
# current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
# envars = current_dir / ".env"
# print(envars)
# load_dotenv(envars)

# # Read 
# sender_email = os.getenv("EMAIL")
# password_email = os.getenv("PASSWORD")


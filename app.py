import smtplib
import ssl
from email.message import EmailMessage
from tkinter import Tk, filedialog

# Fixed sender email and app password
SENDER_EMAIL = "shaheenyasub18@gmail.com"
APP_PASSWORD = "wpcxcyguvrubsmnl"  # Gmail App Password (no spaces)

def send_email():
    # Prompt user for recipient
    recipient = input("Enter recipient email: ").strip()
    
    # Open file picker dialog
    Tk().withdraw()  # Hide the main Tk window
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not file_path:
        print("❌ No file selected. Exiting.")
        return
    
    # Create the email
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient
    msg["Subject"] = "Here is your PDF file"
    msg.set_content("Please find the attached PDF file.")
    
    # Attach the file
    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)
    
    # Send email securely
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
    
    print("✅ Email sent successfully!")

if __name__ == "__main__":
    send_email()

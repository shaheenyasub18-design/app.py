import smtplib
import ssl
from email.message import EmailMessage
import streamlit as st

# Streamlit App
st.set_page_config(page_title="📧 Email Sender", layout="centered")
st.title("📧 Send Email with Attachment")

# User inputs
sender_email = st.text_input("Your Email (Gmail only):")
app_password = st.text_input("Your 16-digit Gmail App Password:", type="password")
recipient_email = st.text_input("Recipient Email:")
subject = st.text_input("Subject:")
body = st.text_area("Message:")

# File uploader
uploaded_file = st.file_uploader("Upload a file to attach", type=["pdf", "jpg", "png", "docx", "txt"])

# Send email button
if st.button("Send Email"):
    if not sender_email or not app_password or not recipient_email or not subject or not body:
        st.error("⚠️ Please fill all the fields before sending.")
    elif not uploaded_file:
        st.error("⚠️ Please upload a file to send.")
    else:
        try:
            # Create email
            msg = EmailMessage()
            msg["From"] = sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.set_content(body)

            # Attach file
            file_data = uploaded_file.read()
            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename=uploaded_file.name,
            )

            # Send email securely
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, app_password)
                server.send_message(msg)

            st.success("✅ Email sent successfully!")

        except Exception as e:
            st.error(f"❌ Error: {e}")

# utils.py
from mailjet_rest import Client
import threading
from django.conf import settings

def send_email_async(subject, message, from_email, to_email):
    def send_mailjet_email():
        mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET), version='v3.1')
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "info@yourdomain.com",  # Use your verified domain address here
                        "Name": "Your Platform Name"
                    },
                    "To": [
                        {
                            "Email": to_email,
                            "Name": "Recipient Name"
                        }
                    ],
                    "Subject": subject,
                    "TextPart": message,
                    "HTMLPart": f"<p>{message}</p>",
                    "ReplyTo": {
                        "Email": from_email,
                        "Name": "Reply To Name"
                    }
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())

    threading.Thread(target=send_mailjet_email).start()

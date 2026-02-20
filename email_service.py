import os
import requests

RESEND_API_URL = "https://api.resend.com/emails"

def send_email(to_email: str, subject: str, html: str):
    api_key = os.getenv("RESEND_API_KEY")
    

    if not api_key:
        raise RuntimeError("RESEND_API_KEY not configured")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "from": "onboarding@resend.dev",
        "to": [to_email],
        "subject": subject,
        "html": html
    }

    response = requests.post(
        RESEND_API_URL,
        json=payload,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    return response.json()

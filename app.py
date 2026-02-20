from flask import Flask, request, jsonify
from dotenv import load_dotenv
from email_service import send_email
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/send-email", methods=["POST"])
def send_email_route():
    data = request.json

    if not data:
        return jsonify({
            "status": "error",
            "message": "Invalid JSON"
        }), 400

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    subject = data.get("subject")
    message = data.get("message")

    if not all([name, email, subject, message]):
        return jsonify({
            "status": "error",
            "message": "Missing required fields"
        }), 400

    try:
        html_content = f"""
        <h2>New Contact Form Submission</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Subject:</strong> {subject}</p>
        <p><strong>Message:</strong></p>
        <p>{message}</p>
        """

        send_email(
            to_email="metellusjunior56@gmail.com",
            subject=f"Contact Form: {subject}",
            html=html_content
        )

        return jsonify({
            "status": "success",
            "message": "Email sent successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)

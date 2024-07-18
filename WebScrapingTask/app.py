from flask import Flask
import yagmail, os

app = Flask(__name__)

@app.route('/send_email', methods=['GET'])
def send_email():
    recipient = "pradeep.meena@iitgn.ac.in"
    cc_recipient = "pradeep.meena2026@gmail.com"
    subject = "Python (Selenium) Assignment - Pradeep Kumar Meena"
    body = "Please find the attached confirmation page screenshot and PDF files."
    screenshot_path = "confirmation_page.png"
    resume_path = 'PradeepCV.pdf'
    report_path = 'WebScrapingApproach.pdf'
    
    yag = yagmail.SMTP("pradeepmeena1608@gmail.com", "rnlefxqxgijtizba")
    yag.send(
        to=recipient,
        cc=cc_recipient,
        subject=subject,
        contents=body,
        attachments=[screenshot_path, resume_path, report_path]
    )
    return "Email sent!"

if __name__ == "__main__":
    if not os.path.exists("confirmation_page.png"):
        raise FileNotFoundError("Screenshot not found. Ensure the form filling script is run first.")
    
    app.run(debug=True)
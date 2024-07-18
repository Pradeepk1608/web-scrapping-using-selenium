from flask import Flask
import yagmail, os

app = Flask(__name__)

@app.route('/send_email', methods=['GET'])
def send_email():
    recipient = "tech@themedius.ai"
    cc_recipients = ["hr@themedius.ai", 'pradeep.meena@iitgn.ac.in']
    subject = "Python (Selenium) Assignment - Pradeep Kumar Meena"
    body = """
        Respected Sir/Madam,

        I hope this email finds you well.

        Please find attached the required documents for the Python (Selenium) assignment:

        1. Screenshot of the form filled via code.
        2. Source code in a GitHub repository: https://github.com/Pradeepk1608/web-scrapping-using-selenium
        3. Brief documentation of my approach
        4. My resume.
        5. Links to past projects/work samples: https://drive.google.com/drive/folders/1RvTUqin45e056q9bzfuOefnXMR7GKdI0?usp=sharing, https://github.com/Pradeepk1608/geolocational-data-analysis, https://github.com/Pradeepk1608/alien_onslaught etc.
        6. I confirm my availability to work full time from 10 am to 7 pm for the next 3-6 months.
        Please let me know if you need any further information.

        Thank you for your time and consideration.

        Best regards,

        Pradeep Kumar Meena
        Contact: 8209221145
        LinkedIn: www.linkedin.com/in/pradeep-k-54b77b25b
        """
    screenshot_path = "confirmation_page.png"
    resume_path = 'PradeepCV.pdf'
    report_path = 'WebScrapingApproach.pdf'
    
    yag = yagmail.SMTP("pradeepmeena1608@gmail.com", "rnlefxqxgijtizba")
    yag.send(
        to=recipient,
        cc=cc_recipients,
        subject=subject,
        contents=body,
        attachments=[screenshot_path, resume_path, report_path]
    )
    return "Email sent!"

if __name__ == "__main__":
    if not os.path.exists("confirmation_page.png"):
        raise FileNotFoundError("Screenshot not found. Ensure the form filling script is run first.")
    
    app.run(debug=True)
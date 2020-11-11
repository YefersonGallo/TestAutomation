class Tester:
    import smtplib
    import email.message

    def __init__(self, name, emailTest, date, serverTest):
        self.name = name
        self.emailTest = emailTest
        self.date = date
        self.serverTest = serverTest

    def sendReport(self):
        server = self.smtplib.SMTP('smtp.gmail.com:587')
        email_content = """
        <html>
        <body>
        <h1> Test </h1>
        </body>
        </html>


        """

        msg = self.email.message.Message()
        msg['Subject'] = 'Reporte de Errores de la prueba'

        msg['From'] = 'test1monolegal@gmail.com'
        msg['To'] = self.emailTest
        password = "MonoTest0_1Legal"
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)

        s = self.smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        # Login Credentials for sending the mail
        s.login(msg['From'], password)

        s.sendmail(msg['From'], [msg['To']], msg.as_string())

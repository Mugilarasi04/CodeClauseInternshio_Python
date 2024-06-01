from PyQt5.QtWidgets import *
from PyQt5 import uic
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail_App(QMainWindow):
    
    def __init__(self):
        super(Mail_App, self).__init__()
        uic.loadUi("mail.ui", self)
        self.show()
        self.login1.clicked.connect(self.login)
        self.attach1.clicked.connect(self.attach)
        self.send1.clicked.connect(self.send)
        self.server = None
        self.msg = MIMEMultipart()

    def login(self):
        try:
            self.server = smtplib.SMTP(self.server1.text(), self.port.text())
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.email.text(), self.password.text())

            self.email.setEnabled(False)
            self.password.setEnabled(False)
            self.server1.setEnabled(False)
            self.port.setEnabled(False)
            self.login1.setEnabled(False)

            self.to.setEnabled(True)
            self.subject.setEnabled(True)
            self.message.setEnabled(True)
            self.send1.setEnabled(True)
            self.attach1.setEnabled(True)

        except Exception as e:
            QMessageBox.critical(self, "Login Failed", str(e))

    def attach(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Attach", "", "All Files (*)", options=options)
        if file_path:
            attachment = MIMEApplication(open(file_path, 'rb').read())
            attachment.add_header('Content-Disposition', 'attachment', filename=file_path.split("/")[-1])
            self.msg.attach(attachment)
            QMessageBox.information(self, "Attachment", "File attached successfully!")


    def send(self):
        try:
            self.msg['From'] = 'Mugilarasi'
            self.msg['To'] = self.to.text()
            self.msg['Subject'] = self.subject.text()
            self.msg.attach(MIMEText(self.message.toPlainText(), 'plain'))
            text = self.msg.as_string()
            self.server.sendmail(self.email.text(), self.to.text(), text)
            QMessageBox.information(self, "Message Sent", "Email sent successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Message Failed", str(e))
            
        finally:
            if self.server:
                self.server.quit()

app = QApplication([])
window = Mail_App()
app.exec_()


import os
from twilio.rest import Client
from data_manager import DataManager
# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self._account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self._auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.client = Client(self._account_sid, self._auth_token)

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.

        Parameters:
        message_body (str): The text content of the SMS message to be sent.

        Returns:
        None

        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)
    
    def send_email(self, message_body, email_data):
        """
        Sends an email notification 

        Actually doesn't, because I send email in code all the time,
        and don't want to setup SMTP or any other email service here.
        This function is a placeholder for sending email notifications.
        """
        for user in email_data:
            to_email = user["whatIsYourEmailAddress?"]
            # Here you would implement the logic to send an email using an SMTP server or an email service API.
            # For example, using smtplib or a service like SendGrid, Mailgun, etc.
            # Implementation for sending emails would go here
            print(f"Email sent from 'alert@flightaleart.moc' to {to_email} with subject 'Flight Price Alert' and body '{message_body}'")
        

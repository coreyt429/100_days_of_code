"""
This module is responsible for sending notifications with the deal flight details.
"""

import os
import logging
from twilio.rest import Client


class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """

    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, message):
        """
        Send an SMS with the deal flight details.
        """
        MY_WHATSAPP_NUMBER = os.getenv('MY_WHATSAPP_NUMBER')
        TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
        # message = client.messages.create(
        #   from_='+18663506246',
        #   body='Hello from Twilio',
        #   to='+18777804236'
        # )
        twilio_message = self.client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=MY_WHATSAPP_NUMBER
        )
        # Twilio setup
        # message = self.client.messages.create(
        #     body=message,
        #     from_=os.getenv("TWILIO_PHONE_NUMBER"),
        #     to=os.getenv("MY_PHONE_NUMBER"),
        # )
        logging.debug("Message sent: %s", twilio_message.sid)

    def __str__(self):
        return (
            f"NotificationManager(account_sid={self.account_sid}, "
            f"phone_number={os.getenv('TWILIO_PHONE_NUMBER')})"
        )


os.listdir()
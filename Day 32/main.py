"""
Day 32 - Birthday Wisher
"""
import os
import json
from random import choice
import smtplib
import datetime as dt
import pandas as pd



##################### Extra Hard Starting Project ######################
LETTER_DIR = "letter_templates"

with open("secrets.json", encoding="utf-8") as secrets_file:
    secrets = json.load(secrets_file)

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
for birthday in birthdays_dict:
    if (
        birthday["month"] == dt.datetime.now().month
        and birthday["day"] == dt.datetime.now().day
    ):
        # 3. If step 2 is true, pick a random letter from letter templates and
        # replace the [NAME] with the person's actual name from birthdays.csv
        file_name = choice(os.listdir(LETTER_DIR))
        # print(f"opening {LETTER_DIR}/{file_name}")
        with open(f"{LETTER_DIR}/{file_name}", encoding="utf-8") as letter_file:
            letter_content = letter_file.read()
            letter_content = letter_content.replace("[NAME]", birthday["name"])
            letter_content = letter_content.replace("Angela", "Corey")

        # print(letter_content)
        # 4. Send the letter generated in step 3 to that person's email address.
        my_email = secrets["gmail"]["address"]
        password = secrets["gmail"]["app_password"]

        with smtplib.SMTP(
            secrets["gmail"]["smtp_server"], port=secrets["gmail"]["smtp_port"]
        ) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_content}",
            )

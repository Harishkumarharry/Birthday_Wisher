import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "You're mail id"
password = "Password for the above mail id"

current_datetime = dt.datetime.now()
current_tuple = (current_datetime.month, current_datetime.day)

df = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if current_tuple in birthday_dict:
    birthday_person = birthday_dict[current_tuple]
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # tls = transport layer security
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],  # Receiver Mail ID
            msg=f"Subject:Happy Birthday!!!\n\n{contents}"
        )

import yagmail

password = ""
with open("/home/pi/.local/share/.email_password", "r") as f:
    password = f.read()

yag = yagmail.SMTP("kousoubirusangou@gmail.com", password)

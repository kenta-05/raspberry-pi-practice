import yagmail

password = ""
with open("/home/pi/.local/share/.email_password", "r") as f:
    password = f.read()

yag = yagmail.SMTP("kousoubirusangou@gmail.com", password)

yag.send(
    to="kenta.sato.05@gmail.com",
    subject="first email",
    contents="Hello from Raspberry Pi",
)
print("Email sent successfully")

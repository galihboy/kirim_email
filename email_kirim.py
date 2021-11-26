'''
Kirim email menggunakan akun Google
by Galih Hermawan (https://galih.eu)
'''

import smtplib

host = "smtp.gmail.com"
port = 587
subjek = "coba kirim email"
dari = "email_pengirim@gmail.com"
passw = "email_passw"
tujuan = "email_tujuan@apapun.com"
isi = "Halo, salam kenal. Tes kirim email ya. Thanks"
body = "\r\n".join((
    f"From: {dari}",
    f"To: {tujuan}",
    f"Subject: {subjek}",
    "",
    isi)
)
server = smtplib.SMTP(host, port)
server.starttls() # mengaktifkan keamanan
server.login(dari, passw) # login dengan akun email dan password
server.sendmail(dari, tujuan, body)
server.quit()
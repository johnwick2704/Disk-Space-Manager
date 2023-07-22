import os
import smtplib

threshold=80
with os.popen('df -h /') as cmd:
    content = cmd.read()
    content=content.split()
    del content[0:7]  #to remove headers(filesystem,used,avail,etc)
for i in content:
    if i.endswith('%'):
        if(int(i[:-1])>threshold):
            final_content='Used space in some of your drives has gone above threshold value. Please use the disk manager tool to free space. Thanks. '
print(final_content)        
mail=smtplib.SMTP('smtp.gmail.com:587')
mail.ehlo()
mail.starttls()
mail.login('emailid','google_app_password')
mail.sendmail('emailid','emailid',final_content)
mail.close()
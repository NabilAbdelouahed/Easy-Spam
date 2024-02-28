import time, os
import smtplib, ssl
import random

smtp_server = 'smtp.gmail.com'
port = 587
destinateur = os.getenv("MY_USERNAME")
password = os.getenv("MY_PASSWORD")

destinataire = 'toto@gmail.com'

context = ssl.create_default_context()

n = int(input("Combien de fois ? : "))

 
while(n!=0):
    print(n-1)
    
    f=open("spam", "r")
    m=random.randint(1,3408)
    L=f.readlines(m)
    random.shuffle(L)
    
    msg=f.readlines(3408)
    random.shuffle(msg)
    h=random.randint(1, 10)
    objet=msg[0:h]
    
    ch=''
    for i in range(len(objet)):
        objet[i]=objet[i][0:len(objet[i])-1]
        ch+=objet[i]+' '
        
    ch1=''
    for k in range(len(L)):
        L[k]=L[k][0:len(L[k])-1]
        ch1+=L[k]+' '
        
    msg=ch1
    objet=ch
    message="Subject : "+objet+" \n\n "+msg 

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(destinateur, password)
        server.sendmail(destinateur, destinataire, message)

    except Exception as exep:
            print(exep)
    finally:
        server.quit()
    time.sleep(random.randint(10,60))
    n-=1


     
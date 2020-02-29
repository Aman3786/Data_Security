from datetime import datetime as dt
import time


website =["www.example2.com", "example2.com","www.example1.com","example1.com"]
# this host file path is for Windows
# host_windows =r"C:\Windows\System32\drivers\etc\hosts"
host_linux = r"/etc/hosts"
redirect = "127.0.0.1"

min_time = dt(dt.now().year,dt.now().month,dt.now().day,5)
max_time = dt(dt.now().year,dt.now().month,dt.now().day,16,35)

while True:
    if min_time < dt.now() < max_time:
        # print("cllg time")
        with open(host_linux,"r+") as file:
            content =file.read()
            # print(content)
            for web in website:
                if web not in content:
                    file.write(redirect+"  "+web+"\n")
                    
    else:
        with open(host_linux,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(web in line for web in website):
                    file.write(line)
                file.truncate() 
        # print("funtime")  
    time.sleep(1)
      

# if condition is true then "if not any" condition make it false then it will go outside 
# otherwise it will go inside
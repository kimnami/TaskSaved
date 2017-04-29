# import debttest
import requests, json
from time import sleep
from random import randint

def login(name, pswd):
    link = "http://127.0.0.1:8000"
    sleep(0.05)
    try:
        res = requests.get(link, auth=(name, pswd))
        if res.status_code != 200:
            print("ERROR: Cannot get {0} : {1}".format(link, res.status_code))
    except Exception:
        print("ERROR: Cannot post {0}".format(link))
        exit(1)

def post_or_error(link, data):
    sleep(0.05)
    try:
        headers = {'Content-Type': 'application/json;'}
        res = requests.post(link, data=json.dumps(data), headers=headers)
        if res.status_code != 201:
            print("ERROR: Cannot post {0} : {1}".format(link, res.status_code))
            exit(1)
    except Exception:
        print("ERROR: Cannot post {0}".format(link))
        exit(1)



#post user
# link = "http://127.0.0.1:8000/register/"
# userN = 1
# print("Checking POST {0} by creating {1} users.".format(link, userN))

# for i in range(0, userN):
#     account = {}
#     user = {}
#     user["username"] = "ttttest"+str(i)
#     user["password"] = "test"+str(i)*4
#     user["last_name"] = str(i)
#     user["first_name"] = "test"

#     account["user"] = user
#     account["birthday"] = "2000-0"+str(randint(1,9))+"-"+str(randint(10,28))
#     account["gender"] = randint(1,2)


#     print("\tposting new user : {0}".format(user["username"]))
#     post_or_error(link, account)

login("test0", "test0000")
login("test1","test0000")
login("test","d")


print("TEST SUCCESSFUL")
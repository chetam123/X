import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('./x-project-29dd5-firebase-adminsdk-4an1j-ca48193e85.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://x-project-29dd5-default-rtdb.asia-southeast1.firebasedatabase.app'
})
# Get a database reference to our posts
ref = db.reference('users')

def pushUser(data):
    ref.push(data)

def getAllUser():
    userList = ref.get()
    # print(userList)
    if(userList == None or userList == "None"):
        return []
    flatUsers = [{'id': key, **value} for key, value in userList.items()]

    print(flatUsers)
    return flatUsers

def updateUser(user):
    userRef = ref.child(user.get("id"))
    userRef.update({
        "name":  user.get("name"),
        "mail": user.get("mail"),
        "pass": user.get("pass"),
        "token": user.get("token")
    })

getAllUser()
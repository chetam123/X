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

def pushUser(name, email, password, token):
    ref.push({
        "name":  name,
        "mail": email,
        "pass": password,
        "token": token
    })


def getAllUser():
    userList = ref.get()
    flatUsers = [value for obj in userList for value in obj.values()]
    return flatUsers
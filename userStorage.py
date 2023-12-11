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

refAuth = db.reference('AuthenUsers')
refPenddingUser = db.reference('penddingUser')

def pushUser(data):
    ref.push(data)

# lay danh sach tat ca user thuong
def getAllUser():
    userList = ref.get()
    # print(userList)
    if(userList == None or userList == "None"):
        return []
    flatUsers = [{'id': key, **value} for key, value in userList.items()]

    print(len(flatUsers))
    return flatUsers

# Tao user thuong
def updateUser(user):
    userRef = ref.child(user.get("id"))
    userRef.update({
        "name":  user.get("name"),
        "mail": user.get("mail"),
        "pass": user.get("pass"),
        "token": user.get("token")
    })

# chuyen tu user thuong sang danh sach cho xac nhan
def moveToAuthUser(user):
    srcRef = ref.child(user.get("id"))
    srcRef.delete()
    destRef= refAuth.child(user.get("id"))
    destRef.set({
        "name":  user.get("name"),
        "mail": user.get("mail"),
        "pass": user.get("pass"),
        "token": user.get("token")
    })

# chuyen tu danh sach cho xac nhan sang user thuong
def moveFromAuthToUser(user):
    srcRef = refAuth.child(user.get("id"))
    srcRef.delete()
    destRef = ref.child(user.get("id"))
    destRef.set({
        "name":  user.get("name"),
        "mail": user.get("mail"),
        "pass": user.get("pass"),
        "token": user.get("token")
    })

# chuyen tu user thuong sang danh sach user bi yeu cau nhap ma code
def moveToPenddingUser(user):
    srcRef = ref.child(user.get("id"))
    srcRef.delete()
    destRef = refPenddingUser.child(user.get("id"))
    destRef.set({
        "name":  user.get("name"),
        "mail": user.get("mail"),
        "pass": user.get("pass"),
        "token": user.get("token")
    })

# chuyen tu user thuong sang danh sach user bi yeu cau nhap ma code
def moveFromPenddingToUser(user):
    srcRef = refPenddingUser.child(user.get("id"))
    srcRef.delete()
    destRef = ref.child(user.get("id"))
    destRef.set({
        "name":  user.get("name"),
        "mail": user.get("mail"),
        "pass": user.get("pass"),
        "token": user.get("token")
    })





user = {'id': '-NlCAevh9KlKwGPu1ySY', 'mail': '983cb56574036d@crankymonkey.info', 'name': '@duy_gia5830', 'pass': 'Congtam@779', 'token': '9657a302e3f31e25e090d451fe79a9ab535502b0'}
# moveToAuthUser(user)
# moveFromAuthToUser(user)
# moveToPenddingUser(user)
# moveFromPenddingToUser(user)
# getAllUser()
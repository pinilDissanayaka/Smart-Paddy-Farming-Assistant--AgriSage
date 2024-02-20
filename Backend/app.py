from flask import Flask, request, session, jsonify
from utils.user import User

app=Flask(__name__)

user=User()

@app.route("/sign-in", methods=['GET', 'POST'])
def signIn():
    emailAddress = str(request.args['emailAddress'])
    password = str(request.args['password'])
    
    status, user_=user.logInUser(emailAddress=emailAddress, password=password)
    
    if status == "Loging successfull":
        responce={"status": status, 'username': user_['username']}
        
    elif status == "Incorrect password":
        responce={"status": status, 'username': None}
        
    elif status == "User not found":
        responce={"status": status, 'username': None}
        
        
    return jsonify({"responce": responce})





if __name__=="__main__":
    app.run(debug=True, port=5000)
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


@app.route("/validate-password", methods=['GET', 'POST'])
def validatePassword():
    password = str(request.args['password'])
    
    status=user.validatePassword(password=password)
    
    responce={"status": status}
    
    return jsonify({"responce" : responce})



@app.route("/sign-up", methods=['GET', 'POST'])
def signUp():
    username = str(request.args['username'])
    emailAddress = str(request.args['emailAddress'])
    phoneNumber = str(request.args['phoneNumber'])
    password = str(request.args['password'])
        
    status=user.addUser(username=username, emailAddress=emailAddress, phoneNumber=phoneNumber, password=password)
    
    if status:
        session['loggedIn'] = True
        session['emailAddress'] = emailAddress
        session['username']=username
        
        responce={"status": "success", 'username': username}
        
    else:
        responce={"status": "unsuccess", 'username': None}

    return jsonify({"responce" : responce})






if __name__=="__main__":
    app.run(debug=True, port=5000)
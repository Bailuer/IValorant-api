from flask import Flask,jsonify,request,session
import index
app = Flask(__name__)
@app.route('/login', methods=['POST', 'GET'])
def login():
    usernames = request.form.get("username",None)
    passwords = request.form.get("password",None)
    print(usernames,passwords)
    apiresult = index.main(usernames,passwords)
    return jsonify(apiresult)
    '''
    if(index.auth.Auth.if2fa):
        return jsonify("please return the vc")
    else:
        return jsonify(apiresult)
    '''
if __name__ == '__main__':
    app.run(debug=True)
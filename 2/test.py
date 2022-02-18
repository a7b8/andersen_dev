
from flask import Flask, request
app = Flask(__name__)


@app.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    print(username)
    print(password)
 

if __name__ == '__main__':
    app.run(debug=True)

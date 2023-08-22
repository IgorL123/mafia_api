from flask import Flask, request
# import db

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/create_game', methods = ["POST"])
def create():
    TCI = request.json
    db.query_ins_chat(TCI)


    

@app.route('/start_game')
def start():  # Команда принимает на вход 
    pass

@app.route('/action')
def action(): 
    pass

if __name__ == '__main__':
    app.run()
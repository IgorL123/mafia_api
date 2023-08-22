from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/create_game')
def create(str truechatid):



    

@app.route('/start_game')
def start():  # Команда принимает на вход 
    

@app.route('/action')
def action(): 


if __name__ == '__main__':
    app.run()
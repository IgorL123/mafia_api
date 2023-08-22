from flask import Flask, request, jsonify
import db
import api_functions


app = Flask(__name__)


@app.route('/action', methods=["POST"])
def action():  # put application's code here
    data = request.json
    trueChatID = data['chatID']
    killedUserID = data['KilledUserID']
    healedUserID = data['HealedUserID']
    checkedUserID = data['CheckedUserID']

    response = {
        "killedUserId": "",
        "isEndGame": "",
        "checkedRole": False
    }

    cur = db.cursor

    if killedUserID != healedUserID:
        cur.execute(f"Select UserID from chats join userschats uc on uc.chatid = chats.chatid join "
                    f"users on users.userid = uc.userid where truechatid = '{trueChatID}' and TrueUserID = '{killedUserID}'")
        id = cur.fetchall()[0]
        cur.execute(f"UPDATE Users SET isAlive = false WHERE UserID = '{id}'")
        response["killedUserId"] = killedUserID

    cur.execute(f"SELECT role FROM users WHERE TrueUserID ='{checkedUserID}';")
    role = cur.fetchall()[0]

    if role == 4:
        response["checkedRole"] = True

    response["isEndGame"] = api_functions.isEnd(cur, trueChatID)

    return jsonify(response), 200


@app.route('/create_game', methods=["POST"])
def create():
    TCI = request.json['chatID']
    cursor = db.connection.cursor()
    db.query_ins_chat(TCI, cursor)
    db.close(cursor)


@app.route('/start_game', methods=["POST"])
def start():  # Команда принимает на вход
    TCI = request.json['chatID']
    userlist = request.json['usderIDs']
    cursor = db.connection.cursor()
    for id in userlist:
        db.query_ins_user(id, curs)
    db.close()


if __name__ == '__main__':
    app.run()

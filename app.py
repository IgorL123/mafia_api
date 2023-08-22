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
        "killedUserId": None,
        "isEndGame": None,
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


@app.route('/create_chat', methods=["POST"])
def create():
    tci = request.json['chatID']
    cursor = db.connection.cursor()
    db.query_ins_chat(tci, cursor)
    return 'ok', 200


@app.route('/start_game', methods=["POST"])
def start():  # Команда принимает на вход
    return '', 501


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

from flask import Flask, request, jsonify
import db

app = Flask(__name__)


def isEnd(cur, trueChatID):
    # cur.execute(f"SELECT ChatID FROM Chats WHERE TrueChatID = '{trueChatID}'")
    # row = cur.fetchall()
    # chatID = row[0]
    #
    # cur.execute(f"SELECT UserID FROM UsersChats WHERE ChatID = '{chatID}'")
    # usersIDs = cur.fetchall()
    #
    # allAlive = True
    # for id in usersIDs:
    #     cur.execute(f"SELECT isAlive FROM Users WHERE UserID = '{id}', role = ")
    #     row = cur.fetchall()
    #     if row[0] == False:
    #         allAlive = False

    cur.execute(f"Select role from chats join userschats uc on uc.chatid = chats.chatid join "
                f"users on users.userid = uc.userid where truechatid = '{trueChatID}' and isAlive = true")
    roles = cur.fetchall()

    m = roles.count(4)
    if m == 0:
        return "citizens"
    elif m >= len(roles) - m:
        return "mafia"

    return ""


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

    response["isEndGame"] = isEnd(cur, trueChatID)

    return jsonify(response), 200


if __name__ == '__main__':
    app.run()
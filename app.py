from flask import Flask, request, jsonify
import db
import logging
from logging.handlers import RotatingFileHandler
import api_functions

app = Flask(__name__)

app.logger.handlers.clear()
if True:
    app.logger.setLevel(logging.INFO)
    file_handler = RotatingFileHandler("log.log", maxBytes=1024 * 1024 * 10)
    formatter = logging.Formatter(fmt="%(asctime)s - %(message)s")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(logging.StreamHandler())


@app.route("/")
def act():
    app.logger.info("default routing")
    return "Welcome to Api"


@app.route('/action', methods=["POST"])
def action():
    # TODO: обработка ошибок + логи
    data = request.json
    true_chat_id = data['chatID']
    killed_user_id = data['KilledUserID']
    healed_user_id = data['HealedUserID']
    checked_user_id = data['CheckedUserID']

    response = {
        "killedUserId": None,
        "isEndGame": None,
        "checkedRole": False
    }

    cursor = db.connection.cursor()

    if killed_user_id != healed_user_id:
        cursor.execute(f"Select UserID from chats join userschats uc on uc.chatid = chats.chatid join "
                    f"users on users.userid = uc.userid where truechatid = '{true_chat_id}' "
                    f"and TrueUserID = '{killed_user_id}'")
        generated_user_id = cursor.fetchall()[0]
        cursor.execute(f"UPDATE Users SET isAlive = false WHERE UserID = '{generated_user_id}'")
        response["killedUserId"] = killed_user_id

    cursor.execute(f"SELECT role FROM users WHERE TrueUserID ='{checked_user_id}';")
    role = cursor.fetchall()[0]

    if role == 4:
        response["checkedRole"] = True

    response["isEndGame"] = api_functions.isEnd(cursor, true_chat_id)
    db.close(cursor)
    app.logging.info("Actions route")
    return jsonify(response), 200


@app.route('/create_chat', methods=["POST"])
def create():
    # TODO: обработка ошибок + логи
    tci = request.json['chatID']
    cursor = db.connection.cursor()
    db.chat_add(tci, cursor)
    app.logger.info("Created new chat")
    db.close(cursor)
    return 'ok', 200


@app.route('/start_game', methods=["POST"])
def start():  # Команда принимает на вход
    tci = request.json['chatID']
    user_list = request.json['userIDs']
    cursor = db.connection.cursor()

    for current_user in user_list:
        db.user_add(current_user, tci, cursor)
        db.connection.commit()
    app.logger.info(f"Added {len(user_list)} users")

    db.close(cursor)
    resp = api_functions.role_distribution(user_list)
    return "", resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

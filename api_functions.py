import random


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


def role_distribution(userIDs):  # Распределение ролей
    user_count = len(userIDs)
    # Сначала нам необходимо понять, сколько каких ролей будет в зависимости от кол-ва игроков
    userIDs = list(userIDs)
    resp = {}  # Инициализируем будущий ответ(в формате словаря {ID : Роль})
    ls = [0, 0, 1, 1, 0]
    # Массив с ролями, где индекс - роль (0 - inactive, 1 - civil, 2 - doc, 3 - comm, 4 - maf), док и ком всегда один
    ls[4] = user_count//4
    # Мафии вычисляются, как кол-во игроков//4, остальные мирные
    ls[1] = user_count - ls[4]-2
    # Перемешиваем массив чтоб постоянно одни и те же роли не выпадали
    random.shuffle(userIDs)
    for i in range(5):
        for j in range(ls[i]):
            # Ну и, пробегая по каждой роли, убираем из массива один ID,
            resp[userIDs.pop()] = str(i)
            # присваивая ему роль, добавляя в словарь вывода

    return resp

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
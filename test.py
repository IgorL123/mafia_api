# for i in range(0):
#     print(i)

# d = dict
# print(d)
import random

def role_distribution(userIDs):
    user_count = len(userIDs)
    userIDs = list(userIDs)
    resp = {}    # resp = {userIDs[i]: 0 for i in range(len(userIDs))}
    ls = [0, 0, 1, 1, 0]
    ls[4] = user_count//4
    ls[1] = user_count - ls[4]-2
    random.shuffle(userIDs)
    for i in range(5):
        for j in range(ls[i]):
            print(type(userIDs))
            resp[userIDs.pop()] = str(i)

    return resp
a = ["a", "b", "c", "d", "e", "f", "g"]

print(role_distribution(a))

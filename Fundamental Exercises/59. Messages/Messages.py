registered_users = []
messages = []
class User:

    def __init__(self, username, received_msgs=None):
        self.username = username
        if received_msgs is None:
            received_msgs = []
        self.received_msgs = received_msgs

class Message:

    def __init__(self, msg_sender, content):
        self.msg_sender = msg_sender
        self.content = content

data = input()

while not data == "exit":
    input_data = data.split()
    if input_data[0] == "register":
        username = input_data[1]
        new_user = User(username, None)
        registered_users.append(new_user)
    else:
        sender = input_data[0]
        receiver = input_data[2]
        content = input_data[3:]
        sender_exists = False
        receiver_exists = False
        for i in registered_users:
            if sender == i.username:
                sender_exists = True
            elif receiver == i.username:
                receiver_exists = True
        if sender_exists and receiver_exists:
            new_message = Message(sender, content)
            receiver_msg = User(receiver, new_message)
            messages.append(receiver_msg)

    data = input()
data = input().split(' ')
first_user = data[0]
second_user = data[1]
have_spoken = False


for i in messages:
    user = i.received_msgs.msg_sender
    if first_user == user:
        if second_user == i.username:
            have_spoken = True
            break
    elif second_user == user:
        if first_user == i.username:
            have_spoken == True
            break

if have_spoken:
    input_users_msgs = {}
    input_users_msgs[first_user] = []
    input_users_msgs[second_user] = []
    for i in messages:
        if first_user == i.received_msgs.msg_sender and second_user == i.username:
            input_users_msgs[first_user].append(i.received_msgs.content[0])
        elif second_user == i.received_msgs.msg_sender and first_user == i.username:
            input_users_msgs[second_user].append(i.received_msgs.content[0])


    #max_len_list = len(max(input_users_msgs[first_user], input_users_msgs[second_user]))
    if len(input_users_msgs[first_user]) >  len(input_users_msgs[second_user]):
        min_len_list = input_users_msgs[second_user]
        max_len_list = input_users_msgs[first_user]
        longer_user = first_user
    else:
        min_len_list = input_users_msgs[first_user]
        max_len_list = input_users_msgs[second_user]
        longer_user = second_user
    i = 0
    j = 0
    for keys, values in input_users_msgs.items():
        for v in values:
            while j < len(min_len_list):
                print(f'{first_user}: {input_users_msgs[first_user][j]}')
                print(f'{input_users_msgs[second_user][j]} :{second_user}')
                j += 1
                i += 1
            while i < len(max_len_list):
                print(f'{longer_user}: {max_len_list[i]}')
                i += 1
""""
register Ivan
register Pesho
Ivan send Pesho pesho
Ivan send Pesho pesho_tam_li_si?
Pesho send Ivan kaji_vanka
Pesho send Ivan tuk_sum
Pesho send Ivan chakai_che_bachkam
Ivan send Pesho kvo_stava
Ivan send Pesho kak_si
Ivan send Pesho deka_izbega_be?
Ivan send Pesho pecaaa!!!
exit
Ivan Pesho
"""
usernames = ['urban-robot', 'automatic-memory', 'admin','reimagined-happiness', ' fluffy-computing-machine', 
'improved-succotash', 'studious-octo-palm-tree', 'furry-octo-couscous']

# 5-9 No Users:
# usernames = []

if usernames: 
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Greetings, ' + username + '. Thank you for logging in again. ')
else:
    print('We need to find some users!')

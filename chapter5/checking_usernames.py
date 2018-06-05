current_users = ['urban-robot', 'automatic-memory','reimagined-happiness', ' fluffy-computing-machine', 
'improved-succotash']

new_users = ['studious-octo-palm-tree', 'furry-octo-couscous', 'AUTOMATIC-memory', 'upgraded-octo-potato', 'urban-robot']

for user in new_users:
    if user.lower() in current_users:
        print('Username currently being used. Please choose another one.')
    else:
        print('Username available')


        
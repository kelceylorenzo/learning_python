guest_list = ["Leslie Knope", "Alexander Hamilton", "Dumbledore"]
invitation = "\nPlease join me for dinner! \nSincerely, \nMe"
# print("Dear " + guest_list[0] + "," + invitation)
# print("Dear " + guest_list[1] + "," + invitation)
# print("Dear " + guest_list[2] + "," + invitation)

# 3-5 Changing Guest List

# print("Sorry, I cannot make it. \n - " + guest_list[0])
guest_list[0] = "Ben Wyatt"

# 3-6 More Guests

bigger_table = "\nI have found a bigger dinner table and shall be inviting more people. \nSee you soon, \nMe"
# print("Dear " + guest_list[0] + "," + bigger_table)
# print("Dear " + guest_list[1] + "," + bigger_table)
# print("Dear " + guest_list[2] + "," + bigger_table)

guest_list.insert(0, "April Ludgate")
guest_list.insert(2, "Harry Potter")
guest_list.append("Aaron Burr")
# print("Dear " + guest_list[0] + "," + invitation)
# print("Dear " + guest_list[1] + "," + invitation)
# print("Dear " + guest_list[2] + "," + invitation)
# print("Dear " + guest_list[3] + "," + invitation)
# print("Dear " + guest_list[4] + "," + invitation)
# print("Dear " + guest_list[5] + "," + invitation)

# 3-7 Shrinking Guest List

apology_message = "\nI regret to inform that I can only invite two guests to dinner. Confirmation messages will be sent out soon. \nBest, \nMe"
# print("Dear " + guest_list[0] + "," + apology_message)
# print("Dear " + guest_list[1] + "," + apology_message)
# print("Dear " + guest_list[2] + "," + apology_message)
# print("Dear " + guest_list[3] + "," + apology_message)
# print("Dear " + guest_list[4] + "," + apology_message)
# print("Dear " + guest_list[5] + "," + apology_message)

uninvited_message = "\nI regret to inform that you have been uninvited to my dinner. \nBest, \nMe"
uninvited = guest_list.pop()
# print("Dear " + uninvited + "," + uninvited_message)
uninvited = guest_list.pop()
# print("Dear " + uninvited + "," + uninvited_message)
uninvited = guest_list.pop()
# print("Dear " + uninvited + "," + uninvited_message)
uninvited = guest_list.pop()
# print("Dear " + uninvited + "," + uninvited_message)

confirmation = "\nYou are still invited to my dinner. See you there! \nBest, \nMe"
# print("Dear " + guest_list[0] + "," + confirmation)
# print("Dear " + guest_list[1] + "," + confirmation)
del guest_list[0]
del guest_list[0]
print(guest_list)
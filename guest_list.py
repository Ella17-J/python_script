guests_list = ['Esther', 'Herty', 'Marian']
len(guests_list)
dinner_invitation = guests_list[0].title() + ", Would you like to join me for dinner tonight? "
print(dinner_invitation)
dinner_invitation = guests_list[1].title() + ", Would you like to join me for dinner tonight? "
print(dinner_invitation)
dinner_invitation = guests_list[2].title() + ", Would you like to join me for dinner tonight? "
print(dinner_invitation)
dinner_declination = guests_list[1].title() + " cannot make it."
print(dinner_declination)

#new list excluding the one who cannot make it 
guests_list[1] = "Harriet"
dinner_invitation = guests_list[0].title() + ", Would you like to join me for dinner tonight? "
print(dinner_invitation)
dinner_invitation = guests_list[1].title() + ", Would you like to join me for dinner tonight? "
print(dinner_invitation)
dinner_invitation = guests_list[2].title() + ", Would you like to join me for dinner tonight? "
print(dinner_invitation)
print("To all my guests, I found a bigger table which implies more people joining us.")
guests_list.insert(1, "Ezekiel")
print(guests_list)
#dinner_invitation = guests_list.title() + ", Would you like to join me for dinner tonight? "
#print(dinner_invitation)

print("There are only two spaces available now for dinner.")
guests_list.pop(2)
print(guests_list)
print("I am sorry to inform you that your dinner invitation is no more available.")
guests_list.pop()
print(guests_list)
print("I am sorry to inform you that your dinner invitation is no more available. ")
del guests_list[1]
print(guests_list)
del guests_list[0]
print(guests_list)

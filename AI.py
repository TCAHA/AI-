import random


#boolians
age = 0
names = ('David','Bebra','Adolf','Carl')
surname = ('Sony Ericson', 'toyota','Lebosvckyu')
family_status = ("Rich family", "Medium sallary family","Poor family")
father = ("father")
mother = ("mother")
abilities = ("low","Medium","High")
money = (0)
start=(0)
school = False
work = False
Health = (100)
Fat = random.randint(0.5,2)
Injuries =(0)
Medicine_overdose = False
sociopathetic = (0)
depresion = (0)
stamina = (10)
stamina_capacity = (10)
action = (0)
actions =('ilnes','DTP','smth')
#name


#start
print("Do you want to start Journey? [(1)yes/(2)no]")
start = (input(""))
if start == 1:
 print ("OK, your game starting")
 print ("You are:",names, surname,age,father,mother,abilities,family_status,"Good Luck with that")
else:
    print("OK,goodbye")
exit(start)

#Life
    if age == 1:
    print("You now can walk, you exlporing world around you, everything is pretty scary and interesting at same time to you")

    if age == 4:
        print("Now you can talk with your parent and interact with surroundings more accuratly ")
    if age == 5:
        print("Its time to go to school",mother)
        school = True

    #починаючи від 5 до 45 можна накидати дуже багато сюжету
    if age == 56
        #для прикладу
        #stamina_capacity= int.randit(5,30)/stamina_capacity = (a"те що в ігрока на цей час, написав так бо треба вводити ще одну змінy" - int.randit(0,100)
        # Health = (a - int.randit(10,100)
    #Тута якась випадковість? action = int randit (0,100)
    #if action =< 10 (nothing)
    #if action =>10 print("You`ve got", actions "do something with that!"

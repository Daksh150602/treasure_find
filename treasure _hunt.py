print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
where_to_go=input("you are at a cross road where you want to go left or right\n")
if where_to_go=="left":
    print("you have came to a lake . there is an island in middle of lake ")
    activity=input("type 'wait' to wait for the boat , or type 'swim' to swim across\n")
    if activity=="wait":
        print("you arrived at the island unharmed.There is a house with three doors.")
        door_to_choose=input("one red, one blue, and one yellow . which color do you choose\n")
        if door_to_choose=="red":
            print("Burned by fire.Game Over.")
        elif door_to_choose=="blue":
            print("Eaten by beasts.Game Over.")
        elif door_to_choose=="yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")


import random, time
random.seed()
points = 0
eventCounter = 0
characterName = input("Name your character: ")

#Direction
direction = input("Choose a direction (N,E,S,W) to begin your journey: ")

if direction == "N" or direction == "n":
    direction = 1

elif direction == "E" or direction == "e":
    direction = 2

elif direction == "W" or direction == "w":
    direction = 3

elif direction == "S" or direction == "s":
    direction = 4

randomDirection = [1,2,3,4]
random.shuffle(randomDirection)

while direction != randomDirection[0] and direction != randomDirection[1] and direction != randomDirection[2]:

    if direction == randomDirection[3]:
        print("You run into a deadend and turn back going back to where you started.")
        direction = input("Choose a direction: ")
        
    else:
        print("Invalid input")
        direction = input("Choose a direction to travel: ")

    if direction == "N" or direction == "n":
        direction = 1

    elif direction == "E" or direction == "e":
        direction = 2

    elif direction == "W" or direction == "w":
        direction = 3

    elif direction == "S" or direction == "s":
        direction = 4

print("{0:>40s}{1:.2f}".format("Points:",points))
while eventCounter != 10:



    #Path 1
    if direction == randomDirection[0]:
        print("The path seems darker than the others and their a strong scent of danger")
        time.sleep(3)
        print("")
        randomEvent = random.randint(1,20)
        if randomEvent < 2: #10%
            #Event 1
            print("There is an animal in the bush. He runs and attacks you.")
            print("Lose 300 points")
            points -= 300
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")
        elif randomEvent < 5: #15%
            #Event 2
            print("A random number of points will be added or subtracted to your points")
            randomNum = random.randint(-500,500)
            points = points + randomNum
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")

        elif randomEvent < 7: #10%
            #Event 3
            print("You encounter a wizard.")
            print("He makes you an offer.")
            print("There is a 70% chance that you earn 750 points and a 30% chance that your points are cut in half")
            userDecision = input("Do you accept the offer? (Y/N)")
            if userDecision == "Y" or userDecision == "y":
                chance = random.randint(1,10)
                if chance < 8:
                    points += 750
                    print("You earned 750 points")
                else:
                    points = points/2
                    print("Your points were cut in half")
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")
        elif randomEvent < 11: #20%
            #Event 4
            print("You find food on the ground (earn 500 points)")
            points += 500
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")
        else:                   #45%
            #Event 5
            enemyAtk = random.randint(1,3)#LightAttack, HeavyAttack, Block
            print("You encounter an enemy snail!")
            print("Choose something to do:")
            print("1 for Light Attack")
            print("2 for Heavy Attack")
            print("3 for Block")
            userInput = int(input(""))

            while userInput != 1 and userInput != 2 and userInput !=3:
                userInput = int(input("Please enter a valid option"))

            while userInput == enemyAtk:
                
                if userInput == 1:
                    print("Both you and the enemy light attack. Nobody is injured")

                elif userInput == 2:
                    print("Both you and enemy heavy attack. Nobody is injuerd")

                else:
                    print("Both you and the enemy block. Nobody is injured")
                enemyAtk = random.randint(1,3)
                userInput = int(input("Choose another attack (1,2,3):"))

            if userInput % 3 + 1 == enemyAtk:

                if userInput == 1:
                    print("The enemy heavy attacks but you hit it first with a light attack")

                elif userInput == 2:
                    print("The enemy blocks but you penetrate it with the heavy attack")

                else:
                    print("The enemy light attacks but you block it defeating the enemy")
                print("You successfully defeat the enemy and you gain 1000 points")
                points += 1000

            elif enemyAtk % 3 + 1 == userInput:

                if userInput == 1:
                    print("The enemy blocks your light attack and defeats you")

                elif userInput == 2:
                    print("The enemy light attacks and hits you first defeating your heavy attack")

                else:
                    print("The enemy heavy attacks and breaks your block to defeat you")
                print("You are defeated by the enemy snail. You lose 200 points")
                points -= 200
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")   
        eventCounter += 1


    #Path 2
    elif direction == randomDirection[1]:
        print("The path looks bright and happy ")
        time.sleep(3)
        print("")
        randomEvent = random.randint(1,20)
        if randomEvent < 2: #10%
            #Event 1
            print("There is an animal in the bush. He runs and attacks you.")
            print("Lose 300 points")
            points -= 300
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")
        elif randomEvent < 5: #15%
            #Event 2
            print("A random number of points will be added or subtracted to your points")
            randomNum = random.randint(-500,500)
            points = points + randomNum
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")

        elif randomEvent < 9: #20%
            #Event 3
            print("You encounter a wizard.")
            print("He makes you an offer.")
            print("There is a 70% chance that you earn 750 points and a 30% chance that your points are cut in half")
            userDecision = input("Do you accept the offer? (Y/N)")
            if userDecision == "Y" or userDecision == "y":
                chance = random.randint(1,10)
                if chance < 8:
                    points += 750
                    print("You earned 750 points")
                else:
                    points = points/2
                    print("Your points were cut in half")
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")
        elif randomEvent < 17: #40%
            #Event 4
            print("You find food on the ground (earn 500 points)")
            points += 500
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")
        else:                   #15%
            #Event 5
            enemyAtk = random.randint(1,3)#LightAttack, HeavyAttack, Block
            print("You encounter an enemy snail!")
            print("Choose something to do:")
            print("1 for Light Attack")
            print("2 for Heavy Attack")
            print("3 for Block")
            userInput = int(input(""))

            while userInput != 1 and userInput != 2 and userInput !=3:
                userInput = int(input("Please enter a valid option"))

            while userInput == enemyAtk:
                
                if userInput == 1:
                    print("Both you and the enemy light attack. Nobody is injured")

                elif userInput == 2:
                    print("Both you and enemy heavy attack. Nobody is injuerd")

                else:
                    print("Both you and the enemy block. Nobody is injured")
                enemyAtk = random.randint(1,3)
                userInput = int(input("Choose another attack (1,2,3):"))

            if userInput % 3 + 1 == enemyAtk:

                if userInput == 1:
                    print("The enemy heavy attacks but you hit it first with a light attack")

                elif userInput == 2:
                    print("The enemy blocks but you penetrate it with the heavy attack")

                else:
                    print("The enemy light attacks but you block it defeating the enemy")
                print("You successfully defeat the enemy and you gain 1000 points")
                points += 1000

            elif enemyAtk % 3 + 1 == userInput:

                if userInput == 1:
                    print("The enemy blocks your light attack and defeats you")

                elif userInput == 2:
                    print("The enemy light attacks and hits you first defeating your heavy attack")

                else:
                    print("The enemy heavy attacks and breaks your block to defeat you")
                print("You are defeated by the enemy snail. You lose 200 points")
                points -= 200
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")   
        eventCounter += 1


    #Path 3
    elif direction == randomDirection[2]:
        print("The path looks mysterious almost as if anything could be hiding here")
        time.sleep(3)
        print("")
        randomEvent = random.randint(1,20)
        if randomEvent < 5: #25%
            #Event 1
            print("There is an animal in the bush. He runs and attacks you.")
            print("Lose 300 points")
            points -= 300
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")
        elif randomEvent < 8: #15%
            #Event 2
            print("A random number of points will be added or subtracted to your points")
            randomNum = random.randint(-500,500)
            points = points + randomNum
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")

        elif randomEvent < 12: #20%
            #Event 3
            print("You encounter a wizard.")
            print("He makes you an offer.")
            print("There is a 70% chance that you earn 750 points and a 30% chance that your points are cut in half")
            userDecision = input("Do you accept the offer? (Y/N)")
            if userDecision == "Y" or userDecision == "y":
                chance = random.randint(1,10)
                if chance < 8:
                    points += 750
                    print("You earned 750 points")
                else:
                    points = points/2
                    print("Your points were cut in half")
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")
        elif randomEvent < 15: #15%
            #Event 4
            print("You find food on the ground (earn 500 points)")
            points += 500
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")
        else:                   #25%
            #Event 5
            enemyAtk = random.randint(1,3)#LightAttack, HeavyAttack, Block
            print("You encounter an enemy snail!")
            print("Choose something to do:")
            print("1 for Light Attack")
            print("2 for Heavy Attack")
            print("3 for Block")
            userInput = int(input(""))

            while userInput != 1 and userInput != 2 and userInput !=3:
                userInput = int(input("Please enter a valid option"))

            while userInput == enemyAtk:
                
                if userInput == 1:
                    print("Both you and the enemy light attack. Nobody is injured")

                elif userInput == 2:
                    print("Both you and enemy heavy attack. Nobody is injuerd")

                else:
                    print("Both you and the enemy block. Nobody is injured")
                enemyAtk = random.randint(1,3)
                userInput = int(input("Choose another attack (1,2,3):"))

            if userInput % 3 + 1 == enemyAtk:

                if userInput == 1:
                    print("The enemy heavy attacks but you hit it first with a light attack")

                elif userInput == 2:
                    print("The enemy blocks but you penetrate it with the heavy attack")

                else:
                    print("The enemy light attacks but you block it defeating the enemy")
                print("You successfully defeat the enemy and you gain 1000 points")
                points += 1000

            elif enemyAtk % 3 + 1 == userInput:

                if userInput == 1:
                    print("The enemy blocks your light attack and defeats you")

                elif userInput == 2:
                    print("The enemy light attacks and hits you first defeating your heavy attack")

                else:
                    print("The enemy heavy attacks and breaks your block to defeat you")
                print("You are defeated by the enemy snail. You lose 200 points")
                points -= 200
            print("{0:>40s}{1:.2f}".format("Points:",points))
            print("")   
        eventCounter += 1
        
#BOSS BATTLE
print("You encounter the Boss of the level. The giant snail lunges towards you")
PlayerHlth = 3
BossHlth = 3

while PlayerHlth != 0 and BossHlth != 0:
    time.sleep(3)
    enemyAtk = random.randint(1,3)#LightAttack, HeavyAttack, Block
    print("Choose something to do:")
    print("1 for Light Attack")
    print("2 for Heavy Attack")
    print("3 for Block")
    userInput = int(input(""))

    while userInput != 1 and userInput != 2 and userInput !=3:
        userInput = int(input("Please enter a valid option "))

    while userInput == enemyAtk:
        
        if userInput == 1:
            print("Both you and the enemy light attack. Nobody is injured")

        elif userInput == 2:
            print("Both you and enemy heavy attack. Nobody is injuerd")

        else:
            print("Both you and the enemy block. Nobody is injured")
        enemyAtk = random.randint(1,3)
        userInput = int(input("Choose another attack (1,2,3): "))

    if userInput % 3 + 1 == enemyAtk:

        if userInput == 1:
            print("The enemy heavy attacks but you hit it first with a light attack damaging the enemy")

        elif userInput == 2:
            print("The enemy blocks but you penetrate it with the heavy attack damaging the enemy")

        else:
            print("The enemy light attacks but you block it damaging the enemy")
        BossHlth -= 1
        print("Boss Health:",BossHlth)
        print("Player Health:", PlayerHlth)
    elif enemyAtk % 3 + 1 == userInput:

        if userInput == 1:
            print("The enemy blocks your light attack and damages you")

        elif userInput == 2:
            print("The enemy light attacks and hits you first defeating your heavy attack damaging you")

        else:
            print("The enemy heavy attacks and breaks your block to damage you")
        PlayerHlth -= 1
        print("Boss Health:",BossHlth)
        print("Player Health:", PlayerHlth)

if PlayerHlth == 0:
    print("You lost the Boss Battle and do not earn points")
    print("")
    print(characterName, "You completed the game with",points, "points")
else:
    print("You defeated the Boss and earn 2000 points")
    points += 2000
    print(characterName, "You completed the game with",points, "points") 

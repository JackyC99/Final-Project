 # The script of the game goes in this file.

init:

     python:
           import random
define config.name = _('Tree Owner')

define gui.show_name = True

define config.version = "1.0"

define gui.about = _("Created by Jacky Chen(Freshman).\n\nI do not own most of the image and photos used in this project.\n\nAll the credits for the image are on Github, in ReadMe\nhttps://github.com/JackyC99/Final-Project.")

define e = Character("Narrator")
define b = Character("Boss")
define c = Character("clerk")
define water = 75
define day = 1
define growth = 0
define coins = 100
define earned = 0

image boss = "Speedwagon.png"
image black = "#000"
image bg tiled = Tile("tile.jpg")  

image Cashier = "Cashier.png"
image black = "#000"
image bg tiled = Tile("tile.jpg")
     
label start:


    scene bg forest


    image sap = "sapling.png"
    image black = "#000"
    image bg tiled = Tile("tile.jpg")

    image sap2 = "sap2.png"
    image black = "#000"
    image bg tiled = Tile("tile.jpg")

    image sa3 = "sap3.png"
    image black = "#000"
    image bg tiled = Tile("tile.jpg")

    image sap4 = "Tree.png"
    image black = "#000"
    image bg tiled = Tile("tile.jpg")

    show sap 
    e "Here is a sapling."
    e "Now take care of it."
    e "If you're wonding why I'm telling you to do it."
    e "It's because you decided to play this"
    e "So Enjoy"
    

    label cycle:
        scene bg house
        "Day [day]"
        if growth < 25:
            show sapling 
        if growth >= 25 and growth < 50:
            show sap2
        if growth >= 50 and growth < 75:
            show sap3
        if growth >= 75 and growth < 99:
            show spa4

        e "Your tree is [growth]\% finish growing"
        e "Your water level is at [water]"
        e "You currently have [coins] coins on you."
        if growth == 100:
            jump end
        e "Morning."
        e "What would you like to do for the day"
        menu:
            "Sleep":
                 jump accomplish

            "Water the plant for 15 coins":
                 call water

            "Work":
                 jump office
        jump days
   
    label water:
        if coins >= 15:
            $coins = coins - 15
            e "You spent 15 coins"
            $ water = water + random.randint(2,5)
        else:
           e "You don't have enough to water the plant."
        e "Your water level is at [water]\%"
    jump options

    label accomplish:
        scene bg bedroom
        e "You slept"
        if water <= 25:
            $growth = growth + random.randint(1,2)

        elif water > 25 and water <= 50:
            $growth = growth + random.randint(3,5)

        elif water > 50 and water <= 75:
            $growth = growth + random.randint(7,9)

        elif water > 75 and water <= 100:
            $growth = growth + random.randint(10,12)

        else:
            $growth = growth - 5
        

    label days:
        $ day += 1
        $ water = water - random.randint(2,4)
        jump cycle
       
    
label options:
    e "Now what are you going to do?"
    menu:
        "Sleep":
            jump accomplish
        "Go to Work":
            jump office
        

    label office:
        scene bg office 
        e "You should get to work"
        $flip = random.choice(["H","T"])
        if flip == "H":
          $water = water - random.randint(2,5)
        else:
          $water = water - 1

        if growth <= 25:
            $earned = earned + random.randint(18,22)
        elif growth > 25 and growth <= 50:
            $earned = earned + random.randint(14,18)
        elif growth > 50 and growth <= 75:
            $gearned = earned + random.randint(8,14)
        elif growth > 75 and growth <= 100:
            $earned = earned + random.randint(3,8)

        menu:
            "Ask for raise":
                 call extra
            "Talk with co-worker":
                 e "You talked with your coworkers"
                 e "And you left for the day"
                 jump night
        
    label extra:
        scene bg bossroom
        show boss

        b "What do you want?"
        $bonus = 0
        $flip = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        if flip == 1:
          $bonus = bonus + random.randint(4,8)
          e "You gained a [bonus] coin bonus"
          b "You have been working hard, so..."
        elif flip == 2:
          $ebonus = bonus + random.randint(10,15)
          e "You gained a [bonus] coin bonus"
          b "I like you a lot, maybe I should give you a raise"
        else:
          $bonus = bonus + 0
          e "You didn't get any bonus"
          b "Maybe next time."
        $earned = earned + bonus
        $bonus = 0
     
    label night:
       scene bg street
       e "Good job"
       e "You earned [earned] coins for the day"
       $coins = coins + earned
       $earned = 0
       e "What is your plan now?"
       menu:
            "Sleep":
                 jump accomplish
            "Shop":
                 jump store
    
    label store:
        scene bg store
        
        show Cashier  
        c "Welcome, what woukd you like today."
        menu:
            "Nothing":
                jump accomplish
            "Rob the place":
                jump bad_end
            "I'm hungry":
                jump stock
    
    label stock:
        $Thing1 = ""
        $Thing2 = ""
        $price1 = 0
        $price2 = 0
        $stocks = {1:"bread", 2:"soda"}
        $prices = {"bread":10, "soda":5}
        $s1 = random.randint(1,2)
        $s2 = random.randint(1,2)
        $Thing1 = stocks.get(s1)
        $Thing2 = stocks.get(s2)
        $price1 = prices.get(Thing1)
        $price2 = prices.get(Thing2)
        menu:
            "Do you want [Thing1] which cost [price1]":
                 
                 if coins >= price1:
                    $coins = coins - price1
                 e "You bought [Thing1] for [price1]"
                 e "You now have [coins] coins left"
            "Or do you want [Thing2] which cost [price2]":
                 if coins >= price2:
                    $coins = coins - price2
                 e "You bought [Thing2] for [price2]"
                 e "You now have [coins] coins left"
        e "Now lets go home"
        jump accomplish

label end:
    scene bg TreasureTree
    e "Congrats, your tree is fully grown"
    e "and it only took you [day] days to grow it."
    e "That must be some sort of record."
    e "Would you like to play again?"
    menu:
        "Yes":
          $ water = 75
          $ day = 1
          $ growth = 25
          jump cycle
         
        "No":
          return

        "Credits":
            jump start

label bad_end:
    e "If you get caught,"
    e "There is nothing I can do, so"
    $ MainMenu(confirm=False)()

    
    


define player = Character("You")
define lonn = Character("Mr. Lonn")
define kelpie = Character("Kelpie")
define drey = Character ("Drey")
define heom = Character ("Heom")
define perr = Character("Miss Perr")
default k=0
label start:
    "You ride your bike past the towering skyscrapers that rise all around you while trying to catch a glimpse of the opening day of \"The Roadroller\"."
    "\"The Roadroller\" is a state of the art immersive arcade which has basically everything including an entire indoor pool and also zero gravity chambers."
    "But you are already late for your new part time job at Lonn's Pizzeria. You need the money to earn a ticket into \"The Roadroller\"."
    "You can see the pizzeria in all its glory from outside. It is also equipped with an outdoor pizza oven!"
    lonn "There-a you are! I have-a been waiting for you!"
    "You notice that Mr. Lonn has a very very mario-esque accent but you choose to ignore it."
    lonn "Follow-a me! I'll help-a you get used to my meraviglioso pizzeria!"
    "You follow Mr. Lonn inside."
    "The pizzeria is deserted at this time of the hour. It only officially opens at 10."
    lonn "Please-a! Take a seat-a here. I'll be back with my dear friend Kelpie who will-a be helping you today!"
    "Mr. Lonn goes into the kitchen."
    jump alone
label alone:
    menu:
        "What do you want to do?"
        "Follow Mr. Lonn into the kitchem." if k==0:
                jump kitchen
        "Look around the lobby.":
            jump lobby
        "Sit and wait.":
            jump kelpie
label kitchen:
    $ k=1
    "You creep behind Mr. Lonn quitely, hiding the thud of your footsteps with his."
    "You duck behind a towering rake of baguettes waiting to be baked."
    lonn "He's here-a Kelpie! I want-a you to teach him how to make a pizza by the end of the day."
    lonn "I'll be in the cheese-a room if you need me."
    kelpie "Yep! You got it. I'll just finish making the margherita for today. He wouldn't mind right?"
    menu:
        "What do you want to do?"
        "Stay hidden and observe Kelpie.":
            jump margherita
        "Quietly follow Mr. Lonn into the cheese room.":
            jump cheese
        "Go back to the lobby and wait for Kelpie to be done":
            jump alone

label lobby:
    "You walk around the lobby taking in everything."
    "There's a bunch of tables that spill out the side door which also leads to the outdoor seating."
    "The walls are lined with a lot of medals and a huge trophy shaped like a pizza is hung over the cash register."
    "There are multiple other doors in the sides."
    menu:
        "What do you do?"
        "Go out the backdoor.":
            jump backdoor
        "Explore what the sidedoors offer.":
            jump sidedoor
        "Stay put and wait for Kelpie":
            jump kelpie
label kelpie:
label margherita:
label cheese:
label backdoor:
label sidedoor:

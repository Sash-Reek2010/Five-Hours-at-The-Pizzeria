
define player = Character("You")
define lonn = Character("Mr. Lonn")
define kelpie = Character("Kelpie")
define drey = Character ("Drey")
define heom = Character ("Heom")
define perr = Character("Miss Perr")
default persistant.haskey = False
default persistant.rackclimber = False
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
    "The kitchen is as magnificent as the entire pizzeria. There's a line of racks along the entire wall and a lot more near the main door of the kitchen."
    "There's shelves and shelves of ingredients from possibly every corner of the universe."
    "The amazing smell of oregano hits your nose like a roadroller on freshly lain tar."
    "You do notice something creepy. There's barely anyone inside this HUGE room. Its you and Mr. Lonn and one more person."
    "This gives you a bad feelind."
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
            "You slowly retrace your steps outside the kitchen and end up in the lobby."
            jump alone

label lobby:
    "You walk around the lobby taking in everything."
    "The lobby is a really huge sphere with a low ceiling."
    "The walls are painted the colors of Italy - Red, White and Green with huge paintings of pizza toppings!"
    "The main desk is on the far side of the lobby exactly opposite to the main door. The kitchen door is behind the main desk."
    "There's a huge menu on the side with nearly every topping you could think of!"
    "A bunch of tables spill out the side door which also leads to the outdoor seating."
    "The walls are lined with medals and a huge trophy shaped like a pizza is hung over the cash register."
    "There are multiple other doors leading to various different rooms."
    "You suddenly get this weird creepy feeling when you look at one specific battered old door."
    menu:
        "What do you do?"
        "Go out the sidedoor.":
            jump sidedoor
        "Explore what the other doors offer.":
            jump secretdoor
        "Stay put and wait for Kelpie":
            jump kelpie
label kelpie:
    kelpie "Hello! I'm Kelpie! What's your name?"
    "Kelpie is wearing a comical apron on which makes him look tinier than he is."
    $name = renpy.input(default='You', prompt="What is your name?")
    kelpie "Nice to meet you [name]!"
    kelpie "Alright! So do you want to jump straight into making a pizza or you want me to show you around?"
    menu:
        "What do you want to do?"
        "Look around with Kelpie.":
            jump lookaround
        "Learn to make pizza with Kelpie.":
            jump pizza
label margherita:
    "You decide to stay hidden. Mr. Lonn walks into the cheese room and you catch a whiff of the musty smell inside, belch!"
    "Kelpie starts by dragging in a sack of tomatoes and he starts washing each one."
    "You get increasingly bored as Kelpie keeps washing an endless amount of tomatoes"
    player "No way people eat this much pizza a day."
    kelpie "HUH! WHO'S THERE?"
    "Kelpie walks over to the baguette rack."
    menu:
        "Climb up the rack and hide from Kelpie":
            if persistant.rackclimber = False:
                jump monkeybusiness
            else:
                jump hidden
        "Let Kelpie catch you":
            jump freekitchen
label monkeybusiness:
    "You try climbing over the rack but because of your bad upperbody strength you fall."
    "Kelpie grabs you by the collar and shakes you violently."
    kelpie "HEY! Who are you?"
    player "I'm the new guy."
    "Kelpie lets go of you."
    kelpie "Oh! I'm really sorry! I thought you were trying to rob the store."
    kelpie "Well, why were you snooping around here. I would've been more than happy to show you around."
    "Kelpie quickly cleans up the counter and leads you out the kitchen."
    $ persistant.rackclimber = True
    jump lookaround
label freekitchen:
    "You wait for Kelpie to catch you but right when he comes by, the cheese room door bursts open."
    lonn "There's a disaster here-a! We are out of milk."
    "Kelpie runs off into the cheese room."
    "You are alone in the kitchen now"
    menu:
        "What do you do? CHOOSE FAST!!!!!"
        "Explore the kitchen":
            jump kitchenexplore
        "Go back to the lobby":
            "You slowly walk back to the lobby."
            jump alone

label cheese:
    "You hide behind the shadows and make your way toward the cheese room. The smell is unbearable but you manage to not pass out."
    lonn "Come on Drey! Fetch-a me the cheese paddle. I want to check how good the cheese is."
    drey "Right away!"
    "The cheese room is probably the smallest room in the entire pizzeria. There's barely enough space to walk around because of the HUGEEE shelves."
    "Upon closer inspection, you notice that the shelves are fully occupied by parmesan wheels waiting to age."
    "You can see large vats of milk on either side of the entrance being paddled by giant robotic arms."
    lonn "DREY!! Where's-a my paddle!!"
    "There is an eerie silence in the cheese room except for the splash of the paddles."
    lonn "That little-a kid."
    "Mr. Lonn rushes to the back of the cheese room where there's a little door. Persumably leading to the cold storage."
    menu:
        "What do you do?"
        "Follow Mr. Lonn":
            jump storage
        "Go back to the lobby.":
            "You silently move back into the kitchen."
            kelpie "HEY! Who are you?"
            "Kelpie grabs you by the collar and shakes you violently."
            "You did't notice Kelpie behind you."
            player "I'm the new guy."
            "Kelpie lets go of you."
            kelpie "Oh! I'm really sorry! I thought you were trying to rob the store."
            kelpie "Well, why were you snooping around here. I would've been more than happy to show you around."
            "Kelpie quickly cleans up the counter and leads you out the kitchen."
            jump lookaround
label secretdoor:
    "You start opening doors at random."
    "One door leads to the broom closet."
    "Another one takes you up a set of stairs into the terrace of the pizzeria."
    "One more door brings you out the main entrance again."
    "You finally reach the weird door."
    if persistant.haskey==False:
        "You try the handle but it doesn't give way."
        "It's locked."
        "Maybe there's a key to it somewhere!"
    else:
        jump secretencounter
        
label sidedoor:
    "You walk toward the sidedoor and go out."
    "You can hear wood splintering near you and the smell of firewood is in the air."
    "Around the corner is the massive outdoor pizza oven!"
    "You evade all the near tables in the grass and walk toward the oven."
    heom "Hello! You must be the new guy. I'm Heom!."
    "A girl wearing an apron walks out a door behind the oven."
    heom "I'm in charge of this beaut here."
    "She points to the oven."
    heom "So, what made you want to join the pizzeria?"
    menu:
        "What do you say?"
        "I'm saving up for \"The Roadroller\".":
            jump roadrollerfanbase
        "I was bored at home.":
            jump boredheom
        "My parents wanted me to get a job.":
            jump boredheom

label lookaround:
label pizza:
label hidden:
label kitchenexplore:
label storage:
label secretencounter:
label roadrollerfanbase:
label boredheom:
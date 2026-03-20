
default name="You"
define player = Character("[name]")
define lonn = Character("Mr. Lonn")
define kelpie = Character("Kelpie")
define drey = Character ("Drey")
define heom = Character ("Heom")
define perr = Character("Miss Perr")
default persistent.haskey = False
default persistent.rackclimber = False
default k=0
default has_been_in_cheese=False
default has_met_kelpie=False
default milk=False
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
    kelpie "Yep! You got it. I'll just finish making the marinara for today. He wouldn't mind right?"
    menu:
        "What do you want to do?"
        "Stay hidden and observe Kelpie.":
            jump marinara
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
            $kelp=0
            jump sidedoor
        "Explore what the other doors offer.":
            jump secretdoor
        "Stay put and wait for Kelpie":
            jump kelpie
label kelpie:
    $has_met_kelpie=True
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
label marinara:
    "You decide to stay hidden. Mr. Lonn walks into the cheese room and you catch a whiff of the musty smell inside, belch!"
    "Kelpie starts by dragging in a sack of tomatoes and he starts washing each one."
    "You get increasingly bored as Kelpie keeps washing an endless amount of tomatoes"
    player "No way people eat this much pizza a day."
    kelpie "HUH! WHO'S THERE?"
    "Kelpie walks over to the baguette rack."
    menu:
        "Climb up the rack and hide from Kelpie":
            if persistent.rackclimber==False:
                jump monkeybusiness
            else:
                jump hidden
        "Let Kelpie catch you":
            jump freekitchen
label monkeybusiness:
    "You try climbing over the rack but because of your bad upperbody strength you fall."
    "Kelpie grabs you by the collar and shakes you violently."
    $has_met_kelpie=True
    kelpie "HEY! Who are you?"
    player "I'm the new guy."
    "Kelpie lets go of you."
    kelpie "Oh! I'm really sorry! I thought you were trying to rob the store."
    kelpie "Well, why were you snooping around here. I would've been more than happy to show you around."
    "Kelpie quickly cleans up the counter and leads you out the kitchen."
    kelpie "So, what's your name?"
    $name=renpy.input(default='You', prompt="What is your name?")
    kelpie "Nice to meet you [name]!"
    $ persistent.rackclimber==True
    jump lookaround
label freekitchen:
    "You wait for Kelpie to catch you but right when he comes by, the cheese room door bursts open."
    lonn "There's a disaster here-a! We are out of milk."
    "Kelpie runs off into the cheese room."
    "You are alone in the kitchen now"
    menu:
        "What do you do?"
        "Explore the kitchen":
            jump kitchenexplore
        "Go back to the lobby":
            "You slowly walk back to the lobby."
            jump alone

label cheese:
    $has_been_in_cheese=True
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
            $has_met_kelpie=True
            kelpie "HEY! Who are you?"
            "Kelpie grabs you by the collar and shakes you violently."
            "You did't notice Kelpie behind you."
            player "I'm the new guy."
            "Kelpie lets go of you."
            kelpie "Oh! I'm really sorry! I thought you were trying to rob the store."
            kelpie "Well, why were you snooping around here. I would've been more than happy to show you around."
            "Kelpie quickly cleans up the counter and leads you out the kitchen."
            kelpie "So, what's your name?"
            $name=renpy.input(default='You', prompt="What is your name?")
            kelpie "Nice to meet you [name]!"
            jump lookaround
label secretdoor:
    "You start opening doors at random."
    "One door leads to the broom closet."
    "Another one takes you up a set of stairs into the terrace of the pizzeria."
    "One more door brings you out the main entrance again."
    "You finally reach the weird door."
    if persistent.haskey==False:
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
    kelpie "So! This is the lobby. The floor waiters only come here after 6 because we offer fine dining for dinners here."
    "Kelpie takes you into the kitchen."
    kelpie "This is the kitchen! We make everything here."
    kelpie "Then up next is the cheese room, my favourite place in the entire pizzeria! Follow me."
    "He leads you toward the cheese room door when suddenly it bursts open!"
    lonn "WE ARE OUT OF MILK!!!!!!"
    $milk=True
    kelpie "I think I should go handle this. Why don't you go out the side door and meet Heom there."
    "You are back in the lobby."
    jump sidedoor
label roadrollerfanbase:
    heom "NO WAY! I'm here for the same thing! I usually run the pizza bake for my school but they don't pay me nearly as much as Mr. Lonn does."
    heom "I'm so glad you're here! No offence but Kelpie isn't really a big Roadroller fan."
    "You smile, you are also glad you met someone with the same interests."
    heom "So, what's the first game you're playing there......"
    "You two spend about two hours yapping about \"The Roadroller\""
    heom "Okay, I think I must get back to work. This was nice."
    "You go back into the lobby."
    kelpie "There you are! I sorted the milk situation. Want to work on your pizza skills now?"
    jump pizza
label boredheom:
    heom "Oh, thats nice. I personally am here to save up for \"The Roadroller\"."
    "You are dissapointed that you missed your chance to make a friend."
    heom "Anyway, I have to get going. Catch you later?"
    menu:
        "What do you do?"
        "Go back to the lobby.":
            "You walk back to the lobby."
            kelpie "There you are! I sorted the milk situation. Want to work on your pizza skills now?"
            jump pizza
        "Explore the outdoor seating.":
            "You walk around the over and find two other doors."
            if c==1:
                "The door leads into the cheese room. You aren't very keen on going inside."
                "The other door meanwhile leads into greenhouse."
                jump greenhouse
            else:
                "The door leads into the cheese room. You walk inside."
                jump latercheeseroom
label latercheeseroom:
    if not has_met_kelpie:
        $has_met_kelpie=True
        kelpie "Hello! I'm Kelpie! What's your name?"
        "Kelpie is wearing a comical apron on which makes him look tinier than he is."
        $name = renpy.input(default='You', prompt="What is your name?")
        kelpie "Nice to meet you [name]!"
        kelpie "I'm afraid there is a milk situation here. Please wait in the lobby for me."
        $milk=True
        "You walk back to the lobby."
        kelpie "There you are! I sorted the milk situation. Want to work on your pizza skills?"
    else:
        kelpie "Oh you're back. I'm afraid the cheese situation is still ongoing. Wait in the lobby will you?"
        "You can hear angry italian noises coming from the back of the cheese room."
        menu:
            "What do you do?"
            "Stay in the cheese room.":
                jump cheesestay
            "Go back to the lobby":
                "You walk back to the lobby."
                kelpie "There you are! I sorted the milk situation. Want to work on your pizza skills now?"
                jump pizza
label pizza:
    kelpie "Alright! Follow me into the kitchen!"
    if not milk:
        "You go with Kelpie into the kitchen."
        "Suddenly the door in the corner bursts open."
        lonn "WE ARE OUT OF MILK!!!!"
        kelpie "I better go deal with this. Stay here for a while."
        jump stuffhappen
    else:
        "He leads you infront of the huge marble counter and hands you a measuring scale."
        kelpie "The first thing you'll need to know is to measure."
        "He spends a long time talking about measurements and you totally zone out."
        kelpie "Alright! I feel like you got all that. You're quite the natural you know?"
        kelpie "Okay! It's time to finally start making a pizza."
        "He brings out a tub of marinara, and a tray of pizza dough balls."
        kelpie "I'll make the pizza first and then I'll let you make your own!"
        "He takes the ball of dough and plops it on the marble which already has a bunch of semolina on it."
        kelpie "You first make the balls into a really thin base."
        kelpie "Then you add the marinara. The premeasured scoops will really be a good help here."
        kelpie "Now its time for the CHEESE! My favourite part of the pizza making!"
        "He grabs a fistfull of shreded cheese and showers it all over the pizza. Then he adds the basil leaves."
        kelpie "Me personally, I only like basil on my pizza but feel free to make whataver you like!"
        "Suddenly Kelpie's face drops. He stares into your eyes."
        kelpie "Just don't ever go into the cheese room without me knowing."
        if has_been_in_cheese:
            kelpie "You went in right?"
            "Kelpie becomes slightly aggressive."
            kelpie "Did you?"
            player "..........no"
            kelpie "Is that so?......."
        kelpie "Anyway, I'll be outside near the oven. Make your pizza quickly and I'll taste test it."
        "You are a bit scared of Kelpie."
        "But you get the sudden urge to go into the cheese room."
        menu(time=4.0, timeout="kelpiecatch"):
            "What do you do? CHOOSE FAST!"
            "Go into the cheese room":
                jump cheeseagain
            "Stay in the kitchen.":
                jump pizzamore
label kelpiecatch:
label cheeseagain:
label pizzamore:
label greenhouse:
label hidden:
label kitchenexplore:
label storage:
label secretencounter:
label stuffhappen:
label cheesestay:
    $has_been_in_cheese=True

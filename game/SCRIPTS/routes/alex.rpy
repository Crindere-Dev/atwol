label alexroute:
    scene bg locker
    "You walk into school as you nod your head to your music."
    "Not knowing one of the most popular kids has caught you by the eye."
    "He stares at you as you make your way down the hallway."
    "He calls out to you."
    q "Yo,"
    "You turn to look for where the low rough voice came from."
    show alexnormal with easeinbottom
    q "Nice clothes you are wearing, you seem like you are rich enough to hang with us. "
    "You turn to see a boy with black hair -the hair dyed red at the front- piercings and a scar on his cheek."
    "You look at him, not knowing what to say."
    you "Ummm, thanks?"
    q "What's your name?"

python:
    name = renpy.input("What is your name?", length=32, screen=u'input')
    name = name.strip()

    if not name:
        name = "Dumbass"
    
you "[name]?"
hide alexnormal
show alexsmile
q "Nice name cupcake,"
al "The name's alex, don't forget it."
"You think to yourself in confusement, Cupcake?"
you "Ok?"
you "It's almost class, I gotta get going."
hide alexnormal
"You turn and walk away, not before hearing whispers from all across the hall."
"I wish Alex complimented me."
"you whisper under your breath:"
you "Hes so weird."

    
scene black with dissolve
"You make your way to your class and sit down, waiting for the teacher to arrive."

"5mins later..."
"..."
"Your Teacher arrives and puts their stuff down, taking a quick look around the classroom to see who is here and who will be in trouble."
"Alex arrives a minute late, Your Teacher scolds him for being late."
show alexsus with easeinbottom
"{color=#a39bec}Teacher{/color}" "Ugh! Why are you late? You should have been here before me!"
you "Honestly, he looks like somebody who would be late."
hide alexsus
show alexsmile
al "Sorry teach, I was just chatting it up with the boys."
"Alex stood with amazing confidence that you swear you could feel a warm glow."
"{color=#a39bec}Teacher{/color}" "Yes, of course"
"{color=#a39bec}Teacher{/color}""Just like every other day, your punishment will be a written apology during lunch break."
hide alexsmile
show alexsus
"You think to yourself,"
you "I mean, new school year, new me."
you "Maybe I should help him?"

menu:
    "Should you stand up for Alex?"
    "Yes":
        $ alpoints =+1
        "You stand up, mentally begging that this works."
        you "Ms, Alex was helping his friends get to the nurses office."
        you "It's not right for him to be punished for such a good dead."
        "{color=#a39bec}Teacher{/color}" "Is that so? Well Alex, you're free to go."
        hide alexsus
        show alexsmile2
        "Alex sends a grin your way as he goes to sit down."
        hide alexsmile2
        

    "No":
        hide alexsus
        show alexnormal

        al "Yeah yeah whatever."
        "He goes to sit down at his desk."
        hide alexnormal


label lunchtime:
    scene black
    "You sit idly, listening to your teacher waffle about Romans."
    play audio "damn.wav" volume 2.0
    "You then hear a quiet notification coming from your phone."
    "You hide your phone underneath your desk and cautiously check the message:"
label phone:

    call phone_start
    call message_start("Alex", "Yo ;)")
    call message("Alex", "wanna hangout with me and the boys during lunch?")
    call reply_message("How did you get my number.")
    call message("Alex", "dont worry bout that :)")
    call reply_message("??")
    return
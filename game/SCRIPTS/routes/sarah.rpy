label sarahroute:
    scene bg locker
    q "Hey!"
    "A voice called out, a very annoying one, in fact. "
    show sarahsmile with easeinbottom
    q "Hey!!!" 
    "You turn to see a girl with bright pink hair and a bright smile."
    q "I see that you are an Anti-Gacha Chan fan too!! I’m happy I’m not the only one!!" 
    "The girl squealed."
    you "Um yeah, I guess?"
    "You looked at her with a confused look on your face"
    hide sarahsmile
    show sarahnorm
    s "What’s your name? I’m Sarah!"
    "She asked curiously."

python:
    name = renpy.input("What is your name?", length=32, screen=u'input')
    name = name.strip()

    if not name:
        name = "Dumbass"

you "I’m [name], nice to meet you..?"
hide sarahnorm
show sarahsmile
s "Ok! I gotta get going now! It was nice meeting you!"
"She waved as she left."
hide sarahsmile with dissolve
you"..."
you "What the fuck what that about?"


   



    
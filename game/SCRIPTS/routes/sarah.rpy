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
s "What a cool name!"
s "Ok! I gotta get going now! It was nice meeting you!"
"She waved as she left."
hide sarahsmile with easeoutright
you"..."
you "What the fuck was that about?"

scene black with dissolve
"You make your way to your class and sit down, waiting for the teacher to arrive."

"5mins later..."
"..."
"Your Teacher arrives and puts their stuff down, taking a quick look around the classroom to see who is here and who will be in trouble."
"Sarah arrives a minute late, Your Teacher scolds them for being late."
"{color=#a39bec}Teacher{/color}" "Ugh! Why are you late? You should have been here before me!"
you "You think to yourself: How is she late?"
you "She literally went to class before me!"
show sarahsus with dissolve
s "Sorry Mrs Gonal, I was distracted by a book this morning."
s "... Hehe."
"Sarah stood like a whimpering dog in the cold."
"{color=#a39bec}Teacher{/color}" "{b}Sigh,{/b}yes of course you were, you always are."
"{color=#a39bec}Teacher{/color}""This time the punishment is a written apology during your lunch break."
"Maybe you should be selfless for once, do you stand up for Sarah?"
menu:
    "Stand up for Sarah":
        "You hastily jot down teachers note on a loose peace of paper and forges one of your teachers signitures.."
        "You stand up and crosses your fingers that it will work."
        you "Hey, Miss? I forgot to give you this."
        you "Sarah was busy with Mr Jamesy and he told me to give you this note as an excuse for her lateness."
        you "You think to yourself: Please, Please work!"
        "Your teacher skims your note and puts it down."
        "{color=#a39bec}Teacher{/color}" "I see, well then Sarah, I’ll give you your lunch back."
        hide sarahsus
        show sarahsmileblush
        s "Sarah looks at you with a smile on her face, as it she was thanking you silently."
        $ spoints =+ 1

    "Stay quiet.":
        hide sarahsus
        show sarahsmile
        "Sarah sat down at her desk two in front and one to the left of you."
        "She looked rather happy after being punished. What’s up with that?"
    


# “Sorry (teacher) I was distracted by a book this morning.” Sarah stood like a whimpering dog in the cold. (Teacher) sighed “yes of course you were, you always are. This time the punishment is a written apology during your lunch break miss”

   



    
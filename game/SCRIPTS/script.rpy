default Her = "Her"
default her = "her"
default She = "She"
default she = "she"
default Hers = "Hers"
default hers = "hers"
default Herself = "Herself"
default herself = "herself"
default sarah = False
default alex = False
image sarahnorm = "sarahnormal.png"

define a = Character("Ava",
                    who_color="#e7e6ff", callback = callback)

define s = Character("Sarah",
                    who_color="#a39bec", callback = callback)

define you = Character("You",
                    who_color="#a39bec", callback = callback)

define q = Character("???",
                    who_color="#a39bec", callback = callback)


label splashscreen:
 scene black
with Pause (1)

show splashscreen with dissolve
with Pause(2)
hide splashscreen with dissolve

return

label start:
 stop music

 scene black

 "You wake up and lazily get out of bed."
 "You walk over to your bathroom and stare at your mirror."

scene bg mirror
"...and you see yourself."
"What is your Gender?"

label gender:
    
call screen gender with dissolve


label girl:
    scene bg mirror with dissolve
    "You're a girl?"
    menu:
        "yes":
            $ girl = True
            jump stage2
        "no":
            jump gender
        
      
        

label boy:
    "You're a boy?"
    menu:
        
        "yes":
            $ Her = "His"
            $ her = "his"
            $ She = "He"
            $ she = "he"
            $ Herself = "Himself"
            $ herself = "himself"
            jump stage2
        "no":
            jump gender

label nb:
    "You're non binary?"
    menu:
        
        "yes":
            $ Her = "Them"
            $ her = "them"
            $ She = "They"
            $ she = "they"
            $ Herself = "Themself"
            $ herself = "themself"
            jump stage2
        "no":
            jump gender

label stage2:
    scene bg mirror with dissolve
    you " First day of school, huh? Summer flew by so quickly."

    "You brush your teeth quickly and take a shower, walking back to your room afterwards."
    scene bg bed
    " You dry yourself off with a towel then look to see two options on what you can wear today."
    menu clothes:
        "What clothes should you wear today?"
        " A blue “Anti Gacha Chan” jumper with some average jeans and white converses.":
            $ sarah = True
            
        "A plain white hoodie with “owo” plasted on the front with black pants and white jays.":
            $ alex = True
        
"You grab your phone and look at the time."
"Oh shit! You’re late!"
"You grab your bag from the other side of the room and bolt out of your bedroom doorway and through your front door."
scene bg bus with dissolve
"You run down your street, trying to be quick as you can to get a seat on the bus."
"You twist and turn, your bag flying in your hand."
"You barely make it to the bus..."
"You gasp for air as you try to find a seat on the full bus. "

"You sit down at a window seat and plug in your headphones as the bus heads to school."

scene black with dissolve
$ renpy.movie_cutscene('bago.ogv') 

scene black with dissolve
"You hop of the bus and start walking into the campus."

if alex == True:
    jump alexroute

if sarah == True:
    jump sarahroute
return
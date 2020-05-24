# Main game script.
#
# This file is where the whole script of the game is contained (characters, text, backgrounds and choices)
# Change log:
# v1.0 - Created the game - 24/05/20 - Group 2

# Character definition
# Arguments:
# * 1st: Character name (shown during dialogs)
# * 2nd: Character color (color of the title during dialog)
define g = Character("Group 2", color="EEEEEE")
define s = Character("Selena", color="9900FF")
define o = Character("Ortega", color="62A9FF")
define a = Character("Angela", color="9C9705")
define m = Character("Mariano", color="336600")

# Start of the game
label start:

    # Show the initial background (a dorm room)
    scene room

    # Initial dialogue
    g "Man... I need to finish this assignment already, or I'm going to fail this class!"
    
    "My name is Group 2, and I'm a computer sciences student.\nI have been asked to do an assignment for the Artificial Intelligence and Videogames subject."

    # Display a character (with a dissolve effect)
    # The character name is directly the image file (without extension)
    # The position in the screen can be specified
    show ortega at left with dissolve
    
    o "Let's do something funny! That will make everyone laugh!"
    
    show selena at right with dissolve
    
    s "No, of course not! We have to stick to the rules, the teacher told us to take this seriously."
    
    "Okay, this may look weird... let me explain."
    
    "I usually have many people debating in my mind about what I should do, and these are the two most prominent ones."
    
    "Ortega, the one who only wants to have fun,"
    
    "and Selena, the one that always tries to do everything right."
    
    o "But Selena, if you don't have fun doing your work, surely you don't believe that other people will have fun with what you do, right?"
    
    s "Nobody said you can't have fun while doing what the teacher asked you to do..."
    
    "You're probably asking yourself why is my mind in such a predicament. That's because the teacher asked me to create a Visual Novel in Ren'py, to test the technology."
    
    "This derived from a presentation I did about Visual Novels, in which I explained what they are and how they are useful to create a virtual world."
    
    o "Okay, sure... Well, I'm not going to say anything else. If you want to do something dull that's fine by me. I'm going to be sleeping for the rest of this Visual No- I mean, for the rest of the day. Have fun with whatever choice you make!"
    
    # Hides a character being shown on the screen
    hide ortega with dissolve
    
    s "Well... as I said earlier, you can make something fun while sticking to the proper thing. Whatever you choose, I'm fine with it."
    
    hide selena with dissolve
    
    # Creates a choice menu. Diferent choices can go to different places in the code
    menu:
        "This is quite a problem. I think I will..."
        
        # This works like a standard if else statement in Python
        # (depending on the choice taken, you enter one or another point)
        "Do something weird and funny that everyone will enjoy":
            # Instead of declaring the whole option inside the if, we can simply declare it outside as a label
            jump huge_meme
        
        "Create a serious Visual Novel and stick to what the teacher told me":
            jump serious_vn
    
    # Finish the game
    return
    
# Option 1 (Create a Meme VN)
# Labels can be seen as "methods" or tags. With a jump instruction, we can jump to any tag
label huge_meme:
    
    "Okay, I've decided, I think I'll make a huge meme."
            
    "I just have to be careful to stick to what the teacher told us, and everything will be fine..."
    
    scene black with dissolve
    
    "Some time later..."
    
    scene room night with dissolve
    
    "Okay, I think I have a great idea! I can do something amazing with this."
    
    "*ring ring*"
    
    "Huh? I hear my phone buzzing... who could be calling now?"
    
    show mariano with dissolve
    
    m "Hey, Group 2, is that you? Sorry to bother you, but I really need your help with the most important thing that I could ever ask you!"
    
    "This is Mariano. He's a childhood friend from my neighbourhood, we have been playing together since we were very young."
    
    "Normally, talking to him would be great... but right now, it is a big problem."
    
    "I need to start with the assignment right now, or I won't be able to finish it in time. And I just have 6 more hours to submit it!"
    
    g "I'm busy right now, what is the thing you need help with? Is it really that important?"
    
    m "There's an 80\% discount at the arcade right now! But only if you come with a friend... and you're the only one I can ask this."
    
    "Okay, he was right, this is VERY important. It's a once in a lifetime opportunity! It may never happen again! But I still have to finish the assignment..."
    
    m "So, what do you say? Are you coming? You're coming, right?!"
    
    menu:
        "I think I will..."
        
        "Stay in my room and continue working, the assignment comes first":
            jump huge_meme_stay_room
        
        "Go to the arcade with Mariano, friendship comes first":
            jump huge_meme_arcade
          
     # All label blocks must end with a return
    return

# Option 1 (Create a Meme VN) A (Continue working on the game)
label huge_meme_stay_room:
    
    g "Sorry Mariano, but I have a very important assignment to do for today. I can't come with you."
    
    m "Oh, come on! It will be fi-"
    
    hide mariano
    
    "I hang up the phone."
    
    "Okay, back to work!"
    
    scene black with dissolve
    
    "Some hours later..."
    
    scene room with dissolve
    
    "Finally, I did it... and I'm very happy with the result!"
    
    "Let's see what an expert thinks about it... Casually, I'm best friends with one of the most influential game reviewers in all history. Let me call her."
    
    "The phone rings and..."
    
    show angela with dissolve
    
    a "Yes? Oh, Group 2, is that you?"
    
    g "It's me, Angela. Can you check my assignment? I think I did something great!"
    
    a "Okay, let me check..."
    
    # You can change the expression of the character by displaying it again
    show angela happy 
    
    a "Wow, this is the best game I've ever seen! If you release it, I'm sure you'll become a millionaire - or even a billionaire - in a night! Want me to publish it real quick?"
    
    g "Yeah, sure, do it. All in a day's work."
    
    hide angela with dissolve
    
    "And that's how I became a trillionaire overnight. The game sold billions of copies seconds after being published."
    
    "It was published in all planets in our universe, and some collindant universes too."
    
    "Sadly... the game was not good enough for me to pass the subject."
    
    scene black with dissolve
    
    "36 years have passed since then."
    
    "I was finally able to pass the subject after spending all of the money I earned with the VN in courses and private teachers that helped me accomplish this."
    
    "Now, I just have to pass three more subjects... better start working on a new game!"
    
    "GOOD ENDING\n\n(BUT NOT GOOD ENOUGH TO PASS THE SUBJECT)"
    
    return
    
# Option 1 (Create a Meme VN) B (Go to the arcade with Mariano)
label huge_meme_arcade:
    
    g "Of course I'm going! You are my friend after all... and the discount is really good, I can't miss that."
    
    scene arcade with fade
    
    "We spent the whole six hours in the arcade. Time passed very quickly while we were here"
    
    scene room night with fade
    
    "Due to that, I arrived home very late..."
    
    g "There is no way I can finish my assignment now in time... I'll just leave it there and tell the professor what happened, he will surely understand."
    
    scene black with dissolve
    
    "36 years have passed since that moment."
    
    "The professor did not understand, and I had to leave the degree I was studying because I was not able to pass the subject after four years since I was not able to afford the fees."
   
    "Now I'm working as a waiter at a bar. Luckily, my life is not that bad after all..."
    
    "I mean, I only have to work 26 hours a day to pay for all of my arcade debts!"
    
    "ARCADE ENDING\n\n(YOU'LL FINISH PAYING IT... EVENTUALLY)"
    
    return

# Option 2 (Create a serious VN)
label serious_vn:
    
    "I have to take this more seriously! The teacher told me to make a specific thing, and I should stick to it."
    
    scene black with dissolve
    
    "Three hours later..."
    
    scene room night with dissolve
    
    "Thankfully, I progressed very quickly with the visual novel, and it is already almost halfway done. I can even have some free time after I finish it!"
    
    "*ring ring*"
    
    "I think I can hear my phone buzzing, but I was so focused on my work that I didn't notice"
    
    scene black with dissolve
    
    "Some time later..."
    
    scene room night with dissolve
    
    "Phew, I think it is done... I think this is good already, but I would like for someone else to check it. Thankfully, I'm friends with one of the most influent game reviewers in all history. I'll call her."
    
    "The phone rings and..."
    
    show angela with dissolve
    
    a "Yes? Group 2, is it you?"
    
    g "Hey Angela, it's me. Can you check my assignment? I think it's good, but I'm not that sure..."
    
    a "Okay, let me check it..."
    
    show angela dissapointed
    
    a "Yeah, it's fine, but it's not that great. Maybe if you change these 179 little things it could be better, but I suppose if it's just a class assignment it will be okay."
    
    g "Okay, thanks, I'll take your opinion into account"
    
    hide angela dissapointed
    
    "I hang the phone, and see that I have a missed call. I wonder who it is?"
    
    "It's a call from Mariano, my childhood friend. He has also sent me a text message, let me see..."
    
    show mariano
    
    m "Why do you even have a phone if you don't answer calls?! There's a discount at the arcade and I need to go with a friend, wanna come? ;) <3"
    
    "Taking a break sounds nice, but I should be dilligent and do all the improvements that Angela told me."
    
    menu:
        "I think I will..."
        
        "Do the improvements, I need to remain focused until the end":
            jump serious_vn_improvements
        
        "Go to the arcade with Mariano, I've already done what I was supposed to do":
            jump serious_vn_arcade
          
     # All label blocks must end with a return
    return

# Option 2 (Create a serious VN) A (Continue working on the game)
label serious_vn_improvements:
    
    "I'll continue improving my assignment. Since I'm already working on it..."
    
    scene black with dissolve
    
    "I spent the entire night working on the assignment."
    
    "The next day, Mariano was badmouthing me for not going to the arcade with him, and soon everyone sided with him."
    
    "In the end, I didn't pass the subject. This assignment was worth 0,001\% of the final grade, and it seems like there was no actual way to obtain the remaining score."
    
    "I was dissapointed... why did I work so hard for this?"
    
    "Apparently some big shots heard about my great perseverance, working hard and tirelessly for nothing in return, and I was awarded the Nobel Peace Prize for some reason I don't really understand."
    
    "I wish I could trade this prize for a passing mark..."
    
    "NOBEL ENDING\n\n(YOU MAY HAVE ACHIEVED WORLD PEACE, BUT YOU'RE STILL NOT PASSING THE SUBJECT)"
    
    return
    
# Option 2 (Create a serious VN) B (Go to the arcade with Mariano)
label serious_vn_arcade:
    
    "I'll go to the arcade with Mariano. I'm already tired of working on this assignment, so I'll just leave it like that."

    scene arcade with fade
    
    "We spent the entire night at the arcade, having lots of fun."
    
    scene room with fade
    
    "The next day, I got a fairly good mark on the assignment, but the teacher said it was not good enough to pass the subject."
    
    "Later, I heard that it was impossible to pass the subject, and I felt really angry."
    
    scene arcade with fade
    
    show mariano
    
    "I started going with Mariano to the arcade day after day, and eventually I stopped going to class."
    
    "After a few weeks, I had to quit college due to the massive debt from the arcade. The debt was so big that I was not even able to afford medicine."
    
    scene black with dissolve
    
    "Finally, I caught a strange disease called Covid-19+1 and died peacefully in my sleep."
    
    "You may wonder if the disease killed me... but that was not the case. I just tried to cross the street and a tractor ran over me."
    
    "... or so I thought. Apparently, I died just from the shock of seeing a tractor so close to me. It was even stopped in the middle of the road, there was no way it was going to hit me..."
    
    "I should have worked harder in college."
    
    "BAD ENDING\n\n(WHO EVEN DIES TO A TRACTOR?)"
    
    return

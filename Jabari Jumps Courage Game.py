import art
import termcolor


print("Hi, Welcome to the Jabari Jumps courage game. You will be asked a couple questions and answer based on your opinion. HAVE FUN")
name = input("Please Type your name: ")
greeting = "Good  Luck   " + name
word=art.text2art(greeting)
print (word)


answers1 = [1, 2, 3]
validinput = False
while validinput == False:
    Question1 = int(input("Question A: What do you think is the defenition of courage?   1. Thinking and reacting quick.  2. Doing the right thing.  3. Being brave enought to overcome your fears. Type either 1, 2, or 3:  "))

    if answers1[0] == Question1:
        answercolor= termcolor.colored("The smartest people are the ones who can make make decisions quick","green")
        print (answercolor)
        validinput= True

    elif answers1[1] == Question1:
        answercolor= termcolor.colored("Doing the right think can benefit more than one person","blue")
        print (answercolor)
        validinput=True

    elif answers1[2]==Question1:
        answercolor= termcolor.colored("Sometimes overcoming your fears is what makes you strong","magenta")
        print (answercolor)
        validinput=True
    else:
        answercolor= termcolor.colored("Try again","red")
        print (answercolor)

print("""
             .=.,
            ;c =\ 
          __|  _/
        .'-'-._/-'-._
       /..   ____    )
      /' _  [<_->] )  )
     (  / \--\_>/-/'._ )
      \-;_/\__;__/ _/ _/
       '._}|==o==\{_\/
        /  /-._.--\  \ 
       // /   /|   \ \ \ 
      / | |   | \;  |  \ \ 
     / /  | :/   \: \   \ \ 
    /  |  /.'|   /: |    \ \ 
    |  |  |--| . |--|     \_\ 
    / _/   \ | : | /___--._) \ 
   |_(---'-| >-'-| |       '-'
          /_/     \_\ 
""")    
        
answers2 = [1, 2, 3]
validinput = False
while validinput == False:
    Question2 = int(input("Question B:  You are woken up by a strange noise coming from downstairs, what do you do?   1. Think about what the best thing to do is.  2. Stay in bed and hope the noise will go away.  3. get out of bed and investigate.   Type either 1, 2, or 3:  "))
    if answers2[0] == Question2:
        answercolor= termcolor.colored("You remember that your uncle is staying the night and it his him.","green")
        print (answercolor)
        validinput= True
    elif answers2[1] == Question2:
        answercolor= termcolor.colored("You realize it was just the noise of the plumbing","blue")
        print (answercolor)
        validinput=True
    elif answers2[2]==Question2:
        answercolor= termcolor.colored("You go on a hunt","magenta")
        print (answercolor)
        validinput=True
    else:
        answercolor= termcolor.colored("Try again","red")
        print (answercolor)

print("""
          _____|~~\_____      _____________
      _-~               \    |    )
      _-    | )     \    |__/   \   )
      _-         )   |   |  |     \   )
      _-    | )     /    |--|      |  |
     __-_______________ /__/_______|  |_________
    (                |----         |  |
     `---------------'--))))      .`--'
                                  `||||

""")
answers3 = [1, 2, 3]
validinput = False
while validinput == False:
    Question3 = int(input("Question C:  You see a classmate getting bullied at recess, what do you do?   1. Talk with your friends to find the best thing to do about it.  2. Go get the teacher to tell her what's happening.  3. Step in and stick up for the boy getting bullied.   Type either 1, 2, or 3:  ")) 
    if answers3[0] == Question3:
        answercolor= termcolor.colored("You and your friends help the boy","green")
        print (answercolor)
        validinput= True
    elif answers3[1] == Question3:
        answercolor= termcolor.colored("You tell the teacher and she helps the boy being bullied","blue")
        print (answercolor)
        validinput=True
    elif answers3[2]==Question3:
        answercolor= termcolor.colored("You help the boy and make a new friend","magenta")
        print (answercolor)
        validinput=True
    else:
        answercolor= termcolor.colored("Try again","red")
        print (answercolor)
    
print("""

  \_/
  --(_)--  .
    / \   (_)
          |Q|
    .-----' '-----.                                  __
   /____[SCHOOL]___\                                ()))
    | [] .-.-. [] |                                (((())
  ..|____|_|_|____|..................................)(... 

""") 

answers4 = [1, 2, 3]
validinput = False
while validinput == False:
    Question4 = int(input("Question D: You get lost at the top of a hard ski hill with no family around, what do you do?  1.  Ask yourself if you will be safe on the ski hill.  2. Go back and look for a stranger to ask for help.  3. Go down the ski hill and hope to make it down safe.  Type either 1, 2, or 3.  "))
    if answers4[0] == Question4:
        answercolor= termcolor.colored("You realize it may be safe if gone the right path","green")
        print (answercolor)
        validinput= True
    elif answers4[1] == Question4:
        answercolor= termcolor.colored("You find a man that helps you find your family","blue")
        print (answercolor)
        validinput=True
    elif answers4[2]==Question4:
        answercolor= termcolor.colored("You have a lot of fun but have trouble on the hill","magenta")
        print (answercolor)
        validinput=True
    else:
        answercolor= termcolor.colored("Try again","red")
        print (answercolor)

print("""

                       __
                      (=[)
                    /`\ -.
`` ,,``           /`| ,_,_`-._
     ,,'         /  `---,)`--.)
  ``,,  ''      (  '._-/_   /
 ,,    `` ``,,   \   /') )/'
  , ``,''`;; ,,   `>' / / 
 `` '',`;;,`;;, -/' /| |
    ``,; --..._/|  \ ```---...___
             /'  ```---...___   _```--'
                             ```
 
""")
answers5 = [1, 2, 3]
validinput = False
while validinput == False:
    Question5 = int(input("Question E: Some of your classmates are pure pressuring you to do something that makes you feel uncomftorable. What do you do?  1. Give it some time and dont do it untill you are ready.  2. Say no because this makes you feel unsafe.  3. Say yes and risk getting in danger.  Type either 1, 2, or 3.  "))
    if answers5[0] == Question5:
        answercolor= termcolor.colored("After thinking you decide to do it","green")
        print (answercolor)
        validinput= True
    elif answers5[1] == Question5:
        answercolor= termcolor.colored("You decline but end up doing other fun things together","blue")
        print (answercolor)
        validinput=True
    elif answers4[2]==Question5:
        answercolor= termcolor.colored("You overcome your fear and have fun","magenta")
        print (answercolor)
        validinput=True
    else:
        answercolor= termcolor.colored("Try again","red")
        print (answercolor)
    
print("""
                       _.---~~~~~~~-.       ____
                  _.-~' _.-~   _     `.__,-|
                 (  _.-(_ _.-~^ )        | |
                  ~~     `( _.-~ )       | |
                          `( _.-~ )   ___| |
                            `-..-~--~'   `-| O
                                            `----$$$$$$$$$$$$$$$$$$$$$$$$$


""")
pointtotal=int(Question1)+int(Question2)+int(Question3)+int(Question4)+int(Question5)

if pointtotal<8:
    answercolor= termcolor.colored("After all of your answers, we can say that you like think before acting to make sure you make the decision that you like best","magenta")
    print (answercolor)
if pointtotal>8 and pointtotal<13:
    answercolor= termcolor.colored("After all of your answers, we can say that you like to make the decision that benefits yourself or others and has the best impact","magenta")
    print (answercolor)
if pointtotal>12:
    answercolor= termcolor.colored("You like to be adventerous and overcoming your fears","magenta")
    print (answercolor)
  
answercolor= termcolor.colored("CONGRATULATIONS on completing this game " +name + ". I hope you had fun","yellow")
print (answercolor)
print("""
    |@@@@|     |####|
    |@@@@|     |####|
    |@@@@|     |####|
    \@@@@|     |####/
     \@@@|     |###/
      `@@|_____|##'
           (O)
        .-'''''-.
      .'  * * *  `.
     :  *       *  :
    : C O U R A G E :
    : ~ A W A R D ~ :
     :  *       *  :
      `.  * * *  .'
        `-.....-'

""")

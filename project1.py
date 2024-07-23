import random
options=['Stone','Paper','Scissor']
options_dict={'s':0,'p':1,'sc':2}

computer=random.choice([0,1,2])
you=input("Enter Your Choice (s for Stone p for Paper sc for Scissor): ")
your_choice=options_dict[you]
print(f"Your Choice {options[your_choice]} \n Computer Choice is {options[computer]}")
if computer==your_choice:
    print("Draw")
else:
    if computer==0 and your_choice==1:
        print("You Win")
    elif computer==0 and your_choice==2:
        print("You Loose")    
    elif computer==1 and your_choice==0:
        print("You Loose")     
    elif computer==1 and your_choice==2:
        print("You Win")
    elif computer==2 and your_choice==0:
        print("You Loose")          
    elif computer==2 and your_choice==1:
        print("You Win")
    else:
        print("Something Went wrong")     

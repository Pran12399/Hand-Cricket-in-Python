import random
print(('-'*30).center(100))
print("HAND CRICKET GAME BY PRANAV KUMAR".center(100))
print(('-'*30).center(100))
print("Game Rules:\n1.IF YOU AND COMPUTER ENTERED A SAME NUMBER THEN YOU ARE OUT\n2.IF THE NUMBERS BOTH ENTERED ARE DIFFERENT THEN THE SCORE WILL BE ADDED\nPRANAV KUMAR(GAME CREATOR)WISHES THE PLAYER ALL THE BEST")

def toss():
    selection = ['Batting','Bowling']
    print("Toss \npress 1 for Heads \nPress 0 for tails")
    a=int(input())
    if(a>1 or a<0):
        print("Key not Valid \nEnter a valid Key")
        toss()
    elif(a==random.randint(0,1)):
        print("Congrats you won the Toss\nPress 1 for Batting\nPress 0 for bowling")
        bat_sel=int(input())
        score1=0
        score2=0
        ref=0
        if(bat_sel==1):
            score1 = batting(score1,ref,score2)
            print("Your Score is",score1,"Computer needs to score",score1+1,"to win")
            score2 = bowling(score2,ref,score1)
            if(score1>score2):
                print("You Win")
            else:
                print("You Lost")
            
        else:
             score1=bowling(score1,ref,score2)
             print("Computer Score is",score1,"You need to score",score1+1,"to win")
             score2=batting(score2,ref,score1)
             if(score2>score1):
                 print("You Win")
             else:
                 print("You Lost! Better Luck Next Time!")
             
    else:
        score1=0
        score2=0
        ref=0
        comp_sel = random.randint(0,1)
        print("Computer Won the toss and choose to {}".format(selection[comp_sel]))
        if comp_sel==0:
             score1=bowling(score1,ref,score2)
             print("Computer Score is",score1,"You need to score",score1+1,"to win")
             score2=batting(score2,ref,score1)
             if(score2>score1):
                 print("You Win")
             else:
                 print("You Lost! Better Luck Next Time!")
        else:
            score1 = batting(score1,ref,score2)
            print("Your Score is",score1,"Computer needs to score",score1+1,"to win")
            score2 = bowling(score2,ref,score1)
            if(score1>score2):
                print("You Win".center('*',50))
            else:
                print("You Lost".center('*',50))
        
        

def bowling(score,ref,dec):
    print(dec)
    print('-'*80)
    print("Now You Are Bowling: \n Your Score is ",score)
    score = 0
    print('-'*80)
    while(1):
        print("Enter a number to be bowled")
        bowl=int(input())
        comp_bowl=random.randint(0,6)
        if bowl==comp_bowl:
            print("You and computer entered a same number.Computer lost its turn")
            print("Score is :",score)
            ref+=1
            return score
        else:
            
            score+=comp_bowl
            if(ref!=0 and score>dec):
                print("Computer number is {}\t\tcomputer score is [{}]".format(comp_bowl,score))
                print("You LOST".center(75,'*'))
                
                return score
            print("Computer number is {}\t\tcomputer score is [{}]".format(comp_bowl,score))
             
          
            
            
    



    
def batting(score,ref,dec):
    print(dec)
    print('-'*80)
    print("Now You Are Batting: \n Your Score is ",score)
    score = 0
    print('-'*80)
    while(1):
        print("Enter a number: ")
        num = int(input())
        num2= random.randint(0,6)
        if(num==num2):
            print("Both You and computer Entered A same Number:")
            print("You Are Out,Your score is {}".center(55,' ').format(score))
            ref+=1
            return score
        
        else:
            score+=num
            if(ref>0 and score>dec):
                print("You Win".center(75,'*'))
            print("score is {}".center(75,' ').format(score))
 
              
            
   
toss()       






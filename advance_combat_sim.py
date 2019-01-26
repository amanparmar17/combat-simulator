#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 02:20:25 2019

@author: aman
"""

#%%
import random
import sys
#from combat_simulator import 
#%%
#making the health and attack dictionary for each tyoe of fighter
health={
        'A':1,
        'S':2,
        'K':3,
        'W':10,
        'SE':10
        }

attack={
        'advantage':3,
        'disadvantage':1,
        'tie':2
        }
#%%

#ADD THE FIRST CODE SECTION FROM THE VS CODE EDITOR#SECTION 1
#%%
#function for revival
def revive(money,user,score,loser):
    if(money>0):
        user.append(loser)
        money -= 1
        score += 1
    return (user,money,score)

#%% formation of army of user 2 i.e. computer
#consists of atleast 1 member
def inputmem2():
    user2 = []
    t = random.randint(1,10)
    for i in range(0,t):
        u = random.randint(1,5)
        if(u == 1):
            user2.append("A")
        if(u == 2):
            user2.append("S")
        if(u == 3):
            user2.append("K")            
        if(u == 4):
            user2.append("W")            
        if(u == 5):
            user2.append("SE")            
    archer2 = user2.count("A")
    soldier2 = user2.count("S")
    knight2 = user2.count("K")
    wizard2 = user2.count("W")
    seigo2 = user2.count("SE")
    print("Player2 army consists of:")
    print("Knights: ",knight2)
    print("Archers: ",archer2)
    print("Soldiers: ",soldier2)
    print("Wizards: ",wizard2)
    print("Seigo Equipment: ",seigo2)
    return user2
    
#%% formation of army of user1----------METHOD1

def inputmem1():
    user1 = input().split(" ")
    n = user1.count('')
    for i in range(0,n):
        user1.remove('')
    archer1 = user1.count("A")
    soldier1 = user1.count("S")
    knight1 = user1.count("K")
    wizard1 = user1.count("W")
    seigo1 = user1.count("SE")
    if(len(user1) > 10 or archer1 > 10 or soldier1 > 10 or knight1 > 10 or wizard1 > 10 or seigo1 > 10):
        print("Sorry wrong input, please try again")
        inputmem1()
    print("Your army consists of:")
    print("knights: ",knight1)
    print("Archers: ",archer1)
    print("Soldiers: ",soldier1)
    print("Wizards: ",wizard1)
    print("Seigo Equipment: ",seigo1)
    return user1

#%% toss to select the first turn
#def toss():
#    t = random.randint(1,2)
#    if(t==1):
#        print("User1 plays first")
#    else:
#        print("User2 plays first")


#%%
def fight(score1,score2,i,j,us1,us2,money1,money2):
    Player1 = us1[i]
    Player2 = us2[j]
    heal1 = health[Player1]
    heal2 = health[Player2]
    print("running the fight function")
    print("health1="+str(heal1))
    print("health2="+str(heal2))
#    return battle(Player1, Player2, i, j, score1, score2,us1,us2,money1,money2,heal1,heal2)
    hh= battle(Player1, Player2, i, j, score1, score2,us1,us2,money1,money2,heal1,heal2)
    return hh
#%% fucntion to start the battle

#def fight(score1,score2,i,j,user1,user2):
#    Player1 = user1[i]
#    Player2 = user2[j]
#    return battle(Player1, Player2, i, j, score1, score2,user1,user2)
#%% battle function redefined 


def compare(Player1,Player2):
    if(Player1 == "A" and Player2 == "S"):
        return Player1
    if(Player1 == "S" and Player2 == "A"):
        return Player2
    if(Player1 == "A" and Player2 == "A"):
        return "tie"
    if(Player1 == "A" and Player2 == "K"):
        return Player2
    if(Player1 == "S" and Player2=="S"):
        return "tie"
    if(Player1 == "S" and Player2 == "K"):
        return Player1
    if(Player1 == "K" and Player2 == "K"):
        return "tie"
    if(Player1 == "K" and Player2 == "S"):
        return Player2
    if(Player1 == "K" and Player2 == "A"):
        return Player1
    
    
    
    
    
    
    
    
    
    if(Player1 == "SE" and (Player2 == "K" or Player2 == "W") ):
        return Player2
    
    if(Player2 == "SE" and (Player1 == "K" or Player1 == "W") ):
        return Player1
    if(Player2 == "SE" and (Player1 == "A" or Player1 == "S") ):
        return Player2
    
    if(Player1 == "SE" and (Player2 == "A" or Player2 == "S")):
        return Player1
    
    
    
    
    
    
    
    
    
    if((Player1 == "W" and Player2 == "A")):
        return Player2
    if(Player1 == "A" and Player2 == "W"):
        return Player1

    if(Player1 == "W" and (Player2 == "S" or Player2 == "K" or Player2 == "SE")):
        return Player1
    if(Player2 == "W" and (Player1 == "S" or Player1 == "K" or Player1 == "SE")):
        return Player2
    if(Player1 == "W" and Player2 == "W"):
        return "tie"
    if(Player1 == "SE" and Player2 == "SE"):
        return "tie"
    
 
#%% battle redefined

# giving direct preference to the seigo equipment when the other opponent is either soldier and archer.
# if the opponents are seigo eq. and either of knight or wizard, direct win will be awarded to the wizards and knights

#siimilarly when the opponents are wizards and archers, direct win to archer
#otherwise wizard wins in all other scenarios



#%%
def battle(Player1, Player2, i, j, score1, score2,us1,us2,money1,money2,heal1,heal2):
#    if(len(user1)>9 or len(user2)>9):
#        sys.exit(0)
    print("==================================1")
    if(score1==0 and score2==0):
        return 3
    if(score1==0):
        return 2
    if(score2==0):
        return 1
    
    print("==================================2")
    
    if(Player1=="W" or Player2=="W" or Player1=="SE" or Player2=="SE"):
        print()
        print("=====================98989")
        adv=compare(Player1,Player2)
        if(adv==Player1):
            print("==================================200")
            j+=1
            score2-=1
            
            if(j < 10):
                us2,money2,score2=revive(money2,us2,score2,Player2)
                print("==================================300")
                Player2=us2[j]
            else:
                print("==================================400")
                return 1
            health2 = health[Player2]
        elif(adv==Player2):
            print("==================================500")
            i+=1
            score1-=1
            
            if(i < 10):
                us1,money1,score1=revive(money1,us1,score1,Player1)
                print("==================================600")
                Player1=us1[i]
            else:
                print("==================================700")
                return 2
            health1 = health[Player1]
        else:
            print("==================================800")
            i+=1
            j+=1
            score1-=1
            score2-=1
            
            if(i < 10 and j < 10):
                us1,money1,score1=revive(money1,us1,score1,Player1)
                us2,money2,score2=revive(money2,us2,score2,Player2)
                print("==================================900")
                Player1 = us1[i]
                Player2 = us2[j]
            else:
                print("==================================1000")
                return 3 
            print("==================================2000")
            health1=health[Player1]
            health2=health[Player2]
        
        return battle(Player1, Player2, i, j, score1, score2,us1,us2,money1,money2,heal1,heal2)
    
    print("==================================3")
    
    health1=heal1
    health2=heal2
    
    print("==================================4")
    
    adv=compare(Player1, Player2)
    
    
    if(adv==Player1):
        print("==================================7100")
        health1-=1
        disadv=Player2
    elif(adv=="tie"):
        print("==================================7200")
        health1-=2
        health2-=2
        disadv=10
    else:
        print("==================================7300")
        health2-=1
        disadv=Player1
    
    a=1
    
    print("adv"+str(adv))
    print("disadv"+str(disadv))
    
    print("==================================5")
    if(health1>0 and health2>0):
        while(health1 <= 0 or health2 <= 0):
            print("==================================6")
            if(a%2!=0):
               print("==================================7")
               if(disadv==Player1):
                   health1-=3
    #                   disadv=Player2
                   a+=1
               if(disadv==Player2):
                   health2-=3
    #                   disadv=Player1
                   a+=1
               if(disadv==10):
    #               health1-=2
    #               health2-=2
    #                   disadv=10
                   a+=1
            else:
                print("==================================8")
                if(adv==Player1):
                   health1-=1
                   print("==================================18")
    #                   disadv=Player2
                if(adv==Player2):
                   health2-=1
                   print("==================================28")
    #                   disadv=Player1
                if(adv==10):
                   health1-=2
                   health2-=2
                   print("==================================38")
    #                   disadv=10 
    print("==================================10")
    if(health1<=0):
        print("==================================7400")
        i+=1
        score1-=1
        us1,money1,score1=revive(money1,us1,score1,Player1)
        if(i < 10):
            print("==================================7500")
            Player1=us1[i]
        else:
            print("==================================7600")
            return 2
        health1=health[Player1]
    elif(health2<=0):
        print("==================================7700")
        j+=1
        score2-=1
        us2,money2,score2=revive(money2,us2,score2,Player2)
        if(j < 10):
            print("==================================7800")
            Player2=us1[j]
        else:
            print("==================================7900")
            return 1
        health2=health[Player2]
    else:
        print("==================================7900")
        i+=1
        j+=1
        score1-=1
        score2-=1
        us1,money1,score1=revive(money1,us1,score1,Player1)
        us2,money2,score2=revive(money2,us2,score2,Player2)
        if(i<10 and j<10):
            print("==================================8000")
            Player1 = us1[i]
            Player2 = us2[j]
        else:
            print("==================================8100")
            return 3
        health1=health[Player1]
        health2=health[Player2]
        
    print("==================================11")
    
    return battle(Player1,Player2,i,j,score1,score2,us1,us2,money1,money2,health1,health2)
    
#%% 
def healthList(user):
    power = []
    for i in range(0,len(user)):
        power.append(health[user[i]])
    return power
    
#%% main block to run the whole code

if __name__=='__main__':
    print("Enter the army members in the order you want them to battle (maximum 10)")
    print("###########\nFor Soldier: S \nFor Knight : K \nFor Archer : A\nFor Wizard: W\nFor Sigo Equipment: SE\n###########")
    user1 = inputmem1()
    user2 = inputmem2()
    score1 = len(user1)
    score2 = len(user2)
#    heal1 = healthList(user1)
#    heal2 = healthList(user2)
    
    for i in user1:
        print(i,end=" ")
    print()
    for j in user2:
        print(j,end=" ")
        
    
    
    #NEW ADDON TO THE CODE
    money1=10-score1
    money2=10-score2
    #
    print(score1)
    print(score2)
    print(end = '\n')
    i = j = 0
    print("finding the winner...")
    oo = fight(score1,score2,i,j,user1,user2,money1,money2)
    
    if(oo==3):
        print("The match is a tie")
    if(oo==2):
        print("The winner of the match is Player2")
    if(oo==1):
        print("The winner of the match is Player1")
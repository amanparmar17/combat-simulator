#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 00:16:43 2019

@author: aman
"""
#%%
import random
#%% formation of army of user 2 i.e. computer
#consists of atleast 1 member
def inputmem2():
    user2 = []
    t = random.randint(0,10)
    for i in range(0,t):
        u = random.randint(1,3)
        if(u==1):
            user2.append("A")
        if(u==2):
            user2.append("S")
        if(u==3):
            user2.append("K")            
    archer2 = user2.count("A")
    soldier2 = user2.count("S")
    knight2 = user2.count("K")
    print("Player2 army consists of:")
    print("Knights: ",knight2)
    print("Archers: ",archer2)
    print("Soldiers: ",soldier2)
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
    if(len(user1) > 10 or archer1 > 10 or soldier1 > 10 or knight1 > 10):
        print("Sorry wrong input, please try again")
        inputmem1()
    print("Your army consists of:")
    print("knights: ",knight1)
    print("Archers: ",archer1)
    print("Soldiers: ",soldier1)
    return user1

#%% toss to select the first turn
def toss():
    t = random.randint(1,2)
    if(t==1):
        print("User1 plays first")
    else:
        print("User2 plays first")
        
#%%
def fight(score1,score2,i,j):
    Player1 = user1[i]
    Player2 = user2[j]
    return battle(Player1, Player2, i, j, score1, score2)
#%% fucntion to start the battle

#def fight(score1,score2,i,j,user1,user2):
#    Player1 = user1[i]
#    Player2 = user2[j]
#    return battle(Player1, Player2, i, j, score1, score2,user1,user2)
#%% battle function redefined 

def compare(Player1,Player2):
    if(Player1=="A" and Player2=="S"):
        return Player1
    if(Player1=="S" and Player2=="A"):
        return Player2
    if(Player1=="A" and Player2=="A"):
        return "tie"
    if(Player1=="A" and Player2=="K"):
        return Player2
    if(Player1=="S" and Player2=="S"):
        return "tie"
    if(Player1=="S" and Player2=="K"):
        return Player1
    if(Player1=="K" and Player2=="K"):
        return "tie"
    if(Player1=="K" and Player2=="S"):
        return Player2
    if(Player1=="K" and Player2=="A"):
        return Player1
        
def battle(Player1, Player2, i, j, score1, score2):
    if(score1==0 and score2==0):
        return 3
    if(score1==0):
        return 2
    if(score2==0):
        return 1
    winner = compare(Player1, Player2)
    
    if(winner=="tie"):
        score1 -= 1
        score2 -= 1
        i += 1
        j += 1
    if(winner==Player1):
        score2 -= 1
        j += 1
    if(winner==Player2):
        score1 -= 1
        i += 1
    if(i<len(user1) and j<len(user2)):
        Player1 = user1[i]
        Player2 = user2[j]
    elif(i>=len(user1)):
        return 2
    else:
        return 1
    print("Player1: {0}, Player2:{1}".format(Player1, Player2))
    print("Winner: {1} : Player1 Score: {2}, Player2 Score: {0} ".format(score2,winner,score1))
    print("\n")
    return battle(Player1, Player2, i, j, score1, score2)   

#%% main block to run the whole code

if __name__=='__main__':
    print("Enter the army members in the order you want them to battle (maximum 10)")
    print("###########\nFor Soldier: S \nFor Knight : K \nFor Archer : A\n###########")
    user1 = inputmem1()
    user2 = inputmem2()
    score1 = len(user1)
    score2 = len(user2)
    print(end = '\n')
    i = j = 0
    oo = fight(score1,score2,i,j)
    
    if(oo==3):
        print("The match is a tie")
    if(oo==2):
        print("The winner of the match is Player2")
    if(oo==1):
        print("The winner of the match is Player1")
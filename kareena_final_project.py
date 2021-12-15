#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 08:58:55 2021

@author: kareenakloek
"""
set1 = set()

set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("let's play a game of tic tac toe")
print("You are x's and I am o's")

print("1 / 2 / 3")
print("- + - + - ")
print("4 / 5 / 6")
print("- + - + - ")
print("7 / 8 / 9")

tl = " "
tm = " "
tr = " "
ml = " "
mm = " "
mr = " "
bl = " "
bm = " "
br = " " 


def drawBoard():

    print(f"{tl}|{tm}|{tr}\n------\n{ml}|{mm}|{mr}\n------\n{bl}|{bm}|{br}")

def myturn():
    x = int(input("pick a number from 1 - 9 to make a move"))
    
    if x in set2:
        print(x)
        
    else:
        print("that number is not between 1 and 9. Pick another number")
        x = int(input("pick a number from 1 - 9 to make a move"))

    global tl, tm, tr, ml, mm, mr, bl, bm, br
    if x == 1 and tl == " ":
        tl = "X"
    elif x == 2 and tm == " ":
        tm = "X"
    elif x == 3 and tr == " ":
        tr = "X"
    elif x == 4 and ml == " ":
        ml = "X"
    elif x == 5 and mm == " ":
        mm = "X"
    elif x == 6 and mr == " ":
        mr = "X"
    elif x == 7 and bl == " ":
        bl = "X"
    elif x == 8 and bm == " ":
        bm = "X"
    elif x == 9 and br == " ":
        br = "X"
    
    else:
        print("this spot is already been chosen. Chose another number from 1- 9")
        myturn()
    
        

def yourturn():
    print("nice move! now its my turn")
    import random 
    y = random.randint(1,9) 
    global tl, tm, tr, ml, mm, mr, bl, bm, br
    if y == 1 and tl == " ":
        tl = "O"
        print(f"i chose {y}")
    elif y == 2 and tm == " ":
        tm = "O"
        print(f"i chose {y}")
    elif y == 3 and tr == " ":
        tr = "O"
        print(f"i chose {y}")
    elif y == 4 and ml == " ":
        ml = "O"
        print(f"i chose {y}")
    elif y == 5 and mm == " ":
        mm = "O"
        print(f"i chose {y}")
    elif y == 6 and mr == " ":
        mr = "O"
        print(f"i chose {y}")
    elif y == 7 and bl == " ":
        bl = "O"
        print(f"i chose {y}")
    elif y == 8 and bm == " ":
        bm == "O"
        print(f"i chose {y}")
    elif y == 9 and br == " ":
        br = "O"
        print(f"i chose {y}")
    else:
        print("this spot is already been chosen. Chose another number from 1- 9")
        yourturn()
    

    
    

def isWin():
    if tl == tm and tm == tr and tl != " ":
        if tl == "X":
            print("game over! you won!")
            
        else:
            print("game over! i won!")
        return True
            
    elif ml == mm and mm == mr and ml != " ":
        if ml == "X":
            print("game over! you won!")
            
        else:
            print("game over! i won!")
        return True
   
    
    elif bl == bm and bm == br and bl != " ":
        if bl == "X":
            print("game over! you won!")
            
        else:
            print("game over! i won!")
        return True
        
        
    elif tl == mm and mm == br and tl != " ":
        if tl == "x":
            print("game over! you won!")
           
        else:
            print("game over! i won!")
        return True
    
    elif tr == mm and mm == bl and tr != " ":
        if tr == "X":
            print("game over! you won!")
            
        else:
            print("game over! i won")
        return True
            
    elif tl == ml and ml == bl and tl != " ":
        if tl == "X":
            print("game over! you won!")
            
        else:
            print("game over! i won!")
        return True

    elif tm == mm and mm == bm and tm != " ":
        if tm == "X":
            print("game over! you won!")
            
        else:
            print("game over! i won!")
        return True
        
    elif tr == mr and mr == br and tr != " ":
        if tr == "X":
            print("game over! you won!")
            
        else:
            print("game over! i won!")
        return True
    else:
        return False

        
        


while True:    
    
    drawBoard()
    if not isWin():  
        myturn()
    else:
        break
    if not isWin():
        yourturn()
    else:
        break


    
    

        


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 08:58:55 2021

@author: kareenakloek
"""
set1 = {}

print("let's play a game of tic tac toe")
print("You are x's and I am o's")

print("1 / 2 / 3")
print("- + - + - ")
print("4 / 5 / 6")
print("- + - + - ")
print("7 / 8 / 9")

x = int(input("pick a number from 1 - 9 to make a move"))
print(x)

tl = " "
tm = " "
tr = " "
ml = " "
mm = " "
mr = " "
bl = " "
bm = " "
br = " " 

if x == 1:
    tl = "X"
if x == 2:
    tm = "X"
if x == 3:
    tr = "X"
if x == 4:
    ml = "X"
if x == 5:
    mm = "X"
if x == 6:
    mr = "X"
if x == 7:
    bl = "X"
if x == 8:
    bm = "X"
if x == 9:
    br = "X"


print(f"{tl}|{tm}|{tr}\n------\n{ml}|{mm}|{mr}\n------\n{bl}|{bm}|{br}")


print("nice move! now its my turn")
import random 
y = random. randint(1,9) 
print(y)

set1.add(x)
if y in set1:
    random.  randint(1,9)  
    

if y == 1:
    tl = "O"
if y == 2:
    tm = "O"
if y == 3:
    tr = "O"
if y == 4:
    ml = "O"
if y == 5:
    mm = "O"
if y == 6:
    mr = "O"
if y == 7:
    bl = "O"
if y == 8:
    bm = "O"
if y == 9:
    br = "O"
    
print(f"{tl}|{tm}|{tr}\n------\n{ml}|{mm}|{mr}\n------\n{bl}|{bm}|{br}")
    

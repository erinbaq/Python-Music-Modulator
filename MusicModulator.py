# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:50:11 2020

@author: rbaqu
"""
import tkinter
from tkinter import filedialog
import turtle
import time



def translateGtoC(song):	
    note = song.split()
    G_to_C = {"G":"C","A":"D","B":"E","C":"F","D":"G","E":"A","F":"B"}
    result = [G_to_C.get(i,i)for i in note]
    string = ""
    return string.join(result)

def translateFtoC(song):	
    note = song.split()
    F_to_C = {"F":"C","G":"D","A":"E","Bb":"F","C":"G","D":"A","E":"B"}
    result = [F_to_C.get(i,i)for i in note]
    string = ""
    return string.join(result)

def translateEtoC(song):	
    note = song.split()
    E_to_C = {"E":"C","F#":"D","G#":"E","A":"F","B":"G","C#":"A","D#":"B"}
    result = [E_to_C.get(i,i)for i in note]
    string = ""
    return string.join(result)

def translateDtoC(song):	
    note=song.split()
    D_to_C = {"D":"C","E":"D","F#":"E","G":"F","A":"G","B":"A","C#":"B"}
    result = [D_to_C.get(i,i)for i in note]
    string = ""
    return string.join(result)

def translateBtoC(song):	
    note = song.split()
    B_to_C = {"B":"C","C#":"D","D#":"E","E":"F","F#":"G","G#":"A","A#":"B"}
    result = [B_to_C.get(i,i)for i in note]
    string = ""
    return string.join(result)

def translateAtoC(song):	
    note = song.split()
    A_to_C = {"A":"C","B":"D","C":"E","D":"F","E":"G","F":"A","G#":"B"}
    result = [A_to_C.get(i,i)for i in note]
    string = ""
    return string.join(result)

def main():
    userx = input("Does your file already exist?(yes or no) ")
    user = userx.lower()
    root = tkinter.Tk()
    root.withdraw()
    if user == "yes":
        fileName = filedialog.askopenfilename()
        file = open(fileName,"r")
        fileSong = file.readline()
        file.close()
    if user =="no":
        songName= input("What is the name of the song?\n")
        fileSong= input("Input all the notes(separated by SPACES only!)")
        fileName= songName+".txt"
        
    keyToTranslate= input("What key is the original song in? (type A, B, D, E, F, or G)\n")
   # 
    convertedSong = ""
    if keyToTranslate == "G":
        convertedSong = translateGtoC(fileSong)
    elif keyToTranslate == "F":
        convertedSong= translateFtoC(fileSong)
    elif keyToTranslate == "E":
        convertedSong = translateEtoC(fileSong)    
    elif keyToTranslate == "D":
        convertedSong = translateDtoC(fileSong)
    elif keyToTranslate == "B":
        convertedSong = translateBtoC(fileSong)
    elif keyToTranslate == "A":
        convertedSong = translateAtoC(fileSong)

    
    newSong= open(fileName,"w")
    newSong.write(convertedSong)
    print(convertedSong)
    newSong.close()

    #draw
    t = turtle.Turtle()
    
    t.color('black')
    style = ('Courier', 15, 'italic')
    turtle.write(songName, font=style, align='center')
    turtle.hideturtle()
    time.sleep(2)

    t.color('white')
    t.right(90)
    t.forward(20)
    t.left(90)

    t.color('white')
    t.right(90)
    t.forward(20)
    t.left(90)

    for x in range(4):
        t.color('black')
        t.backward(200)

        t.color('black')
        t.forward(400)

        t.color('black')
        t.right(90)  
        t.forward(10)
        t.right(90)
        t.forward(200)
        t.right(180)

    t.backward(200)
    t.left(90)

    t.color('white')
    t.forward(35)

    t.color('black')
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(10)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(7)

    t.left(90)
    t.color('white')
    t.forward(15)
    t.color('black')
    t.backward(5)
    t.color('white')
    t.backward(10)
    t.right(90)
    
    t.color('black')
    t.forward(12)

    t.left(90)
    t.color('white')
    t.forward(15)
    t.color('black')
    t.backward(5)
    t.color('white')
    t.backward(10)
    t.right(90)



    t.color('black')
    t.right(45)
    t.forward(23)

    t.right(45)
    t.forward(10)
    
    t.right(90)

    for x in range(4):
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.backward(10)
        t.left(90)

    t.right(90)
    t.forward(75)
    t.right(90)

    t.forward(1)

    t.color('white')
    t.forward(7)

    t.color('black')
    t.forward(1)
    
    t.color('white')
    t.forward(1)

    t.color('black')
    t.right(135)
    t.forward(5)
    t.left(45)
    t.forward(5)
    t.left(45)
    t.forward(5)
    t.left(45)
    t.forward(15)
    t.left(45)
    t.forward(5)
    t.left(45)
    t.forward(5)
    t.left(45)
    t.forward(5)

    t.color('white')
    t.right(135)
    t.forward(4)
    t.color('black')
    t.forward(1)
    t.color('white')
    t.forward(9)
    t.color('black')
    t.forward(1)

    t.left(90)
    t.forward(334)
    t.backward(7)
    t.left(90)
    t.forward(40)
    t.backward(40)
    t.right(90)
    t.backward(250)

    for y in range(0,len(convertedSong)):
        if(str(convertedSong[y]) == "F"):
            t.pendown()
            t.circle(5)
            t.penup()
            t.forward(10)
            continue
        elif(str(convertedSong[y]) == "G"):
            t.left(90)
            t.forward(36)
            t.pendown()
            t.circle(5)
            t.penup()
            t.right(180)
            t.forward(36)
            t.left(90)
            t.forward(10)
            continue
        elif(str(convertedSong[y]) == "A"):
            t.left(90)
            t.forward(32)
            t.pendown()
            t.circle(5)
            t.penup()
            t.right(180)
            t.forward(32)
            t.left(90)
            t.forward(10)
            continue
        elif(str(convertedSong[y]) == "B"):
            t.left(90)
            t.forward(28)
            t.pendown()
            t.circle(5)
            t.penup()
            t.right(180)
            t.forward(28)
            t.left(90)
            t.forward(10)
            continue
        elif(str(convertedSong[y]) == "C"):
            t.left(90)
            t.forward(24)
            t.pendown()
            t.circle(5)
            t.penup()
            t.right(180)
            t.forward(24)
            t.left(90)
            t.forward(10)
            continue
        elif(str(convertedSong[y]) == "D"):
            t.left(90)
            t.forward(20)
            t.pendown()
            t.circle(5)
            t.penup()
            t.right(180)
            t.forward(20)
            t.left(90)
            t.forward(10)
            continue
        elif(str(convertedSong[y]) == "E"):
            t.left(90)
            t.forward(16)
            t.pendown()
            t.circle(5)
            t.penup()
            t.right(180)
            t.forward(16)
            t.left(90)
            t.forward(10)
            continue
        else:
            t.forward(10)
            continue
        
main()
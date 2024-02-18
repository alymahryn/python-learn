import random
import tkinter as tk
from tkinter import ttk

decision = str

def dungeon():
    global decision
    while True:
        try:
                print("You're in a dark room")
                print("Threre is no ligth nor escape")
                print("Brave warrior, choose your path! (left / right)")
                decision = input()
                
                if decision == "left":
                    print("You chose the wrong path")
                    print("You're now Dead!")
                
                if decision == "right":
                    print("You have escaped")
                
                else:
                    print("Please enter a either left or right")
                    break    
                    
    
        except ValueError:
            print("Please enter either left or right in the terminal")
    
    
dungeon()    
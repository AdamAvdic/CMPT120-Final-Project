# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s):D100, Adam Avdic, 301429186
# Author(s):D100, Crystal Waleed, 301423982
# Programmed with Replit.com
# Date: 06/12/2021
# Description: Final project for cmpt120

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()
 # list of system options
system = [
             "Q: Quit",
             "O: Open Image",
             "S: Save Current Image",
             "R: Reload Original Image"
          ]

 # list of basic operation options
basic = [
           "1: Apply Red Filter",
           "2: Apply Green filter",
           "3: Apply Blue Filter",
           "4: Apply Sepia Filter",
           "5: Apply Warm Filter",
           "6: Apply Cold Filter",
           "7: Switch to Advanced Functions",
          ]

 # list of advanced operation options
advanced = [
              "1: Rotate Left",
              "2: Rotate Right",
              "3: Double Size",
              "4: Half Size",
              "5: Locate Fish",
              "6: Switch to Basic Functions",
              ]
 # a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
     """
     Input:  state - a dictionary containing the state values of the application
     Returns: a list of strings, each element represets a line in the interface
     """
     menuString = ["Welcome to CMPT 120 Image Processer!"]
     menuString.append("") # an empty line
     menuString.append("Choose the following options:")
     menuString.append("") # an empty line
     menuString += system
     menuString.append("") # an empty line

     # build the list differently depending on the mode attribute
     if state["mode"] == "basic":
         menuString.append("--Basic Mode--")
         menuString += basic
         menuString.append("")
         menuString.append("Enter your choice (Q/O/S/R or 1-6)")
     elif state["mode"] == "advanced":
         menuString.append("--Advanced Mode--")
         menuString += advanced
         menuString.append("")
         menuString.append("Enter your choice (Q/O/S/R or 1-6)")
     else:
         menuString.append("Error: Unknown mode!")

     return menuString
def handleUserInput(state, img):
     userInput = state["lastUserInput"].upper()
     # handle the system functionalities
     if userInput.isalpha(): # check if the input is an alphabet
         print("Log: Doing system functionalities " + userInput)
         if userInput == "Q": 
             print("Log: Quitting...")
         #open image to apply filters    
         elif userInput == "O":
           print("Log: Opening Image...")
           tkinter.Tk().withdraw()
           openFilename = tkinter.filedialog.askopenfilename()
           img = cmpt120imageProjHelper.getImage(openFilename)
           cmpt120imageProjHelper.showInterface(img, "open-image",generateMenu(state))
           state["lastOpenFilename"] = openFilename
         #save the current image
         #dont need to input ".jpg"
         elif userInput == "S":
           print("Log: Saving Image...")
           tkinter.Tk().withdraw()
           saveFilename = tkinter.filedialog.asksaveasfilename()
           cmpt120imageProjHelper.saveImage(img,saveFilename + ".jpg")
           cmpt120imageProjHelper.showInterface(img,"project image",generateMenu(state))
         #reload the original image
         elif userInput == "R":
          print("Log: Reloading... ")
          img=cmpt120imageProjHelper.getImage(state["lastOpenFilename"])
          cmpt120imageProjHelper.showInterface(img,"reload file",generateMenu(state))

     #or handle the manipulation functionalities based on which mode the application is in
     
     elif userInput.isdigit(): # has to be a digit for manipulation options
         print("Log: Doing manipulation functionalities " + userInput)
         if state["mode"] == "basic":
           ##basic function iterations
           #Applying the red filter
           if userInput == "1":
             print("Log: Performing " + basic[int(userInput)-1])
             img = cmpt120imageManip.applyRedFilter(currentImg)
             cmpt120imageProjHelper.showInterface(img, "Apply Red FIlter", generateMenu(state)) 
           #Applying the green filter 
           elif userInput == "2":
             print("Log: Performing " + basic[int(userInput)-1])
             img = cmpt120imageManip.GreenFilter(currentImg)
             cmpt120imageProjHelper.showInterface(img,"Apply Green Filter",generateMenu(state))
           #Applying the blue filter
           elif userInput == "3":
             print("Log: Performing " + basic[int(userInput)-1])
             img = cmpt120imageManip.BlueFilter(currentImg)
             cmpt120imageProjHelper.showInterface(img, "Apply blue filter ", generateMenu(state))
           #Applying the sepia filter
           elif userInput == "4":
             print("Log: Performing " + basic[int(userInput)-1])
             img = cmpt120imageManip.SepiaFilter(currentImg)
             cmpt120imageProjHelper.showInterface(img, "Apply Sepia Filter ", generateMenu(state))
           #Applying the warm filter
           elif userInput == "5": 
             print("Log: Performing " + basic[int(userInput)-1])
             img = cmpt120imageManip.Combined_Warm(currentImg)
             cmpt120imageProjHelper.showInterface(img, "Apply Warm Filter ", generateMenu(state))
           #applying the cold filter
           elif userInput == "6":
             print("Log: Performing " + basic[int(userInput)-1])
             img = cmpt120imageManip.Combined_Cold(currentImg)
             cmpt120imageProjHelper.showInterface(img, "Apply Cold Filter ", generateMenu(state))
           #Switch the basic functions to the advanced functions
           elif userInput == "7":
             print("Log: Performing " + basic[int(userInput)-1])
             state["mode"] = "advanced"
             cmpt120imageProjHelper.showInterface(img,"project-photo.jpg", generateMenu(state))
           #dictionary to apply advanced functions menu 
         elif state["mode"] == "advanced":
           #Rotate the image to the left
           if userInput == "1":
             img = cmpt120imageManip.rotate_left(currentImg)
             cmpt120imageProjHelper.showInterface(img, "rotated left image", generateMenu(state))
           #Rotate the image to the right
           elif userInput == "2":
             print("Log: Performing " + advanced[int(userInput)-1])
             img=cmpt120imageManip.rotate_right(currentImg)
             cmpt120imageProjHelper.showInterface(img,"rotated right image",generateMenu(state))
           #Double the size of the image
           elif userInput == "3":
             print("Log: Performing " + advanced[int(userInput)-1])
             img=cmpt120imageManip.DoubleSize(currentImg)
             cmpt120imageProjHelper.showInterface(img,"doubled size",generateMenu(state))
           #Half the size of the image
           elif userInput == "4":
             print("Log: Performing " + advanced[int(userInput)-1])
             img=cmpt120imageManip.HalfSize(currentImg)
             cmpt120imageProjHelper.showInterface(img,"half sized",generateMenu(state))
           #Locate the fish in fish.jpg
           elif userInput == "5":
             print("Log: Performing " + advanced[int(userInput)-1])
             fish = cmpt120imageProjHelper.getImage("fish.jpg")
             x=cmpt120imageManip.fish_finder(fish)
             cmpt120imageProjHelper.showInterface(x,"found fish",generateMenu(state)) 
           #Switch back to the basic functions    
           elif userInput == "6":
             state["mode"] = "basic"
             print("Log: Performing " + advanced[int(userInput)-1])
             cmpt120imageProjHelper.showInterface(currentImg,"basic functions menu", generateMenu(state))

     else:  #unrecognized user input
         print("Log: Unrecognized user input: " + userInput)
     return img

 # *** DO NOT change any of the code below this point ***

 # use a dictionary to remember several state values of the application
appStateValues = {"mode": "basic",
                    "lastOpenFilename": "","lastSaveFilename": "",
                    "lastUserInput": ""
                    }

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

 # ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
 # a while-loop getting events from pygame
while keepRunning:
     ### use the pygame event handling system ###
     for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
             appStateValues["lastUserInput"] = pygame.key.name(event.key)
             # prepare to quit the loop if user inputs "q" or "Q"
             if appStateValues["lastUserInput"].upper() == "Q":
                 keepRunning = False
             # otherwise let the helper function handle the input
             else:
                 currentImg = handleUserInput(appStateValues, currentImg)
         elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
             keepRunning = False
 # shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
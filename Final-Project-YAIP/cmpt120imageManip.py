# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): D100, Adam Avdic, 301429186
# Author(s): D100, Crystal Waleed, 301423982
# Date:  06/12/2021
# Description: Final project for cmpt120

import cmpt120imageProjHelper
import numpy


## Red filter function

def applyRedFilter(pixels):
  #get width and height of image
  height = len(pixels)
  width = len(pixels[0])
  #loop through each row and column
  for row in range(height):
    for col in range(width):
      #get red color
      pixel = pixels[row][col]
      red = pixel[0]
      #assign 0 values to blue and green
      pixels[row][col] = [red,0,0]
  return pixels
  
##Green filter function

def GreenFilter(pixels):
  #get width and height
  height = len(pixels)
  width = len(pixels[0])
  #loop through each row and column
  for row in range(height):
    for col in range(width):
      #get green color
      pixel = pixels[row][col]
      green = pixel[1]
      #set blue and red to 0 
      pixels[row][col] = [0,green,0]
  return pixels

##Blue filter function 

def BlueFilter(pixels):
  #get height and width of image
  height = len(pixels)
  width = len(pixels[0])
  #loop through each row and column
  for row in range(height):
    for col in range(width):
      #get blue color 
      pixel = pixels[row][col]
      blue = pixel[2]
      #set green and red to 0 
      pixels[row][col] = [0,0,blue]
  return pixels

##Sepia filter function 

def SepiaFilter(pixels):
  #get height and width of image
  height = len(pixels)
  width = len(pixels[0])
  #loop through each row and column 
  for row in range(height):
    for col in range(width):
      #get red green and blue colors to apply changes
      pixel = pixels[row][col]
      red = pixel[0]
      green = pixel[1]
      blue = pixel[2]
      #Sepia red calculations
      ##use int because of float values
      SepiaRed = int((red*0.393)+ (green *.769) + (blue * .189))
      #Sepia green calculations
      SepiaGreen = int((red * .349) + (green *.686) + (blue * .168))
      #Sepia blue calculations
      SepiaBlue = int((red * .272) + (green *.534) + (blue * .131))
      #If sepia colors are >255, set them to 255
      if SepiaRed > 255:
        SepiaRed = 255
      if SepiaGreen > 255:
        SepiaGreen = 255 
      if SepiaBlue > 255:
        SepiaBlue = 255
      # assign red,green,blue to new filters
      pixels[row][col] = [SepiaRed,SepiaGreen,SepiaBlue]
  return pixels

##Warm filter function scale up 

def WarmFilterScaleUp(result):
  #Warm filter scale up equations for red colors
  if result < 64:
    result = int(result/64*80)
  elif result >= 64 and result < 128:
    result = int((result-64)/(128-64) * (160-80) + 80)
  else:
    result = int((result-128)/(255-128) * (255-160) + 160)
  return result

##Warm filter scale down 

def WarmFilterScaleDown(result):
  #warm filter scale down equations for blue colors
  if result < 64:
    result = int(result/64*80)
  elif result >= 64 and result < 128:
    result = int((result-64)/(128-64) * (100-50) + 50)
  else:
    result = int((result-128)/(255-128) * (255-100) + 100)
  return result

##combined warm filter

def Combined_Warm(pixels):
  #get height and width of image
  height = len(pixels)
  width = len(pixels[0])
  #loop through each row and column
  for row in range(height):
    for col in range(width):
      #assign red, green, and blue colors
      pixel = pixels[row][col]
      red=pixel[0]
      green=pixel[1]
      blue=pixel[2]
      #assign red to scale up function
      Warm_Scale_Up = WarmFilterScaleUp(red)
      #assign blue to scale down function
      Warm_Scale_Down = WarmFilterScaleDown(blue)
      #apply functions to red and blue
      pixels[row][col] = [Warm_Scale_Up,green,Warm_Scale_Down]
  return pixels

##Cold filter scale down

def ColdFilterScaleDown(result):
  #cold filter equations for scaled down red colors
  if result < 64:
    result = result/64*80
  elif result >= 64 and result < 128:
    result = int((result-64)/(128-64) * (100-50) + 50)
  else:
    result = int((result-128)/(255-128) * (255-100) + 100)
  return result

##Cold filter scale up 

def ColdFilterScaleUp(result):
  #cold filter equations for scaled up blue colors
  if result < 64:
    result = result/64*80
  elif result >= 64 and result < 128:
    result = (result-64)/(128-64) * (160-80) + 80
  else:
    result = (result-128)/(255-128) * (255-160) + 160
  return result

##combined cold filter

def Combined_Cold(pixels):
  #get width and height of image
  height = len(pixels)
  width = len(pixels[0])
  #loop through each row and column
  for row in range(height):
    for col in range(width):
      #assign red,green, and blue values
      pixel = pixels[row][col]
      red=pixel[0]
      green=pixel[1]
      blue=pixel[2]
      #apply functions to red and blue
      Cold_Scale_Down = ColdFilterScaleDown(red)
      Cold_Scale_Up = ColdFilterScaleUp(blue)
      pixels[row][col] = [Cold_Scale_Down,green,Cold_Scale_Up]
  return pixels

##flip image to the left 

def rotate_left(pixels):
  #get images height and width 
  height = len(pixels)
  width = len(pixels[0])
  reverse_height = width
  reverse_width = height
  #reverse width and height allowing for rotation
  #create new image
  Black_image = cmpt120imageProjHelper.getBlackImage(reverse_width,reverse_height)
  #loop through each row and column
  for row in range(height):
    for col in range(width):
      #switch rows and -cols to make the image rotate
      Black_image[-col][row]=pixels[row][col]
  return Black_image

#flip image to the right 

def rotate_right(pixels):
  #get images width and height
  width = len(pixels)
  height = len(pixels[0])
  #reverse width and height to allow rotation on new created image
  newWidth = height
  newHeight = width
  #create new image
  Black_image = cmpt120imageProjHelper.getBlackImage(newHeight,newWidth)
  #loop through reach row and column with reversed original images width and height
  for row in range(width):
    for col in range(height):
      #switch row and col due to rotations
      Black_image[col][-row] = pixels[row][col]
  return Black_image

#Double size the image

def DoubleSize(pixels):
  #get height and width of image
  height = len(pixels)
  width = len(pixels[0])
  #create new image with doubling height n width
  black_img=cmpt120imageProjHelper.getBlackImage(width*2,height*2)
  #loop through each row and column
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      #get each pixel from the original image to get a 2x2 block of pixels in the result image
      black_img[row*2][col*2] = pixel
      black_img[row*2][col*2+1] = pixel
      black_img[row*2+1][col*2] = pixel
      black_img[row*2+1][col*2+1] = pixel
  return black_img

#Half size the image

def HalfSize(pixels):
  #get images height and width
  height = len(pixels)
  width = len(pixels[0])
  #get original images height and with and half the size and create a new image
  black_img = cmpt120imageProjHelper.getBlackImage(width//2,height//2)
  #loop through each row and column ans reverse the width and height and half them
  for row in range(width//2):
    for col in range(height//2):
      #Get the averages of the RGB pixels
      pixel_1 = pixels[col*2][row*2] 
      pixel_2 = pixels[col*2+1][row*2] 
      pixel_3 = pixels[col*2][row*2+1] 
      pixel_4 = pixels[col*2+1][row*2+1] 
      averageR = int((pixel_1[0]+pixel_2[0]+pixel_3[0]+pixel_4[0])//4)
      averageG = int((pixel_1[1]+pixel_2[1]+pixel_3[1]+pixel_4[1])//4)
      averageB = int((pixel_1[2]+pixel_2[2]+pixel_3[2]+pixel_4[2])//4)
      #set averages to newly created image
      black_img[col][row] = (averageR,averageG,averageB)
  return black_img

#Fish finder function 

def fish_finder(pixels):
  #get height and width of image
    height = len(pixels)
    width = len(pixels[0])
  #minimum values for row and columns for HSV values
    maxX_value= 0
    maxY_value = 0
    minX_value =1000
    minY_value = 1000
    #loop through each row and column
    for row in range(height):
        for col in range(width):
            pixel = pixels[row][col]
            #assign red,blue and green colors
            Red = pixel[0]
            Green = pixel[1]
            Blue = pixel[2]
            #convert r,g,b to HSV values
            (hue,saturation,value) = cmpt120imageProjHelper.rgb_to_hsv(Red,Green,Blue)
            #https://pinetools.com/image-color-picker
            #^ used for choosing HSV values
            if (hue > 55 and hue < 60) and saturation > 40 and value > 98:
              #iterative comparison for values going over or under indexs'
                if row<minX_value:
                    minX_value = row
                if col<minY_value:
                    minY_value = col
                if col>maxY_value:
                     maxY_value = col
                if row>maxX_value:
                    maxX_value = row
    #function creating green rectangle
    def Create_Rectangle(min_row,start_col,end_row,end_col,img):
      #loop through each row and column for min and max values
      for row in range(min_row,end_row):
        for col in range(start_col,end_col):
          #assign green pixel and apply to min n max HSV values
          green_pixel = [0,255,0]
          img[min(row,min_row)][col] = green_pixel
          img[max(row,end_row)][col] = green_pixel
          img[row][min(col,start_col)] = green_pixel
          img[row][max(col,end_col)] = green_pixel
    #apply rectangle function
    Create_Rectangle(minX_value,minY_value,maxX_value,maxY_value,pixels)
    #create new black image to perform operation 
    black_img = cmpt120imageProjHelper.getBlackImage(width,height)

    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
         black_img[row][col] = pixels[row][col]

    return black_img
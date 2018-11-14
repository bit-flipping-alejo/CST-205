def getPic():
  return makePicture(pickAFile())

def savePicture(pic, fileName):
  file = r"C://temp/" + fileName
  writePictureTo(pic, file)
  
def addSnowMan(pic, targetX, targetY):
  #pic = getPic()
  
  picWidth = getWidth(pic)
  picHeight = getHeight(pic)
  
  # draw the body
  addOval(pic, targetX + 20, targetY, 60, 60, black)
  addOval(pic, targetX + 10, targetY + 50, 80, 80, black)
  addOval(pic, targetX, targetY + 120, 100, 100, black)
  addOvalFilled(pic, targetX + 20, targetY, 60, 60, white)
  addOvalFilled(pic, targetX + 10, targetY + 50, 80, 80, white)
  addOvalFilled(pic, targetX, targetY + 120, 100, 100, white)
  
  # draw the face
  addOvalFilled(pic, targetX + 35, targetY + 15, 5, 5, black)
  addOvalFilled(pic, targetX + 55, targetY + 15, 5, 5, black)
  
  addArcFilled(pic, targetX + 15, targetY + 15, 40, 20, 300, 35, orange)
  addArcFilled(pic, targetX + 30, targetY + 30, 40, 20, 180, 180, black)
  # add arms and buttons
  addOvalFilled(pic, targetX + 47, targetY + 75, 5, 5, black)
  addOvalFilled(pic, targetX + 47, targetY + 95, 5, 5, black)
  addOvalFilled(pic, targetX + 47, targetY + 115, 5, 5, black)
  
  for y in range(0,5):
    addLine(pic, targetX + 10, targetY + 90 - y, targetX - 40, targetY + 65 - y)
    
  for y in range(0,5):
    addLine(pic, targetX + 90, targetY + 90 - y, targetX + 140, targetY + 65 - y)
  
  fileName = "snowManInDesert.jpg"
  savePicture(pic, fileName)
  
# Problem 1. Takes in 4 inputs from the user, 3 pictures and a string. Then creates a collage.

def thanksgivingCollage():
  import java.awt.Font as Font
  # ask user for pictures to make the collage
  print("Please select your background image.")
  background = getPic()
  print("Please select the first picture to integrate.")
  pictureOne = getPic()
  print("Please select the second picture to integrate.")
  pictureTwo = getPic()
  name = raw_input("Please enter your full name: ")
  str = "Happy Thanksgiving from"
  
  backgroundFirstMod = pyCopy(pictureOne, background, 800, 800)
  
  thanksgivingCard = pyCopy(pictureTwo, backgroundFirstMod, 0, 800)
  
  thanksFont = makeStyle("Helvetica", Font.BOLD, 36)
  
  addTextWithStyle(thanksgivingCard, 100, 100, str, thanksFont, white)
  addTextWithStyle(thanksgivingCard, 100, 140, name, thanksFont, white)
  
  show(thanksgivingCard)
  
def pyCopy(source, target, targetX, targetY):
  sourceWidth = getWidth(source)
  sourceHeight = getHeight(source)
  targetWidth = getWidth(target)
  targetHeight = getHeight(target)
 
  # need to consider if the user inputs the copy destination outside the bounds of the 
  # target dimensions. will position the image so the right and bottom edges of the source
  # image will align with the right and bottom edges of the target image
  if (targetX + sourceWidth) > targetWidth:
    targetX = targetWidth - sourceWidth -1
  if (targetY + sourceHeight) > targetHeight:
    targetY = targetHeight - sourceHeight -1
    
  # copy the image to the target destination
  for x in range (sourceWidth):
    newX = (targetX + x)
    for y in range (sourceHeight):
      sourcePixel = getPixel(source, x, y)
      newY = (targetY + y)
      if getGreen(sourcePixel) > 170 and getRed(sourcePixel) < 40 and getBlue(sourcePixel) < 85:
        continue
      else:
        targetPixel = getPixel(target, newX, newY)
        sourceColor = getColor(sourcePixel)
        setColor(targetPixel, sourceColor)
  
  return target
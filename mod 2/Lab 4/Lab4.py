# Ivan Alejandre
# Lab 4 Exercises


def get_pic():
  return makePicture(pickAFile())
  
# Problem 1:

# Takes the left half of the image and mirrors it on the right
def mirrorLeft():
  pic = get_pic()
  file = r"C:\IvanAlejandreImages_Lab4\mirrorLeft.jpg"
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (0, picWidth/2):
    for y in range (0, picHeight):
      pixelCurrent = getPixel(pic, x, y)
      newPix = getPixel(pic, (picWidth - x - 1), y)
      pixelColor = getColor(pixelCurrent)
      setColor(newPix, pixelColor)
  
  writePictureTo(pic, file)

# Takes right half and mirrors it on the left
def mirrorRight():
  pic = get_pic()
  file = r"C:\IvanAlejandreImages_Lab4\mirrorRight.jpg"
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (picWidth/2, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, (picWidth - x), y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  writePictureTo(pic, file)
  
# Takes top half and mirrors it on the bottom
def mirrorTop():
  pic = get_pic()
  file = r"C:\IvanAlejandreImages_Lab4\mirrorTop.jpg"
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (0, picWidth):
    for y in range (0, picHeight/2):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, x, picHeight - y - 1)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
      
  writePictureTo(pic, file)

# Takes bottom half and mirrors it on the top  
def mirrorBottom():
  pic = get_pic()
  file = r"C:\IvanAlejandreImages_Lab4\mirrorBottom.jpg"
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (0, picWidth):
    for y in range (picHeight/2, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, x, picHeight - y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
      
  writePictureTo(pic, file)
  
# Mirrors an image twice. Hardcoded to mirror bottom then right
def doubleMirror():
  pic = get_pic()
  file = r"C:\IvanAlejandreImages_Lab4\doubleMirror.jpg"
  
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  # mirror bottom half first
  for x in range (0, picWidth):
    for y in range (picHeight/2, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, x, picHeight - y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  # then mirror right half of new image
  for x in range (picWidth/2, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, (picWidth - x), y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  writePictureTo(pic, file)
  
# Problems 2-4: I wrote this extra function to help manage inputs and outputs
# of each function. Since each one requires an input parameter, having the user
# select the image and what to do to the image is centralized to one function

def alterPic():
  pic = get_pic()
  
  print("Enter 1 to copy an image,")
  print("Enter 2 to rotate an image 90 degrees to the left,")
  choice = input("Or enter 3 to shrink an image by half: ")
  if choice == 1:
    newPic = simpleCopy(pic)
    file = r"C:\\Temp\copiedImage1.jpg"
    writePictureTo(newPic, file)
  elif choice == 2:
    newPic = rotatePic(pic)
    file = r"C:\Temp\rotatedImage.jpg"
    writePictureTo(newPic, file)
  elif choice == 3:
    newPic = shrink(pic)
    file = r"C:\\Temp\shrunkImage.jpg"
    writePictureTo(newPic, file)
  else:
    print("Invalid entry.")


# Problem 2  
def simpleCopy(pic):
  picWidth = getWidth(pic)
  picHeight = getHeight(pic)
  
  newPic = makeEmptyPicture(picWidth, picHeight)
  
  for x in range (0, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(newPic, x, y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  return newPic
  
# Problem 3
# rotates image 90 degress to the left
def rotatePic(pic):
  picWidth = getWidth(pic)
  picHeight = getHeight(pic)
  
  rotatedPic = makeEmptyPicture(picHeight, picWidth)
  
  for x in range (0, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, (picWidth - x - 1), y)
      newPixel = getPixel(rotatedPic, y, x)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  return rotatedPic
  
# Problem 4
# shrinks image by half
def shrink(pic):
  picWidth = getWidth(pic) / 2
  picHeight = getHeight(pic) / 2

  shrunkPic = makeEmptyPicture(picWidth, picHeight)
  
  for x in range (0, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, (x * 2), (y * 2))
      newPixel = getPixel(shrunkPic, x, y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  return shrunkPic
def simplePic():
  pic = makePicture(pickAFile())
  
  file = r"C:\\Temp\shrunk.jpg"
  
  newPic = shrink(pic)

  show(newPic)
  
  writePictureTo(newPic, file)
  
  
# shrinks image by half
def shrink(pic):
  picWidth = getWidth(pic) / 2
  picHeight = getHeight(pic) / 2
  x2 = 0
  y2 = 0
  
  shrunkPic = makeEmptyPicture(picWidth, picHeight)
  
  print(picHeight)
  print(picWidth)
  for x in range (0, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, (x * 2), (y * 2))
      newPixel = getPixel(shrunkPic, x, y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  return shrunkPic

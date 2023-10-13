from PIL import Image,ImageFilter
myImage = Image.open('C:\chase.jpg')
myImage.load
myImage.format
myImage.size
myImage.show()

#comment out the filters you do not want to use
blur = myImage.filter(ImageFilter.BLUR)
blur.show()

thumbnail = myImage.thumbnail((100,100))
myImage.show()


black_white = myImage.convert('L')#L in the Pillow library changes the color
black_white.show()

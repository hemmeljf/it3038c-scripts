# LAB 7 - Jake Hemmelgarn
I used the plugin in Pillow and here is how to run it to manipulate images. 

First, let's create a Virtual ENV called pillow on our Windows machine

```
virtualenv ~/venv/pillow
.\~/venv/pillow/scripts/activate
pip install pillow 
```

Find and download an image from the internet and save it to your C-drive. 

Create a python file and add the following code

```
from PIL import Image,ImageFilter
myImage = Image.open('path/to/image.jpg')
myImage.load
```

Add the following code to get the image to populate

```
myImage.format
myImage.size
myImage.show()
```

Now we can use ImageFilter module to apply a filter to it and show it.

"Blur the image"
```
blur = myImage.filter(ImageFilter.BLUR)
blur.show()
```

"Make the image a Thumbnail"
```
thumbnail = myImage.thumbnail((100,100))
myImage.show()
```

"Apply a filter to the image"
```
black_white = myImage.convert('L')#L in the Pillow library changes the color
black_white.show()
```

Now that we are done, lets deactivate the Pillow plugin

```
deactivate
```

"""
Author username(s): bulsonjg, johnsoam
Date: 11/10/16
Assignment/problem number: Homework 14
Assignment/problem title: Image Processing
"""

import image

def color2gray(color):
    """Convert a color to a shade of gray.
    Parameter: color, a tuple representing an RGB color
    Produces: a tuple representing an equivalent gray
    """
    #brightness = (color[0] + color[1] + color[2]) // 3
    #return (brightness, brightness, brightness)
    (red, green, blue) = color
    luminance = int(0.2126*red + 0.7152*green + 0.0722*blue)
    return (luminance, luminance, luminance)

def grayscale(photo):
    """Convert a color image to grayscale.
    Parameter: photo, an Image object
    Produces: a new grayscale Image object
    """
    width = photo.width()
    height = photo.height()
    newPhoto = image.Image(width, height, title = 'Grayscale image')
    for y in range(height):
        for x in range(width):
            color = photo.get(x,y)
            newPhoto.set(x, y, color2gray(color))
    return newPhoto

def reduce(photo):
    """Reduce an image to 1/4 of its size by averaging the colors of four pixels for every new pixel

    Parameter:
        photo - an image object

    Returns: a new reduced image object
    """

    width = photo.width()
    height = photo.height()
    newPhoto = image.Image(width//2, height//2, title="Reduced Image")

    # Mod 2s present to account for odd photo dimensions
    for y in range(0, height-height%2, 2):
        for x in range(0, width-width%2, 2):
            red = (photo.get(x,y)[0]+photo.get(x+1,y)[0]+photo.get(x,y+1)[0]+photo.get(x+1,y+1)[0])//4
            green = (photo.get(x,y)[1]+photo.get(x+1,y)[1]+photo.get(x,y+1)[1]+photo.get(x+1,y+1)[1])//4
            blue = (photo.get(x,y)[2]+photo.get(x+1,y)[2]+photo.get(x,y+1)[2]+photo.get(x+1,y+1)[2])//4
            color = (red, green, blue)
            newPhoto.set(x//2, y//2, color)
    return newPhoto

def averageColorChannel(photo, x, y, colorChannel):
    """Finds the average color value (0-255) of a pixel and its surrounding 3x3 pixels.

    Parameters:
        photo: the image file of the original photo
        x: the x coordinate of the pixel
        y: the y coordinate of the pixel
        colorChannel: the color channel wanted (either 0, 1, or 2 for r, g, b respectively)

    Returns: The averaged color value as an integer

    Bug notice:
        See lines 71 and 75
    """
    yboxStart = -1  # Deals with "edge" and "corner" cases =)
    yboxStop = 2    #  (meaning the edges and corners of the image)
    xboxStart = -1
    xboxStop = 2
    if y==0:
        yboxStart = 0
    elif y == photo.height()-1: # The -1 only is needed in the bottom right corner of the image. We are not sure why, and the border of the image does not look properly blurred
        yboxStop = 1
    if x==0:
        xboxStart = 0
    elif x == photo.width()-1:
        xboxStop = 1

    colorAccumulator = 0
    for ybox in range(yboxStart, yboxStop):
        for xbox in range(xboxStart, xboxStop):
            colorAccumulator += photo.get(x+xbox, y+ybox)[colorChannel]
    return colorAccumulator//9

def blur(photo):
    """
    Creates a blurred copy of an image.

    Parameters:
        photo: the image to be blurred as an image file

    Returns: the new blurred photo
    """
    width = photo.width()
    height = photo.height()
    newPhoto = image.Image(width, height, title="Blurred Image")

    for y in range(height):
        for x in range(width):
            # print(x, y)
            red = averageColorChannel(photo, x,y,0)
            green = averageColorChannel(photo, x,y,1)
            blue = averageColorChannel(photo, x,y,2)
            color = (red, green, blue)
            newPhoto.set(x, y, color)
    return newPhoto

def repeatBlur(photo, repeats):
    """
    Repeatedly blurs a given photo

    Parameters:
        photo: the image to be blurred
        repeats: the number of times to blur the image

    Returns: a blurred image
    """
    blurredPhoto = photo
    for iteration in range(repeats+1):
        blurredPhoto = blur(blurredPhoto)
    return blurredPhoto

def crop(photo, topleft_x, topleft_y, width, height):
    """
    Crops an image to the specified area

    Parameters:
        photo: the image to be cropped
        topleft_x: the top-left corner of the cropped area as an integer
        topleft_y: the top-left corner of the cropped area as an integer
        width: the width of the cropped area
        height: the height of the cropped area

    Returns: a smaller, cropped image
    """

    newPhoto = image.Image(width, height, title="Cropped Photo")

    for y in range(height):
        for x in range(width):
            color = photo.get(topleft_x+x, topleft_y+y)
            newPhoto.set(x, y, color)
    return newPhoto


def main():
    penguin = image.Image(file='penguin.gif', title='Penguin')
    blurredPenguin = blur(penguin)
    # croppedPenguin = crop(penguin, 50, 50, 150, 100)
    penguin.show()
    blurredPenguin.show()
    # croppedPenguin.show()
    image.mainloop()

if __name__=='__main__':
    main()

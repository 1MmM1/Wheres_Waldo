from image_slicer import slice
from PIL import Image
import os
import shutil

def cropTiles(src):
    """
    Crops the width/height of the original image to multiples of 64 and generates 64x64 tile images.

    Args:
        src (string): the path to the image to crop
    Returns:
        The number of rows and columns of the image after tiling
    """
    print("Cropping input image:", src)
    im = Image.open(src)
    width, height = im.size

    rWidth = width % 64
    rHeight = height % 64
    imCrop = im.crop((rWidth / 2, rHeight / 2, width - rWidth / 2, height - rHeight / 2))
    if not os.path.isdir('./temp'):
        print("Creating temp folder...")
        os.mkdir('./temp')
        print("Done\n")
    
    # Temporarily saves a cropped version of the original file with height/width as multiples of 64.
    imCrop.save('./temp/temp.jpg')
    cropWidth, cropHeight = imCrop.size

    numRows = int(cropHeight / 64)
    numCols = int(cropWidth / 64)

    # Generates 64x64 tiles
    print("Generating 64x64 tiles from original image...")
    slice('./temp/temp.jpg', col=numCols, row=numRows, save=True)
    print("Done")

    # Removes the cropped original image after generating tiles.
    os.remove('./temp/temp.jpg') 

    return (numRows, numCols)

def stitchTiles(rows, cols, waldoTiles):
    """
    Stiches the tiles back together in black and white, only leaving the specified waldoTiles 
    in color. Saves the final image as foundwaldo.jpg and deletes the temporary images.
    """
    print("Stitching tiles...")
    newImage = Image.new('RGB', (64 * cols, 64 * rows))
    ims = []

    # Iterates through the cropped images and adds them to a list.
    for tile in os.listdir('./temp/'):
        im = Image.open(f'./temp/{tile}')
        if tile not in waldoTiles:
            im = im.convert('1')
        ims.append(im)

    # "Pastes" the cropped tiles into newImage.
    i, x, y = 0, 0, 0
    for _ in range(rows):
        for _ in range(cols):
            newImage.paste(ims[i], (x, y))
            i += 1
            x += 64
        y += 64
        x = 0

    newImage.save("./foundwaldo.jpg")
    print("Done")

    print("\nDeleting tiles...")
    # Removes the temp directory containing the cropped images.
    shutil.rmtree('./temp')
    print("Done")
    
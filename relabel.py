import os
from shutil import copy, copyfile

def main():
    # Changes the labels of the original images to match the cropped images.
    updateLabels()
    prettify()
                
# Changes the labels of the original images to match the cropped images.
def updateLabels():
    resolutions = [64, 128, 256]
    colors = ['', '-bw', '-gray']
    folders = ['waldo', 'notwaldo']

    for res in resolutions:
        for color in colors:
            for folder in folders:
                src = f'./wheres-waldo/{res}{color}/{folder}/'
                # 5_x_x and 6_x_x are duplicates, so delete them here.
                delete(src, 5)
                delete(src, 6)

                relabel(src, 20, 5)
                relabel(src, 21, 6)

    ogSrc = f'./wheres-waldo/original-images/'
    relabelOg(ogSrc, 2, 99)
    relabelOg(ogSrc, 17, 2)
    relabelOg(ogSrc, 13, 17)
    relabelOg(ogSrc, 8, 13)
    relabelOg(ogSrc, 4, 8)
    relabelOg(ogSrc, 19, 4)
    relabelOg(ogSrc, 15, 19)
    relabelOg(ogSrc, 11, 15)
    relabelOg(ogSrc, 7, 11)
    relabelOg(ogSrc, 3, 7)
    relabelOg(ogSrc, 18, 3)
    relabelOg(ogSrc, 14, 18)
    relabelOg(ogSrc, 9, 14)
    relabelOg(ogSrc, 5, 9)
    relabelOg(ogSrc, 99, 5)

    relabelOg(ogSrc, 12, 98)
    relabelOg(ogSrc, 10, 12)
    relabelOg(ogSrc, 6, 10)
    relabelOg(ogSrc, 16, 6)
    relabelOg(ogSrc, 98, 16)

# Changes the label of an original image.
def relabelOg(src, oldNum, newNum):
    os.rename(f'{src}{oldNum}.jpg', f'{src}{newNum}.jpg')

# Changes the label of a cropped image.
def relabel(src, labelNum, newNum):
    # print(f'Relabling images with label {labelNum}_x_x to {newNum}_x_x in {src}...')
    files = os.listdir(src)

    # Iterates through all files in directory
    for file in files:
        # Renames only if file is in the format "labelNum_x_x"
        if (file.startswith(f'{labelNum}_')):
            # Replaces only the first iteration of "labelNum_"
            newLabel = file.replace(f'{labelNum}_', f'{newNum}_', 1)
            os.rename(src + file, src + newLabel)
            # print(file + " --> " + newLabel)

# Removes all cropped images in src with label of the form removeNum_x_x.
def delete(src, removeNum):
    # print(f'Deleting images with label {removeNum}_x_x in {src}...')
    files = os.listdir(src)
    for file in files:
        if (file.startswith(f'{removeNum}_')):
            os.remove(src + file)

# Reorganizes/prettifies the data.
def prettify():
    folders = ['waldo', 'notwaldo']

    # Make new folder structure
    if not os.path.isdir('waldo-data-organized'):
        os.makedirs('waldo-data-organized')
    for i in range(1, 20):
        folder = f'./waldo-data-organized/{i}'
        if not os.path.isdir(folder):
            os.makedirs(folder)
            os.makedirs(f'{folder}/waldo')
            os.makedirs(f'{folder}/notwaldo')

    ogSrc = './wheres-waldo/original-images/'
    for file in os.listdir(ogSrc):
        fileNum = file.replace('.jpg', '')
        copyfile(f'{ogSrc}{file}', f'./waldo-data-organized/{fileNum}/{file}')

    for folder in folders:
        src = f'./wheres-waldo/64/{folder}/'
        files = os.listdir(src)
        
        for file in files:
            fileNum = file.split('_')[0]
            copyfile(f'{src}{file}', f'./waldo-data-organized/{fileNum}/{folder}/{file}')

if __name__ == '__main__':
    main()
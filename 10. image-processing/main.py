#In this project we want to do image processing
from PIL import Image,ImageFilter
img = Image.open('./Flowers/flower2.jpg')
print(img)	#image object
print(img.format)	#image format
print(img.size)	#image size
print(img.mode)	#image mode
print(dir(img))	#image dir

#Adding "BLUR" Filter to Image
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png",'png')

#Adding "SMOOTH" Filter to Image: WE NEED PNG FORMAT
#Adding "SHARPEN" Filter to Image: WE NEED PNG FORMAT

#Convert jpeg format to png format
filtered2_img = img.convert('L')
filtered2_img.save("grey.png", 'png')
filtered2_img.show()	#show image in a seprate page

#Rotate image
rotate_img = filtered2_img.rotate(90)
rotate_img.save("rotate.png", 'png')

#Resize image
resize = filtered2_img.resize((300,300))
resize.save("resize.png", 'png')

#Crop image
box = (100, 100, 1800, 1800)
region = filtered2_img.crop(box)
region.save("crop.png", 'png')

#Working on astro.jpg for correct resizing (using thumbnail) and write in thumbnail.jpg
im = Image.open('./Flowers/astro.jpg')
print(im.size)
im.thumbnail((400,200))
im.save('thumbnail.jpg')
print(im.size)

# Grab images from a same specific folder, work on all images (change,resize,convert...) then add the new images in a new folder that we want to create(new) if it is not already created.

#step1:grab first and second arguments (flowers,new)
import sys
import os 

from PIL import Image
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

#step2:check if new folder exists, if not create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

#step3:loop through flowers. convert all images to PNG and save to new folder.
for items in os.listdir(image_folder):	#get all files in the same directory
	img = Image.open(f'{image_folder}{items}')
	final_images = os.path.splitext(items)[0]	#seperate the filename and type and choose the filename
	img.save(f'{output_folder}/{final_images}.png',"png")
	print('all done!')
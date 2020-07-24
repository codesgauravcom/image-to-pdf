from PIL import Image

#provide path of image that you want to convert into pdf

img = Image.open(r'c:\users\dell\downloads\myfirst.jpeg')

imgg = img.convert('RGB')

#provide path of folder where you want to save pdf with name

imgg.save(r'c:\users\dell\downloads\mynew.pdf')

print('image is saved as mynew.pdf')
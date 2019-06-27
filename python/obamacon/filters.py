from PIL import Image

def load_img(file_name):
    im = Image.open(file_name)
    return im

def show_img(img_object):
    img_object.show()

def save_img(img_object, save_name):
    img_object.save(save_name)

img = load_img("obama.jpg")
save_img(img, "dog.jpg")
#should return a new Image object with filter applied
# def obamacon(img_object)
#     #APPEND
#     original_pixels = img_object.getdata()

# #use for loop to iterate through every single pixel
#      #at every pixel, sum up the RGB values
#      #use conditionals and boolean checks to determine which new color to change to

# Image.getdata(band=None)

#def obamacon(img_object):
    #load_img
    #save_img
obamacon()
 
import face_recognition
import numpy as np
#from PIL import Image, ImageDraw
import cv2
picture_of_me = face_recognition.load_image_file('./Documents/known_people/Andy.png')
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features
# that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file('./Documents/unknown_people/testpic_2.png')
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
fl  = face_recognition.face_locations(unknown_picture)
top, right, bottom, left = fl[0]
#print(fl) #top, right, bottom, left
#im = Image.open('./Documents/known_people/Rosa.png')
#obj = ImageDraw.Draw(picture_of_me)
#obj.rectangle([fl[0][0], fl[0][3], fl[0][1], fl[0][2]])
#im.save('./Documents/known_people/Rosa2.png')
b,g,r = cv2.split(unknown_picture)       # get b,g,r
rgb_img = cv2.merge([r,g,b])
cv2.rectangle(rgb_img, (left, top), (right, bottom), (0, 0, 255),thickness=3)
cv2.imwrite('./Documents/unknown_people/ROSA4.png', rgb_img)
# Now ee can see the two face encodings are of the same person with
# `compare_faces`!

#results = face_recognition.compare_faces([my_face_encoding],
#		unknown_face_encoding)

#if results[0] == True:
#    print("It's a picture of me!")
#else:
#	print("It's not a picture of me!")

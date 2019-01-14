import face_recognition
import numpy as np
#from PIL import Image, ImageDraw
import cv2
import glob
import os
import pdb

path = "/Volumes/Seagate Backup Plus Drive/shawshank_frames/"
#frame_files = os.listdir(path)


frame_files = glob.glob(path+"*.jpg")
print(len(frame_files))
#print(type(frame_files))

picture_of_me = face_recognition.load_image_file('./known_people/Bogs.jpeg')
print('2')
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
print('3')
# film_frames = []
# film_frames.append()

for ith, frame in enumerate(frame_files):
	#frame = os.path.join(path, frame)

	captioned_image = face_recognition.load_image_file(frame)
	try:
		captioned_image_encoding = face_recognition.face_encodings(captioned_image)[0]
		results = face_recognition.compare_faces([my_face_encoding], captioned_image_encoding)
		if results[0] == True:
			location = face_recognition.face_locations(captioned_image)[0]
			print(location)
			top, right, bottom, left = location

			b,g,r = cv2.split(captioned_image)
			rgb_img = cv2.merge([r,g,b])
			cv2.rectangle(rgb_img, (left, top), (right, bottom), (0, 0, 255), thickness=2)
			cv2.imwrite('/Volumes/Seagate Backup Plus Drive/Detected_Bogs/bogs_{}'.format(os.path.basename(frame)), rgb_img)
			print('/Volumes/Seagate Backup Plus Drive/Detected_Bogs/bogs_{}'.format(os.path.basename(frame)),"---complete")
		else:
			pass
	except IndexError:
		print('IndexError:{}'.format(frame))
		pass
	except:
		import traceback
		traceback.print_exc()
		print(frame, "error")



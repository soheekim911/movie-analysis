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


"""
Codes for face recognition with GPU
"""
frames = []
frame_count = 0

# while frame_files.isOpened():
frame = frame_files

# 	if not ret:
# 		break


frame_count += 1
frames.append(frame)


# Every 128 frames(default batch size), batch process the list of frames to find faces
if len(frames) == 128:
	batch_of_face_locations = face_recognition.batch_face_locations(frames, number_of_times_to_upsample=0)
	print('1')
	# Now list all the face we found in all 128 frame
	for frame_number_in_batch, face_locations in enumerate(batch_of_face_locations):
		number_of_faces_in_frame = len(face_locations)
		print('2')	
		frame_number = frame_count - 128 + frame_number_in_batch
		print("I found {} face(s) in frame #{}".format(number_of_faces_in_frame, frame_number))

		# for face_location in face_locations:
		# 	top, right, bottom, left = face_location

		# 	b,g,r = cv2.split(captioned_image)
		# 	rbg_img = cv2.merge([r,g,b])
		# 	cv2.rectangle(rgb_imgm, (left,top), (right, bottom), (255,0,0), thickness=2)
		# 	cv2.imwrite('/Volumes/Seagate Backup Plus Drive/Bbox_test/bbox_{}'.format(os.path.basename(frame)), rgb_img)




"""
This is original codes for face recognition without GPU help
"""

'''
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
			rgb_img = cv2.merge([r,g,b]). # Convert image from BGR to RGB color
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
'''


import cv2
from senas.solution_hand import hand_video

class videos(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		
	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		frame_flip = cv2.flip(image, 1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

	def get_frame1(self):
		success, image = self.video.read()
		frame_flip = hand_video(image)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

def video_generator_solution(camera):
     while True:
        # ret, jpeg = cv2.imencode('.jpg', camera.get_frame())
         frame =  camera.get_frame1()
         yield (b'--frame\r\n'
	 		b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_generator(camera):
     while True:
        # ret, jpeg = cv2.imencode('.jpg', camera.get_frame())
         frame =  camera.get_frame()
         yield (b'--frame\r\n'
	 		b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

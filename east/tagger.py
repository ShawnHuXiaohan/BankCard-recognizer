# Simple Image data tagger.
# Label four point of the object in img,
# which in this case, is bankcard number.
# Start from the top left of the object, and go anti-clockwise.

# Do not run this under PyCharm or other IDE, 
# it may cause error that the main window won't show up.
# Run it by cmd line, 'python label.py'.
# And before doing that. make sure the img and txt dir are right.

import os

from PIL import Image
from pylab import *

img_dir = r"X:\projects\bankcard_rec\east\img"
txt_dir = r"X:\projects\bankcard_rec\east\txt"

if not os.path.exists(txt_dir):
	os.mkdir(txt_dir)

fnm_list = [fnm for fnm in os.listdir(img_dir)]
print("Label process start, press [Ctrl+C] to stop.")
i = 1
for fname in fnm_list:
	img_path = os.path.join(img_dir, fname)
	img = array(Image.open(img_path))
	imshow(img)
	x = ginput(4)
	r = []
	for x1, y1 in x:
		r.append(int(x1))
		r.append(int(y1))
	
	name, ext = os.path.splitext(fname)
	txt_path = os.path.join(txt_dir, name + ".txt")
	with open(txt_path, 'w') as f:
		cnt = ",".join(str(c) for c in r)
		f.write(cnt + ",###")
		print("[write for %s]" % name, cnt, "[%d/%d]" % (len(fnm_list), i))
	i += 1
	show()

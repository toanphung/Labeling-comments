import os

if "Segment_VNese_python" not in os.listdir():
	print("Segmentation library not found! Start downloading...")
	os.system("git clone https://github.com/giangtran24/Segment_VNese_python.git")
else:
	print("Segmentation found")


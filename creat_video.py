import cv2
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
import os
img_root="/home/chengyuan/PycharmProjects/Everybody_Dance_Now_Sun//datasets/test_B/"
fps=50
fourcc=VideoWriter_fourcc(*"MJPG")
videoWriter=cv2.VideoWriter("The_Way_You_Want_to_Save_Your_Vid.avi",fourcc,fps,(512,288))
im_names=os.listdir(img_root)
for im_name in range(len(im_names)):
    frame=cv2.imread(img_root+'{:05d}.png'.format(im_name))
    print(im_name+' '+frame.size)
    videoWriter.write(frame)

videoWriter.release()

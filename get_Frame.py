import cv2
from pathlib import Path
import os
import warnings
warnings.filterwarnings('ignore')
os.environ['CUDA_VISIBLE_DEVICES'] = "3"

#image Path and video Path
save_dir = Path('./datasets/')
save_dir.mkdir(exist_ok=True)

img_dir = save_dir.joinpath('target_image')
img_dir.mkdir(exist_ok=True)

if len(os.listdir('./datasets/target_image/'))<100:
    cap = cv2.VideoCapture(str(save_dir.joinpath('mv_target.mp4')))
    #From which farme
    i = -16000
    while (cap.isOpened()):
        flag, frame = cap.read()
        if flag == False :
            break
        frame = cv2.resize(frame, (512,288))
        if i>=0 :
            cv2.imwrite(str(img_dir.joinpath('{:05}.png'.format(i))), frame)
            #To which farme
            if i>=0 :
                break
        if i%100 == 0:
            print('Has generated %d picetures'%i)
        i += 1
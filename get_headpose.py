import face_alignment
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from skimage import io
from tqdm import tqdm
from pathlib import Path
import os
import time
import cv2

# Run the 3D face alignment on a test image, without CUDA.
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cuda:3', flip_input=True)

img_dir=Path('./datasets/target_image/')
img_dir.mkdir(exist_ok=True)

label_dir=Path('./datasets/source_pose/')
label_dir.mkdir(exist_ok=True)

save_dir=Path('./datasets/target_B/')
save_dir.mkdir(exist_ok=True)
start =time.time()
Alter=[]
for idx in tqdm(range(len(os.listdir(str(img_dir))))):
    img_path = img_dir.joinpath('{:05}.png'.format(idx))
    label_path=label_dir.joinpath('{:05}.png'.format(idx))
    input = io.imread(str(img_path))
    input_l=io.imread(str(label_path))
    try:
        preds = fa.get_landmarks(input)[-1]
    except:
        preds = Alter[-1]

    Alter.append(preds)
    #TODO: Make this nice
    fig = plt.figure()
    # figsize = plt.figaspect(.5)
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(input_l)
    ax.plot(preds[0:17,0],preds[0:17,1],marker='o',markersize=0.5,linestyle='-',color='w',lw=0.3)
    ax.plot(preds[17:22,0],preds[17:22,1],marker='o',markersize=0.5,linestyle='-',color='w',lw=0.3)
    ax.plot(preds[22:27,0],preds[22:27,1],marker='o',markersize=0.5,linestyle='-',color='w',lw=0.3)
    ax.plot(preds[27:31,0],preds[27:31,1],marker='o',markersize=0.5,linestyle='-',color='w',lw=0.3)
    ax.plot(preds[31:36,0],preds[31:36,1],marker='o',markersize=0.5,linestyle='-',color='w',lw=0.3)
    ax.plot(preds[36:42,0],preds[36:42,1],marker='o',markersize=0.5,linestyle='-',color='w',lw=0.3)
    ax.plot(preds[42:48,0],preds[42:48,1],marker='o',markersize=0.5,linestyle='-',color='w',lw=0.3)
    ax.plot(preds[48:60,0],preds[48:60,1],marker='o',markersize=0.5,linestyle='-',color='w',lw=0.3)
    ax.plot(preds[60:68,0],preds[60:68,1],marker='o',markersize=0.5,linestyle='-',color='w',lw=0.3)
    ax.axis('off')

# ax = fig.add_subplot(1, 2, 2, projection='3d')
# surf = ax.scatter(preds[:,0]*1.2,preds[:,1],preds[:,2],c="cyan", alpha=1.0, edgecolor='b')
# ax.plot3D(preds[:17,0]*1.2,preds[:17,1], preds[:17,2], color='blue' )
# ax.plot3D(preds[17:22,0]*1.2,preds[17:22,1],preds[17:22,2], color='blue')
# ax.plot3D(preds[22:27,0]*1.2,preds[22:27,1],preds[22:27,2], color='blue')
# ax.plot3D(preds[27:31,0]*1.2,preds[27:31,1],preds[27:31,2], color='blue')
# ax.plot3D(preds[31:36,0]*1.2,preds[31:36,1],preds[31:36,2], color='blue')
# ax.plot3D(preds[36:42,0]*1.2,preds[36:42,1],preds[36:42,2], color='blue')
# ax.plot3D(preds[42:48,0]*1.2,preds[42:48,1],preds[42:48,2], color='blue')
# ax.plot3D(preds[48:,0]*1.2,preds[48:,1],preds[48:,2], color='blue' )
#
# ax.view_init(elev=70., azim=60.)
# ax.set_xlim(ax.get_xlim()[::-1])
    plt.savefig(str(save_dir.joinpath('{:05}.png'.format(idx))),bbox_inches='tight',dpi=fig.dpi,pad_inches=0.0)
    frame=cv2.imread(str(save_dir.joinpath('{:05}.png'.format(idx))))
    frame = cv2.resize(frame, (512, 288))
    cv2.imwrite(str(save_dir.joinpath('{:05}.png'.format(idx))), frame)


end=time.time()
print (str(len(os.listdir(str(img_dir))))+' images:'+end)

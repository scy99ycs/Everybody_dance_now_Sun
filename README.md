# Everybody_dance_now_Sun
This everybody dance now project is a reproduction bace on https://github.com/CUHKSZ-TQL/EverybodyDanceNow_reproduce_pytorch  and  https://github.com/Lotayou/everybody_dance_now_pytorch . Using openpose python api to get human pose.

Pose get process:

1.Using get_Frame.py to get the source and target video`s frame.

2.Then using pose_estimator to get basic pose.

3.Using name_change.py to change name as {:05d} format.

4.Using get_headpose.py to upgrade basic pose to train pose.

Pose for target video should be put in train_A. Real image for target video should be put in train_B.

Pose for source video should be put in test_A. Real image for target video should be put in test_B.

All data can put into datasets.

Train process:

Script have some train(temporary-smooth) option.

When train start. Checkpoints file will be creat to record train process and save model.


Test process:

Normalization from source pose to target pose is coding now.

Pre-train model can be download here. and this is the video.

Test option also in Script. Result will be save in datasets and creat video in result.

Notice:

Source and target video should have the same fps(50,60,120fps) and with a clean bright background,single person, Fixed lens

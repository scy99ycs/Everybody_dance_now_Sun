# Everybody_dance_now_Sun
This everybody dance now project is a reproduction bace on https://github.com/CUHKSZ-TQL/EverybodyDanceNow_reproduce_pytorch  and  https://github.com/Lotayou/everybody_dance_now_pytorch . Using openpose python api to get human pose.

Using get_Frame.py to get the source and target video`s frame.

Then using pose_estimator to get basic pose.

Using name_change.py to change name as {:05d} format.

Using get_headpose.py to upgrade basic pose to train pose.

Pose for target video should be put in train_A. Real image for target video should be put in train_B.

Pose for source video should be put in test_A. Real image for target video should be put in test_B.

All data can put into datasets.

Script have some train(temporary-smooth) and test option.

When train start. Checkpoints file will be creat to record train process and save model.

Normalization from source pose to target pose is coding now.

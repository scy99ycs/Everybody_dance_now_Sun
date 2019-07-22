# Everybody_dance_now_Sun
This everybody dance now project is a reproduction bace on https://github.com/CUHKSZ-TQL/EverybodyDanceNow_reproduce_pytorch  and  https://github.com/Lotayou/everybody_dance_now_pytorch . Using openpose python api to get human pose.

Pose get process (Prepare):

1.Using get_Frame.py to get the source and target video`s frame (512*288).

2.Then using pose_estimator (./pose_estimator/examples/tutorial_api_python/02_whole_body_from_ image.py) to get basic pose(can select body head and hands)(“./script/get_Pose.sh” has pose get option).

3.Using name_change.py (pip install face_alignment) to change name as {:05d} format.

4.Using get_headpose.py to upgrade basic pose to train pose.

Pose for target video should be put in train_A. Real image for target video should be put in train_B.

Pose for source video should be put in test_A. Real image for target video should be put in test_B.

All data should put into “./datasets”.

Train process:

1.Train.py “./script/train.sh” have some train(temporary-smooth) option.

2.When train start. Checkpoints(./checkpoints) will be create to record train process and save model.

3.(the last trained model is save in “./checkpoints/everybody_dance_now/” , and processed image saved in “./checkpoints/everybody_dance_now/web/”)

Test process:

1.Normalization from source pose to target pose is coding now.

2.Test_video.py. Test option also in “./script/test.sh”. Result will be saved in datasets (./datasets/test_sync/) and create video in result.

3.Using create_video.py or make_gif.py to create result video and gif. Saved in to”./results”

Notice:

Source and target video should have the same fps (50,60,120fps) and with a clean bright background, single person, Fixed lens


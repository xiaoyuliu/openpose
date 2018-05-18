import os

data_folder = '/home/xiaoyu/Documents/action/datasets/ntu/test_videos'
test_videos = os.listdir(data_folder)
from_folder = 'output/ntu-json/'
for test_video in test_videos:
	video_folder = os.path.join(from_folder, test_video.split('.')[0])
	os.system('mv '+video_folder+' output/ntu-json/test_videos/')

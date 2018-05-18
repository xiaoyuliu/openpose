import os, sys

data_folder = '/home/xiaoyu/Documents/action/datasets/benchmark_bruce'
videos = os.listdir(data_folder)
output_folder = 'output/benchmark_bruce/'
if not os.path.exists(output_folder):
	os.mkdir(output_folder)
for i, video in enumerate(videos):
	print('--------------{}/{}------------'.format(i+1, len(videos)))
	video_name = video.split('.')[0]
	video_path = os.path.join(data_folder, video)
	output_path = output_folder + video_name + '.avi'
	command = './build/examples/openpose/openpose.bin --display 0 --scale_number 3 --video '+video_path+' --write_video '+output_path
	print(command)
	os.system(command)
	#output_path = 'output/rendering/' + video_name
	#if not os.path.exists(output_path):
	#	os.mkdir(output_path)
	#command = './build/examples/openpose/openpose.bin --display 0 --video '+video_path+' --write_json '+output_path
	#print(command)
	#os.system(command)

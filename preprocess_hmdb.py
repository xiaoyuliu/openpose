import os
import pdb

video_folder = '/home/xiaoyu/Documents/action/datasets/hmdb51/fall_floor'
video_names = os.listdir(video_folder)
frames_folder = video_folder + '-frame'
if not os.path.exists(video_folder + '-frame'):
    os.mkdir(frames_folder)

def main():
    for video_name in video_names:
        print(video_name)
        video_path = os.path.join(video_folder, video_name)
        video_frame_folder = os.path.join(frames_folder, video_name.split('.')[0])
        if not os.path.exists(video_frame_folder):
            os.mkdir(video_frame_folder)

        # os.system('ffmpeg -i ' + video_path +
        #           ' -r 30 ' +
        #           os.path.join(video_frame_folder, '%04d.jpg'))
        os.system('mkdir output/'+video_name.split('.')[0])
        os.system('./build/examples/openpose/openpose.bin --image_dir ' + video_frame_folder +
                  ' --write_json ' + 'output/' + video_name.split('.')[0] +
                  ' --display 0'
                  )

if __name__ == '__main__':
    main()
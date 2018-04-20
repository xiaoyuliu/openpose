import os

video_folder = '/home/xiaoyu/Documents/action/datasets/hmdb51/fall_floor'
video_names = os.listdir(video_folder)

def main():
    for video_name in video_names:
        video_path = os.path.join(video_folder, video_name)

        os.system('mkdir output/'+video_name.split('.')[0])
        os.system('./build/examples/openpose/openpose.bin --video ' + video_path +
                  ' --write_json ' + 'output/' + video_name.split('.')[0] +
                  ' --display 0'
                  )

if __name__ == '__main__':
    main()
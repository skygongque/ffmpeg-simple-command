import json
import os

def read_json():
    with open('list=PLcetZ6gSk96-FECmH9l7Vlx5VDigvgZpt - 副本.json','r',encoding='utf-8') as f:
        return f.readlines()

def get_video_name(videoId):
    video_path = 'video'
    for file in os.listdir(video_path):
        if videoId in file:
            return file,video_path
    raise Exception('could"t get video_name')

def get_subtilte_name(videoId):        
    subtitle_path = 'subtitle_ass'
    for file in os.listdir(subtitle_path):
        if videoId in file:
            # print(file)
            return file,subtitle_path
    raise Exception('could"t get subtitle_name')

def concat_order(josn_list):
    output_path = 'output_path'
    count = 0
    for item in josn_list:
        count +=1
        if count < 2:
            continue
        item_dict = json.loads(item)
        videoId = item_dict['videoId']
        file_video,video_path = get_video_name(videoId)
        file_subtitle,subtitle_path = get_subtilte_name(videoId)
        file_video_name = str(125 - int(item_dict['index'])).zfill(3)+' '+file_video[4:]
        input_video = os.path.join(video_path,file_video)
        input_subtitle = os.path.join(subtitle_path,file_subtitle)
        output_video = os.path.join(output_path,file_video_name)
        order = 'ffmpeg -i "{}" -filter_complex "subtitles={}:force_style=\'PrimaryColour=&H000000,BackColour=&Hffffff,OutlineColour=&Hffffff,BorderStyle=4,Outline=1,Shadow=0,Bold=0,MarginV=30\'" "{}"'.format(input_video,file_subtitle,output_video)
        # print(count,order)
        # os.system(order)
        # order = 'ffmpeg -loop 1 -i image.jpg -i "{}" -c:a copy -c:v libx264 -shortest "{}"'.format(input_video,output_video)
        # order = 'ffmpeg -i "{}" -vn -acodec copy "{}"'.format(input_video,output_video[:-4]+'.ac3')
        print(order)
        os.system(order)
        # break

        

        


def mian():
    josn_list = read_json()
    concat_order(josn_list)
    

if __name__ == "__main__":
    mian()
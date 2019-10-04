#调用ffmpeg用一张图片和一段音频生成视频
#注意已经从官网下载ffmpeg并配置在环境变量中
import os

#ffmpeg -loop 1 -i image.jpg -i 164.mp3 -c:a copy -c:v libx264 -shortest out.mp4
imagepath ='image'
audiopath ='audio'
video_resultpath ='video_result'

for i in range(1,6):
    num = str(i).zfill(4)
    image = os.path.join(imagepath,num+'.jpg')
    mp3name =  os.path.join(audiopath,num+'.mp3')
    mp4name = os.path.join(video_resultpath,num+'.mp4')
    order = f'ffmpeg -loop 1 -i {image} -i {mp3name} -c:a copy -c:v libx264 -shortest {mp4name}'
    print(f'正在合成{num+".mp4"} 完成后保存在{video_resultpath}')
    os.system(order)
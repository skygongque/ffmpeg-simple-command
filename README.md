# get_englishpod_video

## 使用前准备
1.确保已经安装了python的运行环境并安装了使用的第三方库（pip3安装）

2.安装ffmpeg并配置到环境变量，官网http://ffmpeg.org/

## 使用方法：
1.运行mian.py(会在image目录生成相应的图片)

2.运行image_and_audio2video.py（对应的图片和音频生成视频存于video_result）

## 核心思路
1.提取pdf中文本为字符串

2.根据相应的字符串生成不同的图片

3.用对应的图片和音频生成视频

4.安装ffmpeg并配置到环境变量可在终端运行以下最核心代码
（一张名为image.jpg的图片和一段名为audio.mp3音频合成名为video.mp4的视频）
在终端运行目录需要image.jpg，audio.mp3即可合成video.mp4
核心代码：
'''

ffmpeg -loop 1 -i image.jpg -i audio.mp3 -c:a copy -c:v libx264 -shortest video.mp4
'''
## 其他
1.从pdf中提取文字时使用正则表达式

2.缺陷在单词中间换行



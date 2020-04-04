# useful command


## 格式转换

m4a转mp3
------
`
ffmpeg -i input.m4a output.mp3
`

mkv转mp4
------
`
ffmpeg -i input.m4a output.mp3
`

注意：在不指定参数的情况下所有参数都会使用默认值


## 一张图和一段音频生成视频

`
ffmpeg -loop 1 -i image.jpg -i audio.mp3 -c:a copy -c:v libx264 -shortest video.mp4
`

## 压制硬字幕

`
ffmpeg -i input.mp4 -filter_complex OPTION output.mp4
`
##### OPTION传一个字符串

如"subtitles=subtitleName.ass:force_style='PrimaryColour=&H000000,BackColour=&Hffffff,OutlineColour=&Hffffff,BorderStyle=4,Outline=1,Shadow=0,Bold=0,MarginV=30'"

##### OPTION参数解释

|Name|explanation|example|
| :------------ |:------------|:------------|
| PrimaryColour|字体颜色|&H000000|
| BackColour|背景颜色|&Hffffff|
| OutlineColour|描边颜色|&Hffffff|
| BorderStyle|边框样式|4:不透明3:透明边框|
| BorderStyle|与底部距离|30|





## 例子

(get_englishpod_video)[https://github.com/skygongque/ffmpeg-simple-command/blob/master/get_englishpod_video_intruduction]
----




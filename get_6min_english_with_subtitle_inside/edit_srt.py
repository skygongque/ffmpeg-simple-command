import re
import os
'''
功能：需要srt字幕
使得每次出现2-5行字幕，并尽量句号结尾
'''

def get_original_str(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def parse(str):
    """ 1
    00:00:07,000 --> 00:00:08,420
    Georgina: Hello. This is 6 Minute English
    """
    items = re.findall(
        '\d+\n\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+\n.*?\n\n', str, re.S)
    temp_list = []
    for item in items:
        time = re.search(
            '\d+\n(\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+)\n', item, re.S).group(1)
        content = re.search(
            '\d+\n\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+\n+(.*?)\n\n', item, re.S).group(1)
        # print(time)
        # print(content)
        if len(content) > 0:
            temp_list.append({
                'time': time,
                'content': content
            })
    return temp_list


def edit_list(temp_list):
    num = 0
    result_list = []
    count = 0
    line_count = 0
    for i in range(len(temp_list)):
        if (line_count >= 1 and temp_list[i]['content'][-1] in '.!?') or line_count >= 4:
            line_count = 0
            result = ''
            for concat in range(num, i+1):
                result += '\n' + temp_list[concat]['content']
            # print(num, i)
            # print(result[1:])
            count += 1
            result_list.append({
                'count': count,
                'time': temp_list[num]['time'].split(' --> ')[0] + ' --> ' + temp_list[concat]['time'].split(' --> ')[1],
                'content': result[1:]
            })
            num = i + 1
        else:
            line_count += 1
    return result_list


def save_new_str(result_list, name):
    result = ''
    for each in result_list:
        content = '{}\n{}\n{}\n\n'.format(
            each['count'], each['time'], each['content'])
        result += content
    # print(result)
    with open(name, 'a', encoding='utf-8') as f:
        f.write(result)
    print('finished')


def main(name, dir, save_dir):
    file_path = os.path.join(dir, name)
    original_str = get_original_str(file_path)
    temp_list = parse(original_str)
    result_list = edit_list(temp_list)
    save_path = os.path.join(save_dir, name)
    print(save_path)
    save_new_str(result_list, save_path)

def srt2ass(path,save_dir):
    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        save_path = os.path.join(save_dir,file)[:-3]+'ass'
        order = 'ffmpeg -i "{}" "{}"'.format(file_path,save_path)
        os.system(order)
        # ffmpeg -i rWHGKGS7zSc_modified.srt rWHGKGS7zSc_modified.ass

if __name__ == "__main__":
    dir = 'subtitle'
    save_dir = 'subtitle2'
    for file in os.listdir(dir):
        print(file)
        main(file, dir, save_dir)
    
    # srt转ass
    # path = 'subtitle2'
    # srt2ass(path,'subtitle_ass')

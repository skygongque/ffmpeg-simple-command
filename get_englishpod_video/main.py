from pdf2txt import *
from text2image import*
import re

pdfpath = r'pdf'
imagepath =r'image'
audiopath =r'audio'

def get_text_from_pdf():
    for pdfile in os.listdir(pdfpath):
        file_path = os.path.join(pdfpath,pdfile)
        pdf2TxtManager = CPdf2TxtManager()
        result = pdf2TxtManager.changePdfToText(file_path)
        #提取返回的字符串中我们需要的部分，并在人名代号前换行处理
        #其中Key Vocabulary字符前刚好是我们需要的对话内容
        remove_str = 'Visit.*?Praxis Language Ltd.'
        result = re.sub(remove_str,'',result,re.S)
        match = re.search('(.*?)Key Vocabulary',result,re.S)
        if match:
            result = match.group(1)
        result = re.sub('A:','\nA:',result,re.S)
        result = re.sub('B:','\nB:',result,re.S)
        result = re.sub('C:','\nC:',result,re.S)
        result = re.sub('D:','\nD:',result,re.S)
        result = re.sub('E:','\nE:',result,re.S)
        yield result


if __name__ == "__main__":
    texts = get_text_from_pdf()
    count = 0
    #用处理后的字符串生成各自的图片
    print('准备生成图片。。。')
    for text in texts:
        count+=1
        num = str(count).zfill(4)
        #print(text)
        image_name = os.path.join(imagepath,num)
        n = ImgText(text,image_name)
        n.draw_text()
    print('生成图片完成，已存入image目录')
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import re
import numpy as np
# scores,classes,category_index,image_np=bb.detectt()
from PIL import Image
def quote(topic):
    req = Request("https://www.brainyquote.com/topics/"+topic, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage)
    x=[]
    for link in soup.findAll('a', attrs={'title':'view quote' }):
        x.append(link)
    cleantext=[]
    for i in x:
        cleantext.append(BeautifulSoup(str(i), "html.parser").text)
    return cleantext


def object_detect_lables(scores,classes,category_index,image_np):
    final_score = np.squeeze(scores)
    count = 0
    for i in range(100):
        if scores is None or final_score[i] > 0.5:
                count = count + 1
    print('count',count)
    printcount =0
    for i in classes[0]:
          printcount = printcount +1
          x=category_index[i]['name']

          if(printcount == count):
                break
    im=Image.fromarray(image_np)
    im.save('F:/New folder/models-master/models-master/research/object_detection/static/out.bmp')
    im.show()
    return x


# xx=quote(object_detect_lables())
#
# for i in xx:
#     print(i)
#
# im=Image.fromarray(image_np)
# im.show()
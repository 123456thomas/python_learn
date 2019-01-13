import re,os
import requests
with open("D:\Python_sup\kingworld.txt","r",encoding="utf-8") as f_r:
    Reader=f_r.read()

    #记录标题
    # dpan_title="<title>(.*?)</title>"
    # dpan_rel=re.search(dpan_title,Reader,re.I)
    # with open("D:\Python_sup\kingworld_title.txt","w",encoding="utf-8") as f_w1:
    #     f_w1.write(dpan_rel.group(1))

    #记录图片地址,并加载图片,
    dpan_imgsrc = 'src="(http.*?[(.jpg)(.png)])"'
    dpan_mgs = re.findall(dpan_imgsrc, Reader, re.I)
    with open("D:\Python_sup\kingworld_imgsrc.txt", "w", encoding="utf-8") as f_w2:
        count = 0
        for imgsr in dpan_mgs:
            f_w2.write(imgsr+"\n")
            #加载图片
            enda=imgsr.rpartition(".")[-1]  #获取图片格式
            with open(r"D:\Python_sup\kingworld_img\%s.%s"%(str(count),enda),"bw") as f_w4:
                result2 = requests.get(imgsr)
                f_w4.write(result2.content)
                count += 1



#记录链接地址,
    # dpan_aherf = '<a.*?href="(http.*?)".*?>'
    # dpan_ah = re.findall(dpan_aherf, Reader, re.I)
    # with open("D:\Python_sup\kingworld_href.txt", "w", encoding="utf-8") as f_w3:
    #     for ah in dpan_ah:
    #         f_w3.write(ah+"\n")





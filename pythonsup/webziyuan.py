import requests,re
r=requests.get("https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9984237158435998563%22%7D&n_type=0&p_from=1")
r.encoding="utf-8"
content=r.text
print(r.text)#打印出文档
spanl_title="<title>(.*?)</title>"
spanl_img='src="(.*?)"'
spanl_href='<a.*href="(.*?)"'

# with open(r"D:\Python_sup\webziyuan\title.txt","w",encoding="utf-8") as f_w:
#     result1=re.search(spanl_title,r.text,re.I)  #写入文本
#     f_w.write(result1.group(1))
#
#
with open(r"D:\Python_sup\webziyuan\imgsrc.txt","w",encoding="utf-8") as f_scr:
    result_scr = re.findall(spanl_img,r.text, re.I)  #写入文本
    count = 0
    for img in result_scr:
        f_scr.write(img + "\n")
        with open(r"D:\Python_sup\webziyuan\imgs\%s.png" % (count), "bw") as f_im:
            im_temp = requests.get(img)
            f_im.write(im_temp.content)  #获取图片内容
            count++1



# with open(r"D:\Python_sup\webziyuan\href.txt","w",encoding="utf-8") as f_href:
#     result_href = re.findall(spanl_href,r.text, re.I)  #写入文本
#     for i in result_href:
#         f_href.write(i+"\n")



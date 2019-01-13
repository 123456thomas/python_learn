# 使用requests请求库请求页面源码
# 将结果中img下载存储到本地磁盘
# 将结果中的href超级链接在此请求获取源码 如果源码中有图片 继续存储到磁盘
import requests,re



chiji=requests.get("http://pg.qq.com/main.shtml")
# 得到一个requests.models.Response类,chiji为<Response [200]>

chiji.encoding="uft8"
# 确定请求的编码方式"utf8"

read_con=chiji.text
# 获取源码


# 匹配模型
# 匹配超链接
span_href='<a.*?href="(.*?\.com.*?)".*?>'
result_href=re.findall(span_href,read_con,re.I)
with open("D:\Python_sup\chiji\chiji_href.txt","w",encoding="utf8") as f_w1:
    for i in result_href:
        header = i[:3]
        if header != "htt":
            i="https:"+i
        f_w1.write(i+"\n")


        # 获取下级连接
        chijic = requests.get(i)
        chijic.encoding = "uft8"
        read_conc = chijic.text
        span_imgc = '<img.*?src="([(htt)(/)].*?[(png)(jpg)(shp.qpic.cn)].*?)"'
        result_imgc = re.findall(span_imgc, read_conc, re.I)

        # 写入文件和图片
        with open("D:\Python_sup\chiji\imgs_next.txt","w",encoding="utf8") as f_w21:
            count1=0
            for j in result_imgc:
                header1 = j[:3]
                if header1 != "htt":
                    j="https:"+j
                f_w21.write(j+"\n")
                enda1=j.rpartition(".")[-1][:3]
                if enda1=="png":
                    Enda1="png"
                else:
                    Enda1 = "jpg"
                print(j)
                with open("D:\Python_sup\chiji\imgsc\im%s.%s"%(str(count1),Enda1), "bw") as f_w31:
                    try:
                        resultd = requests.get(j)
                    except Exception as e:
                        print(e)
                        print(resultd,type(resultd))
                    f_w31.write(resultd.content)
                    count1+=1




# 匹配图片地址
span_img='<img.*?src="([(htt)(/)].*?[(png)(jpg)(shp.qpic.cn)].*?)"'
result_img=re.findall(span_img,read_con,re.I)

# with open("D:\Python_sup\chiji\imgs_src.txt","w",encoding="utf8") as f_w2:
#     count=0
#     for i in result_img:
#         header = i[:3]
#         if header != "htt":
#             i="https:"+i
#         # print(i)
#         f_w2.write(i+"\n")
#         enda=i.rpartition(".")[-1][:3]
#         if enda=="png":
#             Enda="png"
#         else:
#             Enda = "jpg"
#             # print(i)
#         with open("D:\Python_sup\chiji\imgs\im%s.%s"%(str(count),Enda), "bw") as f_w3:
#             try:
#                 result2 = requests.get(i)
#             except Exception as e:
#                 print(e)
#                 result2 = requests.get(i)
#             f_w3.write(result2.content)
#             count+=1





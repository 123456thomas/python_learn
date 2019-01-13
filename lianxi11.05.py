import os,json,sys
# Acticel={"Admin":{"sdoijfi":["123","6768sd7889",{"Adminn":["123","6768sd7889"]}]},
#          "Admivn":{"sdoiji":["12j3","6ii768sd7889",{"Admjin":["12nn3","67yy68sd7889"]}]}}

pathtest="Textss"
if not os.path.exists(pathtest):
    os.mkdir(pathtest)
pathx=os.path.join(pathtest,"tx.json")
# with open(pathx,"w",encoding="utf-8") as f_w:
#     json.dump(Acticel,f_w)
with open(pathx,"r",encoding="utf-8") as f_r:
    read=json.load(f_r)

read["Admin"]["Hello"]=["Hellow world,Monika geht nach Hause","768sd7889",{}]

with open(pathx,"w",encoding="utf-8") as f_w:
    json.dump(read,f_w)
import json
from flask import Flask, render_template, request, jsonify
import time
from jishu import entrance
import os

app = Flask(__name__)


@app.route('/111',methods=['POST','GET'])
def test_json():
    #获取JSON数据
    
    img=request.form['img']
    
    img1="templates/counter/public"+img[0:28]
    for filename in os.listdir(r"%s"%img1):              #listdir的参数是文件夹的路径
    	img1=img1+filename
    print(img1)
    
    ktz=request.form['studentnumber']
    name=request.form['studentname']
    pjn=request.form['projectname']
    new_dict = {}
    new_dict['ID'] = img1
    new_dict['TIME'] = time.time()
    new_dict['NAME']=name
    new_dict['RGROUP']=ktz
    new_dict['RNAME']=pjn
    new_dict['PCOUNT']=1
    new_dict['ISFINISHED']=0
    new_dict['B_CNT']=0
    new_dict['G_CNT']=0
    f=open("myjson/receive.json","w")
    json.dump(new_dict,f)
    f.close()
    entrance.ent()
    f1=open("myjson/return.json",'r')
    load_dict=json.load(f1)
    G_num=load_dict['B_CNT']
    B_num=load_dict['G_CNT']
    print(G_num)
    print(B_num)
    a=jsonify({'greenball':G_num})

    print(a)
    print(type(a))
    #返回这里不知道是只返回一个串还是分开
    return str("来自课题组\n"+ktz+"\n的学生\n"+name+"\n在项目\n"+pjn+"\n中的计数结果为：\n"+"绿点数量为:"+str(G_num)+"个,"+"蓝点数量为："+str(B_num)+"个。")

app.run(
      host='0.0.0.0',
      port= 2300,
      debug=True
)

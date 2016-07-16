#_*_coding:utf-8_*_
import time,sys,urllib,urllib2,json
from flask import Flask
#print os.getcwd()     #打印工作的目录
#pprint.pprint(sys.path)
#print (platform.architecture())

app = Flask(__name__)

@app.route("/")
def hello():
	data = {}
	data['name'] = "Robin"
	data['time_now'] = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
	#wealth
	url = 'http://apis.baidu.com/apistore/weatherservice/cityid?cityid=101120201'
	req = urllib2.Request(url)
	req.add_header("apikey", "1de9b3bcea0804d4977589ee9ebf3ce3")
	resp = urllib2.urlopen(req)
	content = resp.read()
	if(content):
		cc = (content.decode("unicode_escape")).encode("utf-8")
    		wealth = eval(cc)
		data['wealth'] = wealth['retData']
	return render_template('template1.html',data=data,wealth=data['wealth'])
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=80)

#_*_coding:utf-8_*_
import time,sys,urllib,urllib2,json
from flask import Flask,render_template
#print os.getcwd()     #打印工作的目录
#pprint.pprint(sys.path)
#print (platform.architecture())
reload(sys)
sys.setdefaultencoding('utf-8')

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
		cc = eval(content)
		city = ((cc['retData']['city']).decode("unicode_escape")).encode("utf-8")
		wt = ((cc['retData']['weather']).decode("unicode_escape")).encode("utf-8")
	return render_template('template1.html',data=data,city=city,wt=wt)
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=80)

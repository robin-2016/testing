#_*_coding:utf-8_*_
import time
from flask import Flask
#print os.getcwd()     #打印工作的目录
#pprint.pprint(sys.path)
#print (platform.architecture())

app = Flask(__name__)

@app.route("/")
def hello():
	data = {}
	data['name'] = "Hello robin !"
	data['time_now'] = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
	return (data['name'] + data['time_now'])
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=80)

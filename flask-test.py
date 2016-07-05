#_*_coding:utf-8_*_
import os,sys,pprint,platform,time
print os.getcwd()
print ("hello world!")
pprint.pprint(sys.path)
print (platform.architecture())
print time.strftime('%Y-%m-%d %X',time.localtime(time.time()))

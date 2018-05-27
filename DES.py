# -*- coding:utf-8 -*-
#Des算法一般密钥长度为8位（可以是8的倍数），且加密与解密算法相同。（私有密钥，对称加密方式）
from pyDes import *
import threading
import Queue
import os
import sys
import time
from multiprocessing import Process,Pool,Manager
import multiprocessing
class maskdes:
    '''
    DES加密算法
    des(key,[mode],[IV],[pad],[padmode])
    @key:密钥(8位长度)
    @mode：模式，支持CBC与ECB
    @IV：
    @pad：
    @padmode：
    @data：明文
    @data_en：密文
    '''
    def __init__(self):
        pass
    def maskencrypt(self,data,key):
        '''
        明文加密
        @data:明文
        @key:密钥
        '''
        k = des(key,CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode=PAD_PKCS5) #des对象
        data_en = k.encrypt(data)       #进行des加密，返回密文
        
        # print u"密文: %r" % data_en
        return data_en
    def maskdecrypt(self,data,key):
        '''
        密文解密
        @data:密文
        @key:密钥
        '''
        k = des(key,CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode=PAD_PKCS5) #des对象
        data_de = k.decrypt(data)   #进行des解密，返回明文
        # print u"明文: %r" % data_de
        return data_de
def des_run(key,cur,data_en):
    '''
    破解des密码函数
    '''
    #print key
    
    data_de=cur.maskdecrypt(data_en,str(key))
    if data_de=="Hello World":
        print data_de
        return True
    else:
        return False
        
        
if __name__=="__main__":
    '''
    已知一个明文，以及密钥，求密文？
    '''
    key="10036934"
    data = "Hello World" #明文
    cur=maskdes()
    data_en=cur.maskencrypt(data,key)
    print u"密文: %r" % data_en
    with open("result.txt","w") as w:
        w.write(data_en)
    '''
    已知一个密文文件，已知长度为8位的密钥(纯数字)，求明文？
    解密时，直接将文本中的内容读取复制给一个变量，进行解密即可
    '''
    #-------------------------多进程---------------------------
    cur=maskdes()
    data_en=open("result.txt","r").read()  ##从文件中读取密文
    
    start=time.time()
    result=Queue.Queue()
    pool = Pool()
    def pool_th():
        for key in xrange(10000000,11111111): ##密钥范围
            try:
                result.put(pool.apply_async(des_run,args=(key,cur,data_en)))   #维持执行的进程总数为10，当一个进程执行完后添加新进程.
            except:
                break
    def result_th():
        while 1:
            a=result.get().get()
            if a:
                pool.terminate()
                break
    t1=threading.Thread(target=pool_th)
    t2=threading.Thread(target=result_th)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print "add Process end"
    pool.join()
    end=time.time()
    print 'time is ',end-start
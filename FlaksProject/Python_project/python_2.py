import gevent
def fun1():
    for i in range(5):
        print("print I am fun1 this is %s"%i)
        gevent.sleep(0)    #设置切换点

def fun2():
    for i in range(5):
        print("print I am fun2 this is %s"%i)
        gevent.sleep(0)     #设置切换点

t1=gevent.spawn(fun1)  #将函数进行协程封装
t2=gevent.spawn(fun2)  #将函数进行协程封装
gevent.joinall([t1,t2])  #集体运行功能





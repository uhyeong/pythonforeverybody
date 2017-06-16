
# coding: utf-8

# In[ ]:

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
import matplotlib.pyplot as plt
import myutil, math, mpld3
class MainHandler(RequestHandler):
    def initialize(self):
        self.count = 0
        self.error=0
    def draw(self,f):
        t= range(-300,300)
        x = [t/100 for t in t]
        y = [f(x) for x in x]
        fig = plt.figure(1)
        plt.plot(x,y)
        html = mpld3.fig_to_html(fig)
        self.render('index.html',mesg=html)
    def get(self):
        x=[0]
        y=[0]
        fig = plt.figure(1)
        plt.plot(x,y)
        html = mpld3.fig_to_html(fig)
        self.render('index.html',mesg=html)
    def post(self):
        ldict = locals()
        y1 = self.get_body_argument('y1')
        y2 = self.get_body_argument('y2')
        y3 = self.get_body_argument('y3')
        y4 = self.get_body_argument('y4')
        y5 = self.get_body_argument('y5')
        y6 = self.get_body_argument('y6')
        y7 = self.get_body_argument('y7')
        y8 = self.get_body_argument('y8')
        y9 = self.get_body_argument('y9')
        lst =[y1,y2,y3,y4,y5,y6,y7,y8,y9]
        for i in lst:
            exec(i,globals(),ldict)
        try:
            y_1 = ldict['y1']
        except Exception as e:
            y_1 ='error'
        try:
            y_2 = ldict['y2']
        except Exception as e:
            y_2 ='error'
        try:
            y_3 = ldict['y3']
        except Exception as e:
            y_3 ='error'
        try:
            y_4 = ldict['y4']
        except Exception as e:
            y_4 ='error'
        try:
            y_5 = ldict['y5']
        except Exception as e:
            y_5 ='error'
        try:
            y_6 = ldict['y6']
        except Exception as e:
            y_6 ='error'
        try:
            y_7 = ldict['y7']
        except Exception as e:
            y_7 ='error'
        try:
            y_8 = ldict['y8']
        except Exception as e:
            y_8 ='error'
        try:
            y_9 = ldict['y9']
        except Exception as e:
            y_9 ='error'
        lst2 = [y_1,y_2,y_3,y_4,y_5,y_6,y_7,y_8,y_9]

        for func in lst2:
            if func !='error':
                t = range(-300,300)
                x= [t/100 for t in t]
                y= [func(x) for x in x]
                plt.plot(x,y)
        fig = plt.figure(1)
        html =mpld3.fig_to_html(fig)
        self.render('index.html',mesg=html)
class Myexcepttion(Exception):
    def __init__(self,mesg):
        self.mesg =mesg
def make_app():
    return Application([(r"/", MainHandler)])
if __name__ == "__main__":
    fs = myutil.FastStop()
    fs.enable()
    app = make_app()
    app.listen(8080)
    IOLoop.current().start()


from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
import matplotlib.pyplot as plt
import myutil, math, mpld3
class MainHandler(RequestHandler):
    def initialize(self):
        self.count = 0
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
        if self.count<=9:
            self.count=self.count+1
            ldict = locals()
            fn = self.get_body_argument('fn')
            exec(fn,globals(),ldict)
            y1 = ldict['y1']
            t = range(-300,300)
            x= [t/100 for t in t]
            y= [y1(x) for x in x]
            fig = plt.figure(1)
            plt.plot(x,y)
            html =mpld3.fig_to_html(fig)
            self.render('index.html',mesg=html)

def Myexception(Exception):
    raise()
def make_app():
    return Application([(r"/", MainHandler)])
if __name__ == "__main__":
    fs = myutil.FastStop()
    fs.enable()
    app = make_app()
    app.listen(8080)
    IOLoop.current().start()


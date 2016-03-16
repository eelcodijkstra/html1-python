import web

urls = (
    '/','Index',
    '/form1','Form1',
    '/form2', 'Form2'
)

app = web.application(urls,globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.index()

class Form1:
    def GET(self):
        input = web.input()
        return render.form1(method="GET", x=input.x, y=input.y)

    def POST(self):
        input = web.input()
        return render.form1(method="POST", x=input.x, y=input.y)

class Form2:
    def GET(self):
        return render.form2(method="GET", input=web.input())

    def POST(self):
        inputx = web.input()
        print(inputx.keys())
        return render.form2(method="POST", input=inputx)

if __name__=='__main__':
    app.run()

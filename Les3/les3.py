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
        return("GET " + str(web.input()))

    def POST(self):
        return("POST " + str(web.input()))

class Form2:
    def GET(self):
        return("GET " + str(web.input()))

    def POST(self):
        return("POST " + str(web.input()))

if __name__=='__main__':
    app.run()

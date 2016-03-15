import web

urls = (
    '/','Index',
    '/form1','Form1',
    '/form2', 'Form2'
)

app = web.application(urls,globals())

pageHtml = """
<!doctype html>
<html>
  <head> <title>Forms test</title>
  </head>
  <body>
    <form action="/form1" method="GET">
      x: <input type="text" name="x" value="..."> <br>
      y: <input type="number" name="y" value="123"> <br>
      <button type="submit">Submit</button>
    </form>
    <hr>
    <form action="/form2" method="POST">
      a: <input type="text" name="a" value="..."> <br>
      b: <input type="number" name="b" value="123"> <br>
      <button type="submit">Send</button>
    </form>
  </body>
</html>
"""

class Index:
    def GET(self):
        return pageHtml

class Form1:
    def GET(self):
        return("GET " + str(web.input))

    def POST(self):
        return("POST " + str(web.input))

class Form2:
    def GET(self):
        return("GET " + str(web.input))

    def POST(self):
        return("POST " + str(web.input))

if __name__=='__main__':
    app.run()

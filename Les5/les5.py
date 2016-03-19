import web
import pymongo

urls = (
    '/','Index',
    '/form1','Form1',
    '/form2', 'Form2',
    '/todos', 'TodoList',
    '/todos/(\d+)', 'TodoElement'
)

app = web.application(urls,globals())

render = web.template.render('templates/')

client = pymongo.MongoClient()
db = client["tododb"]

class Index:
    def GET(self):
        user = web.cookies(username="anonymous")
        return render.index(username=user)

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

class TodoElement:
    def GET(self, id):
        return "GET TodoElement " + str(id)

    def POST(self, id):
        data = web.input()
        todoElt = {"description": data.descr,
                   "done": data.done}
        return "POST TodoElement " + str(id)

class TodoList:
    def GET(self):
        todos = db.todos.find()
        return render.todos(todolist=todos)

    def POST(self):
        data = web.input()
        db.todos.insert_one(
          {"description": data.descr,
           "done": data.done}
        )
        todos = db.todos.find()
        return render.todos(todolist=todos)

if __name__=='__main__':
    app.run()

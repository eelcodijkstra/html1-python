import web
import pymongo
from bson.objectid import ObjectId

urls = (
    '/', 'Index',
    '/todos', 'TodoList',
    '/todos/([0-9a-f]+)', 'TodoElement',
    '/cleanup', 'Cleanup'
)

app = web.application(urls,globals())

render = web.template.render('templates/')

client = pymongo.MongoClient()
db = client["tododb"]

class Index:
    def GET(self):
        cookies = web.cookies(username="anonymous")
        return render.index(username=cookies.username)

class TodoElement:
    def GET(self, id):
        return "GET TodoElement " + str(id)

    def POST(self, id):
        data = web.input()
        db.todos.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"description": data.descr,
                           "done": "done" in data.keys()}}
            )
        raise web.seeother("/todos")

class TodoList:
    def GET(self):
        todos = db.todos.find()
        return render.todos(todolist=todos)

    def POST(self):
        data = web.input()
        db.todos.insert_one(
            {"description": data.descr,
             "done": "done" in data.keys()}
        )
        raise web.seeother("/todos")

class Cleanup:
    def GET(self):
        cnt = db.todos.delete_many({"done": True})
        raise web.seeother("/todos")

if __name__=='__main__':
    app.run()

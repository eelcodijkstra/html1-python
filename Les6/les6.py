import web
import pymongo
from bson.objectid import ObjectId

urls = (
    '/','Index',
    '/users','Users',
    '/users/([0-9a-f]+)/todos/([0-9a-f]+)', 'UserTodoElement',
    '/users/([0-9a-f]+)/todos', 'UserTodoList'
)

app = web.application(urls,globals())

render = web.template.render('templates/')

client = pymongo.MongoClient()
db = client["tododb"]

class Index:
    def GET(self):
        cookies = web.cookies(username="")
        username = cookies.username
        if username == "":
            return render.index(username = "", userid = 0)
        else:
            user = db.users.find_one({"username": username})
            return render.index(username=user["username"], userid=user["_id"])

class Users:
    def GET(self):
        data = web.input()
        if data.username == "":
            return render.index(username="", userid=0)
        else:
            web.setcookie("username", data.username)
            user = db.users.find_one({"username": data.username})
            if user == None:
                userid = db.users.insert_one({"username": data.username})
            else:
                userid = user["_id"]
            raise web.seeother("/users/" + str(userid) + "/todos")

    def POST(self):
        raise web.seeother("/")

class UserTodoElement:
    def GET(self, userid, eltid):
        return "GET TodoElement " + "user=" + userid + "elt=" + eltid

    def POST(self, userid, eltid):
        data = web.input()
        db.todos.update_one(
            {"_id": ObjectId(eltid)},
            {"$set": {"description": data.descr,
                      "done": "done" in data.keys(),
                      "userid": userid}}
        )
        raise web.seeother("/users/" + userid + "/todos")

class UserTodoList:
    def GET(self, userid):
        todos = db.todos.find({"userid": userid})
        return render.usertodos(userid=userid, todolist=todos)

    def POST(self, userid):
        data = web.input()
        db.todos.insert_one(
            {"description": data.descr,
             "done": "done" in data.keys(),
             "userid": userid}
        )
        raise web.seeother("/users/" + userid + "/todos")

if __name__=='__main__':
    app.run()

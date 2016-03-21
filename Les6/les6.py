import web
import pymongo
from bson.objectid import ObjectId

urls = (
    '/','Index',
    '/users','Users',
    '/todos', 'TodoList',
    '/todos/([0-9a-f]+)', 'TodoElement',
    '/users/([0-9a-f]+)/todos/([0-9a-f]+)', 'UserTodoElement',
    '/users/([0-9a-f]+)/todos', 'UserTodoList'
)

app = web.application(urls,globals())

render = web.template.render('templates/')

client = pymongo.MongoClient()
db = client["tododb"]

def getUser():
    cookies = web.cookies(username="")
    username = cookies.username
    if username != "":
        # add new user to db, if necessary:
        user = db.users.find_one({"username": username})
        if user == None:
            db.users.insert_one({"username": username})
        return db.users.find_one({"username": username})
    else:
        return None

class Index:
    def GET(self):
        user = getUser()
        if user == None:
            user = {"username": "anonymous", "_id": "0"}
        return render.index(username=user["username"], userid=user["_id"] )

class Users:
    def GET(self):
        input = web.input()
        if input.username != "":
            web.setcookie("username", input.username)
            user = db.users.find_one({"username": input.username})
            if user == None:
                db.users.insert_one({"username": input.username})
            user = db.users.find_one({"username": input.username})
            userid = str(user["_id"])
            print("user:" + userid)
            raise web.seeother("/users/" + userid + "/todos")
        return render.index(username="", userid=0)

    def POST(self):
        raise web.seeother("/")

class TodoElement:
    def GET(self, id):
        return "GET TodoElement " + str(id)

    def POST(self, id):
        user = getUser()
        if user == None:
            # no user set/logged in, goto home/login page
            raise web.seeother("/")
        # now user is a valid document
        userid = user['_id']
        data = web.input()
        if not ("done" in data.keys()):
            data["done"] = False
        db.todos.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"description": data.descr,
                           "done": data.done,
                           "userid": userid}}
            )
        print("redirect to: " + "/users/" + userid + "/todos")
        raise web.seeother("/users/" + userid + "/todos")

class UserTodoElement:
    def GET(self, userid, eltid):
        return "GET TodoElement " + "user=" + str(userid) +"elt=" +str(id)

    def POST(self, userid, eltid):
        data = web.input()
        if not ("done" in data.keys()):
            data["done"] = False
        db.todos.update_one(
                {"_id": ObjectId(eltid)},
                {"$set": {"description": data.descr,
                           "done": data.done,
                           "userid": userid}}
            )
        print("redirect to: " + "/users/" + userid + "/todos")
        raise web.seeother("/users/" + userid + "/todos")

class UserTodoList:
    def GET(self, userid):
        todos = db.todos.find({"userid": userid})
        print(str(todos))
        return render.usertodos(userid=userid, todolist=todos)

    def POST(self, userid):
        data = web.input()
        if not ("done" in data.keys()):
            data["done"] = False
        db.todos.insert_one(
          {"description": data.descr,
           "done": data.done,
           "userid": userid}
        )
        raise web.seeother("/users/" + userid + "/todos")

class TodoList:
    def GET(self):
        user = getUser()
        if user == None: # no user set/logged in, goto home/login page
            raise web.seeother("/")
        # user is a valid document
        todos = db.todos.find({"userid": user['_id']})
        print(str(todos))
        return render.todos(username=user['username'], todolist=todos)

    def POST(self):
        user = getUser()
        if user == None: # no user set/logged in, goto home/login page
            raise web.seeother("/")
        # user is a valid document
        userid = user["_id"]
        data = web.input()
        if not ("done" in data.keys()):
            data["done"] = False
        db.todos.insert_one(
          {"description": data.descr,
           "done": data.done,
           "userid": userid}
        )
        raise web.seeother("/todos")

if __name__=='__main__':
    app.run()

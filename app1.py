from flask import Flask, jsonify, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET KEY"] = "saurabhgod"
socketio = SocketIO(app)

users = [
    {"id": 2, "name": "saurabh", "age": 20},
    {"id": 1, "name": "bobu", "age": 21},
    {"id": 3, "name": "shobu", "age": 22},
]


@app.route("/")
def index():
    return app.send_static_file("index.html")


@socketio.on("msg")
def handle_msg(data):
    print(data)
    socketio.emit("push", data, broadcast=True, include_self=False)


@app.route(
    "/users"
)  # @app is function decorator- request at the ("") end point, return the underlying fucntion
def getUsers():
    return jsonify(
        users
    )  # jsonify converts into list into json so that it could work on webpage.


@app.route("/users/<id>")
def getUser(id):
    result = [
        u
        for u in users
        if str(u["id"]) == id
        # list(filter(lamba u : str(u['id'])==id, users)))
    ]  # anything packet of info we revieve from http is in str format so convert in for ur use.
    return jsonify(result)


if __name__ == "__main__":
    socketio.run(app)

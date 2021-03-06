"""
astra web framework
author: Gurleen Singh<gs585@drexel.edu>
"""
from routes import blueprint

from astra.wsgi import Astra
from astra.response import Response
from astra.request import Request
from astra.blueprints import Blueprint

app = Astra()

@app.route("/")
def hello(request):
    print(request.extra)
    return Response("Hello, world!")


@app.route("/test")
def test(request):
    return Response("This is a test")


@app.route("/user/:name")
def testwitharg(request):
    name = request.params.get("name", "name")
    message = {"message": f"Hello, {name}!"}
    return Response(message)

@app.route("/post", methods=["POST"])
def post_example(request):
    return Response("You sent a post request!")

app.register_blueprint(blueprint)

def add_value(request) -> Request:
    request.extra["abc"] = "123"
    return request

app.register_middleware(add_value)

if __name__ == "__main__":
    app.run(8000)
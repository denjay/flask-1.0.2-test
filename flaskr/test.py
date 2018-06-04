from flask import Blueprint, render_template


ts = Blueprint("test", __name__, url_prefix="/test")


@ts.route("/hh")
def hh():
    print(render_template("test.html"))
    return render_template("test.html")


@ts.before_request
def haha():
    print("测试", "<<<<<<<<<<")

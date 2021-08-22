from flask import Flask,flash,get_flashed_messages


app = Flask(__name__)


app.secret_key="asdasdsad2asdasdasdsad?Asdasd"


@app.before_request
def test1():
    print("before_request 1")
    flash("this is flash",category="test")

@app.before_request
def test2():
    print("before_request 2")
    flash("this is flash",category="test")

@app.route('/2')
def hello_world2():
    # print(get_flashed_messages(category_filter=["test"]))
    flash("this is flash", category="test")
    return 'Hello World!'

@app.route('/')
def hello_world():
    print(get_flashed_messages(category_filter=["test"]))
    return 'Hello World!'


@app.after_request
def after1(response):
    print("after_request 1")
    flash("this is flash", category="test")
    return response

@app.after_request
def after2(response):
    print("after_request 2")
    flash("this is flash", category="test")
    return response

if __name__ == '__main__':
    app.__call__
    app.run()
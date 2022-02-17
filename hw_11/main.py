from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    name = "Ivan"
    number = "+7 123 456 78 90"
    return render_template('hello.html', name=name, phone=number)


app.run()

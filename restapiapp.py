from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepg():
    return "Welcome"


@app.route("/add/<int:num1>/<int:num2>")
def addpg(num1, num2):
    return f"{num1} + {num2} ={num1 + num2}"


@app.route("/sub/<int:num1>/<int:num2>")
def subpg(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    return f"{num1} - {num2} ={num1 - num2}"


@app.route("/mul/<int:num1>/<int:num2>")
def mulpg(num1, num2):
    return f"{num1} x {num2} ={num1 * num2}"


if __name__ == "__main__":
    app.run(debug=True)


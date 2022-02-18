from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/test")
def test():
    return


if __name__ == '__main__':
    app.run(debug=True)


#print(count * (animal + ' say moooo\n'))
#"\U0001F418"
#"\U0001F404"

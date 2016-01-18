from flask import Flask
app = Flask(__name__)

ocean = [[False for x in range(10)] for x in range(10)]

@app.route("/")
def hello():
    return "The ocean: %s" % ocean

if __name__ == "__main__":
    #print ocean[0][0]
    app.run()

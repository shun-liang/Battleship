from flask import Flask, request
app = Flask(__name__)

ocean = [[False for x in range(10)] for x in range(10)]
ships = None

class Ship:
    def __init__(self, size):
        self.size = size
        self.placed = False

    def can_place(self, x, y, orientation):
        return True

    def place(self, x, y, orientation):
        pass

#carrier = Ship(5)

@app.route("/")
def index():
    return "The ocean: %s" % ocean

@app.route("/place", methods=['GET', 'POST'])
def place():
    index = int(request.args.get('index'))
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    orientation = request.args.get('orientation')
    print str(x) + " " + str(y) + " " + str(orientation)

    ship = ships[index]
    if ship.can_place(x, y, orientation):
        ship.place(x, y, orientation)
        return "Successfully placed ship at " + str(x)  + " " + str(y) + \
            " with" + orientation + " orientation." 
    else:
        return "Cannot place at this position with this orientation."

if __name__ == "__main__":
    carrier = Ship(5)
    battleship = Ship(4)
    crusier = Ship(3)
    destroyer1 = Ship(2)
    destroyer2 = Ship(2)
    submarine1 = Ship(1)
    submarine2 = Ship(1)

    ships  = [carrier, battleship, crusier, destroyer1, destroyer2, submarine1,
            submarine2]

    app.run(debug=True)

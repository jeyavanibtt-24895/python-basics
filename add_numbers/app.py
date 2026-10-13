from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/add")
def add_numbers():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify({"result": add(a, b)})

if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def index ():
    user = request.args.get("user")
    return user

@app.route('/json')
def get_json():
    return jsonify({ "nome": "breno", "sexo":"Sim"})

@app.route("/file/<string:name>")
def get_file(name):
    print(name)
    # return send_from_directory("purple.pdf")

    # Se for para aparecer no browser, ao invés de fazer o download coloca com False
    return send_file("MoneyGame.mp3",  as_attachment=True)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

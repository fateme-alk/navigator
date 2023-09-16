from flask import Flask


app = Flask(__name__)
@app.route('/navigator', methods=['GET'])
def route_handler():
    pass

if __name__ == '__main__':
    app.run()

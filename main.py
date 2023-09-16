from flask import Flask, after_this_request


app = Flask(__name__)
@app.route('/navigator', methods=['GET'])
def route_handler():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

if __name__ == '__main__':
    app.run()

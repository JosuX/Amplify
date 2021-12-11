from flask import Flask, request, render_template

flask_server = Flask(__name__)
global lat
global lng


def saveCoord(data):
    global lat
    global lng
    data = data.split(',')
    lat = float(data[0])
    lng = float(data[1])


@flask_server.route('/')
def index():
    return render_template('map.html')

@flask_server.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['coords']
    saveCoord(jsdata)
    return jsdata

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@flask_server.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    flask_server.run(debug=False, use_reloader=False)
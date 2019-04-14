import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template("index.html")

@socketio.on('message')
def handleMessage(msg):
	msg['Time'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	#print('Message: ' + str(msg))
	send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=5000)
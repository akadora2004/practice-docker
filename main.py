from flask import Flask
port = 5000
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Practice Docker'

app.run(debug=True, host='0.0.0.0', port=port)
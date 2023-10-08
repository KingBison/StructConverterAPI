from flask import Flask, render_template
from flask_cors import CORS
from handlers.convert import convert

app = Flask(__name__)
cors = CORS(app, origins=['*'])

@app.route('/')
def home():
    return render_template('index.html')

app.add_url_rule('/convert', 'convert', convert, methods=['POST'])

if __name__ == '__main__':
    app.run(port=8000, debug=True)
from flask import Flask
from flask.templating import render_template
app = Flask(__name__,static_url_path='')

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)
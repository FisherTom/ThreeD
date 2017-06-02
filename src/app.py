from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/three')
def three():
     return render_template('three.html')

if __name__ == "__main__":
    app.run()

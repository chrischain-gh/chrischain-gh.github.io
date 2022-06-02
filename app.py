from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/account_links.html')
def account_links():
    return render_template('account_links.html')

@app.route('/ig_links.html')
def ig_links():
    return render_template('ig_links.html')

@app.route('/photography.html')
def photography():
    return render_template('photography.html')

@app.route('/video.html')
def video():
    return render_template('video.html')

@app.route('/resume_aviation.html')
def resume_aviation():
    return render_template('resume_aviation.html')

@app.route('/python_code.html')
def python_code():
    return render_template('python_code.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html')

@app.route('/live', methods=['GET', 'POST'])
def live():
    if request.method == 'POST':
        code = request.form['code']
    else:
        code = "NONE"

    return render_template('live.html', code=code)

if __name__ == '__main__':
    app.run(debug=True)
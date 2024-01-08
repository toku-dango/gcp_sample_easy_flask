import os
from flask import Flask
from flask import render_template, request

app = Flask(__name__)
app.config.from_object('config.config')
#print(app.config['DEBUG']) #Config値の取得

@app.route("/")
def index():
    my_dict = {
        'insert_something': ['title1', 'title2', 'title3'],
    }
    return render_template('index.html', my_dict = my_dict)
# def hello_world():
#     """Example Hello World route."""
#     name = os.environ.get("NAME", "World")
#     return f"Hello {name}!"

@app.route("/test1")
def test1():
    name = "test1"
    return f"Hello {name}!"

# @app.route("/sampleform")
# def sample_form():
#     return render_template('sampleform.html')

@app.route('/sampleform', methods=['GET', 'POST'])
def sample_form():
    if request.method == 'GET':
        return render_template('sampleform.html')
    if request.method == 'POST':
        print('POSTデータ受け取ったので処理します。')
        req1 = request.form['data1']
        return f'POST受け取ったよ: {req1}'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
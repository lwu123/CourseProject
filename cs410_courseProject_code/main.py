import logcc
from flask import Flask, render_template, request


app = Flask(__name__, template_folder="template")


@app.route('/')
def my_form():
    return render_template('index2.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = logcc.space(text)
    return processed_text


if __name__ == '__main__':
    app.run(debug=True)

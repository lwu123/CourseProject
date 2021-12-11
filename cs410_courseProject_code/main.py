import spacy
from flask import Flask, render_template, request

sp = spacy.load('en_core_web_sm')

app = Flask(__name__, template_folder="template")

#NLP model
def space(tx):
    sen = sp(tx)
    for word in sen:
        vb = f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}'
    return vb


@app.route('/')
def my_form():
    return render_template('index2.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = space(text)
    return processed_text


if __name__ == '__main__':
    app.run(debug=True)

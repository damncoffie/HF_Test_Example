from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


# change
# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=str(search4letters(phrase, letters)))


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!!')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, redirect, url_for, flash
from flask import render_template
from searchForm import SearchForm


app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/search', methods=['GET', 'POST'])
def search():
    # TODO Validering af form skal laves
    # Kig på om der skal valideres på den overordnede form eller de specifikke værdier i hver variable

    form = SearchForm()
    flash(u'test')
    if form.validate_on_submit():
        return redirect(url_for('data'))
    # if request.method == 'POST' and form.validate():
    #     search = searchForm(searchForm.DataRequired)
        #user = User(form.username.data, form.email.data,
                   #form.password.data)

    #TODO Når der søges og noget går galt, skal inputs gemmes
    return render_template('search.html', form=form)


@app.route('/data')
def data():


    return render_template('data.html',
                           dataTitle='Dataoversigt')
if __name__ == '__main__':
    app.run(debug=True)


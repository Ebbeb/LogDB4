from flask import Flask, request, redirect, url_for, flash
from flask import render_template
from searchForm import SearchForm
from flask_wtf.csrf import CSRFProtect
import connect

app = Flask(__name__)
app.config.from_object('config')
csrf = CSRFProtect(app)
csrf.init_app(app)
with app.app_context():



    #TODO Hvad skal der stå i indexet - skal der være et index?
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html',
                               title='Home')


    @app.route('/search', methods=['GET', 'POST'])
    def search():
        # TODO Validering af form skal laves - kig på CSRF for dette
        # Kig på om der skal valideres på den overordnede form eller de specifikke værdier i hver variable

        searchform = SearchForm()
        #TODO Find ud af hvorfor validate_on_submit ikke fungerer
        #Der er ingen data på variablerne der bliver sendt tilbage til validate_on_submit
        #Der er data på variablerne når der bruges POST metode
        #Hvor valideres der så ikke? Bruges den forkerte metode til at validere?
        #inputs = SearchForm(request)
        # if searchform.validate_on_submit(): #Denne bruges til at validere med CSRF - skal implementeres
        if request.method == 'GET':
            return render_template('search.html', form=searchform)

        elif request.method == 'POST':
            if searchform.is_submitted():
                flash("Successful") #flash virker ikke - hvorfor?
                #     result = SearchForm(searchform.roadStart.data) #Der bliver sendt for mange objekter ned til __init__, Det betyder at searchform kun tager 2 objekter
                roadStart = searchform.roadStart.data
                roadStart = request.form['roadStart']
                roadEnd = request.form['roadEnd']
                return data(roadStart, roadEnd)
                # return redirect(url_for('data'), result2)
                #TODO Send dataene videre til def data så der kan laves SQL statements ud af det
                # return render_template('/data.html', roadStart=roadStart, roadEnd=roadEnd)
            else:
                #Returnér searchform med de samme værdier i
                return render_template('search.html', form=searchform)
        # if request.method == 'POST' and form.validate():
        #     search = searchForm(searchForm.DataRequired)
        #     user = User(form.username.data, form.email.data,
        #                form.password.data)



    """/submit kigger på valideringen af inputtet og sender det videre til data, hvis valideringen går godt"""
    @app.route('/submit', methods=['GET', 'POST'])
    def submit():
        # TODO Når der søges og noget går galt, skal inputs gemmes

        # if request.method == 'POST' and form.validate:
        #     result = request.form
        #
        #     return redirect(url_for('data'))

        # return redirect(url_for('search'))
        return 0

    #TODO Implementér SQL søgning og datavisning
    @app.route('/data')
    def data(roadstart, roadend):
        conn = connect.Connect()
        result = conn.searchdb()
        #TODO data.html skal omstruktureres og der skal laves en properties fil til den
        return render_template('data.html',
                               roadStart=roadstart,
                               roadEnd=roadend,
                               result="Antallet af StatusBrightness: " + str(result))
    if __name__ == '__main__':
        app.run(debug=True)


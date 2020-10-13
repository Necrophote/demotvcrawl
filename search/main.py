from app import app
from db_setup import init_db, db_session
from forms import MusicSearchForm
from flask import flash, render_template, request, redirect
from models import Product
from tables import Results
init_db()
@app.route('/', methods=['GET', 'POST'])
def index():
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)
@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search_string:
        qry = db_session.query(Product).filter(Product.name.contains(search_string))
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)
if __name__ == '__main__':
    app.run()
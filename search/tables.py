from flask_table import Table, Col

class Results(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    price_nkim = Col('NKim')
    price_tiki = Col('Tiki')
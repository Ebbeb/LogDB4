# import things
from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    log_id = Col('log_id')
    t_timestamp = Col('t_timestamp')
    s_system = Col('s_system')
    logical_id = Col('logical_id')

# Get some objects
class Item(object):
    def __init__(self, log_id, t_timestamp, s_system, logical_id):
        self.log_id = log_id
        self.t_timestamp = t_timestamp
        self.s_system = s_system
        self.logical_id = logical_id
items = [Item(object, 'Description1'),
         Item('Name2', 'Description2'),
         Item('Name3', 'Description3'),
         Item('Name4', 'Description4')]
# Or, equivalently, some dicts
items = [dict(name='Name1', description='Description1'),
         dict(name='Name2', description='Description2'),
         dict(name='Name3', description='Description3'),
         dict(name='Name4', description='Description4')]

# Or, more likely, load items from your database with something like
# items = ItemModel.query.all()

# Populate the table
table = ItemTable(items)

# Print the html
print(table.__html__())
# or just {{ table }} from within a Jinja template
import BDD

class Item():

    def init(self, connection):
        self.connection = connection

    def add(self, cursor, name, author_id):
        add_item_query = 'INSERT INTO items (name, author_id) VALUES (%s, %s)'
        item_data = (name, author_id)
        cursor.execute(add_item_query, item_data)

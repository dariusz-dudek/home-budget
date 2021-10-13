import sqlite3


class EntryRepository:
    def get_costs(self):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''select e.id, e.created_at, e.amount, c.name 
                   from entry e left join category c on c.id = e.category_id order by created_at''')
            return cursor.fetchall()

    def save(self, name, category_id, amount):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO entry (category_id, name, amount) VALUES (?, ?, ?)',
                (category_id, name, amount)
            )
            connection.commit()


class CategoryRepository:
    def get_by_name(self, name):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT id, name FROM category WHERE name=?', (name,))
            return cursor.fetchone()

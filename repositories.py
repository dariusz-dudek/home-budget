import sqlite3


class EntryRepository:
    def get_costs(self):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''SELECT e.id, e.name, e.created_at, e.amount, c.name 
                   FROM entry e LEFT JOIN category c ON c.id = e.category_id 
                   WHERE e.amount < 0 ORDER BY created_at''')
            return cursor.fetchall()

    def get_incomes(self):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''SELECT e.id, e.name, e.created_at, e.amount, c.name 
                   FROM entry e LEFT JOIN category c ON c.id = e.category_id 
                   WHERE e.amount > 0 ORDER BY created_at''')
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


class RaportRepository:
    def get_saldo(self):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT COUNT(*) as quantiry, SUM(amount) as saldo FROM entry')
            return cursor.fetchone()

    def get_by_category(self):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''SELECT c.name, COUNT(*) AS quantiry, SUM(amount) FROM entry e 
                LEFT JOIN category c ON c.id = e.category_id GROUP BY c.name''')
            return cursor.fetchall()

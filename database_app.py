from flask import Flask, request, jsonify
from werkzeug.exceptions import abort
import sqlite3

# helperfuncties
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_book(isbn):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE isbn = ?', (isbn,)).fetchone()
    conn.close
    if book is None:
        abort(404)
    return book

app = Flask(__name__)

#endpoints
@app.route('/')
def index():
    conn = get_db_connection()
    result = conn.execute('SELECT * FROM books')
    rows = result.fetchall()
    conn.close()
    books = []
    for row in rows:
        book = {"isbn": row['isbn'], "title": row['title'], "writer": row['writer']}
        books.append(book)

    return jsonify(books)


@app.route('/detail/<isbn>')
def detail(isbn):
    book = get_book(isbn)
    book_dict = dict(book)
    return jsonify(book_dict)



@app.route('/', methods=["POST"])
def add_book():
    new_book = request.get_json()
    isbn = new_book['ISBN']
    title = new_book['title']
    writer = new_book['writer']

    conn = get_db_connection()
    conn.execute("INSERT INTO users (ISBN, title, writer) values(?,?,?)", (isbn, title, writer))
    conn.commit()
    conn.close()

    response = {"message": f"{title} is added to the database"}
    return jsonify(response), 200



@app.route('/delete/<isbn>')
def delete(isbn):
    user = get_book(isbn)
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE isbn=?', (isbn))
    conn.commit()
    conn.close()
    return f"The user with isbn:{isbn} has been removed"




@app.route('/edit/<isbn>', methods=["GET", "PUT"])
def edit(isbn):
    book = get_book(isbn)
    book_changes = request.get_json()
    title = book_changes['title']
    writer = book_changes['writer']

    conn = get_db_connection()
    conn.execute('UPDATE books SET title =?, writer =? WHERE isbn =?', (title, writer, isbn))
    conn.commit()
    conn.close()

    book = get_book(isbn)
    book_dict = dict(book)
    return jsonify(book_dict) 
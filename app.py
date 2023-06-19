from flask import Flask

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def get_books():
    return 'this is the list of books'

@app.route('/api/books/books/<book_id>',methods=['GET'])
def get_book(book_id):
    return f'This is book {book_id}'

@app.route('/api/books', methods=['POST'])
def create_book():
    return 'New book created'

@app.route('/api/books/book_id', methods=['PUT'])
def update_book(book_id):
    return f'Book {book_id} updated'

@app.route('/api/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    return f'Book {book_id} deleted'

if __name__ == '__main__':
    app.run(debug=True)
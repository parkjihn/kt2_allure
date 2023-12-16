import json
import csv

def update_users(file_path):
    res = []
    with open(file_path) as users_file:
        templates = json.load(users_file)
    for temp in templates:
        newitem = [temp['name'], temp['gender'], temp['address'], temp['age']]
        res.append(newitem)
    return res

def update_books(file_path):
    books = []
    with open(file_path, 'r') as books_file:
        csvreader = csv.reader(books_file)
        for row in csvreader:
            newbook = {'title': row[0], 'author': row[1], 'pages': row[3], 'genre': row[2]}
            books.append(newbook)
    return books

def make_json(users, books, output_file):
    m_books, extra_books = len(books) // len(users), len(books) % len(users)
    to_json = []
    i_b = 0

    for user in users:
        new_user = {'name': user[0], 'gender': user[1], 'address': user[2], 'age': user[3], 'books': []}
        for i in range(i_b, i_b + m_books):
            new_user['books'].append(books[i])
        i_b += m_books
        if extra_books != 0:
            new_user['books'].append(books[i_b])
            extra_books -= 1
            i_b += 1
        to_json.append(new_user)

    with open(output_file, 'w') as output:
        json.dump(to_json, output, indent=2)

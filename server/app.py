#!/usr/bin/env python3

from flask import request, session, jsonify, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

import os
from config import create_app, db, api
from models import Book, BookSchema

env = os.getenv("FLASK_ENV", "dev")
app = create_app(env)


@app.route('/books')
def get_books():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    pagination = Book.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    books = [BookSchema().dump(book) for book in pagination.items]

    response = {
        "page": pagination.page,
        "per_page": pagination.per_page,
        "total": pagination.total,
        "total_pages": pagination.pages,
        "items": books
    }

    return response, 200


class Books(Resource):
    def get(self):
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 5, type=int)

        pagination = Book.query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        books = [BookSchema().dump(book) for book in pagination.items]

        response = {
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "total_pages": pagination.pages,
            "items": books
        }

        return response, 200


if __name__ == '__main__':
    print("=== REGISTERED ROUTES ===")
    for rule in app.url_map.iter_rules():
        print(f"  {rule.endpoint}: {rule.rule}")
    print("========================")
    
    app.run(port=5555, debug=True)
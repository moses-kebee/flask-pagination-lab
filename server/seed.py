#!/usr/bin/env python3

from app import app
from config import db
from models import Book
from faker import Faker
import random

fake = Faker()

def seed_books():
    with app.app_context():
        # Clear existing books
        Book.query.delete()
        print("Deleting all books...")
        
        # Create 500 books
        books = []
        for i in range(500):
            book = Book(
                title=fake.sentence(nb_words=3).rstrip('.'),
                author=fake.name(),
                description=fake.paragraph(nb_sentences=3)
            )
            books.append(book)
        
        db.session.add_all(books)
        db.session.commit()
        print(f"Created {Book.query.count()} books!")

if __name__ == '__main__':
    seed_books()
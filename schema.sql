-- schema.sql
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    
    'ISBN' TEXT NOT NULL,
    'title' INTEGER NOT NULL,
    'writer' TEXT NOT NULL
);
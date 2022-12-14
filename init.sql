CREATE TABLE auth (
	id SERIAL PRIMARY KEY,
	username TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS profiles (
	id INT,
	username TEXT NOT NULL UNIQUE,
	name TEXT,
	age INT
);

CREATE TABLE post (
	id SERIAL PRIMARY KEY,
	owner INT NOT NULL,
	title TEXT,
	text TEXT,
	created TIMESTAMP
);

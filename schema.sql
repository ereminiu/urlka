DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL
);

INSERT INTO users (NAME) VALUES ('katya'), ('valera'), ('tilzik');
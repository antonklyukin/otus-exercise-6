CREATE TABLE users (
    user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP 
);

INSERT INTO users (username, email, created_on) VALUES
('Anton KLyukin', 'antonklyukin@gmail.com', now()),
('Manya Batareykina', 'batareykina@mail.ru', now()),
('Иван Сусанин', 'susanin@yandex.ru', now());
-- PostgreSQL schema for a normalized Netflix analytics warehouse
CREATE TABLE IF NOT EXISTS contents (
    content_id VARCHAR(20) PRIMARY KEY,
    content_type VARCHAR(20) NOT NULL,
    title TEXT NOT NULL,
    date_added DATE,
    release_year INT,
    rating VARCHAR(30),
    duration_value INT,
    duration_unit VARCHAR(20),
    maturity_category VARCHAR(30),
    content_age INT
);

CREATE TABLE IF NOT EXISTS countries (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS content_countries (
    content_id VARCHAR(20) REFERENCES contents(content_id),
    country_id INT REFERENCES countries(country_id),
    PRIMARY KEY(content_id, country_id)
);

CREATE TABLE IF NOT EXISTS content_genres (
    content_id VARCHAR(20) REFERENCES contents(content_id),
    genre_id INT REFERENCES genres(genre_id),
    PRIMARY KEY(content_id, genre_id)
);

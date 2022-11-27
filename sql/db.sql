SET timezone = 'America/Santiago';

DROP DATABASE IF EXISTS reduce;
CREATE DATABASE reduce;
\c reduce;
CREATE TABLE registros (
    id SERIAL NOT NULL,
    palabra varchar NOT NULL,
    numero int NOT NULL,
    archivo int NOT NULL,
    PRIMARY KEY (id)
);
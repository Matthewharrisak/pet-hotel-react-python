CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name character varying(255) NOT NULL,
    breed character varying(255) NOT NULL,
    color character varying(255) NOT NULL,
    is_checked_in character varying(255) NOT NULL
);

CREATE TABLE owner (
    id SERIAL PRIMARY KEY,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    admin boolean,
    pet_id integer REFERENCES pets(id) ON DELETE SET DEFAULT ON UPDATE SET DEFAULT
);
-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(500) NOT NULL,
    "first_name" VARCHAR(30) NOT NULL,
    "last_name" VARCHAR(30) NOT NULL,
    "date_of_birth" DATE NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);

INSERT INTO "user" ("id", "email", "username", "password", "first_name", "last_name", "date_of_birth") VALUES (
    uuid_generate_v4(),
    'string@string.io',
    'string',
    '$2b$12$PaBJXQrK49btJx2T5wH9Be1UoVVMTl99Lmno32SzHszRIuhysmGE.',
    'Janusz',
    'Polski',
    '2000-01-01'::date
);
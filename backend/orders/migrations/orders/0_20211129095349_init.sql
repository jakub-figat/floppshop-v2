-- upgrade --
CREATE TABLE IF NOT EXISTS "category" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "email" VARCHAR(100) NOT NULL,
    "first_name" VARCHAR(30) NOT NULL,
    "last_name" VARCHAR(30) NOT NULL
);
CREATE TABLE IF NOT EXISTS "order" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "product" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "price" DECIMAL(6,2) NOT NULL,
    "count" INT NOT NULL,
    "order_id" UUID NOT NULL REFERENCES "order" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "product_category" (
    "product_id" UUID NOT NULL REFERENCES "product" ("id") ON DELETE CASCADE,
    "category_id" UUID NOT NULL REFERENCES "category" ("id") ON DELETE CASCADE
);

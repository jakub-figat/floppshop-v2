-- upgrade --
CREATE TABLE IF NOT EXISTS "category" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS "product" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "price" DECIMAL(6,2) NOT NULL
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

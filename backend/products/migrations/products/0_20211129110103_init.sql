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

INSERT INTO "category" ("id", "name") VALUES
    ('1b861ec7-b249-4104-8ae0-9819935a47cb', 'Plush toys'),
    ('ca82ca83-5b0d-4b70-bcec-225738b1a0b1', 'Tools');


INSERT INTO "product" ("id", "name", "price") VALUES
    ('32176e92-1074-49ab-9393-6e6645b948f1', 'Floppa plush toy', 40.99),
    ('2a1286d1-c62d-440e-9d7f-32f3061c3173', 'Tools', 100.99);

INSERT INTO "product_category" ("product_id", "category_id") VALUES
    ('32176e92-1074-49ab-9393-6e6645b948f1', '1b861ec7-b249-4104-8ae0-9819935a47cb'),
    ('32176e92-1074-49ab-9393-6e6645b948f1', 'ca82ca83-5b0d-4b70-bcec-225738b1a0b1'),
    ('2a1286d1-c62d-440e-9d7f-32f3061c3173', 'ca82ca83-5b0d-4b70-bcec-225738b1a0b1');
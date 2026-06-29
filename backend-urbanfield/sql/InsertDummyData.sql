USE urban_fields;

-- Insert dummy data for users
INSERT INTO users (username, password, user_document, role, email, phone_number) VALUES
    ('admin_user', 'scrypt:32768:8:1$w2OLutD9INjTziqK$76b9990a30efd81f589528faa17b5f38dae28339f8cbced36af1d6f7aae45ca80ceaf1cf144d87b5bfc348c2cc0005ca2376f8f21fc9217ec0d18828e556cb51', NULL, 'admin', 'admin1@example.com', '+1234567890'),
    ('admin_user2','scrypt:32768:8:1$gWJuM1V1MDfds1nS$8f9a4e2075baaa1a727d82ec2833b2a6539547d5e4c3fda980ac6926bca37d0c750ce59726c91e274f8e81acaa65d10f133983470f172ac9858abcb636ebd82a', NULL, 'admin', 'admin2@example.com', '+6282345653879'),
    ('admin_user3', 'scrypt:32768:8:1$w2OLutD9INjTziqK$76b9990a30efd81f589528faa17b5f38dae28339f8cbced36af1d6f7aae45ca80ceaf1cf144d87b5bfc348c2cc0005ca2376f8f21fc9217ec0d18828e556cb51', NULL, 'admin', 'admin3@example.com', '+6285551234567'),
    ('admin_user4', 'scrypt:32768:8:1$w2OLutD9INjTziqK$76b9990a30efd81f589528faa17b5f38dae28339f8cbced36af1d6f7aae45ca80ceaf1cf144d87b5bfc348c2cc0005ca2376f8f21fc9217ec0d18828e556cb51', NULL, 'admin', 'admin4@example.com', '+6235551234567'),
    ('alexsmith_admin', 'scrypt:32768:8:1$Yo1CMn4vm8ORpoRl$408e1b61df4b73354b96a4dadd685ed2e47a051515c61ab236826726ff6532cd2421bf342f8c5ee569c38023fda810d271c62c4f0b89cf9c039cd7578b85b0a0', NULL, 'admin', 'alexsmith@example.com', '+6285546667771'),
    ('janedoe_admin', 'scrypt:32768:8:1$UyQ1Uo8MCSQ1aE10$51eea833b96a6023498c641f420f59b4b65e7c611d82f2789b7df2e5c88b29cdf9c62b9d9f3ee1e417708213beedaa62e17f7b55811ec39790014f9fe38bc60a', NULL, 'admin', 'janedoe@example.com', '+6287774889990'),
    ('johndoe_admin', 'scrypt:32768:8:1$hTN9bhuyi2qunhs2$abc6d11c17a9f10c904d92f4ed16eb78206c438ffbc49859dd192d539fe3aaef128eb54adb57beda772972145f1e06d1b436305e892a0ccb065a56c13614cbe6', NULL, 'admin', 'johndoe@example.com', '+6289876543210'),
    ('customer1', 'scrypt:32768:8:1$ThhCoTJ2vsM6yjoS$c05c68438f380dcf745cda1276cdff0f26531e98f50eb6b974bb6f199f8daabab78981832bec343e97b5ee801222c9ee6ae23780b9c7ccd6f72b0abe47de4f1c', NULL, 'customer', 'customer1@example.com', '+1987654321'),
    ('customer2', 'scrypt:32768:8:1$n8Vlum4hrFqL7eL8$fdc6fbc3d76bb2e8af84cff5d69207373237d9292860613bbdf43825f569109ad914efb6ca5552686f25fe53dc80ec20b3e662993692395ca8d0eb8af160b637', NULL, 'customer', 'customer2@example.com', '+1765432987'),
    ('john_doe', 'scrypt:32768:8:1$XSrmaNLGhT2jWG3s$cbbc77a0f880e70bbe7e97a61e2e8784dc2fdb4060f464fa76a0404e7ea9956af042d815e5713f29929254ccbc1827a9da8fd3e80ab243285649b3a665bec3b5', NULL, 'customer', 'john.doe@example.com', '+1654321987'),
    ('jane_smith', 'scrypt:32768:8:1$fEEUaGtRH5uC4tla$454d2f4bbe889446e43a4f92c84d0d5da305f77c5eedc49d1f3b22b6f94ba9c24b3cc1f7c5214cc2e3110b26c1c3f69347ad0ab2503ca16f8ec82b9f544653b1', NULL, 'customer', 'jane.smith@example.com', '+1543219876'),
    ('alice_jones', 'scrypt:32768:8:1$vwF1KdIQHvhjPzWk$49ae6984e663d9b5ba26845daea7c705a8ff41fb598dbc92ca7c68dd090d2937fc3b355b5d12f3b40dd464fb6db07948ed00c595a70989aae7051fae72e7eeed', NULL, 'customer', 'alice.jones@example.com', '+1432198765'),
    ('bob_smith', 'scrypt:32768:8:1$YpeBkVCsvssmHpj0$144052cfa3101561fe8ff2edb2b8823cc52b7cdc59b011b066a0026465adedb028fd732380bb4c4db8be20f676f76faf3c8e4f78d32ed86a2271fd48c6d7e025', NULL, 'customer', 'bob.smith@example.com', '+1321987654'),
    ('charlie_brown', 'scrypt:32768:8:1$t18I9QSyPf1IWbGI$af0c5f73680989d410661fc0152e8cbf49144b362ea65fb96d1e44603dd673886d3ffb63558c4f7d6522fff57147ab1865e56c80a45f8c0c9270acf1063c60d2', NULL, 'customer', 'charlie.brown@example.com', '+1219876543'),
    ('david_cole', 'scrypt:32768:8:1$NRcMvXn7B9mODBv2$8e7483dcfc460131b10127784774911f2c49fe4750a45152fe6579f303c1e46d3a6443fcc1ec250b11236a37d9784add33f7d6615b9d8263b9fa3d42f8090776', NULL, 'customer', 'david.cole@example.com', '+1198765432'),
    ('emily_davis', 'scrypt:32768:8:1$dzFDQRrgkoCsyQXV$8bf7bac649814e2cde8e9d7e797a1b65f9ad45ff9713e072552b2dcaaad2d00a8587c2cc804837545213f8468c907c0df9b126ad39aff575765756a2b4299390', NULL, 'customer', 'emily.davis@example.com', '+1098765432'),
    ('frank_thomas', 'scrypt:32768:8:1$K9O2g9NSEJ7JULcv$ba5df0cebea6ae7dfaaf3471fe1bd227a3eb8adb18c4aaef56d17aeef3221a8f8f006097ac70cd1bb3df2753993c5cad66f352de631c7134a1fc14f2938a17ff', NULL, 'customer', 'frank.thomas@example.com', '+1987654320'),
    ('grace_miller', 'scrypt:32768:8:1$0b1UazqHQPUmLcgl$e8fb872c3b26b3a8fbbbfd03e0a14bce052d669bd0c0f5c9f27d874bb49aacd0a723af7e21c0d3c62297be15f12111f53751d92841dc78f55e0cf87345d38f10', NULL, 'customer', 'grace.miller@example.com', '+1876543210'),
    ('henry_wilson', 'scrypt:32768:8:1$gvS2uqvlUAr8qsc8$489640528dff128ac8a5f76e1670adbd2a114858a846069fa4aa1ea73e99a542ac49d4754828e4a01f33db2fc00c40807beede7fd0153a6fb5728133cfe573f4', NULL, 'customer', 'henry.wilson@example.com', '+1765432109'),
    ('isabella_scott', 'scrypt:32768:8:1$VioalJOHbfhItz9I$5df15d7a94e39bb9c8b6fca58b4e1f9314cd26ef66ee857acb631c5949468c7ce68aa1928dd0142b30ebee3872dc8c256429736cbe9f53694cc8a45067b4fd09', NULL, 'customer', 'isabella.scott@example.com', '+1654321098'),
    ('jacob_lee', 'scrypt:32768:8:1$Dmy6CGd7KyTkVaL5$fd89b8ace78ea330f77e8313e143748174dc33649e56662e0fa6b26335ca8d1cf4937a3ed84edbfee904d51ecc0011124bfcc26e557091d4a74ed1ce15fc3af6', NULL, 'customer', 'jacob.lee@example.com', '+1543210987'),
    ('kate_harris', 'scrypt:32768:8:1$zzzxSSNhcFhdgBbw$3c56137ff63d444ec055615594ab174ec15fe8e11158e60c8cd2c7748f1432e993456d417afff2cd36c4029d33b34fbf339b90f50090b00704d8a1c646eee8b8', NULL, 'customer', 'kate.harris@example.com', '+1432109876'),
    ('leo_robinson', 'scrypt:32768:8:1$9pvsBgmUWygPeyRY$2a1fbb6642c4b63df530846f701fd06403b8643f2580d8f9476b61e38da9adb30bf9e257e7c6b4459fb5e04f4817a4c210c4d4ca85a1d1cf6e3808145ab4fc6b', NULL, 'customer', 'leo.robinson@example.com', '+1321098765'),
    ('mia_nguyen', 'scrypt:32768:8:1$47CVqz0ZlsiODSzr$942d3f5fc7e18023567197cc1069c1b36ad8ad9d59add38fcb28ed64a589eb95b9dcb72bc529cd5a884af6ac8cb25ed5a040366cdba1d8856e8b37ef30c8958f', NULL, 'customer', 'mia.nguyen@example.com', '+1210987654'),
    ('nathan_king', 'scrypt:32768:8:1$joEZoSGzw3BsY8Y6$3a0074033fe9becbe13c2949187f00488a8d6cfe8fd66e2229c9166b5fa0b0e323bfe9b6cb05a0817bc4bc2517785538470c803a011f4428433d0c9d57758060', NULL, 'customer', 'nathan.king@example.com', '+1198765430'),
    ('olivia_clark', 'scrypt:32768:8:1$icjd7ADnTq3GspjA$03166b96f4bc013ddf5128434894be204db668509ec2fd3e18126921c03d68d13451e8290be0f35fb0d85f0e493eb0da76af91cf4f542a5a64e6a96ebda36c2e', NULL, 'customer', 'olivia.clark@example.com', '+1098765430');

-- Insert dummy data for field types
INSERT INTO field_types (name) VALUES
    ('Futsal'),
    ('Badminton'),
    ('Voli');

-- Insert dummy data for fields
INSERT INTO fields (name, type_id, city, address, street_address, image_url, image_url2, image_url3, price_per_hour, opening_time, closing_time) VALUES
    ('Gor Badminton Pelita', 2, 'Kota Makassar', 'Kecamatan Rappocini', 'Jl. Pelita Raya IV No.32, Balla Parang, Kec. Rappocini, Kota Makassar, Sulawesi Selatan 90222', '/img/field_image/gorbadmintonpelita1.png', '/img/field_image/gorbadmintonpelita2.png', '/img/field_image/gorbadmintonpelita3.png', 30000, '07:00:00', '19:00:00'),
    ('Laniang Badminton Hall', 2, 'Kota Makassar', 'Kecamatan Tamalanrea', 'Blok AA No. 9, BTP Jl. Laniang, Tamalanrea, Kec. Tamalanrea, Kota Makassar, Sulawesi Selatan 90245', '/img/field_image/laniangbadminton1.png', '/img/field_image/laniangbadminton2.png', '/img/field_image/laniangbadminton3.png', 55000, '09:00:00', '23:00:00'),
    ('Lapangan Bulutangkis Phinisi', 2, 'Kota Makassar', 'Kecamatan Rappocini', 'Jl. Phinisi No. 1, Balla Parang, Kec. Rappocini, Kota Makassar, Sulawesi Selatan 90222', '/img/field_image/badmintonphinisi1.png', '/img/field_image/badmintonphinisi2.png', '/img/field_image/badmintonphinisi3.png', 40000, '08:00:00', '20:00:00'),
    ('The Cage Makassar', 2, 'Kota Makassar', 'Kecamatan Panakkukang', 'Jl. Inspeksi Kanal No.69, Karuwisi, Kec. Panakkukang, Kota Makassar, Sulawesi Selatan 90231', '/img/field_image/thecagemakassar1.png', '/img/field_image/thecagemakassar2.png', '/img/field_image/thecagemakassar3.png', 30000, '10:00:00', '23:00:00'),
    ('Celebes dan gym', 1, 'Kota Makassar', 'Kecamatan Manggala', 'Jl. Tamangapa Raya 3 No.24, Bangkala, Kec. Manggala, Kota Makassar, Sulawesi Selatan 90235', '/img/field_image/futsalgymcelebes1.png', '/img/field_image/futsalgymcelebes2.png', '/img/field_image/futsalgymcelebes3.png', 55000, '07:00:00', '23:00:00'),
    ('Lapangan GOR MBC Borong', 2, 'Kota Makassar', 'Kecamatan Manggala', 'Jl. Borong Raya Baru, Batua, Kec. Manggala, Kota Makassar, Sulawesi Selatan 90233', '/img/field_image/mbcborong1.png', '/img/field_image/mbcborong2.png', '/img/field_image/mbcborong3.png', 60000, '07:00:00', '23:00:00'),
    ('Jo & K Badminton', 2, 'Kota Makassar', 'Kecamatan Tamalate', 'Jl. Daeng Tata 1 No.2, Parang Tambung, Kec. Tamalate, Kota Makassar, Sulawesi Selatan 90223', '/img/field_image/jokbadminton1.png', '/img/field_image/jokbadminton2.png', '/img/field_image/jokbadminton3.png', 65000, '08:00:00', '17:00:00'),
    ('The Futsal NTI Makassar', 1, 'Kota Makassar', 'Kecamatan Tamalanrea', 'Jl. Nusa Tamalanrea Indah, Kapasa, Tamalanrea, Kota Makassar, Sulawesi Selatan 90245, Makassar 90245', '/img/field_image/futsalntimakassar1.png', '/img/field_image/futsalntimakassar2.png', '/img/field_image/futsalntimakassar3.png', 50000, '08:00:00', '23:00:00'),
    ('Smash Badminton Court', 2, 'Kota Makassar', 'Kecamatan Makassar', 'Jl. S. Saddang II No.16, Maradekaya Sel., Kec. Makassar, Kota Makassar, Sulawesi Selatan 90143', '/img/field_image/smashbadmintoncourt1.png', '/img/field_image/smashbadmintoncourt2.png', '/img/field_image/smashbadmintoncourt3.png', 40000, '08:00:00', '19:00:00'),
    ('Futsal arena Telkom', 1, 'Kota Makassar', 'Kecamatan Rappocini', 'Jl. A. P. Pettarani No.2, Gn. Sari, Kec. Rappocini, Kota Makassar, Sulawesi Selatan 90221', '/img/field_image/futsalarenatelkom1.png', '/img/field_image/futsalarenatelkom2.png', '/img/field_image/futsalarenatelkom3.png', 54000, '08:00:00', '23:00:00'),
    ('Futsal Holic', 1, 'Kota Makassar', 'Kecamatan Rappocini', 'Jl. Monginsidi Baru Blok AB 12 No.7, Balla Parang, Kec. Rappocini, Kota Makassar, Sulawesi Selatan 90222', '/img/field_image/futsalholic1.png', '/img/field_image/futsalholic2.png', '/img/field_image/futsalholic3.png', 75000, '08:00:00', '23:00:00'),
    ('Lapangan Bola Voli Karebosi', 3, 'Kota Makassar', 'Kecamatan Ujung Pandang', 'Jln.kajaolalido no.1, Makassar, Sulawesi Selatan 90000', '/img/field_image/volikarebosi1.png', '/img/field_image/volikarebosi2.png', '/img/field_image/volikarebosi3.png', 75000, '08:00:00', '23:00:00');

-- Insert dummy data for facilities
INSERT INTO facilities (name, icon) VALUES
    ('Parkiran', 'car'),
    ('Musholla', 'musholla'),
    ('Ruang Ganti', 'hanger'),
    ('Kantin', 'cafe'),
    ('Toilet', 'toilet');

-- Insert dummy data for field facilities
INSERT INTO field_facility (field_id, facility_id) VALUES
    (1, 1), (1, 2), (1, 4), (1, 5),
    (2, 1), (2, 3), (2, 4), (2, 5),
    (3, 1), (3, 2), (3, 5),
    (4, 2), (4, 5),
    (5, 1), (5, 3),
    (6, 1), (6, 3),
    (7, 1), (7, 3),
    (8, 1), (8, 3),
    (9, 1), (9, 3),
    (10, 1), (10, 3),
    (11, 1), (11, 3),
    (12, 1), (12, 3);

-- Insert dummy data for field reviews
INSERT INTO field_review (field_id, user_id, rating, review) VALUES
    (1, 2, 8, 'Great place, clean and comfortable, highly recommended!'),
    (1, 3, 7, 'Nice place, but parking is limited'),
    (2, 2, 9, 'Spotless and cozy place, highly recommended!'),
    (2, 3, 10, 'Great place, but the changing room is small'),
    (3, 2, 9, 'Clean and comfortable space, highly recommended!'),
    (3, 3, 8, 'Lovely place, but the prayer room is small'),
    (4, 2, 7, 'Very clean and cozy, highly recommended!'),
    (4, 3, 6, 'Nice place, but the cafeteria is small'),
    (5, 2, 5, 'Clean and comfortable, highly recommended!'),
    (5, 3, 8, 'Great place, but the restroom is small'),
    (6, 2, 9, 'Immaculate and comfortable, highly recommended!'),
    (6, 3, 5, 'Nice place, but the parking space is limited'),
    (7, 2, 5, 'Clean and cozy, highly recommended!'),
    (7, 3, 4, 'Nice place, but the changing room is small'),
    (8, 2, 8, 'Spotlessly clean and cozy, highly recommended!'),
    (8, 3, 9, 'Great place, but the prayer room is small'),
    (9, 2, 10, 'Exceptionally clean and comfortable, highly recommended!'),
    (9, 3, 7, 'Lovely place, but the cafeteria is small'),
    (10, 2, 4, 'Clean and comfy, highly recommended!'),
    (10, 3, 8, 'Great place, but the restroom is small'),
    (11, 2, 8, 'Very clean and cozy, highly recommended!'),
    (11, 3, 9, 'Nice place, but the parking space is limited'),
    (12, 2, 7, 'Clean and comfortable, highly recommended!'),
    (12, 3, 7, 'Great place, but the changing room is small');

-- Insert dummy data for payment methods
INSERT INTO payment_methods (method, icon) VALUES
    ('BCA', '/img/payment/bca.png'),
    ('BNI', '/img/payment/bni.png'),
    ('BRI', '/img/payment/bri.png'),
    ('GoPay', '/img/payment/gopay.png'),
    ('OVO', '/img/payment/ovo.png'),
    ('ShopeePay', '/img/payment/shopeepay.png'),
    ('DANA', '/img/payment/dana.png'),
    ('Qris', '/img/payment/qris.png');

-- Insert dummy data for bookings
INSERT INTO bookings (user_id, field_id, date, time, payment_method_id) VALUES
    (1, 1, '2021-12-01', '09:00:00', 1),
    (2, 2, '2021-12-01', '10:00:00', 2),
    (3, 3, '2021-12-01', '11:00:00', 3),
    (4, 4, '2021-12-01', '12:00:00', 4),
    (5, 5, '2021-12-01', '13:00:00', 5),
    (6, 6, '2021-12-01', '14:00:00', 6),
    (7, 7, '2021-12-01', '15:00:00', 7),
    (8, 8, '2021-12-01', '16:00:00', 8),
    (9, 9, '2021-12-01', '17:00:00', 1),
    (10, 10, '2021-12-01', '18:00:00', 2),
    (11, 11, '2021-12-01', '19:00:00', 3),
    (12, 12, '2021-12-01', '20:00:00', 4);

-- Insert dummy data for payments
INSERT INTO payments (booking_id, amount, payment_date) VALUES
    (1, 30000.00, '2021-12-01 09:15:00'),
    (2, 55000.00, '2021-12-01 10:20:00'),
    (3, 40000.00, '2021-12-01 11:10:00'),
    (4, 30000.00, '2021-12-01 12:05:00'),
    (5, 55000.00, '2021-12-01 13:30:00'),
    (6, 60000.00, '2021-12-01 14:15:00');
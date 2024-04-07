

INSERT INTO "Boards" ("name") VALUES
('Board 1');


INSERT INTO "Ports" ("Boards.id") VALUES
(1),  -- 1
(1),  -- 2
(1),  -- 3
(1),  -- 4
(1),  -- 5
(1),  -- 6
(1),  -- 7
(1),  -- 8
(1);  -- 9


INSERT INTO "Roads" ("Boards.id") VALUES
(1),  -- 1
(1),  -- 2
(1),  -- 3
(1),  -- 4
(1),  -- 5
(1),  -- 6
(1),  -- 7
(1),  -- 8
(1),  -- 9
(1),  -- 10
(1),  -- 11
(1),  -- 12
(1),  -- 13
(1),  -- 14
(1),  -- 15
(1),  -- 16
(1),  -- 17
(1),  -- 18
(1),  -- 19
(1),  -- 20
(1),  -- 21
(1),  -- 22
(1),  -- 23
(1),  -- 24
(1),  -- 25
(1),  -- 26
(1),  -- 27
(1),  -- 28
(1),  -- 29
(1),  -- 30
(1),  -- 31
(1),  -- 32
(1),  -- 33
(1),  -- 34
(1),  -- 35
(1),  -- 36
(1),  -- 37
(1),  -- 38
(1),  -- 39
(1),  -- 40
(1),  -- 41
(1),  -- 42
(1),  -- 43
(1),  -- 44
(1),  -- 45
(1),  -- 46
(1),  -- 47
(1),  -- 48
(1),  -- 49
(1),  -- 50
(1),  -- 51
(1),  -- 52
(1),  -- 53
(1),  -- 54
(1),  -- 55
(1),  -- 56
(1),  -- 57
(1),  -- 58
(1),  -- 59
(1),  -- 60
(1),  -- 61
(1),  -- 62
(1),  -- 63
(1),  -- 64
(1),  -- 65
(1),  -- 66
(1),  -- 67
(1),  -- 68
(1),  -- 69
(1),  -- 70
(1),  -- 71
(1);  -- 72


INSERT INTO "Settlements" ("Boards.id") VALUES
(1),  -- 1
(1),  -- 2
(1),  -- 3
(1),  -- 4
(1),  -- 5
(1),  -- 6
(1),  -- 7
(1),  -- 8
(1),  -- 9
(1),  -- 10
(1),  -- 11
(1),  -- 12
(1),  -- 13
(1),  -- 14
(1),  -- 15
(1),  -- 16
(1),  -- 17
(1),  -- 18
(1),  -- 19
(1),  -- 20
(1),  -- 21
(1),  -- 22
(1),  -- 23
(1),  -- 24
(1),  -- 25
(1),  -- 26
(1),  -- 27
(1),  -- 28
(1),  -- 29
(1),  -- 30
(1),  -- 31
(1),  -- 32
(1),  -- 33
(1),  -- 34
(1),  -- 35
(1),  -- 36
(1),  -- 37
(1),  -- 38
(1),  -- 39
(1),  -- 40
(1),  -- 41
(1),  -- 42
(1),  -- 43
(1),  -- 44
(1),  -- 45
(1),  -- 46
(1),  -- 47
(1),  -- 48
(1),  -- 49
(1),  -- 50
(1),  -- 51
(1),  -- 52
(1),  -- 53
(1);  -- 54


INSERT INTO "Tiles" ("Boards.id", "coordinate") VALUES
(1, ARRAY[2,0]::INT[2]),  -- 1
(1, ARRAY[1,0]::INT[2]),  -- 2
(1, ARRAY[3,0]::INT[2]),  -- 3
(1, ARRAY[0,1]::INT[2]),  -- 4
(1, ARRAY[2,1]::INT[2]),  -- 5
(1, ARRAY[4,1]::INT[2]),  -- 6
(1, ARRAY[1,1]::INT[2]),  -- 7
(1, ARRAY[3,1]::INT[2]),  -- 8
(1, ARRAY[0,2]::INT[2]),  -- 9
(1, ARRAY[2,2]::INT[2]),  -- 10
(1, ARRAY[4,2]::INT[2]),  -- 11
(1, ARRAY[1,2]::INT[2]),  -- 12
(1, ARRAY[3,2]::INT[2]),  -- 13
(1, ARRAY[0,3]::INT[2]),  -- 14
(1, ARRAY[2,3]::INT[2]),  -- 15
(1, ARRAY[4,3]::INT[2]),  -- 16
(1, ARRAY[1,3]::INT[2]),  -- 17
(1, ARRAY[3,3]::INT[2]),  -- 18
(1, ARRAY[2,4]::INT[2]);  -- 19


INSERT INTO "PortsSettlements" (
	"Boards.id", "Side's Corners.id", "Corner's Sides.id", "Settlements.id", "Ports.id"
)
SELECT "Boards"."id", "Side's Corners"."id", "Corner's Sides"."id", T."Settlements.id", T."Ports.id"
FROM 
(
	VALUES
	('Board 1', 'BOTTOM_LEFT', 'TOP', 3, 1),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 4, 1),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 5, 2),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 6, 2),
	('Board 1', 'RIGHT', 'SIDE', 7, 3),
	('Board 1', 'LEFT', 'SIDE', 12, 4),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 13, 3),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 18, 4),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 25, 5),
	('Board 1', 'LEFT', 'BOTTOM', 30, 6),
	('Board 1', 'RIGHT', 'SIDE', 31, 5),
	('Board 1', 'BOTTOM_LEFT', 'SIDE', 36, 6),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 44, 7),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 47, 8),
	('Board 1', 'RIGHT', 'SIDE', 49, 7),
	('Board 1', 'LEFT', 'SIDE', 52, 8),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 53, 9),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 54, 9)
) AS T ("Boards.name", "Side's Corners.label", "Corner's Sides.label", "Settlements.id", "Ports.id")
JOIN "Boards" ON T."Boards.name" = "Boards"."name"
JOIN "Side's Corners" ON T."Side's Corners.label" = "Side's Corners"."label"
JOIN "Corner's Sides" ON T."Corner's Sides.label" = "Corner's Sides"."label";

INSERT INTO "RoadsSettlements" (
	"Boards.id", "Corner's Edges.id", "Edge's Corners.id", "Roads.id", "Settlements.id"
)
SELECT "Boards"."id", "Corner's Edges"."id", "Edge's Corners"."id", T."Roads.id", T."Settlements.id"
FROM 
(
	VALUES
	('Board 1', 'SIDE',    'LEFT',  1,  1),
	('Board 1', 'SIDE',    'RIGHT', 1,  2),
	('Board 1', 'TOP',     'RIGHT', 2,  1),
	('Board 1', 'BOTTOM',  'LEFT',  2,  4),
	('Board 1', 'TOP',     'LEFT',  3,  2),
	('Board 1', 'BOTTOM',  'RIGHT', 3,  5),
	('Board 1', 'SIDE',    'LEFT',  4,  3),
	('Board 1', 'SIDE',    'RIGHT', 4,  4),
	('Board 1', 'SIDE',    'LEFT',  5,  5),
	('Board 1', 'SIDE',    'RIGHT', 5,  6),
	('Board 1', 'TOP',     'RIGHT', 6,  3),
	('Board 1', 'BOTTOM',  'LEFT',  6,  8),
	('Board 1', 'TOP',     'LEFT',  7,  4),
	('Board 1', 'BOTTOM',  'RIGHT', 7,  9),
	('Board 1', 'BOTTOM',  'RIGHT', 8,  5),
	('Board 1', 'TOP',     'LEFT',  8, 10),
	('Board 1', 'BOTTOM',  'LEFT',  9,  6),
	('Board 1', 'TOP',     'RIGHT', 9, 11),
	('Board 1', 'SIDE',   'LEFT',  10,  7),
	('Board 1', 'SIDE',   'RIGHT', 10,  8),
	('Board 1', 'SIDE',   'LEFT',  11,  9),
	('Board 1', 'SIDE',   'RIGHT', 11, 10),
	('Board 1', 'SIDE',   'LEFT',  12, 11),
	('Board 1', 'SIDE',   'RIGHT', 12, 12),
	('Board 1', 'BOTTOM', 'RIGHT', 13,  7),
	('Board 1', 'TOP',    'LEFT',  13, 13),
	('Board 1', 'BOTTOM', 'LEFT',  14,  8),
	('Board 1', 'TOP',    'RIGHT', 14, 14),
	('Board 1', 'BOTTOM', 'RIGHT', 15,  9),
	('Board 1', 'TOP',    'LEFT',  15, 15),
	('Board 1', 'TOP',    'LEFT',  16, 10),
	('Board 1', 'BOTTOM', 'RIGHT', 16, 16),
	('Board 1', 'TOP',    'RIGHT', 17, 11),
	('Board 1', 'BOTTOM', 'LEFT',  17, 17),
	('Board 1', 'TOP',    'LEFT',  18, 12),
	('Board 1', 'BOTTOM', 'RIGHT', 18, 18),
	('Board 1', 'SIDE',   'LEFT',  19, 14),
	('Board 1', 'SIDE',   'RIGHT', 19, 15),
	('Board 1', 'SIDE',   'LEFT',  20, 16),
	('Board 1', 'SIDE',   'RIGHT', 20, 17),
	('Board 1', 'TOP',    'LEFT',  21, 13),
	('Board 1', 'BOTTOM', 'RIGHT', 21, 19),
	('Board 1', 'TOP',    'RIGHT', 22, 14),
	('Board 1', 'BOTTOM', 'LEFT',  22, 20),
	('Board 1', 'TOP',    'LEFT',  23, 15),
	('Board 1', 'BOTTOM', 'RIGHT', 23, 21),
	('Board 1', 'TOP',    'RIGHT', 24, 16),
	('Board 1', 'BOTTOM', 'LEFT',  24, 22),
	('Board 1', 'TOP',    'LEFT',  25, 17),
	('Board 1', 'BOTTOM', 'RIGHT', 25, 23),
	('Board 1', 'TOP',    'RIGHT', 26, 18),
	('Board 1', 'BOTTOM', 'LEFT',  26, 24),
	('Board 1', 'SIDE',   'LEFT',  27, 19),
	('Board 1', 'SIDE',   'RIGHT', 27, 20),
	('Board 1', 'SIDE',   'LEFT',  28, 21),
	('Board 1', 'SIDE',   'RIGHT', 28, 22),
	('Board 1', 'SIDE',   'LEFT',  29, 23),
	('Board 1', 'SIDE',   'RIGHT', 29, 24),
	('Board 1', 'TOP',    'RIGHT', 30, 19),
	('Board 1', 'BOTTOM', 'LEFT',  30, 25),
	('Board 1', 'TOP',    'LEFT',  31, 20),
	('Board 1', 'BOTTOM', 'RIGHT', 31, 26),
	('Board 1', 'TOP',    'RIGHT', 32, 21),
	('Board 1', 'BOTTOM', 'LEFT',  32, 27),
	('Board 1', 'TOP',    'LEFT',  33, 22),
	('Board 1', 'BOTTOM', 'RIGHT', 33, 28),
	('Board 1', 'TOP',    'RIGHT', 34, 23),
	('Board 1', 'BOTTOM', 'LEFT',  34, 29),
	('Board 1', 'TOP',    'LEFT',  35, 24),
	('Board 1', 'BOTTOM', 'RIGHT', 35, 30),
	('Board 1', 'SIDE',   'LEFT',  36, 26),
	('Board 1', 'SIDE',   'RIGHT', 36, 27),
	('Board 1', 'SIDE',   'LEFT',  37, 28),
	('Board 1', 'SIDE',   'RIGHT', 37, 29),
	('Board 1', 'TOP',    'LEFT',  38, 25),
	('Board 1', 'BOTTOM', 'RIGHT', 38, 31),
	('Board 1', 'TOP',    'RIGHT', 39, 26),
	('Board 1', 'BOTTOM', 'LEFT',  39, 32),
	('Board 1', 'TOP',    'LEFT',  40, 27),
	('Board 1', 'BOTTOM', 'RIGHT', 40, 33),
	('Board 1', 'TOP',    'RIGHT', 41, 28),
	('Board 1', 'BOTTOM', 'LEFT',  41, 34),
	('Board 1', 'TOP',    'LEFT',  42, 29),
	('Board 1', 'BOTTOM', 'RIGHT', 42, 35),
	('Board 1', 'TOP',    'RIGHT', 43, 30),
	('Board 1', 'BOTTOM', 'LEFT',  43, 36),
	('Board 1', 'SIDE',   'LEFT',  44, 31),
	('Board 1', 'SIDE',   'RIGHT', 44, 32),
	('Board 1', 'SIDE',   'LEFT',  45, 33),
	('Board 1', 'SIDE',   'RIGHT', 45, 34),
	('Board 1', 'SIDE',   'LEFT',  46, 35),
	('Board 1', 'SIDE',   'RIGHT', 46, 36),
	('Board 1', 'TOP',    'RIGHT', 47, 31),
	('Board 1', 'BOTTOM', 'LEFT',  47, 37),
	('Board 1', 'TOP',    'LEFT',  48, 32),
	('Board 1', 'BOTTOM', 'RIGHT', 48, 38),
	('Board 1', 'TOP',    'RIGHT', 49, 33),
	('Board 1', 'BOTTOM', 'LEFT',  49, 39),
	('Board 1', 'TOP',    'LEFT',  50, 34),
	('Board 1', 'BOTTOM', 'RIGHT', 50, 40),
	('Board 1', 'TOP',    'RIGHT', 51, 35),
	('Board 1', 'BOTTOM', 'LEFT',  51, 41),
	('Board 1', 'TOP',    'LEFT',  52, 36),
	('Board 1', 'BOTTOM', 'RIGHT', 52, 42),
	('Board 1', 'SIDE',   'LEFT',  53, 38),
	('Board 1', 'SIDE',   'RIGHT', 53, 39),
	('Board 1', 'SIDE',   'LEFT',  54, 40),
	('Board 1', 'SIDE',   'RIGHT', 54, 41),
	('Board 1', 'TOP',    'LEFT',  55, 37),
	('Board 1', 'BOTTOM', 'RIGHT', 55, 43),
	('Board 1', 'TOP',    'RIGHT', 56, 38),
	('Board 1', 'BOTTOM', 'LEFT',  56, 44),
	('Board 1', 'TOP',    'LEFT',  57, 39),
	('Board 1', 'BOTTOM', 'RIGHT', 57, 45),
	('Board 1', 'TOP',    'RIGHT', 58, 40),
	('Board 1', 'BOTTOM', 'LEFT',  58, 46),
	('Board 1', 'TOP',    'LEFT',  59, 41),
	('Board 1', 'BOTTOM', 'RIGHT', 59, 47),
	('Board 1', 'TOP',    'RIGHT', 60, 42),
	('Board 1', 'BOTTOM', 'LEFT',  60, 48),
	('Board 1', 'SIDE',   'LEFT',  61, 43),
	('Board 1', 'SIDE',   'RIGHT', 61, 44),
	('Board 1', 'SIDE',   'LEFT',  62, 45),
	('Board 1', 'SIDE',   'RIGHT', 62, 46),
	('Board 1', 'SIDE',   'LEFT',  63, 47),
	('Board 1', 'SIDE',   'RIGHT', 63, 48),
	('Board 1', 'TOP',    'LEFT',  64, 44),
	('Board 1', 'BOTTOM', 'RIGHT', 64, 49),
	('Board 1', 'TOP',    'RIGHT', 65, 45),
	('Board 1', 'BOTTOM', 'LEFT',  65, 50),
	('Board 1', 'TOP',    'LEFT',  66, 46),
	('Board 1', 'BOTTOM', 'RIGHT', 66, 51),
	('Board 1', 'TOP',    'RIGHT', 67, 47),
	('Board 1', 'BOTTOM', 'LEFT',  67, 52),
	('Board 1', 'SIDE',   'LEFT',  68, 49),
	('Board 1', 'SIDE',   'RIGHT', 68, 50),
	('Board 1', 'SIDE',   'LEFT',  69, 51),
	('Board 1', 'SIDE',   'RIGHT', 69, 52),
	('Board 1', 'TOP',    'LEFT',  70, 50),
	('Board 1', 'BOTTOM', 'RIGHT', 70, 53),
	('Board 1', 'TOP',    'RIGHT', 71, 51),
	('Board 1', 'BOTTOM', 'LEFT',  71, 54),
	('Board 1', 'SIDE',   'LEFT',  72, 53),
	('Board 1', 'SIDE',   'RIGHT', 72, 54)
) AS T ("Boards.name", "Corner's Edges.label", "Edge's Corners.label", "Roads.id", "Settlements.id")
JOIN "Boards" ON T."Boards.name" = "Boards"."name"
JOIN "Corner's Edges" ON T."Corner's Edges.label" = "Corner's Edges"."label"
JOIN "Edge's Corners" ON T."Edge's Corners.label" = "Edge's Corners"."label";


INSERT INTO "RoadsTiles" (
	"Boards.id", "Side's Edges.id", "Edge's Sides.id", "Roads.id", "Tiles.id"
)
SELECT "Boards"."id", "Side's Edges"."id", "Edge's Sides"."id", T."Roads.id", T."Tiles.id"
FROM 
(
	VALUES
	('Board 1', 'BOTTOM', 'TOP', 1, 1),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 2, 1),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 3, 1),
	('Board 1', 'BOTTOM', 'TOP', 4, 2),
	('Board 1', 'BOTTOM', 'TOP', 5, 3),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 6, 2),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 7, 1),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 7, 2),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 8, 1),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 8, 3),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 9, 3),
	('Board 1', 'BOTTOM', 'TOP', 10, 4),
	('Board 1', 'TOP', 'BOTTOM', 11, 1),
	('Board 1', 'BOTTOM', 'TOP', 11, 5),
	('Board 1', 'BOTTOM', 'TOP', 12, 6),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 13, 4),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 14, 2),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 14, 4),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 15, 2),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 15, 5),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 16, 3),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 16, 5),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 17, 3),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 17, 6),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 18, 6),
	('Board 1', 'TOP', 'BOTTOM', 19, 2),
	('Board 1', 'BOTTOM', 'TOP', 19, 7),
	('Board 1', 'TOP', 'BOTTOM', 20, 3),
	('Board 1', 'BOTTOM', 'TOP', 20, 8),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 21, 4),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 22, 4),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 22, 7),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 23, 5),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 23, 7),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 24, 5),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 24, 8),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 25, 6),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 25, 8),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 26, 6),
	('Board 1', 'TOP', 'BOTTOM', 27, 4),
	('Board 1', 'BOTTOM', 'TOP', 27, 9),
	('Board 1', 'TOP', 'BOTTOM', 28, 5),
	('Board 1', 'BOTTOM', 'TOP', 28, 10),
	('Board 1', 'TOP', 'BOTTOM', 29, 6),
	('Board 1', 'BOTTOM', 'TOP', 29, 11),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 30, 9),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 31, 7),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 31, 9),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 32, 7),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 32, 10),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 33, 8),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 33, 10),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 34, 8),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 34, 11),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 35, 11),
	('Board 1', 'TOP', 'BOTTOM', 36, 7),
	('Board 1', 'BOTTOM', 'TOP', 36, 12),
	('Board 1', 'TOP', 'BOTTOM', 37, 8),
	('Board 1', 'BOTTOM', 'TOP', 37, 13),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 38, 9),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 39, 9),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 39, 12),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 40, 10),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 40, 12),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 41, 10),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 41, 13),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 42, 11),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 42, 13),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 43, 11),
	('Board 1', 'TOP', 'BOTTOM', 44, 9),
	('Board 1', 'BOTTOM', 'TOP', 44, 14),
	('Board 1', 'TOP', 'BOTTOM', 45, 10),
	('Board 1', 'BOTTOM', 'TOP', 45, 15),
	('Board 1', 'TOP', 'BOTTOM', 46, 11),
	('Board 1', 'BOTTOM', 'TOP', 46, 16),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 47, 14),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 48, 12),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 48, 14),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 49, 12),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 49, 15),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 50, 13),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 50, 15),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 51, 13),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 51, 16),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 52, 16),
	('Board 1', 'TOP', 'BOTTOM', 53, 12),
	('Board 1', 'BOTTOM', 'TOP', 53, 17),
	('Board 1', 'TOP', 'BOTTOM', 54, 13),
	('Board 1', 'BOTTOM', 'TOP', 54, 18),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 55, 14),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 56, 14),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 56, 17),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 57, 15),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 57, 17),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 58, 15),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 58, 18),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 59, 16),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 59, 18),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 60, 16),
	('Board 1', 'TOP', 'BOTTOM', 61, 14),
	('Board 1', 'TOP', 'BOTTOM', 62, 15),
	('Board 1', 'BOTTOM', 'TOP', 62, 19),
	('Board 1', 'TOP', 'BOTTOM', 63, 16),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 64, 17),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 65, 17),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 65, 19),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 66, 18),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 66, 19),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 67, 18),
	('Board 1', 'TOP', 'BOTTOM', 68, 17),
	('Board 1', 'TOP', 'BOTTOM', 69, 18),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 70, 19),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 71, 19),
	('Board 1', 'TOP', 'BOTTOM', 72, 19)
) AS T ("Boards.name", "Side's Edges.label", "Edge's Sides.label", "Roads.id", "Tiles.id")
JOIN "Boards" ON T."Boards.name" = "Boards"."name"
JOIN "Side's Edges" ON T."Side's Edges.label" = "Side's Edges"."label"
JOIN "Edge's Sides" ON T."Edge's Sides.label" = "Edge's Sides"."label";


INSERT INTO "SettlementsTiles" (
	"Boards.id", "Side's Corners.id", "Corner's Sides.id", "Settlements.id", "Tiles.id"
)
SELECT "Boards"."id", "Side's Corners"."id", "Corner's Sides"."id", T."Settlements.id", T."Tiles.id"
FROM 
(
	VALUES
	('Board 1', 'BOTTOM_LEFT', 'TOP', 1, 1),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 2, 1),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 3, 2),
	('Board 1', 'LEFT', 'SIDE', 4, 1),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 4, 2),
	('Board 1', 'RIGHT', 'SIDE', 5, 1),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 5, 3),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 6, 3),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 7, 4),
	('Board 1', 'LEFT', 'SIDE', 8, 2),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 8, 4),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 9, 1),
	('Board 1', 'RIGHT', 'SIDE', 9, 2),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 9, 5),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 10, 1),
	('Board 1', 'LEFT', 'SIDE', 10, 3),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 10, 5),
	('Board 1', 'RIGHT', 'SIDE', 11, 3),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 11, 6),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 12, 6),
	('Board 1', 'LEFT', 'SIDE', 13, 4),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 14, 2),
	('Board 1', 'RIGHT', 'SIDE', 14, 4),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 14, 7),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 15, 2),
	('Board 1', 'LEFT', 'SIDE', 15, 5),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 15, 7),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 16, 3),
	('Board 1', 'RIGHT', 'SIDE', 16, 5),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 16, 8),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 17, 3),
	('Board 1', 'LEFT', 'SIDE', 17, 6),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 17, 8),
	('Board 1', 'RIGHT', 'SIDE', 18, 6),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 19, 4),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 19, 9),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 20, 4),
	('Board 1', 'LEFT', 'SIDE', 20, 7),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 20, 9),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 21, 5),
	('Board 1', 'RIGHT', 'SIDE', 21, 7),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 21, 10),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 22, 5),
	('Board 1', 'LEFT', 'SIDE', 22, 8),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 22, 10),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 23, 6),
	('Board 1', 'RIGHT', 'SIDE', 23, 8),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 23, 11),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 24, 6),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 24, 11),
	('Board 1', 'LEFT', 'SIDE', 25, 9),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 26, 7),
	('Board 1', 'RIGHT', 'SIDE', 26, 9),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 26, 12),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 27, 7),
	('Board 1', 'LEFT', 'SIDE', 27, 10),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 27, 12),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 28, 8),
	('Board 1', 'RIGHT', 'SIDE', 28, 10),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 28, 13),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 29, 8),
	('Board 1', 'LEFT', 'SIDE', 29, 11),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 29, 13),
	('Board 1', 'RIGHT', 'SIDE', 30, 11),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 31, 9),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 31, 14),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 32, 9),
	('Board 1', 'LEFT', 'SIDE', 32, 12),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 32, 14),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 33, 10),
	('Board 1', 'RIGHT', 'SIDE', 33, 12),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 33, 15),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 34, 10),
	('Board 1', 'LEFT', 'SIDE', 34, 13),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 34, 15),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 35, 11),
	('Board 1', 'RIGHT', 'SIDE', 35, 13),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 35, 16),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 36, 11),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 36, 16),
	('Board 1', 'LEFT', 'SIDE', 37, 14),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 38, 12),
	('Board 1', 'RIGHT', 'SIDE', 38, 14),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 38, 17),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 39, 12),
	('Board 1', 'LEFT', 'SIDE', 39, 15),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 39, 17),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 40, 13),
	('Board 1', 'RIGHT', 'SIDE', 40, 15),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 40, 18),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 41, 13),
	('Board 1', 'LEFT', 'SIDE', 41, 16),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 41, 18),
	('Board 1', 'RIGHT', 'SIDE', 42, 16),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 43, 14),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 44, 14),
	('Board 1', 'LEFT', 'SIDE', 44, 17),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 45, 15),
	('Board 1', 'RIGHT', 'SIDE', 45, 17),
	('Board 1', 'BOTTOM_LEFT', 'TOP', 45, 19),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 46, 15),
	('Board 1', 'LEFT', 'SIDE', 46, 18),
	('Board 1', 'BOTTOM_RIGHT', 'TOP', 46, 19),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 47, 16),
	('Board 1', 'RIGHT', 'SIDE', 47, 18),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 48, 16),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 49, 17),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 50, 17),
	('Board 1', 'LEFT', 'SIDE', 50, 19),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 51, 18),
	('Board 1', 'RIGHT', 'SIDE', 51, 19),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 52, 18),
	('Board 1', 'TOP_LEFT', 'BOTTOM', 53, 19),
	('Board 1', 'TOP_RIGHT', 'BOTTOM', 54, 19)
) AS T ("Boards.name", "Side's Corners.label", "Corner's Sides.label", "Settlements.id", "Tiles.id")
JOIN "Boards" ON T."Boards.name" = "Boards"."name"
JOIN "Side's Corners" ON T."Side's Corners.label" = "Side's Corners"."label"
JOIN "Corner's Sides" ON T."Corner's Sides.label" = "Corner's Sides"."label";




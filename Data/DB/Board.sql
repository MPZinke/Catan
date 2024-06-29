
INSERT INTO "Templates" ("name", "size") VALUES
('Board 1', ARRAY[5, 5]::INT[2]);


INSERT INTO "TemplatesPorts" ("id", "Templates.id", "ResourceTypes.id", "TemplatesSettlements.ids") VALUES
(1, 1, NULL, ARRAY[NULL, NULL, NULL,    4,    3, NULL]::INT[6]),
(2, 1, NULL, ARRAY[NULL, NULL, NULL,    6,    5, NULL]::INT[6]),
(3, 1, NULL, ARRAY[NULL, NULL,    7,   13, NULL, NULL]::INT[6]),
(4, 1, NULL, ARRAY[NULL, NULL, NULL, NULL,   18,   12]::INT[6]),
(5, 1, NULL, ARRAY[NULL,   25,   31, NULL, NULL, NULL]::INT[6]),
(6, 1, NULL, ARRAY[NULL, NULL, NULL, NULL,   36,   30]::INT[6]),
(7, 1, NULL, ARRAY[NULL,   44,   49, NULL, NULL, NULL]::INT[6]),
(8, 1, NULL, ARRAY[  47, NULL, NULL, NULL, NULL,   52]::INT[6]),
(9, 1, NULL, ARRAY[  53,   54, NULL, NULL, NULL, NULL]::INT[6]);


INSERT INTO "TemplatesRoads" ("id", "Templates.id", "TemplatesSettlements.ids", "TemplatesTiles.ids") VALUES
( 1, 1, ARRAY[ 1,  2]::INT[2], ARRAY[NULL,    1]::INT[2]),
( 2, 1, ARRAY[ 4,  1]::INT[2], ARRAY[NULL,    1]::INT[2]),
( 3, 1, ARRAY[ 2,  5]::INT[2], ARRAY[NULL,    1]::INT[2]),
( 4, 1, ARRAY[ 3,  4]::INT[2], ARRAY[NULL,    2]::INT[2]),
( 5, 1, ARRAY[ 5,  6]::INT[2], ARRAY[NULL,    3]::INT[2]),
( 6, 1, ARRAY[ 8,  3]::INT[2], ARRAY[NULL,    2]::INT[2]),
( 7, 1, ARRAY[ 4,  9]::INT[2], ARRAY[   1,    2]::INT[2]),
( 8, 1, ARRAY[10,  5]::INT[2], ARRAY[   1,    3]::INT[2]),
( 9, 1, ARRAY[ 6, 11]::INT[2], ARRAY[NULL,    3]::INT[2]),
(10, 1, ARRAY[ 7,  8]::INT[2], ARRAY[NULL,    4]::INT[2]),
(11, 1, ARRAY[ 9, 10]::INT[2], ARRAY[   1,    5]::INT[2]),
(12, 1, ARRAY[11, 12]::INT[2], ARRAY[NULL,    6]::INT[2]),
(13, 1, ARRAY[13,  7]::INT[2], ARRAY[NULL,    4]::INT[2]),
(14, 1, ARRAY[ 8, 14]::INT[2], ARRAY[   2,    4]::INT[2]),
(15, 1, ARRAY[15,  9]::INT[2], ARRAY[   2,    5]::INT[2]),
(16, 1, ARRAY[10, 16]::INT[2], ARRAY[   3,    5]::INT[2]),
(17, 1, ARRAY[17, 11]::INT[2], ARRAY[   3,    6]::INT[2]),
(18, 1, ARRAY[12, 18]::INT[2], ARRAY[NULL,    6]::INT[2]),
(19, 1, ARRAY[14, 15]::INT[2], ARRAY[   2,    7]::INT[2]),
(20, 1, ARRAY[16, 17]::INT[2], ARRAY[   3,    8]::INT[2]),
(21, 1, ARRAY[13, 19]::INT[2], ARRAY[   4, NULL]::INT[2]),
(22, 1, ARRAY[20, 14]::INT[2], ARRAY[   4,    7]::INT[2]),
(23, 1, ARRAY[15, 21]::INT[2], ARRAY[   5,    7]::INT[2]),
(24, 1, ARRAY[22, 16]::INT[2], ARRAY[   5,    8]::INT[2]),
(25, 1, ARRAY[17, 23]::INT[2], ARRAY[   6,    8]::INT[2]),
(26, 1, ARRAY[24, 18]::INT[2], ARRAY[   6, NULL]::INT[2]),
(27, 1, ARRAY[19, 20]::INT[2], ARRAY[   4,    9]::INT[2]),
(28, 1, ARRAY[21, 22]::INT[2], ARRAY[   5,   10]::INT[2]),
(29, 1, ARRAY[23, 24]::INT[2], ARRAY[   6,   11]::INT[2]),
(30, 1, ARRAY[25, 19]::INT[2], ARRAY[NULL,    9]::INT[2]),
(31, 1, ARRAY[20, 26]::INT[2], ARRAY[   7,    9]::INT[2]),
(32, 1, ARRAY[27, 21]::INT[2], ARRAY[   7,   10]::INT[2]),
(33, 1, ARRAY[22, 28]::INT[2], ARRAY[   8,   10]::INT[2]),
(34, 1, ARRAY[29, 23]::INT[2], ARRAY[   8,   11]::INT[2]),
(35, 1, ARRAY[24, 30]::INT[2], ARRAY[NULL,   11]::INT[2]),
(36, 1, ARRAY[26, 27]::INT[2], ARRAY[   7,   12]::INT[2]),
(37, 1, ARRAY[28, 29]::INT[2], ARRAY[   8,   13]::INT[2]),
(38, 1, ARRAY[25, 31]::INT[2], ARRAY[   9, NULL]::INT[2]),
(39, 1, ARRAY[32, 26]::INT[2], ARRAY[   9,   12]::INT[2]),
(40, 1, ARRAY[27, 33]::INT[2], ARRAY[  10,   12]::INT[2]),
(41, 1, ARRAY[34, 28]::INT[2], ARRAY[  10,   13]::INT[2]),
(42, 1, ARRAY[29, 35]::INT[2], ARRAY[  11,   13]::INT[2]),
(43, 1, ARRAY[36, 30]::INT[2], ARRAY[  11, NULL]::INT[2]),
(44, 1, ARRAY[31, 32]::INT[2], ARRAY[   9,   14]::INT[2]),
(45, 1, ARRAY[33, 34]::INT[2], ARRAY[  10,   15]::INT[2]),
(46, 1, ARRAY[35, 36]::INT[2], ARRAY[  11,   16]::INT[2]),
(47, 1, ARRAY[37, 31]::INT[2], ARRAY[NULL,   14]::INT[2]),
(48, 1, ARRAY[32, 38]::INT[2], ARRAY[  12,   14]::INT[2]),
(49, 1, ARRAY[39, 33]::INT[2], ARRAY[  12,   15]::INT[2]),
(50, 1, ARRAY[34, 40]::INT[2], ARRAY[  13,   15]::INT[2]),
(51, 1, ARRAY[41, 35]::INT[2], ARRAY[  13,   16]::INT[2]),
(52, 1, ARRAY[36, 42]::INT[2], ARRAY[NULL,   16]::INT[2]),
(53, 1, ARRAY[38, 39]::INT[2], ARRAY[  12,   17]::INT[2]),
(54, 1, ARRAY[40, 41]::INT[2], ARRAY[  13,   18]::INT[2]),
(55, 1, ARRAY[37, 43]::INT[2], ARRAY[  14, NULL]::INT[2]),
(56, 1, ARRAY[44, 38]::INT[2], ARRAY[  14,   17]::INT[2]),
(57, 1, ARRAY[39, 45]::INT[2], ARRAY[  15,   17]::INT[2]),
(58, 1, ARRAY[46, 40]::INT[2], ARRAY[  15,   18]::INT[2]),
(59, 1, ARRAY[41, 47]::INT[2], ARRAY[  16,   18]::INT[2]),
(60, 1, ARRAY[48, 42]::INT[2], ARRAY[  16, NULL]::INT[2]),
(61, 1, ARRAY[43, 44]::INT[2], ARRAY[  14, NULL]::INT[2]),
(62, 1, ARRAY[45, 46]::INT[2], ARRAY[  15,   19]::INT[2]),
(63, 1, ARRAY[47, 48]::INT[2], ARRAY[  16, NULL]::INT[2]),
(64, 1, ARRAY[44, 49]::INT[2], ARRAY[  17, NULL]::INT[2]),
(65, 1, ARRAY[50, 45]::INT[2], ARRAY[  17,   19]::INT[2]),
(66, 1, ARRAY[46, 51]::INT[2], ARRAY[  18,   19]::INT[2]),
(67, 1, ARRAY[52, 47]::INT[2], ARRAY[  18, NULL]::INT[2]),
(68, 1, ARRAY[49, 50]::INT[2], ARRAY[  17, NULL]::INT[2]),
(69, 1, ARRAY[51, 52]::INT[2], ARRAY[  18, NULL]::INT[2]),
(70, 1, ARRAY[50, 53]::INT[2], ARRAY[  19, NULL]::INT[2]),
(71, 1, ARRAY[54, 51]::INT[2], ARRAY[  19, NULL]::INT[2]),
(72, 1, ARRAY[53, 54]::INT[2], ARRAY[  19, NULL]::INT[2]);


INSERT INTO "TemplatesSettlements" ("id", "Templates.id", "TemplatesPorts.ids", "TemplatesRoads.ids", "TemplatesTiles.ids") VALUES
( 1, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[NULL,    2,   1]::INT[3], ARRAY[NULL,    1, NULL]::INT[3]),
( 2, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[NULL,    3,   1]::INT[3], ARRAY[NULL,    1, NULL]::INT[3]),
( 3, 1, ARRAY[   1, NULL, NULL]::INT[3], ARRAY[NULL,    6,   4]::INT[3], ARRAY[NULL,    2, NULL]::INT[3]),
( 4, 1, ARRAY[   1, NULL, NULL]::INT[3], ARRAY[   2,    7,   4]::INT[3], ARRAY[NULL,    2,    1]::INT[3]),
( 5, 1, ARRAY[   2, NULL, NULL]::INT[3], ARRAY[   3,    8,   5]::INT[3], ARRAY[NULL,    3,    1]::INT[3]),
( 6, 1, ARRAY[   2, NULL, NULL]::INT[3], ARRAY[NULL,    9,   5]::INT[3], ARRAY[NULL,    3, NULL]::INT[3]),
( 7, 1, ARRAY[NULL, NULL,    3]::INT[3], ARRAY[NULL,   13,   10]::INT[3], ARRAY[NULL,    4, NULL]::INT[3]),
( 8, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[   6,   14,   10]::INT[3], ARRAY[NULL,    4,    2]::INT[3]),
( 9, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[   7,   15,   11]::INT[3], ARRAY[   1,    5,    2]::INT[3]),
(10, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[   8,   16,   11]::INT[3], ARRAY[   1,    5,    3]::INT[3]),
(11, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[   9,   17,   12]::INT[3], ARRAY[NULL,    6,    3]::INT[3]),
(12, 1, ARRAY[NULL, NULL,    4]::INT[3], ARRAY[NULL,   18,   12]::INT[3], ARRAY[NULL,    6, NULL]::INT[3]),
(13, 1, ARRAY[   3, NULL, NULL]::INT[3], ARRAY[  13,   21, NULL]::INT[3], ARRAY[NULL, NULL,    4]::INT[3]),
(14, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  14,   22,   19]::INT[3], ARRAY[   2,    7,    4]::INT[3]),
(15, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  15,   23,   19]::INT[3], ARRAY[   2,    7,    5]::INT[3]),
(16, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  16,   24,   20]::INT[3], ARRAY[   3,    8,    5]::INT[3]),
(17, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  17,   25,   20]::INT[3], ARRAY[   3,    8,    6]::INT[3]),
(18, 1, ARRAY[   4, NULL, NULL]::INT[3], ARRAY[  18,   26, NULL]::INT[3], ARRAY[NULL, NULL,    6]::INT[3]),
(19, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  21,   30,   27]::INT[3], ARRAY[   4,    9, NULL]::INT[3]),
(20, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  22,   31,   27]::INT[3], ARRAY[   4,    9,    7]::INT[3]),
(21, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  23,   32,   28]::INT[3], ARRAY[   5,   10,    7]::INT[3]),
(22, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  24,   33,   28]::INT[3], ARRAY[   5,   10,    8]::INT[3]),
(23, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  25,   34,   29]::INT[3], ARRAY[   6,   11,    8]::INT[3]),
(24, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  26,   35,   29]::INT[3], ARRAY[   6,   11, NULL]::INT[3]),
(25, 1, ARRAY[NULL,    5, NULL]::INT[3], ARRAY[  30,   38, NULL]::INT[3], ARRAY[NULL, NULL,    9]::INT[3]),
(26, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  31,   39,   36]::INT[3], ARRAY[   7,   12,    9]::INT[3]),
(27, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  32,   40,   36]::INT[3], ARRAY[   7,   12,   10]::INT[3]),
(28, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  33,   41,   37]::INT[3], ARRAY[   8,   13,   10]::INT[3]),
(29, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  34,   42,   37]::INT[3], ARRAY[   8,   13,   11]::INT[3]),
(30, 1, ARRAY[NULL,    6, NULL]::INT[3], ARRAY[  35,   43, NULL]::INT[3], ARRAY[NULL, NULL,   11]::INT[3]),
(31, 1, ARRAY[NULL, NULL,    5]::INT[3], ARRAY[  38,   47,   44]::INT[3], ARRAY[   9,   14, NULL]::INT[3]),
(32, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  39,   48,   44]::INT[3], ARRAY[   9,   14,   12]::INT[3]),
(33, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  40,   49,   45]::INT[3], ARRAY[  10,   15,   12]::INT[3]),
(34, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  41,   50,   45]::INT[3], ARRAY[  10,   15,   13]::INT[3]),
(35, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  42,   51,   46]::INT[3], ARRAY[  11,   16,   13]::INT[3]),
(36, 1, ARRAY[NULL, NULL,    6]::INT[3], ARRAY[  43,   52,   46]::INT[3], ARRAY[  11,   16, NULL]::INT[3]),
(37, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  47,   55, NULL]::INT[3], ARRAY[NULL, NULL,   14]::INT[3]),
(38, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  48,   56,   53]::INT[3], ARRAY[  12,   17,   14]::INT[3]),
(39, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  49,   57,   53]::INT[3], ARRAY[  12,   17,   15]::INT[3]),
(40, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  50,   58,   54]::INT[3], ARRAY[  13,   18,   15]::INT[3]),
(41, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  51,   59,   54]::INT[3], ARRAY[  13,   18,   16]::INT[3]),
(42, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  52,   60, NULL]::INT[3], ARRAY[NULL, NULL,   16]::INT[3]),
(43, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  55, NULL,   61]::INT[3], ARRAY[  14, NULL, NULL]::INT[3]),
(44, 1, ARRAY[NULL,    7, NULL]::INT[3], ARRAY[  56,   64,   61]::INT[3], ARRAY[  14, NULL,   17]::INT[3]),
(45, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  57,   65,   62]::INT[3], ARRAY[  15,   19,   17]::INT[3]),
(46, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  58,   66,   62]::INT[3], ARRAY[  15,   19,   18]::INT[3]),
(47, 1, ARRAY[NULL,    8, NULL]::INT[3], ARRAY[  59,   67,   63]::INT[3], ARRAY[  16, NULL,   18]::INT[3]),
(48, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  60, NULL,   63]::INT[3], ARRAY[  16, NULL, NULL]::INT[3]),
(49, 1, ARRAY[NULL, NULL,    7]::INT[3], ARRAY[  64, NULL,   68]::INT[3], ARRAY[  17, NULL, NULL]::INT[3]),
(50, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  65,   70,   68]::INT[3], ARRAY[  17, NULL,   19]::INT[3]),
(51, 1, ARRAY[NULL, NULL, NULL]::INT[3], ARRAY[  66,   71,   69]::INT[3], ARRAY[  18, NULL,   19]::INT[3]),
(52, 1, ARRAY[NULL, NULL,    8]::INT[3], ARRAY[  67, NULL,   69]::INT[3], ARRAY[  18, NULL, NULL]::INT[3]),
(53, 1, ARRAY[NULL,    9, NULL]::INT[3], ARRAY[  70, NULL,   72]::INT[3], ARRAY[  19, NULL, NULL]::INT[3]),
(54, 1, ARRAY[NULL,    9, NULL]::INT[3], ARRAY[  71, NULL,   72]::INT[3], ARRAY[  19, NULL, NULL]::INT[3]);


INSERT INTO "TemplatesTiles" ("id", "Templates.id", "coordinate", "count", "ResourceTypes.id", "TemplatesRoads.ids", "TemplatesSettlements.ids") VALUES
( 1, 1, ARRAY[2, 0]::INT[2], NULL, NULL, ARRAY[ 1,  3,  8, 11,  7,  2]::INT[6], ARRAY[ 1,  2,  5, 10,  9,  4]::INT[6]),
( 2, 1, ARRAY[1, 0]::INT[2], NULL, NULL, ARRAY[ 4,  7, 15, 19, 14,  6]::INT[6], ARRAY[ 3,  4,  9, 15, 14,  8]::INT[6]),
( 3, 1, ARRAY[3, 0]::INT[2], NULL, NULL, ARRAY[ 5,  9, 17, 20, 16,  8]::INT[6], ARRAY[ 5,  6, 11, 17, 16, 10]::INT[6]),
( 4, 1, ARRAY[0, 1]::INT[2], NULL, NULL, ARRAY[10, 14, 22, 27, 21, 13]::INT[6], ARRAY[ 7,  8, 14, 20, 19, 13]::INT[6]),
( 5, 1, ARRAY[2, 1]::INT[2], NULL, NULL, ARRAY[11, 16, 24, 28, 23, 15]::INT[6], ARRAY[ 9, 10, 16, 22, 21, 15]::INT[6]),
( 6, 1, ARRAY[4, 1]::INT[2], NULL, NULL, ARRAY[12, 18, 26, 29, 25, 17]::INT[6], ARRAY[11, 12, 18, 24, 23, 17]::INT[6]),
( 7, 1, ARRAY[1, 1]::INT[2], NULL, NULL, ARRAY[19, 23, 32, 36, 31, 22]::INT[6], ARRAY[14, 15, 21, 27, 26, 20]::INT[6]),
( 8, 1, ARRAY[3, 1]::INT[2], NULL, NULL, ARRAY[20, 25, 34, 37, 33, 24]::INT[6], ARRAY[16, 17, 23, 29, 28, 22]::INT[6]),
( 9, 1, ARRAY[0, 2]::INT[2], NULL, NULL, ARRAY[27, 31, 39, 44, 38, 30]::INT[6], ARRAY[19, 20, 26, 32, 31, 25]::INT[6]),
(10, 1, ARRAY[2, 2]::INT[2], NULL, NULL, ARRAY[28, 33, 41, 45, 40, 32]::INT[6], ARRAY[21, 22, 28, 34, 33, 27]::INT[6]),
(11, 1, ARRAY[4, 2]::INT[2], NULL, NULL, ARRAY[29, 35, 43, 46, 42, 34]::INT[6], ARRAY[23, 24, 30, 36, 35, 29]::INT[6]),
(12, 1, ARRAY[1, 2]::INT[2], NULL, NULL, ARRAY[36, 40, 49, 53, 48, 39]::INT[6], ARRAY[26, 27, 33, 39, 38, 32]::INT[6]),
(13, 1, ARRAY[3, 2]::INT[2], NULL, NULL, ARRAY[37, 42, 51, 54, 50, 41]::INT[6], ARRAY[28, 29, 35, 41, 40, 34]::INT[6]),
(14, 1, ARRAY[0, 3]::INT[2], NULL, NULL, ARRAY[44, 48, 56, 61, 55, 47]::INT[6], ARRAY[31, 32, 38, 44, 43, 37]::INT[6]),
(15, 1, ARRAY[2, 3]::INT[2], NULL, NULL, ARRAY[45, 50, 58, 62, 57, 49]::INT[6], ARRAY[33, 34, 40, 46, 45, 39]::INT[6]),
(16, 1, ARRAY[4, 3]::INT[2], NULL, NULL, ARRAY[46, 52, 60, 63, 59, 51]::INT[6], ARRAY[35, 36, 42, 48, 47, 41]::INT[6]),
(17, 1, ARRAY[1, 3]::INT[2], NULL, NULL, ARRAY[53, 57, 65, 68, 64, 56]::INT[6], ARRAY[38, 39, 45, 50, 49, 44]::INT[6]),
(18, 1, ARRAY[3, 3]::INT[2], NULL, NULL, ARRAY[54, 59, 67, 69, 66, 58]::INT[6], ARRAY[40, 41, 47, 52, 51, 46]::INT[6]),
(19, 1, ARRAY[2, 4]::INT[2], NULL, NULL, ARRAY[62, 66, 71, 72, 70, 65]::INT[6], ARRAY[45, 46, 51, 54, 53, 50]::INT[6]);




INSERT INTO "TemplatesDiceValuesCounts" ("Templates.id", "count", "value") VALUES
(1, 1,  2),
(1, 2,  3),
(1, 2,  4),
(1, 2,  5),
(1, 2,  6),
(1, 1,  7),
(1, 2,  8),
(1, 2,  9),
(1, 2, 10),
(1, 2, 11),
(1, 1, 12);


INSERT INTO "TemplatesTilesResourceTypesCounts" ("Templates.id", "count", "ResourceTypes.id")
SELECT T."Templates.id", T."count", "ResourceTypes"."id"
FROM 
(
	VALUES
	(1, 1, 'DESERT'),
	(1, 4, 'WHEAT'),
	(1, 4, 'WOOD'),
	(1, 4, 'SHEEP'),
	(1, 3, 'STONE'),
	(1, 3, 'BRICK')
) AS T ("Templates.id", "count", "ResourceTypes.label")
JOIN "ResourceTypes" ON T."ResourceTypes.label" = "ResourceTypes"."label";


INSERT INTO "TemplatesPortsResourceTypesCounts" ("Templates.id", "count", "ResourceTypes.id")
SELECT T."Templates.id", T."count", "ResourceTypes"."id"
FROM 
(
	VALUES
	(1, 0, 'DESERT'),
	(1, 1, 'WHEAT'),
	(1, 1, 'WOOD'),
	(1, 1, 'SHEEP'),
	(1, 1, 'STONE'),
	(1, 1, 'BRICK')
) AS T ("Templates.id", "count", "ResourceTypes.label")
JOIN "ResourceTypes" ON T."ResourceTypes.label" = "ResourceTypes"."label";


INSERT INTO "TemplatesPortsResourceTypesCounts" ("Templates.id", "count", "ResourceTypes.id") VALUES
(1, 4, NULL);

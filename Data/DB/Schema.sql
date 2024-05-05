

DROP TABLE IF EXISTS "ResourceTypes" CASCADE;
DROP TABLE IF EXISTS "SettlementTypes" CASCADE;
DROP TABLE IF EXISTS "Corner's Edges" CASCADE;
DROP TABLE IF EXISTS "Corner's Sides" CASCADE;
DROP TABLE IF EXISTS "Edge's Corners" CASCADE;
DROP TABLE IF EXISTS "Edge's Sides" CASCADE;
DROP TABLE IF EXISTS "Side's Corners" CASCADE;
DROP TABLE IF EXISTS "Side's Edges" CASCADE;
DROP TABLE IF EXISTS "Boards" CASCADE;
DROP TABLE IF EXISTS "Ports" CASCADE;
DROP TABLE IF EXISTS "Roads" CASCADE;
DROP TABLE IF EXISTS "Settlements" CASCADE;
DROP TABLE IF EXISTS "Tiles" CASCADE;
DROP TABLE IF EXISTS "PortsSettlements" CASCADE;
DROP TABLE IF EXISTS "RoadsSettlements" CASCADE;
DROP TABLE IF EXISTS "RoadsTiles" CASCADE;
DROP TABLE IF EXISTS "SettlementsTiles" CASCADE;
DROP TABLE IF EXISTS "DiceValuesCounts" CASCADE;
DROP TABLE IF EXISTS "PortsResourceTypesCounts" CASCADE;
DROP TABLE IF EXISTS "TilesResourceTypesCounts" CASCADE;
DROP TABLE IF EXISTS "Games" CASCADE;
DROP TABLE IF EXISTS "GamesPorts" CASCADE;
DROP TABLE IF EXISTS "GamesRoads" CASCADE;
DROP TABLE IF EXISTS "GamesSettlements" CASCADE;
DROP TABLE IF EXISTS "GamesTiles" CASCADE;
DROP TABLE IF EXISTS "GamesPortsGamesSettlements" CASCADE;
DROP TABLE IF EXISTS "GamesRoadsGamesSettlements" CASCADE;
DROP TABLE IF EXISTS "GamesRoadsGamesTiles" CASCADE;
DROP TABLE IF EXISTS "GamesSettlementsGamesTiles" CASCADE;
DROP TABLE IF EXISTS "Players" CASCADE;
DROP TABLE IF EXISTS "PlayersResources" CASCADE;
DROP TABLE IF EXISTS "GamesRobbers" CASCADE;
DROP TABLE IF EXISTS "GamesBiggestArmies" CASCADE;
DROP TABLE IF EXISTS "GamesLongestRoads" CASCADE;


CREATE TABLE "ResourceTypes"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


CREATE TABLE "SettlementTypes"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE,
	"multiplier" INT NOT NULL DEFAULT 0 CHECK("multiplier" < 3)
);


-- ——————————————————————————————————————————————————— DIRECTIONS ——————————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "Corner's Edges"  -- The edges of a corne.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


CREATE TABLE "Corner's Sides"  -- The sides of a corner.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


CREATE TABLE "Edge's Corners"  -- The corners of a edge.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


CREATE TABLE "Edge's Sides"  -- The sides of a edge.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);

CREATE TABLE "Side's Corners"  -- The corners of a side.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


CREATE TABLE "Side's Edges"  -- The edges of a side.
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"label" VARCHAR(16) NOT NULL UNIQUE
);


-- ————————————————————————————————————————————————————— BOARDS ————————————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

-- A template used to create a Game from.
CREATE TABLE "Boards"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"name" VARCHAR(32) NOT NULL UNIQUE
);


CREATE TABLE "Ports"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id")
);


CREATE TABLE "Roads"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id")
);


CREATE TABLE "Settlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id")
);


CREATE TABLE "Tiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"coordinate" INT[2] NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id")
);


-- ——————————————————————————————————————————————— BOARDS ASSOCIATION ——————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "PortsSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"Corner's Sides.id" INT NOT NULL,
	"Side's Corners.id" INT NOT NULL,
	"Settlements.id" INT NOT NULL,
	"Ports.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id"),
	FOREIGN KEY ("Corner's Sides.id") REFERENCES "Corner's Sides"("id"),
	FOREIGN KEY ("Side's Corners.id") REFERENCES "Side's Corners"("id"),
	FOREIGN KEY ("Settlements.id") REFERENCES "Settlements"("id"),
	FOREIGN KEY ("Ports.id") REFERENCES "Ports"("id")
);


CREATE TABLE "RoadsSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"Corner's Edges.id" INT NOT NULL,
	"Edge's Corners.id" INT NOT NULL,
	"Roads.id" INT NOT NULL,
	"Settlements.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id"),
	FOREIGN KEY ("Corner's Edges.id") REFERENCES "Corner's Edges"("id"),
	FOREIGN KEY ("Edge's Corners.id") REFERENCES "Edge's Corners"("id"),
	FOREIGN KEY ("Roads.id") REFERENCES "Roads"("id"),
	FOREIGN KEY ("Settlements.id") REFERENCES "Settlements"("id")
);


CREATE TABLE "RoadsTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"Edge's Sides.id" INT NOT NULL,
	"Side's Edges.id" INT NOT NULL,
	"Roads.id" INT NOT NULL,
	"Tiles.id" INT NOT NULL,
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id"),
	FOREIGN KEY ("Edge's Sides.id") REFERENCES "Edge's Sides"("id"),
	FOREIGN KEY ("Side's Edges.id") REFERENCES "Side's Edges"("id"),
	FOREIGN KEY ("Roads.id") REFERENCES "Roads"("id"),
	FOREIGN KEY ("Tiles.id") REFERENCES "Tiles"("id")
);


CREATE TABLE "SettlementsTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Corner's Sides.id" INT NOT NULL,
	"Side's Corners.id" INT NOT NULL,
	"Boards.id" INT NOT NULL,
	"Settlements.id" INT NOT NULL,
	"Tiles.id" INT NOT NULL,
	FOREIGN KEY ("Corner's Sides.id") REFERENCES "Corner's Sides"("id"),
	FOREIGN KEY ("Side's Corners.id") REFERENCES "Side's Corners"("id"),
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id"),
	FOREIGN KEY ("Settlements.id") REFERENCES "Settlements"("id"),
	FOREIGN KEY ("Tiles.id") REFERENCES "Tiles"("id")
);

-- ————————————————————————————————————————————————————— COUNTS ————————————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "DiceValuesCounts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"count" INT NOT NULL CHECK(0 <= "count"),  -- The number of tiles with the value.
	"value" INT NOT NULL CHECK(0 <= "value" AND "value" <= 12),  -- Corresponds to the dice roll value.
	FOREIGN KEY ("Boards.id") REFERENCES "Boards"("id")
);


CREATE TABLE "PortsResourceTypesCounts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"count" INT NOT NULL,  -- The number of tiles with the resource type.
	"ResourceTypes.id" INT DEFAULT NULL,
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


CREATE TABLE "TilesResourceTypesCounts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Boards.id" INT NOT NULL,
	"count" INT NOT NULL,  -- The number of tiles with the resource type.
	"ResourceTypes.id" INT NOT NULL,
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


-- —————————————————————————————————————————————————————— GAME —————————————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "Games"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"started" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"finished" TIMESTAMP DEFAULT NULL,
	"Boards.id" INT DEFAULT NULL
);


-- ————————————————————————————————————————————————————— PORTS —————————————————————————————————————————————————————  --

CREATE TABLE "GamesPorts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Ports.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"ResourceTypes.id" INT,

	FOREIGN KEY ("Ports.id") REFERENCES "Ports"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


CREATE UNIQUE INDEX "GamesPortsUniqueIndex"
ON "GamesPorts" ("Ports.id", "Games.id");

-- ————————————————————————————————————————————————————— ROADS —————————————————————————————————————————————————————  --

CREATE TABLE "GamesRoads"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Roads.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"Players.id" INT DEFAULT NULL,
	FOREIGN KEY ("Roads.id") REFERENCES "Roads"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id")
);


CREATE UNIQUE INDEX "GamesRoadsUniqueIndex"
ON "GamesRoads" ("Roads.id", "Games.id");


-- —————————————————————————————————————————————————— SETTLEMENTS ——————————————————————————————————————————————————  --

CREATE TABLE "GamesSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Settlements.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"Players.id" INT DEFAULT NULL,
	"SettlementTypes.id" INT NOT NULL,
	FOREIGN KEY ("Settlements.id") REFERENCES "Settlements"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("SettlementTypes.id") REFERENCES "SettlementTypes"("id")
);


CREATE UNIQUE INDEX "GamesSettlementsUniqueIndex"
ON "GamesSettlements" ("Settlements.id", "Games.id");


-- ————————————————————————————————————————————————————— TILES —————————————————————————————————————————————————————  --

CREATE TABLE "GamesTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Tiles.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"value" INT NOT NULL CHECK("value" <= 12 AND 0 <= "value"),
	"ResourceTypes.id" INT NOT NULL,
	FOREIGN KEY ("Tiles.id") REFERENCES "Tiles"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


CREATE UNIQUE INDEX "GamesTilesUniqueIndex"
ON "GamesTiles" ("Tiles.id", "Games.id");


-- ———————————————————————————————————————————————— GAME ASSOCIATION ———————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "GamesPortsGamesSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"Corner's Sides.id" INT NOT NULL,
	"Side's Corners.id" INT NOT NULL,
	"GamesSettlements.id" INT NOT NULL,
	"GamesPorts.id" INT NOT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Corner's Sides.id") REFERENCES "Corner's Sides"("id"),
	FOREIGN KEY ("Side's Corners.id") REFERENCES "Side's Corners"("id"),
	FOREIGN KEY ("GamesSettlements.id") REFERENCES "GamesSettlements"("id"),
	FOREIGN KEY ("GamesPorts.id") REFERENCES "GamesPorts"("id")
);


CREATE TABLE "GamesRoadsGamesSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"Corner's Edges.id" INT NOT NULL,
	"Edge's Corners.id" INT NOT NULL,
	"GamesRoads.id" INT NOT NULL,
	"GamesSettlements.id" INT NOT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Corner's Edges.id") REFERENCES "Corner's Edges"("id"),
	FOREIGN KEY ("Edge's Corners.id") REFERENCES "Edge's Corners"("id"),
	FOREIGN KEY ("GamesRoads.id") REFERENCES "GamesRoads"("id"),
	FOREIGN KEY ("GamesSettlements.id") REFERENCES "GamesSettlements"("id")
);


CREATE TABLE "GamesRoadsGamesTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"Edge's Sides.id" INT NOT NULL,
	"Side's Edges.id" INT NOT NULL,
	"GamesRoads.id" INT NOT NULL,
	"GamesTiles.id" INT NOT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Edge's Sides.id") REFERENCES "Edge's Sides"("id"),
	FOREIGN KEY ("Side's Edges.id") REFERENCES "Side's Edges"("id"),
	FOREIGN KEY ("GamesRoads.id") REFERENCES "GamesRoads"("id"),
	FOREIGN KEY ("GamesTiles.id") REFERENCES "GamesTiles"("id")
);


CREATE TABLE "GamesSettlementsGamesTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Corner's Sides.id" INT NOT NULL,
	"Side's Corners.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"GamesSettlements.id" INT NOT NULL,
	"GamesTiles.id" INT NOT NULL,
	FOREIGN KEY ("Corner's Sides.id") REFERENCES "Corner's Sides"("id"),
	FOREIGN KEY ("Side's Corners.id") REFERENCES "Side's Corners"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("GamesSettlements.id") REFERENCES "GamesSettlements"("id"),
	FOREIGN KEY ("GamesTiles.id") REFERENCES "GamesTiles"("id")
);


-- ———————————————————————————————————————————————————— PLAYERS  ———————————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "Players"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"name" VARCHAR(64) NOT NULL,
	"GamesRoads.ids" INT[15] DEFAULT ARRAY[NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL]::INT[15],
	"GamesSettlements.ids" INT[9] DEFAULT ARRAY[NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL]::INT[9],
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id")
);


CREATE TABLE "PlayersResources"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"count" INT NOT NULL DEFAULT 0,
	"Games.id" INT NOT NULL,
	"Players.id" INT NOT NULL,
	"ResourceTypes.id" INT NOT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Players.id") REFERENCES "Players"("id"),
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


CREATE TABLE "GamesRobbers"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"is_friendly" BOOL NOT NULL DEFAULT TRUE,
	"Games.id" INT NOT NULL,
	"GamesTiles.id" INT NOT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("GamesTiles.id") REFERENCES "GamesTiles"("id")
);


CREATE TABLE "GamesBiggestArmies"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"Players.id" INT DEFAULT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Players.id") REFERENCES "Players"("id")
);


CREATE TABLE "GamesLongestRoads"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Games.id" INT NOT NULL,
	"Players.id" INT DEFAULT NULL,
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("Players.id") REFERENCES "Players"("id")
);



ALTER TABLE "GamesRoads" ADD CONSTRAINT "GamesRoads.Players.id" FOREIGN KEY ("Players.id") REFERENCES "Players"("id");
ALTER TABLE "GamesSettlements" ADD CONSTRAINT "GamesSettlements.Players.id" FOREIGN KEY ("Players.id") REFERENCES "Players"("id");


-- FROM: https://stackoverflow.com/a/42784814
CREATE OR REPLACE FUNCTION DefaultSettlementType()
RETURNS TRIGGER 
AS $$ BEGIN
	IF NEW."SettlementTypes.id" IS NULL THEN
		NEW."SettlementTypes.id" = (SELECT "id" FROM "SettlementTypes" WHERE "label" = 'UNENHABITED');
	END IF;

	RETURN NEW;
END; 
$$ language plpgsql; 

CREATE TRIGGER DefaultSettlementType
BEFORE INSERT ON "GamesSettlements"
FOR EACH ROW EXECUTE PROCEDURE DefaultSettlementType();


-- FROM: https://stackoverflow.com/a/42784814
CREATE OR REPLACE FUNCTION DefaultPlayersResources()
RETURNS TRIGGER 
AS $$ BEGIN
	INSERT INTO "PlayersResources" ("Players.id", "Games.id", "ResourceTypes.id")
	SELECT NEW."id", NEW."Games.id", "ResourceTypes"."id"
	FROM "ResourceTypes";
END; 
$$ language plpgsql; 

CREATE TRIGGER DefaultPlayersResources
AFTER INSERT ON "Players"
FOR EACH ROW EXECUTE PROCEDURE DefaultPlayersResources();


-- FROM: https://stackoverflow.com/a/42784814
CREATE OR REPLACE FUNCTION OnNewGame()
RETURNS TRIGGER 
AS $$ BEGIN
	INSERT INTO "GamesRobbers" ("Games.id", "is_friendly", "GamesTiles.id")
	SELECT NEW."id", TRUE, "GamesTiles"."id"
	FROM "GamesTiles"
	JOIN "ResourceTypes" ON "GamesTiles"."ResourceTypes.id" = "ResourceTypes"."id"
	WHERE "ResourceTypes"."label" = 'DESERT';

	INSERT INTO "GamesBiggestArmies" ("Games.id")
	VALUES (NEW."id");

	INSERT INTO "GamesLongestRoads" ("Games.id")
	VALUES (NEW."id");

	RETURN NEW;
END; 
$$ language plpgsql; 

CREATE TRIGGER OnNewGame
AFTER INSERT ON "Games"
FOR EACH ROW EXECUTE PROCEDURE OnNewGame();

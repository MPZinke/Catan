

DROP TABLE IF EXISTS "ResourceTypes" CASCADE;
DROP TABLE IF EXISTS "SettlementTypes" CASCADE;
DROP TABLE IF EXISTS "Corner's Edges" CASCADE;
DROP TABLE IF EXISTS "Corner's Sides" CASCADE;
DROP TABLE IF EXISTS "Edge's Corners" CASCADE;
DROP TABLE IF EXISTS "Edge's Sides" CASCADE;
DROP TABLE IF EXISTS "Side's Corners" CASCADE;
DROP TABLE IF EXISTS "Side's Edges" CASCADE;
DROP TABLE IF EXISTS "Templates" CASCADE;
DROP TABLE IF EXISTS "TemplatesPorts" CASCADE;
DROP TABLE IF EXISTS "TemplatesRoads" CASCADE;
DROP TABLE IF EXISTS "TemplatesSettlements" CASCADE;
DROP TABLE IF EXISTS "TemplatesTiles" CASCADE;
DROP TABLE IF EXISTS "TemplatesPortsSettlements" CASCADE;
DROP TABLE IF EXISTS "TemplatesRoadsSettlements" CASCADE;
DROP TABLE IF EXISTS "TemplatesRoadsTiles" CASCADE;
DROP TABLE IF EXISTS "TemplatesSettlementsTiles" CASCADE;
DROP TABLE IF EXISTS "TemplatesDiceValuesCounts" CASCADE;
DROP TABLE IF EXISTS "TemplatesPortsResourceTypesCounts" CASCADE;
DROP TABLE IF EXISTS "TemplatesTilesResourceTypesCounts" CASCADE;
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
CREATE TABLE "Templates"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"name" VARCHAR(32) NOT NULL UNIQUE,
	"size" INT[2] NOT NULL  -- [columns, rows]
);


CREATE TABLE "TemplatesPorts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Templates.id" INT NOT NULL,
	"ResourceTypes.id" INT DEFAULT NULL,  -- The default resource type of the port.
	"TemplatesSettlements.ids" INT[6] DEFAULT ARRAY[NULL, NULL, NULL, NULL, NULL, NULL]::INT[6],
	FOREIGN KEY ("Templates.id") REFERENCES "Templates"("id"),
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


CREATE TABLE "TemplatesRoads"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Templates.id" INT NOT NULL,
	"TemplatesSettlements.ids" INT[2] DEFAULT ARRAY[NULL, NULL]::INT[2],
	"TemplatesTiles.ids" INT[2] DEFAULT ARRAY[NULL, NULL]::INT[2],
	FOREIGN KEY ("Templates.id") REFERENCES "Templates"("id")
);


CREATE TABLE "TemplatesSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Templates.id" INT NOT NULL,
	"TemplatesPorts.ids" INT[3] DEFAULT ARRAY[NULL, NULL]::INT[3],
	"TemplatesRoads.ids" INT[3] DEFAULT ARRAY[NULL, NULL, NULL]::INT[3],
	"TemplatesTiles.ids" INT[3] DEFAULT ARRAY[NULL, NULL, NULL]::INT[3],
	FOREIGN KEY ("Templates.id") REFERENCES "Templates"("id")
);


CREATE TABLE "TemplatesTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Templates.id" INT NOT NULL,
	"coordinate" INT[2] NOT NULL,
	"count" INT DEFAULT NULL,  -- The default number of tiles with the resource type.
	"ResourceTypes.id" INT DEFAULT NULL,  -- The default resource type of the tile.
	"TemplatesRoads.ids" INT[6] DEFAULT ARRAY[NULL, NULL, NULL, NULL, NULL, NULL]::INT[6],
	"TemplatesSettlements.ids" INT[6] DEFAULT ARRAY[NULL, NULL, NULL, NULL, NULL, NULL]::INT[6],
	FOREIGN KEY ("Templates.id") REFERENCES "Templates"("id"),
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


-- ————————————————————————————————————————————————————— COUNTS ————————————————————————————————————————————————————— --
-- —————————————————————————————————————————————————————————————————————————————————————————————————————————————————— --

CREATE TABLE "TemplatesDiceValuesCounts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Templates.id" INT NOT NULL,
	"count" INT NOT NULL CHECK(0 <= "count"),  -- The number of tiles with the value.
	"value" INT NOT NULL CHECK(0 <= "value" AND "value" <= 12),  -- Corresponds to the dice roll value.
	FOREIGN KEY ("Templates.id") REFERENCES "Templates"("id")
);


CREATE TABLE "TemplatesPortsResourceTypesCounts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Templates.id" INT NOT NULL,
	"count" INT NOT NULL,  -- The number of tiles with the resource type.
	"ResourceTypes.id" INT DEFAULT NULL,
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


CREATE TABLE "TemplatesTilesResourceTypesCounts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"Templates.id" INT NOT NULL,
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
	"size" INT[2] NOT NULL,  -- [columns, rows]
	"Templates.id" INT DEFAULT NULL
);


-- ————————————————————————————————————————————————————— PORTS —————————————————————————————————————————————————————  --

CREATE TABLE "GamesPorts"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"TemplatesPorts.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"ResourceTypes.id" INT,
	"GamesSettlements.ids" INT[6] DEFAULT ARRAY[NULL, NULL, NULL, NULL, NULL, NULL]::INT[6],
	FOREIGN KEY ("TemplatesPorts.id") REFERENCES "TemplatesPorts"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


CREATE UNIQUE INDEX "GamesPortsUniqueIndex"
ON "GamesPorts" ("TemplatesPorts.id", "Games.id");


-- ————————————————————————————————————————————————————— ROADS —————————————————————————————————————————————————————  --

CREATE TABLE "GamesRoads"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"TemplatesRoads.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"Players.id" INT DEFAULT NULL,
	"GamesSettlements.ids" INT[2] DEFAULT ARRAY[NULL, NULL]::INT[2],
	"GamesTiles.ids" INT[2] DEFAULT ARRAY[NULL, NULL]::INT[2],
	FOREIGN KEY ("TemplatesRoads.id") REFERENCES "TemplatesRoads"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id")
);


CREATE UNIQUE INDEX "GamesRoadsUniqueIndex"
ON "GamesRoads" ("TemplatesRoads.id", "Games.id");


-- —————————————————————————————————————————————————— SETTLEMENTS ——————————————————————————————————————————————————  --

CREATE TABLE "GamesSettlements"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"TemplatesSettlements.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"GamesPorts.ids" INT[3] DEFAULT ARRAY[NULL, NULL, NULL]::INT[3],
	"GamesRoads.ids" INT[3] DEFAULT ARRAY[NULL, NULL, NULL]::INT[3],
	"GamesTiles.ids" INT[3] DEFAULT ARRAY[NULL, NULL, NULL]::INT[3],
	"Players.id" INT DEFAULT NULL,
	"SettlementTypes.id" INT NOT NULL,
	FOREIGN KEY ("TemplatesSettlements.id") REFERENCES "TemplatesSettlements"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("SettlementTypes.id") REFERENCES "SettlementTypes"("id")
);


CREATE UNIQUE INDEX "GamesSettlementsUniqueIndex"
ON "GamesSettlements" ("TemplatesSettlements.id", "Games.id");


-- ————————————————————————————————————————————————————— TILES —————————————————————————————————————————————————————  --

CREATE TABLE "GamesTiles"
(
	"id" SERIAL NOT NULL PRIMARY KEY,
	"TemplatesTiles.id" INT NOT NULL,
	"Games.id" INT NOT NULL,
	"coordinate" INT[2] NOT NULL,
	"GamesRoads.ids" INT[6] DEFAULT ARRAY[NULL, NULL, NULL, NULL, NULL, NULL]::INT[6],
	"GamesSettlements.ids" INT[6] DEFAULT ARRAY[NULL, NULL, NULL, NULL, NULL, NULL]::INT[6],
	"value" INT NOT NULL CHECK("value" <= 12 AND 0 <= "value"),
	"ResourceTypes.id" INT NOT NULL,
	FOREIGN KEY ("TemplatesTiles.id") REFERENCES "TemplatesTiles"("id"),
	FOREIGN KEY ("Games.id") REFERENCES "Games"("id"),
	FOREIGN KEY ("ResourceTypes.id") REFERENCES "ResourceTypes"("id")
);


CREATE UNIQUE INDEX "GamesTilesUniqueIndex"
ON "GamesTiles" ("TemplatesTiles.id", "Games.id");


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
CREATE OR REPLACE FUNCTION DefaultRobberType()
RETURNS TRIGGER 
AS $$ BEGIN
	IF NEW."GamesTiles.id" IS NULL THEN
		NEW."GamesTiles.id" = (
			SELECT "GamesTiles"."id"
			FROM "GamesTiles"
			JOIN "ResourceTypes" ON "GamesTiles"."ResourceTypes.id" = "ResourceTypes"."id"
			WHERE "GamesTiles"."Games.id" = NEW."Games.id"
			  AND "ResourceTypes"."label" = 'DESERT'
		);
	END IF;

	RETURN NEW;
END; 
$$ language plpgsql; 

CREATE TRIGGER DefaultRobberType
BEFORE INSERT ON "GamesRobbers"
FOR EACH ROW EXECUTE PROCEDURE DefaultRobberType();


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

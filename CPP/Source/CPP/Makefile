# Directories
# Directories::Source


Catan.o: Game.o Corner.o Edge.o Hexagon.o Resources.o Settlement.o Board_old.o
	@$(eval CATAN_OBJ:=$(OBJECTS_DIR)/Catan.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Catan.cpp -o $(CATAN_OBJ)


Game.o:
	@$(eval GAME_OBJ:=$(OBJECTS_DIR)/Game.o)
	$(CXX) $(FLAGS) $(INCLUDES) -I../../libraries/* -c Game.cpp -o $(GAME_OBJ)


Board_old.o:
	@$(eval BOARD_OLD_OBJ:=$(OBJECTS_DIR)/Board_old.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Board_old.cpp -o $(BOARD_OLD_OBJ)


Corner.o:
	@$(eval CORNER_OBJ:=$(OBJECTS_DIR)/Corner.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Corner.cpp -o $(CORNER_OBJ)


Edge.o:
	@$(eval EDGE_OBJ:=$(OBJECTS_DIR)/Edge.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Edge.cpp -o $(EDGE_OBJ)


Hexagon.o:
	@$(eval HEXAGON_OBJ:=$(OBJECTS_DIR)/Hexagon.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Hexagon.cpp -o $(HEXAGON_OBJ)


Resources.o:
	@$(eval RESOURCES_OBJ:=$(OBJECTS_DIR)/Resources.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Resources.cpp -o $(RESOURCES_OBJ)


Settlement.o:
	@$(eval SETTLEMENT_OBJ:=$(OBJECTS_DIR)/Settlement.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Settlement.cpp -o $(SETTLEMENT_OBJ)

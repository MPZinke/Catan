# Directories
# Directories::Source


Catan.o: Game.o
	@$(eval CATAN_OBJ:=$(OBJECTS_DIR)/Catan.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Catan.cpp -o $(CATAN_OBJ)


Game.o: Association.o Corner.o Edge.o Hexagon.o Resources.o ResourceType.o Settlement.o
	@$(eval GAME_OBJ:=$(OBJECTS_DIR)/Game.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Game.cpp -o $(GAME_OBJ)


Association.o:
	@$(eval ASSOCIATION_OBJ:=$(OBJECTS_DIR)/Association.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Association.cpp -o $(ASSOCIATION_OBJ)


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


ResourceType.o:
	@$(eval RESOURCETYPE_OBJ:=$(OBJECTS_DIR)/ResourceType.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c ResourceType.cpp -o $(RESOURCETYPE_OBJ)


Settlement.o:
	@$(eval SETTLEMENT_OBJ:=$(OBJECTS_DIR)/Settlement.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Settlement.cpp -o $(SETTLEMENT_OBJ)

# Directories
# Directories::Game
GAME_DIR=$(CPP_DIR)/Game


Catan.o: Game.o
	@$(eval CATAN_OBJ:=$(OBJECTS_DIR)/Catan.o)
	$(CXX) $(FLAGS) $(INCLUDES) -c Catan.cpp -o $(CATAN_OBJ)


Game.o:
	@$(MAKE) Game.o -C $(GAME_DIR) \
	  -e CXX="$(CXX)" \
	  -e FLAGS="$(FLAGS)" \
	  -e GAME_DIR="$(GAME_DIR)" \
	  -e INCLUDES="$(INCLUDES)" \
	  -e OBJECTS_DIR="$(OBJECTS_DIR)"


/***********************************************************************************************************************
*                                                                                                                      *
*   created by: MPZinke                                                                                                *
*   on 2023.01.02                                                                                                      *
*                                                                                                                      *
*   DESCRIPTION: TEMPLATE                                                                                              *
*   BUGS:                                                                                                              *
*   FUTURE:                                                                                                            *
*                                                                                                                      *
***********************************************************************************************************************/


#include <iostream>
#include <SFML/Graphics.hpp>


#include "Corner.hpp"
#include "Edge.hpp"
#include "Game.hpp"
#include "Hexagon.hpp"
#include "Player.hpp"
#include "ResourceType.hpp"
#include "Settlement.hpp"


int main()
{
	Game game("GameData.json");
	game.hexagon(0)->hexagon(15);

	sf::RenderWindow window(sf::VideoMode(800, 600), "Catan");
    window.display();
	// Start the game loop
    while (window.isOpen())
    {
        // Process events
        sf::Event event;
        while (window.pollEvent(event))
        {
            // Close window: exit
            if (event.type == sf::Event::Closed)
                window.close();
        }
    }
    return EXIT_SUCCESS;
	// return 0;
}

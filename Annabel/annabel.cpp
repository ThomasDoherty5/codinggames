#include "annabel.h"

int main() {
	std::string wait;
	std::cout << "Press any button to continue." << std::endl;
	std::cin >> wait;
	std::cout << "Annabel" << std::endl;
	std::cin >> wait;
	std::cout << "A game by Santiago Mackenzie." << std::endl;
	std::cin >> wait;
	std::cout << "With help from Adam Hutchings, Nathan Solomon, Jake, Vand, and more." << std::endl;
	std::cin >> wait;
	std::string game_start;
	while(game_start != "q") {
		std::cout << "Press q to continue" << std::endl;
		std::cin >> game_start;
	}

	return 0;
}
#include "general_functions.h"

void action_runner(std::string button, std::string action, std::string refusal_message) {
	std::string input;
	while(input != button) {
		std::cout << "Press " << button << " " << action << "." << std::endl;
		std::cin >> input;
		if(input != button) {
			std::cout << refusal_message << std::endl;
		}
	}
}

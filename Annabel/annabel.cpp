#include "annabel.h"

void gps(int v_road_sign) {
	if(v_road_sign == 3) {
		chapter_one();	// Runs chapter one. Hasn't been written yet.
// There'll be else ifs here for the other road signs.
	} else {
		std::cout << "Perhaps the map is incomplete, but there is no sign of that number. Wherever it may be, may it help some other traveler. Please enter another road sign and we may find it." << std::endl;
		int backup_road_sign = 3;
		std::cin >> backup_road_sign;
		gps(backup_road_sign);
	}
}

int main() {
	std::string wait;
	std::cout << "Press any button to continue." << std::endl;
	std::cin >> wait;
	std::cout << "Annabel" << std::endl;
	std::cin >> wait;
	std::cout << "A game by Santiago Mackenzie." << std::endl;
	std::cin >> wait;
	std::cout << "With help from Adam Hutchings, Nathan Solomon, Jake Roggenbuck, Carter Luck, and more." << std::endl;
	std::cin >> wait;
	std::string game_start;
	while(game_start != "q") {
		std::cout << "Press q to continue" << std::endl;
		std::cin >> game_start;
	}
	std::cout << "You may have come across a road sign on your travels. If you would like to return to that road sign, enter it here. If you have not journeyed before, then this is your first road sign. Its number is 3. Please enter the road sign you would like to return to." << std::endl;
	int road_sign = 3;
	std::cin >> road_sign;
	gps(road_sign);

	return 0;
}

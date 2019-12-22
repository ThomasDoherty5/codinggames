#include "chapter_one.h"

void chapter_one() {
	for(int i; i <= 50; i++) {
		std::cout << "\n";
	}
	std::cout << "The road stretches away to the horizon before you. The heat from the desert makes the air wave in the distance. This is the start, and you don't remember what came before. The road stretches ahead." << std::endl;
	std::string walk = "w";
	while(walk != "w") {
		std::cout << "Press w to begin walking." << std::endl;
		std::cin >> walk;
		if(walk != "w") {
			std::cout << "It is natural to be wary. You may take as much time as you need." << std::endl;
		}
	}
	std::cout << "You walk. As you walk, the air is still and the ground is firm. As you walk, you notice mountains on the horizon that you hadn't seen before. As you walk, you realize that the Sun's light is making you thirsty. The desert does not seem too keen to provide water. As you ponder the predicament, you notice that you've been carrying a pouch filled with water the entire time. How didn't you notice it? You are confused, and wonder if you should take a sip from the appearing container." << std::endl;
	int refusals = 0;
	while(walk != "e") {
		std::cout << "Press e to have a drink." << std::endl;
		std::cin >> walk;
		if(walk != "e") {
			std::cout << "It makes sense that you doubt the beverage. It has just appeared, seemingly anyway. However, you will need a drink eventually, and knowing the water's habit of appearing, who knows if it'll ever disappear." << std::endl;
			refusals ++;
		}
		if(refusals == 5) {
			std::cout << "You might be smart to refuse the mysterious drink, but you would be smarter to take your chances at this point. You are very thirsty." << std::endl;
		}
		if(refusals > 5) {
			std::cout << "Trying to resist the urge to have a drink is exhausting. So much so that you lie down on the road. 'Just a little nap,' you tell yourself. 'Just a nap.'" << std::endl;
			for(int j; j <= 50; j++) {
				std::cout << "\n";
			}
			std::cout << "This journey has ended. It may have just been time for it to end, though. Of course, you may keep journeying another time." << std::endl;
			exit(0);
		}
	}
}

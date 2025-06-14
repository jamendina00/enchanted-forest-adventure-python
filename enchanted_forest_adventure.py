name = input("Type you name:")
print("Welcome", name, "To The Enchanted Forest Adventure!")
print("You find yourself at the edge of a dark, misty forest. Legends say it holds ancient secrets and treasures, but also dangers.")
print("A narrow path stretches before you, and you hear a faint whisper on the wind.")
print("Do you (1) follow the path deeper into the forest or (2) turn back and leave?")

answer = input("Enter 1, 2, or 3: ").lower()
if answer == "1":
    print("\nYou venture deeper into the forest. The trees grow denser, and the air feels heavy.")
    print("Suddenly, a glowing creature with wings like starlight appears before you.")
    print("It speaks in a soft, melodic voice: 'Greetings", name ,".I guard the Heart of the Forest.'")
    print("'Answer my riddle, and I shall grant you passage. Fail, and you shall be lost forever.'")
    print("The creature asks: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'")
    print("Do you answer (1) 'an echo' or (2) 'a ghost'?")

    answer = input("Enter 1 or 2: ").lower()
    if answer == "1":
        print("\nThe creature's eyes sparkle. 'Correct,' it says. 'You are wise.'")
        print("It leads you to a clearing where a glowing crystal pulses with light.")
        print("'This is the Heart of the Forest. Take its blessing and go in peace.'")
        print("You feel a surge of warmth and awaken outside the forest, stronger than before.")
        print("Congratulations!", name ,". You have won the forest's blessing!")

    elif answer == "2":
        print("\nThe creature sighs. 'Incorrect,' it says, and the forest seems to twist around you.")
        print("The trees close in, and you feel a strange pull, as if the forest is swallowing you.")
        print("You are lost in the depths of the forest. Game Over.")

    else:
        print("\nInvalid choice. The creature vanishes, and you are left alone in the dark forest.")
        print("You wander aimlessly, lost forever. Game Over.")

elif answer == "2":
    print("\nYou turn back, feeling the weight of the forest's gaze on your back.")
    print("As you walk away, the whispers fade, but you can't shake the feeling you missed something important.")
    print("Perhaps one day you will return to uncover the secrets of the forest.")
    print("For now", name ,"you leave with a sense of mystery and wonder.")
    print("You return home safely, but the adventure lingers in your heart and mind.")
    print("Game Over.")
    print("\nThank you for playing! Until next time, brave adventurer.")

elif answer == "3":
    print("\nYou decide to explore the forests edge, searching for another way in.")
    print("After some time, you discovered an overgrown trail leading to a crumbling stone archway.")
    print("A hooded figures stands guard, its face hidden in shadows. it leans against the arch, sharpening a dagger. Their eyes glint as they notice you.")
    print("What's your name, traveler? The figures asks.")
    print("You introduce yourself as", name, "and ask who they are.")
    print(name ,"We are the Keeper of Secrets, they reply. We guard the entrance to the hidden glade.")
    print("' They say, 'few find this path. One of us can guide you to the forest's treasure, but it will cost you.'")
    print("They hold out a hand. 'Give me (1) your gold pouch, (2) your trusty dagger, or (3) refuse and go alone.'")

    answer = input("Enter 1, 2, or 3:").lower()
    if answer == "1":
        print("\nYou hand over your gold pouch. The figure nods and gestures for you to follow.")
        print("You walk through the archway into a hidden glade filled with shimmering flowers and a crystal-clear pond.")
        print("In the center, a treasure chest glows softly. 'Take what you seek,' the figure says, 'but remember, every treasure has its price.'")
        print("You open the chest and find a magical artifact that grants you wisdom and courage.")
        print("Congratulations", name, ", you have found the forest's treasure!")

    elif answer == "2":
         print("\nYou offer your dagger. The figure nods and leads you through the archway.")
         print("But the trail grows dark, and you hear growls in the shadows. Without your weapon, you are defenseless.")
         print("The figure laughs coldly. 'You should have kept that blade.'")
         print("Something lunges from the darkness. Game Over.")

    elif answer == "3":
        print("\nYou refuse and step through the archway alone. The figure shrugs and disappears.")
        print("The trail twists and turns, and soon you are hopelessly lost in the undergrowth.")
        print(f"The forest seems to mock you,", name, ". You wander endlessly. Game Over.")

    else:
        print("\nInvalid choice. The figure vanishes, and you are left alone at the archway.")
        print("You wander aimlessly, lost forever. Game Over.")

else:
    print("\nInvalid choice. Please restart the game and choose either 1 or 2.")
    print("Remember, every adventure begins with a choice!")

print("Thank you for playing! We hope you enjoyed your adventure in the Enchanted Forest.", name)
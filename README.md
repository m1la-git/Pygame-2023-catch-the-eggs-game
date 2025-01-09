# Catch the Eggs Game

This is a simple and fun "Catch the Eggs" game implemented in Python using the Pygame library.

## Features

*   **Engaging Gameplay:** Catch falling eggs with a basket to earn points.
*   **Increasing Difficulty:** The speed of the falling eggs increases as your score goes up.
*   **Lives System:** You have a limited number of lives, and missing an egg reduces your life count.
*   **Scoring System:** Earn points for catching eggs.
*   **High Score Tracking:** The game keeps track of your best score.
*   **Visual Effects:** Includes splash animations when eggs are missed and score pop-ups when eggs are caught.
*   **Sound Effects:** Features background music, egg catch sounds, egg drop sounds, and a game over sound.
*   **Restart Option:** Easily restart the game when you lose.
*   **Simple Graphics:** Colorful and clear visual representation of the game elements.

## How to Play

1. **Run the game:** Execute the Python script.
2. **Move the basket:** Use your mouse to move the basket horizontally at the bottom of the screen.
3. **Catch the eggs:** Position the basket under the falling eggs to catch them.
4. **Earn points:** You get 3 points for each egg you successfully catch.
5. **Avoid missing eggs:** If an egg hits the ground, you lose a life.
6. **Game Over:** The game ends when you run out of lives.
7. **Restart:** Click the "Restart" button or press "Enter" to start a new game after a game over.

## Dependencies

Before running the game, make sure you have the following libraries installed:

*   **Pygame:** This library is used for the game's graphics, sound, and input handling.

    You can install Pygame using pip:

    ```bash
    pip install pygame
    ```

## How to Run the Game

1. **Save the code:** Save the provided Python code as a `.py` file (e.g., `catch_eggs.py`).
2. **Ensure resources are present:** Make sure you have the `images` and `sounds` folders in the same directory as your Python script, containing the following files:
    *   `images/bg.jpg`
    *   `images/bg1.jpg`
    *   `images/basket.png`
    *   `images/egg.png`
    *   `images/restart.png`
    *   `images/splash.png`
    *   `sounds/drop.wav`
    *   `sounds/game_over.wav`
    *   `sounds/music.mp3`
    *   `sounds/splash.mp3`
    *   `fonts/Enjoy.ttf`
3. **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run the script using Python:

    ```bash
    python catch_eggs.py
    ```

## Game Controls

*   **Mouse Movement:** Move the basket left and right.
*   **Mouse Left Click (Hold):**  Continuously move the basket.
*   **Enter Key:** Start a new game after game over.
*   **Escape Key:** Quit the game.

## Potential Issues

*   **Missing Resources:** The game requires image, sound, and font files located in the `images` and `sounds` folders, as well as in the same directory for fonts. Ensure these are in the correct locations.
*   **Performance:** The game is generally lightweight, but very old or low-powered systems might experience slight performance issues.
*   **Screen Resolution:** The game window has a fixed size and might not scale perfectly to all screen resolutions.

## Credits

This game was developed as a personal project and utilizes the Pygame library, which is developed and maintained by the Pygame community.

## License

This project is open-source and available under the [MIT License](LICENSE.txt). (You may want to create a `LICENSE.txt` file if you choose to use a specific license).

Enjoy catching eggs!

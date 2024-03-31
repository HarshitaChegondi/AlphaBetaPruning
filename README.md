1. Student Details

    Full name: Harshita Chegondi
    Student ID: 1002115738

2. Information about Programming language used and libraries:

    Python 3.x is used.
    No external libraries are required as the code uses only the Python Standard Library.
    This code is not omega compatible.

3. About this Red-Blue Nim Game

    The Red-Blue Nim game is a strategic two-player game that involves removing marbles from two different piles, red and blue, with the objective varying based on the game version being played: Standard or Misère. In the Standard version, the player forced to take the last marble loses, while in the Misère version, the player taking the last marble wins.

4. Installation

    No installation is required, just ensure you have Python 3.10 or later version installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

5. How to run the Game

To run the game, navigate to the directory containing the `red_blue_nim.py` file in your terminal or command prompt and execute the following command:

        ```bash
        python3 red_blue_nim.py <num-red> <num-blue> [<version>] [<first-player>] [<depth>]
        ```

6. Parameters

    - `<num-red>`: The initial number of red marbles in the pile (required).
    - `<num-blue>`: The initial number of blue marbles in the pile (required).
    - `<version>`: The version of the game to play. Options are `standard` (default) or `misere` (optional).
    - `<first-player>`: Determines who starts the game. Options are `computer` (default) or `human` (optional).
    - `<depth>`: The depth limit for the MinMax algorithm's search (optional). If not provided, the search depth is unlimited.

7. Sample commands to run the code

To play a Standard game with 5 red marbles and 5 blue marbles, starting with the computer, and without a depth limit:

    ```bash
    python3 red_blue_nim.py 5 5 standard computer
    ```

    To play a Misère game with 3 red marbles and 7 blue marbles, starting with the human player, with a search depth of 4:

    ```bash
    python3 red_blue_nim.py 3 7 misere human 4
    ```

8. Game Play

    - On your turn, you will be prompted to choose a pile (`red` or `blue`) and then the number of marbles to remove from that pile (1 or 2).
    - The computer's turn will automatically be calculated using the MinMax algorithm with Alpha-Beta pruning.
    - Play alternates between the human player and the computer until one pile is empty.
    - The game ends when one of the piles is empty, and the winner (or loser) is declared based on the version of the game being played.

9. Rules

    1. Players take turns removing 1 or 2 marbles from either the red or blue pile.
    2. The game ends immediately when one pile is emptied.
    3. In the Standard version, the player who empties a pile loses. In the Misère version, the player who empties a pile wins.

Enjoy the game!

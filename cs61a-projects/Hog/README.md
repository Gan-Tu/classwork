![Dice Picture](http://tugan0329.bitbucket.io/imgs/github/cs61a-hog.png)

# Academic Honesty
If you are a student from UC Berkeley taking CS61A, please DO NOT read my code before you write your own.
Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, **"Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated."** 
The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. 
If you invest the time to learn the material and complete the projects, you won't need to copy any answers.

## Downloads ##
To download this project, click [here](http://tugan0329.bitbucket.io/downloads/cs61a/hog.zip)

# Description of the Game
In this project, I will develop a simulator and multiple strategies for the dice game Hog. 
I will need to use control statements and higher-order functions together.

To spice up the game, we will play with some special rules:

1. **Pig Out**. If any of the dice outcomes is a 1, the current player's score for the turn is 0.
2. **Piggy Back**. When the current player scores 0, the opposing player receives points equal to the number of dice rolled that turn.
Example: If the current player rolls 3 dice that come up 1, 5, and 1, then the current player scores 0 and the opponent scores 3.
3. **Free Bacon**. A player who chooses to roll zero dice scores one more than the largest digit in the opponent's total score
  
  *Example 1*: If the opponent has 42 points, the current player gains 1 + max(4, 2) = 5 points by rolling zero dice.
  *Example 2*: If the opponent has has 48 points, the current player gains 1 + max(4, 8) = 9 points by rolling zero dice.
  *Example 3*: If the opponent has has 7 points, the current player gains 1 + max(0, 7) = 8 points by rolling zero dice.
4. **Hog Wild**. If the sum of both players' total scores is a multiple of seven (e.g., 14, 21, 35), then the current player rolls four-sided dice instead of the usual six-sided dice.
5. **Hogtimus Prime**. If a player's score for the turn is a prime number, then the turn score is increased to the next largest prime number. 

  *Example*: if the dice outcomes sum to 19, the current player scores 23 points for the turn. This boost only applies to the current player. Note: 1 is not a prime number!
  
6. **Swine Swap**. After the turn score is added, if the last two digits of each player's score are the reverse of each other, the players swap total scores.

  *Example 1*: The current player has a total score of 13 and the opponent has 91. The current player rolls two dice that total 6. The last two digits of the current player's new total score (19) are the reverse of the opponent's score (91). These scores are swapped! The current player now has 91 points and the opponent has 19. The turn ends.
  
  *Example 2*: The current player has 66 and the opponent has 8. The current player rolls four dice that total 14, leaving the current player with 80. The reverse of 80 is 08, the opponent's score. After the swap, the current player has 8 and the opponent 80. The turn ends.
  
  *Example 3*: Both players have 90. The current player rolls 7 dice that total 17, a prime that is boosted to 19 points for the turn. The current player has 109 and the opponent has 90. The last two digits 09 and 90 are the reverse of each other, so the scores are swapped. The opponent ends the turn with 109 and wins the game.

############################
# Description of the Files #
############################

1. hog.py: A starter implementation of Hog
2. dice.py: Functions for rolling dice
3. hog_gui.py: A graphical user interface for Hog
4. ucb.py: Utility functions for CS 61A
5. images: A directory of images used by hog_gui.py

####################################
# Instruction for Playing the Game #
####################################
A **graphical user interface** (GUI, for short) is provided to play a fully interactive version of Hog!

In order to render the graphics, make sure you have Tkinter, Python's main graphics library, installed on your computer. 

Once you've done that, you can run the GUI from your terminal:

For two players to play against each other:
```
python3 hog_gui.py
```

To play against the computer, who has an average win rate of 77%:
```
python3 hog_gui.py -f
```

# README #

This is a data structure project (implemented in Java) completed during Fall 2016 CS61B class: Data Structures, taught at Berkeley under Professor Paul Hilfinger. 

This is a java implementation (with GUI) of strategic board game Ataxx. 

It includes customization functionality for presetting blocks and moves; it allows loading of saved command files; and it includes three game modes: player-to-player, player-to-AI, and AI-to-AI. The AI stategy is implemented by me mainly using provsion table, and Alpha Beta Prunning with a depth of 5. The AI logic will be constantly updated.

The code strictly follows the class cs61b code style guidelines with proper documentation at place.

## Academic Honesty ##
If you are a student from UC Berkeley taking CS61B, please DO NOT try to reverse engineer my code. 

Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, "Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated." The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. If you invest the time to learn the material and complete the projects, you won't need to copy any answers.

## How do I get set up? ##

You only need java 1.7/1.8 or above.

## How to Play the Game ##
There are two (2) ways to play the Ataxx game.

- To play a text based game in your terminal/console:

Run the following line in your terminal:

```
java -jar ataxx.jar
```
- To play a game with built-in GUI:

Run the following line in your terminal:

```
java -jar ataxx.jar --display
```

## Game Background ##
Ataxx is a two-person game played with red and blue pieces on a 7-by-7 board. 

As illustrated below, there are two possible kinds of move: you can extend from a piece of your own color by laying down a new piece of your color in an empty square next to that existing piece (horizontally, vertically, or diagonally), or you can jump: move a piece of your own color to an empty, non-adjacent square that is no more than two rows and no more than two columns distant. In either case, all opposing pieces that are next to the previously empty destination square are replaced by pieces of your color. Here is an example of a starting position (in the middle) and two possible moves with the same piece. Squares marked × show red's other possible jumps with that piece:

 ![figure1.png](http://tugan0329.bitbucket.org/imgs/github/cs61b-ataxx-1.png)
 
 Figure 1. Extends and jumps.

At the beginning of the game, we start with pieces in all four corners:

![figure2.png](http://tugan0329.bitbucket.org/imgs/github/cs61b-ataxx-2.png)

Figure 2. Initial position.

The red player goes first, and play alternates until no more moves are possible, or until there have been 25 jumps with no intervening extends. You are allowed to skip a move (pass) only if you have at least one piece, but no legal move. The winner is the player who has the most pieces at the end of the game (thus, you don't automatically lose just because you can't move, unless you have no pieces left). It is possible also to tie.

## Notation ##
We'll denote columns with letters a—g from the left and rows with numerals 1—7 from the bottom, as shown in Figure 2. An ordinary move consists of two positions separated by a hyphen in the format c0r0−c1r1 (e.g., g1-f2). The first position gives a piece owned by the current player, and the second gives an empty square to which the piece jumps or extends. A single hyphen denotes a case where one player has no move and must pass (it is only legal when there is no other legal move).

## Blocks ##
To make things even more interesting, you can place a set of blocks symmetrically about the center of the board before playing. These are pre-filled squares that may never be moved to (the blocks themselves never move). The illustration below is an example of a starting configuration with 10 blocks. Each block is always reflected across the middle row and the middle column. No block may be placed in the four corner corner squares, since initial configuration has pieces there.

For example, the configuration below may be described by listing three squares: "b2", "c3", and "c4"; reflecting these three gives in addition "f2", "e3", "e4", "b6", "c5", "f6", and "e5". Alternatively, the same configuration may be described as "f2", "c3", and "e4".

![figure3.png](http://tugan0329.bitbucket.org/imgs/github/cs61b-ataxx-3.png)
 
Figure 3. Blocks.
 
## Textual Input Game ##
 
 The players (Red and Blue) can each be either a manual player, entering moves as input, or an automated player (AI). Manual players can talk to the program using either a textual interface, or a GUI.

At any given time, your program can be in one of several states:

- **set-up state**, meaning that no game is in progress is moving, and pieces may be placed on the board to set up a position (this is the initial state);
- **playing state**, where players are entering moves and the game is not yet over; or
- **finished state**, where one or the other player has won and no more moves are possible.

There is one command per line, but otherwise, whitespace may precede and follow command names and operands freely. Empty lines have no effect, and everything from a # character to the end of a line is ignored as a comment.

## Commands to Begin and End a Game ##
- **clear**: Abandons the current game (if one is in progress), clears the board to its initial configuration, and places the program in the set-up state. Abandoning a game implies that you resign. This command is valid in any state.
- **start**: Valid only in set-up state. Enters playing state. Red and Blue alternate moves. If there have been moves made during the set-up state, then play picks up at the point where these moves leave off (so, for example, if there was one set-up move made before start, then Blue will move first). In the (unusual) case where the set-up moves have already won the game, start puts the program in finished state.
- **quit**: Abandons any current game (as for clear) and exits the program. Valid in any state. The end of input has the same effect.

## Setup Commands ##
The following commands are valid only in set-up mode. They set various game parameters prior to the start of play.

- **auto C**: Sets up the program so that player C (Red or Blue) is an AI. Initially, and after a clear command, Red is a manual player and Blue is an AI. Thus, the command auto Red causes both Red and Blue to be AIs, so that the start command causes the machine to play a game against itself.
- **manual C**: Sets up the program so that player C (Red or Blue) is a manual player. Thus, the command manual Blue causes both Red and Blue to be manual players (who presumably alternate entering moves on a terminal).
- **block CR**: Sets a block at square CR and all reflections of that square around the middle row and middle column, as described in Blocks. It is an error to place a block (or one of its reflections) on a previously set up piece. Blocks may not be placed after a piece move, until the board is again cleared. In case of any errors, the command has no effect.
- **seed N**: If your program's AIs use pseudo-random numbers to choose moves, this command sets the random seed to N (a long integer). 

## Entering moves##
One can enter moves either in set-up state or in playing state. In set-up state, moves serve to manually set up a position on the playing board. The first and then every other move is for the red player, the second and then every other is for blue, and the normal legality rules apply to all moves. See Notation for move syntax.

The program rejects illegal moves from any player. An AI makes no illegal moves.

## Miscellaneous Commands ##
The following commands are valid in any state.

- **help**: Print a brief summary of the commands.
- **dump**: This command prints the board out.
- **load file**: Reads the given file and in effect substitutes its contents for the load command itself.

## Contribution guidelines ##

The general skeleton of structure is inspired by the frameworks provided by professor Paul N. Hilfinger and UC Berkeley staff memeber. 

The background information about the ataxx game, interactive notations, and the GUI libraries are also produced by UC Berkeley staff memeber. 

I am responsible for implementing ALL core data structure, the game AI, and the GUI (Graphical User Interface).


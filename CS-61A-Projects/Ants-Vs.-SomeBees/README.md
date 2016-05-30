![Alt Text](http://inst.eecs.berkeley.edu/~cs61a/fa15/proj/ants/assets/splash.png)
#Academic Honesty
If you are a student from UC Berkeley taking CS61A, please DO NOT read my code before you write your own.
Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, **"Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated."** 
The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. 
If you invest the time to learn the material and complete the projects, you won't need to copy any answers.

#Description of the Project
In this project, I will create a tower defense game called **Ants Vs. SomeBees**. 
As the ant queen, I populate my colony with the bravest ants my can muster.
My ants must protect their queen from the evil bees that invade my territory.
Irritate the bees enough by throwing leaves at them, and they will be vanquished. 
Fail to pester the airborne intruders adequately, and my queen will succumb to the bees' wrath. 
This game is inspired by PopCap Games' Plants Vs. Zombies.

1. ants.py: The game logic of Ants Vs. SomeBees
2. ants_gui.py: The original GUI for Ants Vs. SomeBees
3. gui.py: An new GUI for Ants Vs. SomeBees
4. graphics.py: Utilities for displaying simple two-dimensional animations
5. state.py: Abstraction for gamestate for gui.py
6. utils.py: Some functions to facilitate the game interface
7. ucb.py: Utility functions for CS 61A
8. assets: A directory of images and files used by gui.py
9. img: A directory of images used by ants_gui.py

[Click here to view the overall class hierarchy](https://d1b10bmlvqabco.cloudfront.net/attach/ij5ddqc0arp6r4/gry5hwu5rkg/ilreu56djlln/classes_ants_all.pdf)


#Instruction to Play of the Game

Play a game that includes water. To access the wet_layout that includes water, add the --water option (or -w for short) when you start the game.
```
python3 ants_gui.py --water
```

A FireAnt should destroy all co-located Bees when it is stung. 
To start a game with ten food (for easy testing):
```
python3 ants_gui.py --food 10
```

A ThrowerAnt should be able to throw_at a Bee in front of it that is not still in the Hive. 
To start a game with ten food (for easy testing):
```
python3 ants_gui.py --food 10
```

There are two GUIs that you can use. 
The first is an older, but tried-and-true interface that we have been using over the past few years. The command to run it is:
```
python3 ants_gui.py [-h] [-d DIFFICULTY] [-w] [--food FOOD]
```

We've also been developing a new browser GUI that we're looking to phase in. It's still in development, but we will continuously push updates to it, which it will automatically download when it runs. The command to run it is:
```
python3 gui.py [-h] [-d DIFFICULTY] [-w] [--food FOOD]
```

#Control Help Menu
``` -h, --help     show this help message and exit```

``` -d DIFFICULTY  sets difficulty of game (easy/medium/hard/insane)```

```-w, --water    loads a full layout with water```

```--food FOOD    number of food to start with when testing```

#Character Description
Here are the detailed information about each character in this game, such as their functions.
##Bees
  A Bee moves from place to place, following exits and stinging ants, causing damage to ants by 1 each time.
##Ants
1. **HarvesterAnt**
  1. food: 2; armor: 1; damage = 0; watersafe = False (will die if put in the water)
  2. HarvesterAnt produces 1 additional food per turn for the colony.
2. **ThrowerAnt**
  1. food: 4; armor: 1; damage = 1; watersafe = False (will die if put in the water)
  2. ThrowerAnt throws a leaf each turn at the nearest Bee.
3. **LongThrower**
  1. food: 2; armor: 1; damage = 1; watersafe = False (will die if put in the water)
  2. A LongThrower only throws leaves at Bees at least 5 places away.
4. **ShortThrower**
  1. food: 2; armor: 1; damage = 1; watersafe = False (will die if put in the water)
  2. A ShortThrower only throws leaves at Bees at most 3 places away.
5. **SlowThrower**
  1. food: 4; armor: 1; damage = special effect; watersafe = False (will die if put in the water)
  2. A SlowThrower applies a slow effect at the nearest Bee for 3 turns.
6. **StunThrower**
  1. food: 6; armor: 1; damage = special effect; watersafe = False (will die if put in the water)
  2. A StunThrower applies a slow effect at the nearest Bee for 1 turn.
7. **FireAnt**
  1. food: 6; armor: 1; damage = 3; watersafe = False (will die if put in the water)
  2. FireAnt cooks any Bee in its Place when it expires, reducing the armor of all Bees in the same Place as the FireAnt by 3.
8. **WallAnt**
  1. food: 4; armor: 4; damage = 0; watersafe = False (will die if put in the water)
  2. A WallAnt has a large armor value and does nothing in each turn
9. **NinjaAnt**
  1. food: 6; armor: 1; damage = 1; watersafe = False (will die if put in the water)
  2. NinjaAnt does not block the path of bees and damages reducing the armor of all bees in its place by 1. When bees fly by, they will fly past NinjaAnt without stinging it
10. **ScubaThrower**
  1. food: 5; armor: 1; damage = 1; watersafe = True (will NOT die if put in the water)
  2. A subclass of ThrowerAnt that is more costly and watersafe. It throws a leaf each turn at the nearest Bee in its range.
11. **HungryAnt**
  1. food: 4; armor: 1; damage = variable; watersafe = False (will die if put in the water)
  2. HungryAnt will select a random Bee from its place and eat it whole, thus killing it. After eating a Bee, it must spend 3 turns digesting before eating again. While digesting, the HungryAnt can't eat another Bee.
12. **BodyguardAnt**
  1. food: 4; armor: 2; damage = 0; watersafe = False (will die if put in the water)
  2. BodyguardAnt provides protection to other Ants. When a Bee stings the ant that is protected bt the BodyguardAnt, only the BodyguardAnt is damanged. The ant inside the BodyguardAnt can still perform its original action. If the BodyguardAnt dies, the contained ant still remains in the place (and can then be damaged).
13. **TankAnt**
  1. food: 6; armor: 2; damage = 1; watersafe = False (will die if put in the water)
  2. The TankAnt is a BodyguardAnt that protects an ant in its place and also deals 1 damage to all bees in its place each turn. 
14. **QueenAnt**
  1. food: 6; armor: 1; damage = 1; watersafe = True (will NOT die if put in the water)
  2. The queen inspires her fellow ants through her bravery. The QueenAnt doubles the damage of all the ants behind her each time she performs an action. Once an ant's damage has been doubled, it is not doubled again on subsequent turns. If new ants were added later behind it, their damage will also double for one time. 
  3. There can be only one true queen. Any queen instantiated beyond the first one is an impostor. It dies upon taking its first action, without doubling any ant's damage or throwing anything.
  4. The game is over if a bee enters her place and reduces queen's armor to 0.


#Acknowledgments
Tom Magrino and Eric Tzeng developed this project with John DeNero. Jessica Wan contributed the orignal artwork. Joy Jeng and Mark Miyashita invented the queen ant. Many others have contributed to the project as well!

Colin Schoen developed the new browser GUI. The beautiful new artwork was drawn by the efforts of Alana Tran, Andrew Huang, Emilee Chen, Jessie Salas, Jingyi Li, Katherine Xu, Meena Vempaty, Michelle Chang, and Ryan Davis.


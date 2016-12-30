![Yelp Map](http://tugan0329.bitbucket.org/imgs/github/cs61a-map.png)
#Academic Honesty
If you are a student from UC Berkeley taking CS61A, please DO NOT read my code before you write your own.
Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, **"Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated."** 
The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. 
If you invest the time to learn the material and complete the projects, you won't need to copy any answers.

## Downloads ##
To download this project, click [here](http://tugan0329.bitbucket.io/downloads/cs61a/maps.zip)

#Description of the Project

In this project, I will create a visualization of restaurant ratings using **machine learning** and the *Yelp academic dataset*. 
In this visualization, Berkeley is segmented into regions, where each region is shaded by the predicted rating of the closest restaurant 
(yellow is 5 stars, blue is 1 star). Specifically, the visualization I will be constructing is a Voronoi diagram.

In the map, each dot represents a restaurant. 
The color of the dot is determined by the restaurant's location. For example, downtown restaurants are colored green. 
The user that generated this map has a strong preference for Southside restaurants, and so the southern regions are colored yellow.

1. abstractions.py: Data abstractions used in the project
2. recommend.py: Machine learning algorithms and data processing
3. utils.py: Utility functions for data processing
4. ucb.py: Utility functions for CS 61A
5. data: A directory of Yelp users, restaurants, and reviews
6. users: A directory of user files
7. visualize: A directory of tools for drawing the final visualization

#Description of How to Use it 
You should be able to generate a visualization of all restaurants rated by a user. 
Use -u to select a user from the users directory. 
You can even create your own.

      python3 recommend.py 
      python3 recommend.py -u one_cluster

The visualization can indicate which restaurants are close to each other (e.g. Southside restaurants, Northside restaurants). 
Dots that have the same color on the map belong to the same cluster of restaurants. 
You can get more fine-grained groupings by increasing the number of clusters with the -k option.

      python3 recommend.py -k 2
      python3 recommend.py -u likes_everything -k 3

In the visualization, you can now predict what rating a user would give a restaurant, even if they haven't rated the restaurant before. To do this, add the -p option:

      python3 recommend.py -u likes_southside -k 5 -p
      
If you hover over each dot (a restaurant) in the visualization, you'll see a rating in parentheses next to the restaurant name.

#Predicting your own ratings
You can use the project to predict your own ratings too! Here's how:

In the users directory, you'll see a couple of .dat files. Copy one of them and rename the new file to yourname.dat (for example, john.dat).
In the new file (e.g. john.dat), you'll see something like the following:

    make_user(
      'John DoeNero',     # name
      [                   # reviews
         make_review('Jasmine Thai', 4.0),
         ...
      ]
Replace the second line with your name (as a string).
Replace the existing reviews with reviews of your own! You can get a list of Berkeley restaurants with the following command: 
```
python3 recommend.py -r 
```
Rate a couple of your favorite (or least favorite) restaurants.
Use recommend.py to predict ratings for you:
```
python3 recommend.py -u john -k 2 -p -q Sandwiches 
```
(Replace john with your name.) 
Play around with the number of clusters (the -k option) and try different queries (with the -q option)!

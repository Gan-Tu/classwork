# README #

This is a client program, trip, using the graph package I implemented in the directory above this folder. 

The API documentation can be accessed [here](https://tugan0329.bitbucket.io/docs/graph/).

## Downloads ##
To download this project, click [here](http://tugan0329.bitbucket.io/downloads/cs61b/trip.zip)

## Trip Client Program ##
This program is a Trip program, that finds the shortest paths between any two locations, given a map.

To run the make client, a user type according to the following format in the terminal:
```
java trip.Main [ -m MAP ] [ -o OUT ] START_PLACE PLACE ...
```
MAP (default it will look for a file named: 'Map') is the name of the file containing the map data. OUT (default, the standard output) receives the solution. START_PLACE PLACE... is a list of two or more names of points on the map.

For example, you can try it out using the example files provided.
```
java -jar trip.jar -m trip.map -o out.txt Berkeley San_Francisco Santa_Cruz
```
The above line gives the shortest paths going from Berkeley, via San Franciscso, and then to Santa Cruz, by reading the map data in "trip.map" file and output the shortest path directions to the "out.txt" file.

### Map Format ###
The map file will be in free format (a sequence of "words" containing no whitespace and separated by whitespace—blanks, tabs, newlines, etc.). Information comes in two forms: location entries, introduced by the letter L, and road entries, introduced by the letter R.

* Location entries have the form `L C X Y` where `C` designates a place and `X` and `Y` are floating-point numbers. This means that the place named `C` is at coordinates `(X, Y)` (we're sort of assuming a flat earth here.) There may only be one location entry for any given `C`.

* Distance entries have the form `R C0  N  L  D  C1` where each `Ci` designates a place, `N` is the name of a road `L` is a numeric distance (a floating-point number), and `D` is one of the strings NS, EW, WE, SN. 

    * Each `Ci` must be declared in a previous location entry. For example, the entry

    ```
     R Montara US_1 56.0 NS Santa_Cruz
    ```
    would mean that US_1 nominally runs North to South from Montara to Santa Cruz, for a distance of 56.0 miles, and that there are no map points in between (I guess we have a rather idiosyncratically sparse map). Our road connections will all be two way, so the sample entry also indicates a South to North-running route (SN) from Santa Cruz to Montara. There will always be at most one road between any two locations. As in real life, the designations of direction (NS, SN, etc.) on road segments are not related to the (X,Y) positions of the locations they join. (Consider, for example, taking I80 from where it intersects with University Avenue towards Sacramento. At that point, it travels north and slightly west, but it is officially east-bound I80.)

## Academic Honesty ##
If you are a student from UC Berkeley taking CS61B, please DO NOT try to reverse engineer my code. 

Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, "Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated." The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. If you invest the time to learn the material and complete the projects, you won't need to copy any answers.


## How do I get set up? ##

You only need java 1.8 or above.


# README #

This is a data structure project (implemented in Java) completed during Fall 2016 CS61B class: Data Structures, taught at Berkeley under Professor Paul Hilfinger. 

The code strictly follows the class cs61b code style guidelines with proper documentation at place.

Due to class policy, the code for the programs are not disclossed. Source code is avaliable upon request.

## Downloads ##
To download this project, click [here](http://tugan0329.bitbucket.io/downloads/image_rescaler.zip)

## About This Image Rescaler ##
This image rescaler uses [seam carving](http://www.wikiwand.com/en/Seam_carving) technique to do content-aware rescaling of image. You can also learn more about it through this [video](https://www.youtube.com/watch?v=6NcIJXTlugc).

## How To Use It? ##
To use it, type the instruction according to the following format below in your terminal.
```
java -jar image_rescaler.jar [image filename] [num rows to remove] [num columns to remove]
```

For example, you can try it out using the provided sample 'ocean.jpg' file.
```
java -jar image_rescaler.jar ocean.jar 100 200
```
The above line will remove 100 rows and 200 columns from 'ocean.jpg' file while maintaing it's content overall relationship.

Try it out!

## Academic Honesty ##
If you are a student from UC Berkeley taking CS61B, please DO NOT try to reverse engineer my code. 

Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, "Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated." The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. If you invest the time to learn the material and complete the projects, you won't need to copy any answers.


## How do I get set up? ##

You only need java 1.8 or above.


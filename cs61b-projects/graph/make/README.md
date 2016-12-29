# README #

This is a client program, make, using the graph package I implemented in the directory above this folder. 

The API documentation can be accessed [here](https://tugan0329.bitbucket.io/docs/graph/).

## Make Client Program ##
This program is a simple version of the Make program (specifically, GNU make).

To run the make client, a user type according to the following format in the terminal:
```
java -ea make.Main [ -D FILEINFO ][ -f MAKEFILE ] TARGET ...
```

For example, you can try it out using the example files provided.
```
java -ea make.Main -D make.dir -f make.mk run
```

### Makefile ###
Save the content in a file with affix ".mk". For example, "make.mk".

An input file ("makefile") will consist of rules that indicate that one set of objects (called targets) depends on another set (called prerequisites). Any line that starts with # or contains only tabs and blanks is ignored. 

For other lines, the syntax is
```
T: P1 P2 ... Pm
    command set
```
where m ≥ 0, and T starts in the first column. We'll call the first line of the rule its header. Each T or Pj is a string of non-whitespace characters other than :, #, or \. The command set consists of zero of more lines that begin with a blank or tab. Command sets with no lines in them are called empty. The commands for one rule end at the next rule (or the end of file). There may be one or more rules that name any particular target, but no more than one of them may be non-empty.

For example:
```
A: B C D
    rebuild A
B: 
    rebuild B
C: D
    rebuild C
D:
    rebuild D
```

### FileInfo ###
Save the content in a file with affix ".dir". For example, "make.dir".

The FILEINFO argument is a file containing lines of the form
```
NAME   CHANGEDATE
```
where CHANGEDATE is an integer indicating a time (the larger the time, the younger the named object).  

The first line of the FILEINFO file contains only a date (that is, an integer), indicating the current time, and larger than any CHANGEDATE in the file.

For example,
```
100
oldfiles 90
```

## Academic Honesty ##
If you are a student from UC Berkeley taking CS61B, please DO NOT try to reverse engineer my code. 

Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, "Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated." The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. If you invest the time to learn the material and complete the projects, you won't need to copy any answers.


## How do I get set up? ##

You only need java 1.8 or above.


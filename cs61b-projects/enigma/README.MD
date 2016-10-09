# README #

This is a data structure project (implemented in Java) completed during Fall 2016 CS61B class: Data Structures, taught at Berkeley under Professor Paul Hilfinger. 

The code strictly follows the class cs61b code style guidelines with proper documentation at place.

If you want to learn about the mechanics about the Enigma Machine, scroll down way below after the "How do I get set up?" section.

## Academic Honesty ##
If you are a student from UC Berkeley taking CS61B, please DO NOT try to reverse engineer my code. 

Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, "Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated." The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. If you invest the time to learn the material and complete the projects, you won't need to copy any answers.


## How do I get set up? ##

You only need java 1.7/1.8 or above.

### Using the Enigma Machine ###
To use the Enigma Machine, please first generate your own **configuration file** using the guidline provided below. Alternatively, you can use the  "default.conf" file, which I provided in the "testing" folder.

There are three (3) ways to use the Enigma Machine:

- To generate encrypted/decrypted file using provided [configuration file] and [input file].

Run the following line in your terminal:

```
java -jar enigma.jar [configuration file] [input file] [output file]
```

where [output file] will be the destination and the name of generated output file.

For example:
```
java -jar enigma.jar default.conf testing/test.inp testing/test.out
```
The above line uses "default.conf" as the configuration to encrypt/decrypt the "test.inp" file in the "testing" folder, and save the encrypted/decrypted file named "test.out" in the "testing" folder.


- To view encrypted/decrypted message directly in the terminal, using provided [configuration file] and [input file].

Run the following line in your terminal:

```
java -jar enigma.jar [configuration file] [input file]
```

For example:
```
java -jar enigma.jar default.conf testing/test.inp
```
The above line uses "default.conf" as the configuration to encrypt/decrypt the "test.inp" file in the "testing" folder, and then display the encrypted/decrypted message directly in the terminal.


- To encrypt/decrypt direct input with live feedback, using provided [configuration file].

Run the following line in your terminal:

```
java -jar enigma.jar [configuration file]
```


For example:
```
java -jar enigma.jar default.conf
```
The above line uses "default.conf" as the configuration. 

Then, you have to first specifiy your settings line using the guidline provided below. 

For example:
```
* B BETA I II III AXLE (AV) (CD)
```

Next, type the message you want to encrypt/decrypt (without special characters. E.g. "," "!"). After you type the message, enter the message by tap the "return" or "enter" button on your keyboard. The encrypted/decrypted message will be printed directly below your input on your terminal. 


### Configuration File Format ###

The configuration file contains descriptions of the machine and the available rotors. The data are in *free format*. That is, they consist of strings of *non-whitespace* characters separated by arbitrary whitespace (spaces, tabs, and newlines), so that indentation, spacing, and line breaks are irrelevant. 

Each file has the following contents:

- A string of non-blank characters, giving the alphabet. Unless you do the extra credit, you may assume this is the upper-case alphabet.

- Two integer numerals, S>P≥0, where S is the number of rotor slots (including the reflector) and P is the number of pawls — that is, the number of rotors that move. The moving rotors and their pawls are all to the right of any non-moving ones.
- Any number of rotor descriptors. Each has the following components (separated by whitespace):
	1. A name containing any non-blank characters other than parentheses.
	2. One of the characters R, N, or M, indicating that the rotor is a reflector, a non-moving rotor, or a moving rotor, respectively. Non-moving rotors can only be used in positions 2–S−P and moving rotors in positions S−P+1-P.
	3. Immediately after the M for a moving rotor come(s) the letter(s) at which there is a notch on the rotor's ring (no space between M and these letters).
	4.The cycles of the permutation, using the notation discussed above. For example, the German Naval Enigma machine might be described with this configuration file:
	
	```
	ABCDEFGHIJKLMNOPQRSTUVWXYZ
	5 3
	I MQ      (AELTPHQXRU) (BKNW) (CMOY) (DFG) (IV) (JZ) (S)
	II ME     (FIXVYOMW) (CDKLHUP) (ESZ) (BJ) (GR) (NT) (A) (Q)
  	III MV    (ABDHPEJT) (CFLVMZOYQIRWUKXSG) (N)
  	IV MJ     (AEPLIYWCOXMRFZBSTGJQNH) (DV) (KU)
  	V MZ      (AVOLDRWFIUQ)(BZKSMNHYC) (EGTJPX)
  	VI MZM    (AJQDVLEOZWIYTS) (CGMNHFUX) (BPRK)
  	VII MZM   (ANOUPFRIMBZTLWKSVEGCJYDHXQ)
  	VIII MZM  (AFLSETWUNDHOZVICQ) (BKJ) (GXY) (MPR)
  	Beta N    (ALBEVFCYODJWUGNMQTZSKPR) (HIX)
  	Gamma N   (AFNIRLBSQWVXGUZDKMTPCOYJHE)
  	B R       (AE) (BN) (CK) (DQ) (FU) (GY) (HW) (IJ) (LO) (MP)
  	          (RX) (SZ) (TV)
  	C R       (AR) (BD) (CO) (EJ) (FN) (GT) (HK) (IV) (LM) (PW)
              (QZ) (SX) (UY)
    ```


### Input File Format ###


## Backgroud About the Enigma Machine ##

### Basic Mechanism ###
...

 ![figures.png](http://tugan0329.bitbucket.org/imgs/github/cs61b-enigma-1.png)
 ![figures.png](http://tugan0329.bitbucket.org/imgs/github/cs61b-enigma-2.png)
 ![figures.png](http://tugan0329.bitbucket.org/imgs/github/cs61b-enigma-3.png)

### Describing Permutation ###

### Example ###


## Contribution guidelines ##

The general skeleton of structure is inspired by the frameworks provided by professor Paul N. Hilfinger and UC Berkeley staff memeber. 
The introduction of the working mechanism for the Enigma machine above is also produced by UC Berkeley staff memeber. 
I am responsible for implementing ALL core data structure as well as the sample testing cases provided.

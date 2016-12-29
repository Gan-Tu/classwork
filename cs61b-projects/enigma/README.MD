# README #

This is a data structure project (implemented in Java) completed during Fall 2016 CS61B class: Data Structures, taught at Berkeley under Professor Paul Hilfinger. 

The code strictly follows the class cs61b code style guidelines with proper documentation at place.

Due to class policy, the code for the programs are not disclossed. Source code is avaliable upon request.

If you want to learn about the mechanics about the Enigma Machine, scroll down way below after the "How do I get set up?" section.

## Downloads ##
To download this project, click [here](http://tugan0329.bitbucket.io/downloads/enigma.zip)

## Academic Honesty ##
If you are a student from UC Berkeley taking CS61B, please DO NOT try to reverse engineer my code. 

Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, "Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated." The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. If you invest the time to learn the material and complete the projects, you won't need to copy any answers.


## How do I get set up? ##

You only need java 1.8 or above.

### Using the Enigma Machine ###
To use the Enigma Machine, please first generate your own **configuration file** using the guidline provided below. 

Alternatively, you can use the  "default.conf" file, which I provided in the "testing" folder.

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

Next, type the message you want to encrypt/decrypt (without special characters. E.g. "," "!"). 

After you type the message, enter the message by tap the "return" or "enter" button on your keyboard. The encrypted/decrypted message will be printed directly below your input on your terminal. 


### Configuration File Format ###

The configuration file contains descriptions of the machine and the available rotors. The data are in *free format*. That is, they consist of strings of *non-whitespace* characters separated by arbitrary whitespace (spaces, tabs, and newlines), so that indentation, spacing, and line breaks are irrelevant. 

Each file has the following contents:

- A string of non-blank characters, giving the alphabet. The alphabet can be anything except whitespace, '(', ')', or '*'.

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
The input file to your program will consist of a sequence of messages to decode, each preceded by a line giving the initial settings. 

For example: given the configuration file above, a settings line looks like this (all upper case.):
```
* B BETA III IV I AXLE (YF) (ZH)
```

This particular example means that the rotors used are reflector B, and rotors Beta, III, IV, and I, with rotor I in the rightmost, or fast, slot. The remaining parenthesized items indicate that the letter pair Y and F and the pair Z and M are steckered (swapped going in from the keyboard and going out to the lights).

In general for this particular configuration, **rotor 1 is always the reflector; rotor 2 is Beta or Gamma, and each of 3—5 is one of rotors I—VIII**. 

A rotor may not be repeated. 

The four letters of the following word (AXLE in the example) give the initial positions of rotors 2—5, respectively (i.e., not including the reflector). Any number of steckered pairs may follow (including none).

After each settings line comes a message on any number of lines. 

Each line of a message consists only of letters, blanks, and tabs (0 or more). The program should ignore the blanks and tabs and convert all letters to upper case. The end of message is indicated either by the end of the input or by a new configuration line (distinguished by its leading asterisk). 

The machine is not reset between lines, but continues stepping from where it left off on the previous message line. Because the Enigma is a reciprocal cipher, a given translation may either be a decryption or encryption; you don't have to worry about which, since the process is the same in any case.

Output the translation for each message line in groups of five upper-case letters, separated by blanks (the last group may have fewer characters, depending on the message length). 

The following figure contains an example that shows an encryption followed by a decryption of the encrypted message. 

![figures.png](http://tugan0329.bitbucket.org/imgs/github/cs61b-enigma-3.png)

Figure: Sample input and output (using the Naval cipher).


## Backgroud About the Enigma Machine ##

### Basic Mechanism ###

You may have heard of the Enigma machines that Germany used during World War II to encrypt its military communications. If you have not, I recommend you read the wikipedia page on them, or similar resource, especially the part about design and operation. 

This project involves building a simulator for a generalized version of this machine (which itself had several different versions.) Your program will take descriptions of possible initial configurations of the machine and messages to encode or decode (the Enigma algorithms were reciprocal, meaning that encryption is its own inverse operation.)

The Enigmas effect a substitution cipher, on the letters of a message. That is, at any given time, the machine performs a permutation---a one-to-one mapping---of the alphabet onto itself. The alphabet consists solely of the 26 letters in one case (there were various conventions for spaces and punctuation).

Plain substitution ciphers are easy to break (you've probably seen puzzles in newspapers that consist of breaking such ciphers). The Enigma, however, implements a progressive substitution, different for each subsequent letter of the message. This made decryption considerably more difficult.

The device consists of a simple mechanical system of (partially) interchangeable rotors (*Walzen*) that sit side-by-side on a shaft and make electrical contact with each other. Most of these rotors have 26 contacts on both sides, which are wired together internally so as to effect a permutation of signals coming in from one side onto the contacts on the other (and the inverse permutation when going in the reverse direction). 

To the left of the rotors, one could select one of a set of reflectors (*Umkehrwalzen*), with contacts on their right sides only, and wired to connect half of those contacts to the other half. A signal starting from the right through one of the 26 possible contacts will flow through wires in the rotors, "bounce" off the reflector, and then come back through the same rotors (in reverse) by a different route, always ending up permuted to a letter position different from where it started. (*This was a significant cryptographic weakness, as it turned out. It doesn't really do a would-be code-breaker any good to know that some letters in an encrypted message might be the same as the those in the plaintext if he doesn't know which ones. But it does a great deal of good to be able to eliminate possible decryptions because some of their letters are the same as in the plaintext.*)

Each rotor and each reflector implements a different permutation, and the overall effect depends on their configuration: which rotors and reflector are used, what order they are placed in the machine, and which rotational position they are initially set to. This configuration is the first part of the secret key used to encrypt or decrypt a message. 

In what follows, we'll refer to the selected rotors in a machine's configuration as 1–N, with 1 being the reflector, and N the rightmost rotor. In our simulator, N will be a configuration parameter. In actual Enigma machines, it was fixed for any given model (the Navy used four and the Wehrmacht used three.)

The overall permutation changes with each successive letter because some of the rotors rotate after encrypting a letter. Each rotor has a circular ratchet on its right side and a an "alphabet ring" (*Ringstellung*) on its left side that fits over the ratchet of the rotor to its left. Before a letter of a message is translated, a spring-loaded pawl (lever), one to the right of each rotating rotor, tries to engage the ratchet on the right side of its rotor and thus rotate that rotor by one position, changing the permutation performed by the rotor. The lever on the rightmost rotor (N) always succeeds, so that rotor N (the "fast" rotor) rotates one position before each character. The pawls pushing the other rotors, however, are normally blocked from engaging their rotors by the ring on the left side of the rotor to their right.

This ring usually holds the pawl away from its ratchet, preventing the rotor wheel to its left from moving. However, the rings have notches in them (either one or two in the original Enigma machines), and when the pawl is positioned over a notch in the ring for the rotor to its right, it slips through to its own rotor and pushes it forward. A "feature" of the design called "double stepping" (corrected in other versions of the Enigma, since it reduced the period of the cipher) is that when a pawl is in a notch, it also moves the notch itself and the rotor the notch is connected to, so that the rotors on both sides of the pawl move.

Let's illustrate with a much simplified version. Suppose our alphabet has only the letters A-C and we have four rotors (numbered 1-4) each of which has one notch on its ring at the C position. Suppose also that there are 3 pawls, one for each of rotors 2-4. There is no pawl for rotor 1, which will therefore not rotate. We'll start with the rotors set at AAAA. The next 19 positions are as follows:

```
AAAB  AAAC  AABA  AABB  AABC  AACA  ABAB  ABAC
ABBA  ABBB  ABBC  ABCA  ACAB  ACAC  ACBA  ACBB
ACBC  ACCA  AAAB
```

As you can see,

- Rotor 4, the fast rotor, advances each time, pushed by pawl 3.
- Rotor 3 advances whenever rotor 4 is at C, because then pawl 3 pushes on its ratchet.
- Rotor 2 advances whenever rotor 3 is at C, pushed by pawl 2. Rotor 3 also advances when it is at C, because when pawl 2 slips into rotor 3's notch it will push against that notch when it moves.
- There is no pawl 1, so rotor 2 (unlike rotor 3) does not advance just because it is at C.
- Rotor 1 never changes, since there is no pawl on either side of it.

So the advancement of the rotors, while similar to that of the wheels of an odometer, is not quite the same. If it were, then the next position after AACA would be AACB, rather than ABAB.

The effect of advancing a wheel is to change where on the wheel any given signal enters or leaves. When a wheel is in its 'A' setting in the machine, then a signal that arrives from the right at, say, the 'C' position, goes into the 'C' contact on the wheel. Likewise, a signal that leaves the wheel from its left 'C' contact exits at the 'C' position. When the wheel is rotated by one to its 'B' setting, a signal that arrives at the 'C' position goes instead into the 'D' contact on the wheel, and a signal that leaves through the 'D' contact does so at the 'C' position. It's easier to calculate if we use numbers 0—25 rather than letters ('A' is 0, 'B' is 1, etc.). Then, when the wheel is in its k setting, a signal entering at the p position enters the p+kmod26 contact on the wheel, and a signal exiting through the c contact does so at the c−kmod26 position. For example, Figure 1 shows one of the rotors from the real Enigma machines (called rotor "I") and the effect of moving from its 'A' to its 'B' setting.

 ![figures.png](http://tugan0329.bitbucket.org/imgs/github/cs61b-enigma-1.png)

The contacts on the rightmost rotor's right side connect with stationary input and output contacts, which run to keys that, when pressed, direct current to the contact from a battery or, when not pressed, direct current back from the contact to a light bulb indicating a letter of the alphabet. Since a letter never encrypts or decrypts to itself after going back and forth through the rotors, the to and from directions never conflict.

The German Navy used a machine with 12 rotors and five slots for them:

- Eight rotors labeled with roman numerals I—VIII, of which three will be used in any given configuration as the rightmost rotors,
- Two additional non-moving rotors (Zusatzwalzen) labeled "Beta" and "Gamma", of which one will be used in any configuration, as the fourth-from-right rotor, and
- Two reflectors (Umkehrwalzen), labeled 'B' and 'C', of which one will be used in any given configuration as the leftmost rotor.

Given just this equipment, there are 614,175,744 possible configurations (or keys):
- Two possible reflectors, times
- Two possible rotors in the fourth position, times
- 8!/(8−3)!=336 choices for the rightmost three rotors and their ordering, times
- 26^4 possible initial rotational settings for the rightmost four rotors (each reflector had only one possible position.).

Especially by today's standards, this is not a large key size (less than 30 bits). To make things more difficult for code-breakers, therefore, the Enigma incorporated a plugboard (*Steckerbrett*) between the keyboard and the rightmost wheel. It acted as a non-moving, configurable rotor. 

The operator could choose any set of disjoint pairs of letters by means cables placed between them on the plugboard. Each selected pair would then be swapped going into the machine from the keyboard and coming out into the indicator lights. Thus, if the operator connected ("steckered") the letters A and P, then P would be substituted for each A typed and vice versa. Likewise, if an ingoing letter was encrypted to P by the other rotors, it would display as A, and letters decrypted as A would display as P.

### Describing Permutation ###

Since the rotors and the plugboard implement permutations, we'll need a standard way to describe them. We could simply have a table showing each letter and what it maps to, but we'll use a more compact notation known as *cycle representation*. The idea is that any permutation of a set may be described as a set of *cyclic permutations*. 

For example, the notation
```
(AELTPHQXRU) (BKNW) (CMOY) (DFG) (IV) (JZ) (S)
```
describes the permutation in Figure 1. It describes seven cycles:
- A maps to E, E to L, L to T, ..., R to U, and U back to A.
- B maps to K, K to N, N to W, and W back to B.
- C maps to M, M to O, O to Y, and Y back to C.
- D maps to F, F to G, and G back to D.
- I maps to V and V back to I.
- J maps to Z and Z back to J.
- S maps to itself.

The inverse permutation just reverses these cycles:
- U maps to R, R to X, ..., E to A, and A back to U.
- ...
- S maps to itself.

Each letter appears in one and only one cycle, so the mapping is unambiguous. As a shorthand, we'll say that if a letter is left out of all cycles, it maps to itself (so that we could have left off "(S)" In the example above.)

Figure below shows the permutations corresponding to the rotors used in the German Navy's Enigma machine.

 ![figures.png](http://tugan0329.bitbucket.org/imgs/github/cs61b-enigma-2.png)

### Example ###

As an example of a translation, consider the set of rotors from Figure 2, and suppose that

- The rotors in positions 1—5 are, respectively, B, Beta, III, IV, and I.
- The rotors in positions 2—5 are currently at positions A, X, L, E, respectively.
- In the plugboard, the letter pair 'Y' and 'F' and the letter pair 'Z' and 'H' are both interchanged.

We input the letter 'Y', which causes the following steps:

1. The pawls all move. This causes rotor 5 to advance from E to F. The other two pawls are not over notches, so rotors 3 and 4 do not move.
2. The letter 'Y' enters the plugboard and is converted to 'F'.
3. The letter 'F' enters the right side of rotor 5 (an I rotor). Since this rotor is at position 'F' (letter number 5 of the alphabet, numbering from 0), the signal enters the rotor at position 5+5=10, or 'K'.
4. According to Figure 2, rotor I converts 'K' to 'N' (letter number 13). Because of the rotation of rotor I, however, the signal actually comes out at letter position 13−5=8 ('I').
5. The 'I' signal from rotor 5 now goes into the right side of rotor 4. Since rotor 4 is a IV rotor and is in the 'L' (or 11) position, the 'I' enters the 8+11=19 ('T') position, and is translated to 'G' (6), which comes out at position 6−11=−5=21mod26, the fifth letter from the end of the alphabet ('V').
6. The 'V' from rotor 4 goes now to the right side of rotor 3, a III rotor in position 'X' (23). The signal enters the rotor at position 21+23=44=18mod26 ('S'), is translated to 'G' (6), which exits at position 6−23=−17=9mod26 ('J').
7. Rotor 2 (Beta) is in position 'A', and thus translates 'J' to 'W'.
8. Rotor 1 (B) converts the 'W' to 'H' and bounces it back to the left side of rotor 2.
9. Rotor 2 (Beta in the 'A' position) converts 'H' on its left to 'X' (23) on its right.
10. The 'X' from rotor 2 now goes into the 23+23=46=20mod26 ('U') position on the left side of rotor 3 (III in position 'X'), and is converted to 'W' (22), which comes out at position 22−23=−1=25mod26 ('Z') on the right side of rotor 3.
11. 'Z' now enters the left side of rotor 4 (IV in position 'L') at 25+11=36=10mod26 ('K'), and is translated to 'U' (20), which comes out at position 20−11=9 ('J') on the right side of rotor 4.
12. The 'J' from rotor 4 enters the left side of rotor 5 (I at position 'F') at position 9+5=14 ('O'), is translated to 'M' (12), and comes out at position 12−5=7 ('H') on the right side of rotor 5.
13. Finally,the letter 'H' is converted to 'Z' by the plugboard.

Therefore, 'Y' is converted to 'Z'.

After a total of 12 characters are converted, the rotor settings will have become 'AXLQ'. Just before the next character is converted, rotor 5 will advance to 'R' and, since its notch is at position 'Q', rotor 4 will advance to 'M', so that the rotor configuration will be 'AXMR' before the 13th character is converted. After an additional 597 characters have been converted, the configuration will be 'AXIQ'. The character after that will advance rotor 5 to 'R' and rotor 4 to 'J', giving 'AXJR'. The next character will advance 5 to 'S', and, since rotor IV's notch is at 'J', rotor 3 will advance to 'Y'. Also, as rotor 3's pawl advances rotor 3, it also moves the notch on rotor 4, advancing rotor 4 to 'K', so that the configuration goes from 'AXJR' to 'AYKS'. Rotor 3 in this case has a notch at 'V', but since rotor 2 has no pawl, rotor 3's notch never has any effect.

## Contribution guidelines ##

The general skeleton of structure is inspired by the frameworks provided by professor Paul N. Hilfinger and UC Berkeley staff memeber. 
The introduction of the working mechanism for the Enigma machine above is also produced by UC Berkeley staff memeber. 
I am responsible for implementing ALL core data structure as well as the sample testing cases provided.

#Academic Honesty
If you are a student from UC Berkeley taking CS61A, please DO NOT read my code before you write your own.
Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, **"Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated."** 
The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. 
If you invest the time to learn the material and complete the projects, you won't need to copy any answers.

#Introduction
In this project, I will develop an interpreter for a subset of the **Scheme** language. 

Scheme is a simple but powerful functional language. 
To learn more about Scheme, you can read Structure and Interpretation of Computer Programs online for free. 

I will also implement some small programs in Scheme. Files can be find in questions.scm

#Files Contained in the Projects
You can download all of the project code as a zip archive, which contains the following files:

1. scheme.py: the Scheme evaluator
2. scheme_reader.py: the Scheme syntactic analyzer
3. questions.scm: a collection of functions written in Scheme
4. tests.scm: a collection of test cases written in Scheme
5. scheme_tokens.py: a tokenizer for Scheme
6. scheme_primitives.py primitive Scheme procedures
7. buffer.py: a buffer implementation
8. ucb.py: utility functions for 61A

#Development of the Scheme Interpreter 
I will develop the interpreter in several stages:

1. Reading Scheme expressions
2. Symbol evaluation
3. Calling built-in procedures
4. Definitions
5. Lambda expressions and procedure definition
6. Calling user-defined procedures
7. Evaluation of special forms

#Details of Scheme
**Read-Eval-Print** The interpreter reads Scheme expressions, evaluates them, and displays the results.
```
scm> 2
2
scm> (+ 2 3)
5
scm> (((lambda (f) (lambda (x) (f f x)))
       (lambda (f k) (if (zero? k) 1 (* k (f f (- k 1)))))) 5)
120
```

**Load** My load procedure differs from standard Scheme in that I use a symbol for the file name. 
For example, to load tests.scm, evaluate the following call expression.
```
scm> (load 'tests)
```

**Symbols** Various dialects of Scheme are more or less permissive about identifiers (which serve as symbols). 
For example, the language of the current Scheme reference manual excludes "1+" as a possible symbol, but MIT/GNU Scheme allows it (probably because it is a traditional symbol for the successor function in other Lisp dialects). 
Likewise, in MIT/GNU Scheme, identifiers are not case-sensitive; the reference manual says otherwise.

My rule is that

An identifier is a sequence of letters (a-z and A-Z), digits, and characters in !$%&*/:<=>?@^_~-+. that do not form a valid integer or floating-point numeral. 
My version of Scheme is case-insensitive: two identifiers are considered identical if they match except possibly in the capitalization of letters. 
They are internally represented and printed in lower case:
```
scm> 'Hello
hello
```

#Running the Scheme Interpreter
To run my Scheme interpreter in an interactive session, type:
```
python3 scheme.py
```
You can use the Scheme interpreter to evaluate the expressions in an input file by passing the file name as a command-line argument to scheme.py:
```
python3 scheme.py tests.scm
```
To exit the Scheme interpreter, press Ctrl-d or evaluate the exit procedure (after completing problems 3 and 4):
```
scm> (exit)
```

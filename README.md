# Markov-algorithm-interpreter
This is a simple Python program for creating files with commands for Markov algorithms and for interpreting them.

This program gives you possibility to create files (simple text files, .txt extension) with commands for Markov algorithms. Also you can run these files right after their creation or after next start of program.

Operators:

  ->  simple substitution formulas
  
  =>  final substitution formulas

Few examples of commands:

  A->B  B replaces A in string
  
  C->   deleting C from string
  
  D=>   appending D to the front of string and stop program after that

IMPORTANT NOTE:
Don't use space to separate operators and operands because program recognises it in the same way as other symbols. Also don't use operands which include '->' and '=>'.

For more information about Markov algorithms visit
https://en.wikipedia.org/wiki/Markov_algorithm

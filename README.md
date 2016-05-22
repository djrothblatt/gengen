# gengen.py
Author: Daniel J. Rothblatt, June 2015

Description: This program automatically generates Python scripts which
will randomly generate strings of a specified regular language.
This script works by generating a finite-state automaton generating the specified language

Purpose: Certain algorithms (e.g. Angluin's Algorithm) work on large
amounts of data from a regular language. Rather than write strings of
a regular language yourself (which is time-consuming, boring, and
error-prone), or a program that generates a specific regular
language (which, if many regular languages are needed, is still
time-consuming, boring, and error-prone, but more so, since you are
writing a large number of programs; this approach also requires the
user to decide how a regular language would be implemented), this
project enables the user to specify the regular language they want to
generate and simply have a script to generate it. I can attest from
personal experience that this saves hours of work when testing an
algorithm that works on regular languages.

Use:  
     Grammar:    
          \<command\> ::= python3 gengen.py (\<output_spec\>? \<expression\>+ | \<expression\>+ \<output_spec\>?)  
          \<output_spec\> ::= -o \<filename\>  
          \<filename\> ::= \w+.py  
          \<expression\> ::= \<state_flag\> \<label\> \<dest\>+  
          \<state_flag\> ::= -n | -s | -a | -sa  
          \<label\> ::= \d+  
          \<dest\> ::= \<label\> \<output_string\>  
          \<output_string\> ::= \w+  
     EX: python3 gengen.py -o foo.py -sa 0 0 a 1 b -n 1 0 b  
     (\w and \d as in Perl regex character classes)

     Semantics:
        state flags:
              -n : "normal" state -- neither accepting nor starting
              -s : "starting" state -- indicates the output script will start in this state
              -a : "accepting" state -- indicates the output script can stop building a string in this state
              -sa : "starting/accepting" state -- indicates output script will start in this state and can stop a string in this state
              N.B.: There should only be one -s/-sa state in any specification (you can only have one state to start in)
        dest: indicates possible transition from specified state to destination state, printing specified output string
        output: by default, gengen prints to default.py. The user can specify a different name for the output file with an optional output spec.
      EX: python3 gengen.py -o foo.py -sa 0 0 a 1 b -n 1 0 b
          Prints a language to foo.py, which has:  
                 starting/accepting state 0, with transitions to itself print 'a' or to state 1 printing 'b'; AND  
                 a normal state 1 transitioning to 0 printing b  
          The generated regular language will print any number of 'a's and an even number of 'b's in pairs (i.e., 'bba', never 'bab')

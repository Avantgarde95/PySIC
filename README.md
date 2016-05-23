# PySIC
A simple programming language with a BASIC-like grammar.

This language is not suitable for practical use; There are few keywords and the performance is very bad.

I just created this to study about implementing a programming language, but you can play with this freely if you want :)

- Latest version : 1.0

- Usage : python pysic.py YourSourceFile.psc

- Simple documentation :

  (1) All non-empty lines should have the form ```<keyword> <argument 1> <argument 2> ...```

  (2) Currently supported keywords :
  
      - ```in <expr>``` : Input a value from user
      
      - ```out <expr> ...``` : Display a value on the screen
      
      - ```# <expr> ...``` : Comment
      
      - ```let <expr1> <expr2>``` : Declare a variable with name <expr> and value <expr2>
      
      - ```block <expr>``` : Similar to 'LABEL' in BASIC; If you mark a line as a 'block',
                       then you can jump to the line using goto, if, etc.
      
      - ```goto <expr>``` : Jump to the block with name <expr>
      
      - ```pass``` : Do nothing and move to the next line
      
      - ```exit``` : Terminate the program
      
      - ```if / if= / if== / if> / if< / if>= / if<= / if!= <expr1> <expr2> <expr3> <expr4>``` :
              Compare <expr1> and <expr2>. If it is true, move to the block <expr3>.
              Otherwise, move the block <expr4>. (if / if= / if== have the same meaning!)
      
      - ```add / sub / mul / div <expr1> <expr2> <expr3>``` :
              Add / Substitute / Multiply / Divide <expr2> to (by) <expr3>, 
              and set the variable with name <expr1> to that value.


    (3) What I will add in the next version :
        
        - Make the parser to display the SyntaxError message on the pysic shell
          after it raises an parsing error (PsParserInterrupt in exception.py).
        
        - Add some data structures like list, etc.
        
        - Currently, when you write a string in the source file,
          you have to use ^ for denoting the space (ex. "I^love^you!").
          I'll improve the parser to add more flexibility.
          
        - Looping tools like for, while, etc.

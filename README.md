# PySIC
A simple programming language I made for studying PL.
The language has a simple BASIC-like grammar, and has a small number of keywords.

- Latest version : 1.0

- Simple documentation :
  (1) All non-empty lines should have the form '<keyword> <argument 1> <argument 2> ...'
  (2) Currently supported keywords :
      - in <expr> : Input a value from user
      - out <expr> ... : Display a value on the screen
      - # <expr> ... : Comment
      - let <expr1> <expr2> : Declare a variable with name <expr> and value <expr2>
      - block <expr> : Similar to 'LABEL' in BASIC; If you mark a line as a 'block',then you can jump to the line using goto, if, etc.
      - goto <expr> : Jump to the block with name <expr>
      - pass : Do nothing and move to the next line
      - exit : Terminate the program
      - if / if= / if== / if> / if< / if>= / if<= / if != <expr1> <expr2> <expr3> <expr4> : Compare <expr1> and <expr2>. If it is true, move to the block <expr3>. Otherwise, move the block <expr4>. (if / if= / if== have the same meaning!)
      - add / sub / mul / div <expr1> <expr2> <expr3> : Add / Substitute / Multiply / Divide <expr2> to (by) <expr3>, and set the variable with name <expr1> to that value.

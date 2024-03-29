I used recursive depth first searchh algorithm to create a possible valid combination of parentheses. 
I create a set to the resujlts to avoid creating duplicates. 
First I defined a helper function to check if the given string of parantheses is valid.
The main function is to do the depth first search. 
The code shohuld iterate trough the input string and for each character thats not a parentheses it will move onto the next char.
The search should remove the char with a string and call the main function.

Time complexity: the time complexity will depend on the input because the we can not know the number of recursive calls
I will roughly say this is O(2^(N/2)).

Efficiency: With depth first searchh we can reduce the search space but similiar to te time complexity, 
but the time complexity should be enough even if the imput has alot of parentheses.

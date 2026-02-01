name = "Tim"       
    surname = " Jones"          #Compilation error; incorrect space indentation, needs to be in line with 'name' and 'age'
age = 21
   
full_message = name + surname +  is  + age + " years old" #Runtime error; 'age' needs to be cast to a str() + # Compilation error; 'is' is under the wrong syntax, needs to be within " "  

print (full_message)   # Syntax error; fullMessage does not have appropriate spacing requiring: + " " +

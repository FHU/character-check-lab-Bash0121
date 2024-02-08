#Remove pass and complete the code
def check_character(word, index):
   word_chracter=word[index]
   
   whitespace=" "
   string=word_chracter.isalpha()
   numbers=('1', '2', '4', '5', '6', '7', '8', '9')


   if word_chracter in numbers:  
         return "digit"
   elif string==True:
         return "letter"
   elif word_chracter in whitespace
         return "white space"
   else:
         return "unknown"
   
if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
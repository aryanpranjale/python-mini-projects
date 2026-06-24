text =input("Enter the text you want to encrypt:")
try:
      offset = int(input("Enter the shift you want:"))
except ValueError:
      print ("Please entre a vaild input")
      exit()

def caesar(text,offset):
      alphabet= "abcdefghijklmnopqrstuvwxyz"
      msg = text.lower()
      encrypt_text = ''
      
      for i in msg:
            
            
            if not i.isalpha():
                  encrypt_text += i
                  
            else:
                  new_index = alphabet.find(i)
                  new_index += offset
                  new_letter = alphabet[new_index % 26]
                  encrypt_text += new_letter
            
      return encrypt_text

result = caesar(text, offset)
print ( result)
def verify(card_details): 
      card_details_reversed = card_details[::-1]
      odd_digits= card_details_reversed[::2]
      
      sum_odd_digits= 0
      for i in odd_digits:
            
            sum_odd_digits += int(i) 
      even_digits= card_details_reversed[1::2]
      
      sum_even_digits= 0
      for a in even_digits:
            num_even= int(a)
            num_even *= 2
            if num_even >= 10:
                  num_even= num_even//10 + num_even%10
            sum_even_digits+= num_even
      total= sum_odd_digits+ sum_even_digits
      return total
def card_verification():
      card_number = input("Enter the card number:")
      trans_card_num= str.maketrans({" ":"" , "-": ""})
      translated = card_number.translate(trans_card_num)
      if not 13<=len(translated)<=19:
            print ("Enter a valid Card number")
            card_verification()
            
      else:
            num= verify(translated)
            if num %10 == 0 :
                  print(" It is valid!")
            else:
                  print(" It is invalid!")
card_verification()
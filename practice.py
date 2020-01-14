def is_abecedarian(word):
    previous = word[0]
    for c in word:
      if c < previous:
        return False
      previous = c
    return True
  
  
def is_abecedarian(word):
    if len(word) <= 1:
       return True
    if word[0] >word[1]:
       return False
      
    return is_abecedarian(word[1:])

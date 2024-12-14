import random
from random import randint


vowels = ["a", "e", "i", "o", "u", "y"]
consonants = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

noun = ["dog", "cat", "rat", "bird"]
verb = ["runs", "jumps", "climbs", "sings"]
det = ["the", "a", "my", "each"]
adj = ["scary", "silly", "big", "small"]
question_mark = ["?"]
period = ["."]
exclamation_mark = ["!"]
prepositions = ["of", "to", "by", "in"]
comma = [","]
wp = ["who", "what", "where", "when", "whose"]

fsa1 = {
  'S':{0:'A'},
  'A':{0:'B', 'Accept':'Accept'}, 
  'B':{1:'A'}
}

fsa2 = {
  'S':{1:'A'},
  'A':{0:'B', '0':'D', 'Accept':'Accept'},
  'B':{1:'C'},
  'C':{1:'A'},
  'D':{0:'D', 'Accept':'Accept'}
}

fsa3 = {

  'S':{'vowel': 'A', 'consonant': 'E'},
  'A':{'consonant': 'B'},
  'B':{'vowel':'D'},
  'C':{'vowel': 'D', 'Accept':'Accept'},
  'D':{'consonant': 'B', 'vowel': 'A', 'Accept':'Accept'},
  'E':{'vowel':'A'}

}

def word_gen(fsa):
  
  word=''
  current_state = 'S'
  current_states_keys = list(fsa['S'].keys())
  choose_key = current_states_keys[randint(0, len(current_states_keys)-1)]

  
  #start state = fsa[0]
  #choose item in dictionary, then append to word and go to that item. 
  if choose_key == 'vowel':
    list_of_letters = vowels
  if choose_key == 'consonant':
    list_of_letters = consonants

  next_letter = None 


  #loop over this
  while next_letter != 'Accept':
    next_letter = list_of_letters[randint(0, len(list_of_letters)-1)]
    current_state = fsa[current_state][choose_key]

    word += str(next_letter)

    current_states_keys = list(fsa[current_state].keys())
    choose_key = current_states_keys[randint(0, len(current_states_keys)-1)]

    if choose_key == 'vowel':
      list_of_letters = vowels
    if choose_key == 'consonant':
      list_of_letters = consonants
    if choose_key == 'Accept':
      print(" ", word, " ")
      return
    


def main():
  # gen(fsa1)
  # gen(fsa2)
  word_gen(fsa3)

if __name__ == "__main__":
  main()
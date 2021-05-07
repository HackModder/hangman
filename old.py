import random

class RepeatError(Exception):
  pass

class Hangman():
  def __init__(self, player_name):
    self.player = player_name
  def word_for_print(self, current_word, open_char):
    print_word = ""
    for each in current_word:
      if each not in open_char and each != " ":
        current_word = current_word.replace(each,"_")
    for i in range(len(current_word)):
      print_word += current_word[i] + " "
    return print_word
  def hang_counter(self, missed_guess_counter):
    if missed_guess_counter == 0:
      return ("""
      ________
      |      |
      |      
      |    
      |      
      |     
      |""")
    elif missed_guess_counter == 1:
      return ("""
      ________
      |      |
      |      O
      |    
      |      
      |     
      |""")
    elif missed_guess_counter == 2:
      return ("""
      ________
      |      |
      |      O
      |      |
      |      
      |     
      |""")
    elif missed_guess_counter == 3:
      return ("""
      ________
      |      |
      |      O
      |     \|
      |      
      |     
      |""")
    elif missed_guess_counter == 4:
      return ("""
      ________
      |      |
      |      O  -- Easy Easy
      |     \|/    Careful..
      |      
      |     
      |""")
    elif missed_guess_counter == 5:
      return ("""
      ________
      |      |
      |      O  -- Are you nuts!
      |     \|/    I'm dying here!
      |      |
      |     
      |""")
    elif missed_guess_counter == 6:
      return ("""
      ________
      |      |
      |      O  -- WTF!
      |     \|/    Ur next wrong guess kills me :(
      |      |
      |     /
      |""")
    elif missed_guess_counter == 7:
      return ("""
      ________
      |      |
      |      O  -- Aaahhh Aarrghh arghh..
      |     \|/    (✖╭╮✖)   
      |      |
      |     / \\
      |

      G A M E  O V E R""")
  def print_status(self, missed_guess_counter, current_word, open_char, missed_char, remaining_char_count):
    print(self.hang_counter(missed_guess_counter))
    if missed_guess_counter < 7 and remaining_char_count > 0:
      print("\n",self.word_for_print(current_word, open_char))
      missed_char_string = ""
      if len(missed_char) > 0:
        for each in missed_char:
          missed_char_string += each + " "
        print("\nWrong Guesses: " + missed_char_string)
    elif missed_guess_counter < 7 and remaining_char_count == 0:
      print("\n",self.word_for_print(current_word, open_char))
      print("\nGreat! You've saved one more life!")
    else:
      print("\nIt was -->",current_word)

  def guess(self, current_word, current_word_nospace, guess, open_char, missed_char, missed_guess_counter, remaining_char_count):
    if guess.upper() in current_word_nospace:
      open_char.append(guess.upper())
      remaining_char_count -= current_word_nospace.count(guess)
      self.print_status(missed_guess_counter, current_word, open_char, missed_char, remaining_char_count)
      return missed_guess_counter, open_char, missed_char, remaining_char_count
    else:
      missed_char.append(guess.upper())
      missed_guess_counter += 1
      self.print_status(missed_guess_counter, current_word, open_char, missed_char, remaining_char_count)
      return missed_guess_counter, open_char, missed_char, remaining_char_count
    
  
  def word_picker(self, currentlist):
    picked_word = ""
    picked_word = random.choice(currentlist)
    currentlist.remove(picked_word)
    return picked_word, currentlist





# #welcome and ask for name
# print("Welcome to Hangman - COVID version")
# name = input("Enter your name\n")

# #display rules of the games
# print("\nHey " + name + "!\nHere are the rules of the game:")

# #take input for genre
# genre = input("\nChoose a genre out of 1, 2\n")




right_guess_remarks = [["Amazing!",""], ["You're great!",""], ["I already love you",""], ["I think I'm gonna live",""], ["You're the savior!",""], ["Great, keep it up",""], ["Comeon! You can do it!",""], ["Wonderful darling :-*",""], ["Yay yay yayyyy",""]]

wrong_guess_remarks = [["Easy Easy","Careful.."],["Are you nuts!","I'm dying here!"],["It feels like","You're gonna kill me"], [":(","You're good for nothing"],["Oye","Do you really want to kill me?"],["Comeon","Get your guesses right!"],["I think I should","start thinking of my last wish"],["It may be a game for you","But for me, it's my life!"],["Hey God..","Here I come"]]

megalist1 = ["Bollywood Movies","Jodhaa Akbar", "Gully Boy", "Sholay", "Hum Saath Saath Hain"]
megalist2 = ["Tourist Places","Eiffel Tower", "Statue of Liberty", "Machu Pichu", "Vivekanand Memorial", "The Gateway of India"]


genre = 1
if genre == 1: currentlist = megalist1
elif genre == 2: currentlist = megalist2

# open_char = ['L','Y']
# missed_char = ['K','S']

#hanmang init
hangu = Hangman("mansi")


while True:
  picked_word, currentlist = hangu.word_picker(currentlist)
  current_word = picked_word.upper()
  current_word_nospace = current_word.replace(" ","")
  open_char = []
  missed_char = []
  missed_guess_counter = 0
  remaining_char_count = len(current_word_nospace)
  while missed_guess_counter < 7 and remaining_char_count > 0:
    while True:
      try:
        guess = input("\nGuess a letter --> ")
        if guess.upper() in open_char or guess.upper() in missed_char:
          raise RepeatError
        break
      except RepeatError:
        print("You've already guessed this earlier.")
    missed_guess_counter, open_char, missed_char, remaining_char_count = hangu.guess(current_word, current_word_nospace, guess, open_char, missed_char, missed_guess_counter, remaining_char_count)
  
  playagain = input("\nPlay Again? Y/N --> ")
  if playagain == 'n' or 'N':
    break
  else: continue
  
  









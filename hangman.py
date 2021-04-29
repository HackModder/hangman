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
  def print_status(self, missed_guess_counter, current_word, open_char, missed_char):
    print(self.hang_counter(missed_guess_counter))
    print("\n",self.word_for_print(current_word, open_char))
    missed_char_string = ""
    for each in missed_char:
      missed_char_string += each + " "
    print("\nWrong Guesses: " + missed_char_string)
  def guess(self, current_word_nospace, guess)


# #welcome and ask for name
# print("Welcome to Hangman - COVID version")
# name = input("Enter your name\n")

# #display rules of the games
# print("\nHey " + name + "!\nHere are the rules of the game:")

# #take input for genre
# genre = input("\nChoose a genre out of 1, 2, 3, 4\n")

#hangman display
hangu = Hangman("mansi")


list1 = ["Bollywood Movies","Jodhaa Akbar", "Gully Boy", "Sholay", "Hum Saath Saath Hain"]
current_word = list1[2].upper()
current_word_nospace = current_word.replace(" ","")

open_char = ['L','Y']
missed_char = ['K','S']



# guess = input("\nGuess a letter --> ")
# if guess.upper() in current_word_nospace:
#   print("Correct")
#   open_char.append(guess)
#   print(open_char)
# else:
#   print("Wrong")
#   missed_char.append(guess)
#   print(missed_char)

# exit = False

hangu.print_status(3, "GULLY BOY", ['L','Y'], ['K','S'])




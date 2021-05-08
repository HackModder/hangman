import random

class Hangman:
  def __init__(self, player_name):
    self.player_name = player_name
    self.right_guess_remarks = [["-- Amazing!",""], ["-- You're great!",self.player_name + "is great!"], ["-- I already love you",self.player_name], ["-- I think I'm gonna live",""], ["-- You're the savior!",""], ["-- Great, keep it up",""], ["-- Comeon! You can do it!",""], ["-- Wonderful darling :-*",""], ["-- Yay yay yayyyy",""]]
    self.wrong_guess_remarks = [["-- Easy Easy","Careful.."],["-- Are you nuts!","I'm dying here!"],["-- It feels like","You're gonna kill me"], ["-- :(","You're good for nothing"],["-- " + self.player_name + "!!!","Do you really want to kill me?"],["-- Comeon","Get your guesses right!"],["-- I think I should","start thinking of my last wish"],["-- It may be a game for you","But for me, it's my life!"],["-- Hey God..","Here I come"]]
    self.secondlast_wrong_guess_remarks = [["-- Sob sob! Last guess...","I think my life is about to end :("],["-- You M*******!!","Now you just have 1 guess left"]]
    self.secondlast_right_guess_remarks = [["-- Oooohh", "Good good.."], ["-- Nice" + self.player_name,"Keep going slowly like this"], ["-- Goooood Yes", "Come on!"]]

  def hangman_pic(self, wrong_guess_counter, guess_type):
    message = ["",""]
    pic = ""
    if wrong_guess_counter == 0 and guess_type == "first":
      message = ["-- Let's","Begin!"]
    elif wrong_guess_counter < 5 and guess_type == "correct":
      message = random.choice(self.right_guess_remarks)
    elif wrong_guess_counter < 5 and guess_type == "incorrect":
      message = random.choice(self.wrong_guess_remarks)
    elif wrong_guess_counter == 5 and guess_type == "correct":
      message = random.choice(self.secondlast_right_guess_remarks)
    elif wrong_guess_counter == 5 and guess_type == "incorrect":
      message = random.choice(self.secondlast_wrong_guess_remarks)
    
    if wrong_guess_counter == 0:
      pic = """
      ________
      |      |
      |      O  """ + message[0] + """
      |            """ + message[1] + """
      |      
      |     
      |"""
    elif wrong_guess_counter == 1:
      pic = """
      ________
      |      |
      |      O  """ + message[0] + """
      |      |     """ + message[1] + """
      |      
      |     
      |"""
    elif wrong_guess_counter == 2:
      pic = """
      ________
      |      |
      |      O  """ + message[0] + """
      |     \|     """ + message[1] + """
      |      
      |     
      |"""
    elif wrong_guess_counter == 3:
      pic = """
      ________
      |      |
      |      O  """ + message[0] + """
      |     \|/    """ + message[1] + """
      |      
      |     
      |"""
    elif wrong_guess_counter == 4:
      pic = """
      ________
      |      |
      |      O  """ + message[0] + """
      |     \|/    """ + message[1] + """
      |      |
      |     
      |"""
    elif wrong_guess_counter == 5:
      pic = """
      ________
      |      |
      |      O  """ + message[0] + """
      |     \|/    """ + message[1] + """
      |      |
      |     /
      |"""
    elif wrong_guess_counter == 6:
      pic = """
      ________
      |      |
      |      O  -- Aaarghh gghhh ghh..
      |     \|/    (✖╭╮✖) 
      |      |     DEAD!
      |     / \\
      |"""
    return pic

  def guess_word(self, current_word, open_letters):
    to_print = "      "
    for each in current_word:
      if each in open_letters:
        to_print += each + " "
      else:
        to_print += "_ "
    return to_print
  
  def print_response(self, current_word, open_letters, wrong_guess_counter, guess_type):
    print(self.hangman_pic(wrong_guess_counter, guess_type))
    print("")
    print(self.guess_word(current_word, open_letters))
  






# hangu = Hangman("mansi")
# hangu.print_response("GULLY BOY", ['L','Y','O'], 4, "correct")
    
    
  


# print("Welcome to Hangman")
# player_name = input("What's your' name?\n")
# print("Here are the rules of the game,",player_name)
# print("#Rules of the game")
# genre = input("Which genre would you like to play?\n")



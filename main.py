import random

class InputError(Exception):
  pass

class RepeatError(Exception):
  pass

class Hangman:
  def __init__(self, player_name):
    self.player_name = player_name
    self.right_guess_remarks = [["-- Amazing!",""], ["-- You're great!",self.player_name + " is great!"], ["-- I already love you",self.player_name], ["-- I think I'm gonna live",""], ["-- You're the savior!",""], ["-- Great, keep it up",""], ["-- Comeon! You can do it!",""], ["-- Wonderful darling :-*",""], ["-- Yay yay yayyyy",""]]
    self.wrong_guess_remarks = [["-- Easy Easy","Careful.."],["-- Are you nuts!","I'm dying here!"],["-- It feels like","You're gonna kill me"], ["-- :(","You're good for nothing"],["-- " + self.player_name + "!!!","Do you really want to kill me?"],["-- Comeon","Get your guesses right!"],["-- I think I should","start thinking of my last wish"],["-- It may be a game for you","But for me, it's my life!"],["-- Hey God..","Here I come"]]
    self.secondlast_wrong_guess_remarks = [["-- Sob sob! Last guess...","I think my life is about to end :("],["-- You M*******!!","Now you just have 1 guess left"]]
    self.secondlast_right_guess_remarks = [["-- Oooohh", "Good good.."], ["-- Nice" + self.player_name,"Keep going slowly like this"], ["-- Goooood Yes", "Come on!"]]

    self.megalist = [[1, 2, 3], ["Famous Bollywood Movies", "JODHAA AKBAR", "SHOLAY", "HUM SAATH SAATH HAIN", "3 IDIOTS","ABCD","AE DIL HAI MUSHKIL","AGNEEPATH","AIRLIFT","BAAGHI","BABY","BADHAAI HO","BADLA","BADRINATH KI DULHANIA","BAJIRAO MASTANI","BAJRANGI BHAIJAAN","BALA","BANG BANG!","BARFI!","BATLA HOUSE","BHAAG MILKHA BHAAG","BHARAT","BODYGUARD","BOL BACHCHAN","CHENNAI EXPRESS","CHHICHHORE","DABANGG","DANGAL","DE DE PYAAR DE","DHOOM","DILWALE","DREAM GIRL","EK THA TIGER","EK VILLAIN","GHAJINI","GOLD","GOLIYON KI RAASLEELA RAM-LEELA","GOLMAAL","GOLMAAL AGAIN","GOOD NEWWZ","GRAND MASTI","GULLY BOY","HAPPY NEW YEAR","HOLIDAY","HOUSEFULL","JAB TAK HAI JAAN","JAI HO","JOLLY LLB","KAABIL","KABIR SINGH","KESARI","KICK","LUKA CHUPPI","MANIKARNIKA THE QUEEN OF JHANSI","MISSION MANGAL","PADMAAVAT","PK","PREM RATAN DHAN PAYO","RAAJNEETI","RAAZI","RACE","RAEES","RAID","READY","ROWDY RATHORE","RUSTOM","SAAHO","SANJU","SHIVAAY","SIMMBA","SINGH IS BLING","SINGHAM","SINGHAM RETURNS","SON OF SARDAAR","SONU KE TITU KI SWEETY","STREE","SULTAN","TALAASH","TANHAJI","TANU WEDS MANU RETURNS","THUGS OF HINDOSTAN","TIGER ZINDA HAI","TOILET EK PREM KATHA","TOTAL DHAMAAL","TUBELIGHT","URI THE SURGICAL STRIKE","WAR","WELCOME BACK","YEH JAWAANI HAI DEEWANI","ZERO","ZINDAGI NA MILEGI DOBARA"], ["Famous Tourist Places", "GREAT WALL OF CHINA","PETRA","CHRIST THE REDEEMER","MACHU PICCHU","CHICHEN ITZA","COLOSSEUM","GREAT PYRAMID","AGRA FORT","AJANTA CAVES","ELEPHANTA CAVES","ELLORA CAVES","FATEHPUR SIKRI","HAMPI","HUMAYUN TOMB","JANTAR MANTAR","KAZIRANGA NATIONAL PARK","KHAJURAHO","QUTB MINAR","RED FORT","SUN TEMPLE","SUNDARBANS","EIFFEL TOWER","STATUE OF LIBERTY","VIVEKANAND MEMORIAL","THE GATEWAY OF INDIA","TAJ MAHAL"],["Famous Hollywood Movies","ALADDIN","ALICE IN WONDERLAND","AQUAMAN","AVATAR","AVENGERS AGE OF ULTRON","AVENGERS ENDGAME","AVENGERS INFINITY WAR","BEAUTY AND THE BEAST","BLACK PANTHER","CAPTAIN AMERICA CIVIL WAR","CAPTAIN MARVEL","DESPICABLE ME","FINDING DORY","FROZEN","HARRY POTTER AND THE DEATHLY HALLOWS","INCREDIBLES","IRON MAN","JOKER","JURASSIC WORLD","MINIONS","PIRATES OF THE CARIBBEAN","SKYFALL","SPIDER-MAN: FAR FROM HOME","STAR WARS","THE AVENGERS","THE DARK KNIGHT","THE DARK KNIGHT RISES","THE FATE OF THE FURIOUS","THE HOBBIT","THE LION KING","THE LORD OF THE RINGS","TITANIC","TOY STORY","TRANSFORMERS","ZOOTOPIA"]]

    #megalist is a list of lists. The first list of megalist contains the index of all other lists - starting from 1. The rest of the items of megalist are lists - with index zero item as the name of the genre, and rest of the items are words from that genre.

    

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
      elif each == " ":
        to_print += "  "
      else:
        to_print += "_ "
    return to_print
  
  def print_response(self, current_word, open_letters, wrong_guess_counter, guess_type):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(self.hangman_pic(wrong_guess_counter, guess_type))
    print("")
    print(self.guess_word(current_word, open_letters))
  
  def choose_genre(self):
    #this method will ask the user to choose from a list of genres. When the user chooses one, the method will return the list of words from the chosen genre.

    genre_options = ""
    for each in self.megalist[0]:
      genre_options += str(each) + " - " + str(self.megalist[each][0]) + "\n"
  
    choice = 0
    while choice not in self.megalist[0]:
      while True:
        try:
          choice = int(input("\nChoose a category:\n" + genre_options + "Enter a number\n"))
          break
        except ValueError:
          print("\nERROR! Please enter a valid number")

    return self.megalist[choice][1:]

  def choose_word(self, current_list, used_words):
    for each in used_words:
      if each in current_list: current_list.remove(each)
    current_word = random.choice(current_list)
    used_words.append(current_word)
    return current_word, current_list, used_words
  
  def input_guess(self, open_letters, missed_guesses):
    while True:
      try:
        guess = input("\nGuess a letter --> ")
        if guess.upper() in open_letters or guess.upper() in missed_guesses:
          raise RepeatError
        elif not len(guess) == 1:
          raise InputError
        else: break
      except RepeatError:
        print("\nERROR! You've already guessed this earlier")
      except InputError:
        print("\nERROR! Enter a single letter please.\n")
    return guess.upper()
  
  def end_of_word_input(self):
    while True:
      try:
        next = int(input("\n1 - Same Category\n2 - Change Category\n3 - Exit Game\nEnter your choice:\n"))
        if (next in [1,2,3]) == False:
          raise InputError
        else:
          break
      except ValueError:
        print("\nERROR! Enter a valid number")
      except InputError:
        print("\nERROR!")
    return next
  
 
  def check_guess(self, current_word, guess, open_letters, missed_guesses):
    guess_type = ""
    if guess in current_word:
      guess_type = "correct"
      open_letters.append(guess)
    else:
      guess_type = "incorrect"
      missed_guesses.append(guess)
    return guess_type, open_letters, missed_guesses


print("""
 _   _   ___   _   _ _____ ___  ___  ___   _   _ 
| | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
| |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |
|  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
| | | || | | || |\  | |_\ \| |  | || | | || |\  |
\_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/
""")
print("Welcome to Hangman")
player_name = input("\nWhat's your' name?\n").upper()
hangu = Hangman(player_name)
print("\nHere are the rules of the game,",player_name)
print("\n> This is guessing game.\n> You will be guessing either movie names, or tourist places.\n> For each movie/place you will have 6 wrong guesses.\n> If you make 6 wrong guesses, a man will be hanged!\n> Try to guess correctly to save men from being hanged.\n\nWhich category you'd like to play?")
lives_saved = 0
killed = 0

game_is_active = True
used_words = []

while game_is_active:
  current_list = hangu.choose_genre()
  print("\nLet's Start!\n")
  genre_is_active = True

  while genre_is_active:
    current_word, current_list, used_words = hangu.choose_word(current_list, used_words)

    guess_type = "first"
    word_is_active = True

    open_letters = []
    missed_guesses = []
    wrong_guess_counter = 0

    while word_is_active:

      remaining_char = hangu.guess_word(current_word, open_letters).count("_")

      wrong_guess_counter = len(missed_guesses)

      # os.system('cls')

      hangu.print_response(current_word, open_letters, wrong_guess_counter, guess_type)

      if wrong_guess_counter > 0:
        wrong_guesses_string = ""
        for each in missed_guesses:
          wrong_guesses_string += each + " "
        print("\n      Missed Guesses: ", wrong_guesses_string)
      
      if wrong_guess_counter == 6 or remaining_char == 0:
        if wrong_guess_counter == 6:
          killed += 1
          print("\n      G A M E  O V E R ! Man Dead!\n      It was:", current_word, "\n\nPLAY AGAIN?")
        else:
          lives_saved += 1
          print("\n      AMAAYYZEEEEENGGG!!!!\n      You saved a life!\n\nPLAY AGAIN?")  
        next = hangu.end_of_word_input()
        word_is_active = False
        if next == 1:
          continue
        elif next == 2:
          genre_is_active = False
          continue
        elif next == 3:
          genre_is_active = False
          game_is_active = False
          continue

      guess = hangu.input_guess(open_letters, missed_guesses)

      guess_type, open_letters, missed_guesses = hangu.check_guess(current_word, guess, open_letters, missed_guesses)

print("\n\n\nHope you had a good time in\nKILLING",killed,":)\n& SAVING", lives_saved, "lives :(\n\n\n\n")







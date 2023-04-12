import random

story1 = "Nothing happens, the Garage is quiet and its dark and silent."
story2 = """
---------------------------------------------------------------------------------------------------------------
        You decline the man assistance and then out of the shadows steps the executioner to hang him. 
        
        You scream "No ill help" and the excutioner vanishes in a puff of smoke. 
        
                Pick Your next action:
        ***********************************
        1) Start the Puzzle.
        ***********************************
"""
wronganswer = """
---------------------------------------------------------------------------------------------------------------
        "Noooooooo" the man screams as an executioner steps forward, releasing the latch and hanging the man. 
        
"""
instructions = """
---------------------------------------------------------------------------------------------------------------
        "Ok so this games a little different, because if you save me, youll save yourself. I have the last key.
        but if you lose we both die. No matter how many lives you have! (dont ask me i dont make the rules)"
        
        "Ps. if you win, ive heard theyll give you an extra life, not sure why when youre so close to the end!"
        
        "ok so we're going to play hang man, ironic eh? So you need to guess a letter at the time, but theyre
        only giving you 6 guesses, our lives are in your hands. you ready?"
        
"""
correctanswer = """
---------------------------------------------------------------------------------------------------------------
        "Woooooo! You won!" the man jumps and as he does he releases the latch, hanging himself in the process.
        
        You run over to help, but the man is already dead.
        
        A key drops from his hands, a key in the shape of a triangle. You put it in your pocket.
        
        
                                         .___,             |-|
                                        /    |\____________| | 
                                        |()  | ____________  |
                                        \    |/            | |
                                         `---'             |_|
                                         
        You turn and leave the room.        
"""

class puzzleRoom2:
    def __init__(self):
        self.description = """
        ***********************************PUZZLE ROOM TWO ***********************************
        The room is large, and seemed to mimic the outdoors and in the middle of the 
        'courtyard' is a large gallow. In the middle is a man with a bag over his head, 
        standing just below a rope with a noose on the end.
                             ___________.._______
                            | .__________))______|
                            | | / /      ||
                            | |/ /       ||
                            | | /        ||
                            | |/         @@@@@
                            | |         @@@@@@@ 
                            | |         @@@@@@@ 
                            | |         .=====.
                            | |        /Y . . Y|
                            | |       // |   | \|
                            | |      //  | . |  \|
                            | |     ')   |   |   (`
                            | |          ||'||
                            | |          || ||
                            | |          || ||
                            | |          || ||
                            | |         / | | -
                            |::::::::::I=========I:::|
                            |:|''                '|:|
                            | |                   | |
                            : :                   : : 
        
        With a whisper the man speaks.
        "Traveller please help me, i am about to be hung for crime i did not commit, will you
        help me?"
        **************************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Scream YES.
        2) Politley decline.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            # list of words to choose from
            word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']

            # choose a random word from the list
            word = random.choice(word_list)

            # create a set of the unique letters in the word
            letters = set(word)

            # create a dictionary to store the number of incorrect guesses for each letter
            incorrect_guesses = {}

            # initialize the display string with underscores for each letter in the word
            display_string = '_' * len(word)

            # keep track of the number of incorrect guesses
            num_incorrect_guesses = 0
            print(instructions)
            ready = input("<Press ENTER when youre ready>")
            while '_' in display_string and num_incorrect_guesses < 6:
                # print the current state of the game
                print('Word:', display_string)
                print('Incorrect guesses:', incorrect_guesses)
                print('Guesses left:', 6 - num_incorrect_guesses)
                print('')

                # get a guess from the player
                guess = input('Guess a letter: ').lower()

                # check if the guess is valid (i.e. a single letter)
                if len(guess) != 1 or not guess.isalpha():
                    print('Invalid guess! Please enter a single letter.')
                    continue

                # check if the guess has already been made
                if guess in incorrect_guesses or guess in display_string:
                    print('You already guessed that letter! Try again.')
                    continue

                # check if the guess is in the word
                if guess in letters:
                    # update the display string with the new letter
                    for i, letter in enumerate(word):
                        if letter == guess:
                            display_string = display_string[:i] + guess + display_string[i+1:]

                else:
                    # add the letter to the incorrect_guesses dictionary and increment the number of incorrect guesses
                    incorrect_guesses[guess] = incorrect_guesses.get(guess, 0) + 1
                    num_incorrect_guesses += 1

            # print the final state of the game
            if '_' not in display_string:
                print('You win! The word was', word)
                print(correctanswer)
                game.lives += 1
                print ("Lives left:", game.lives)
                game.keys['triangleKey'] = 'Y'
                game.puzzlecomplete['Puzzle2'] = 'Y'
                return 'Upstairs Hall'
            else:
                print('You lose! The word was', word)
                print(wronganswer)
                return 'End Game Death'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
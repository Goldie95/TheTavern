story1 = "Nothing happens, the Garage is quiet and its dark and silent."
story2 = "You try to open the garage door but it doesnt budge, looks like its seized shut."
door1 = "You suxessfully open the door to your left revealing another room."
instructions = """
---------------------------------------------------------------------------------------------------------------
        "You will get 5 questions, if you answer more answers wrong than the amount fo lives you have left,
        you wil perish! But you you left with lives, you will be relased from this prison."
        
        "Good Luck Traveller"
"""
success = """
---------------------------------------------------------------------------------------------------------------
        "Bah, you have won me. I applaud your attention to detail traveller. You may pass, enjoy your stay."
        
        Halothane Junior vanished.
"""
fail = """
---------------------------------------------------------------------------------------------------------------
        "Bahahaha, you have been defated. You will feel my wrath."
        
        "GoodBye Traveller"
"""

class endGamePuzzle:
    def __init__(self):
        self.description = """
        *********************************** END GAME PUZZLE ***********************************
        You step out of the gate and find that youre on the street you were in before you
        entered the tavern, but it seemed to be clouded in a dark fog, you cant see more than 
        a metre in front of you, a figure walks out of the fog.
        
                                                dS$$S$S$S$S$S$S$$Sb                    
                                               :$$S^S$S$S$S$S$S^S$$;                   
                                               SSP   `^$S$S$^'   TSS                   
                                               $$       `"'       $$                   
                                              _SS ,-           -  SS_                  
                                             :-.|  _    - .-   _  |.-;                 
                                              :\(; ' "-._.'._.-" ` |)/;                 
                                              \`|  , O       O .  |'/                  
                                               ":     -'   `-     ;"                   
                                                ;.              :                 
                                                 : `    ._.    ' ;                     
                                               .sSb   ._____.   dSs.                   
                                            _.d8dSSb.   ._.   .SSbT8b._                
                                        _.oOPd88SSSS T.     .P SSSS888OOo.             
                                    _.mMMOOPd888SSSSb TSqqqSP dSSSS88OMOOOMm._         
                                .oOMMMOMOOM8O8OSSSSSb TSSSP dSSSSS8OOMMOOMMOOOo._     
                              .OOMMOOOMMOOMOOOO  "^SSSTSSP dSSS^"OOOOMMOOMMMOOMMMb.   
                              dOOOMMMOMMOOOMOOOO      "^SSSS^"   :OOO8MMMOOMMOOMMOMMb  
                             :MMMOOMMOMMOOMMO8OS         `P      8O8OPdMMOOMMOMMOMMMM; 
                             MMMMOOMMMMMOOMbTO8S;               :8888MMMMMOMMOMMOMMMMM 
                             OMMMMOOMMMMOOOMMOOOS        S     :O8OPdMOMMMOMOMMOOMMMMO 
                            :OMMMMOOMMOMMOOMbTObTb.     :S;   .PdOPdMOOMMMMMOMMOMMMMMO;
                            MOOMMMMOMMOMMOOMMMOObTSSg._.SSS._.PdOPdMOOMMMMOMMMMOMMMMOOM
                            MMOMMMMOMMMOMMOOMMbT8bTSSSSSSSSSPd8OPdOOOMMMMOOMMMMOMMMOOMM
                            MMOMMMOMMMMMOMMOOMMMbT8bTSSSSSPd88PdOOOOMMMMOOMMMMMMMMOOMMM
        
        "Well done Traveller" the man says, his voice in a harsh and evil whisper. "I am 
        Halothane Junior, yes yes, im the one who set you this challenge. You havent gotten
        away so easily. See i wanted to set up a challange for every traveller that entered
        my tavern, im sick of rude customers thinking they can walk all over me. So for your
        final challenge, i will ask you a series of questions about your time in the tavern.
        Lets see if youve actually been taking interest in my business or if you thought you
        could cheat your way through."
        ***************************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Start the challenge.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            questions = [
                {
                    'question': 'What colour was door number 2 in the updatirs hallway?',
                    'options': ['Blue', 'Green', 'Yellow', 'Red'],
                    'answer': 'Green'
                },
                {
                    'question': 'What was the name of my doll, in the first room?',
                    'options': ['Mindy', 'Anabelle', 'Lucy', 'Mia'],
                    'answer': 'Lucy'
                },
                {
                    'question': 'What dead animal watches over the taverns snug?',
                    'options': ['Wolf', 'Bear', 'Stag', 'gazelle'],
                    'answer': 'Bear'
                },
                {
                    'question': 'What was the surname of the Jack in the box?',
                    'options': ['Halfpenny', 'Simba', 'Borgin', 'Symbone'],
                    'answer': 'Symbone'
                },
                {
                    'question': 'How many points were on the star in the photo in my fathers bedroom?',
                    'options': ['5', '6', '7', '8'],
                    'answer': '8'
                }
            ]

            score = 0

            print(instructions)

            for i, question in enumerate(questions):
                print(f'Question {i+1}: {question["question"]}')
                for j, option in enumerate(question["options"]):
                    print(f'{j+1}. {option}')
                user_answer = input('\nEnter your answer (1-4): ')
                if user_answer == str(question['options'].index(question['answer']) + 1):
                    print('Correct!\n')
                    score += 1
                else:
                    print('Incorrect!\n')
                    game.lives -= 1

            print(f'Quiz complete! You scored {score}/{len(questions)}')
            if game.lives <= 0:
                print(fail)
                return 'End Game Death'
            else:
                print(success)
                return 'End Game Complete' 
        elif action == "stats":
            return 'stats'
        else:
            return None
        
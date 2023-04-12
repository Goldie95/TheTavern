story1 = """
---------------------------------------------------------------------------------------------------------------
        You search the Snug but theres nothing of interest, though the bears head seems interesting. 
        Maybe you could investigate that.
"""
story2 = """
---------------------------------------------------------------------------------------------------------------
        You grab a chair, pull it over to the bears head and stand up until youre face to face with the grizzly.
        Theres nothing of interest on the outside but when you look inside the mouth you see a peice of 
        parchment sticking out from one of this back teeth.
        
        You pull out the parchment, unroll it and read:
          ______________________________
        / \                             \.
        |   |                            |.
         \_ |                            |.
            | I know im either dead or   |.
            | i have escaped this place  |.
            | but if youve found this    |.
            | note youre looking in the  |.
            | right places. The code you |.
            | seek is hidden in a riddle |.
            | inside the juniors room    |.
            | but to make it easy i      |.
            | thought id give it to you  |.
            | straight, the code is EIGHT|.
            WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
            
        The note ends abruptly, it seems the parhment was torn and seems like drops of blood stain the eges.
        
        You place the note back in its place, incase anyone else could use the note.
        
        Pick Your next action:
        ***********************************
        1) Search the Snug for clues.
        3) Go back into the Tavern Mess Hall.
        ***********************************
"""
story3 = """
---------------------------------------------------------------------------------------------------------------
        You climb back up to the bears head and take back out the note.

          ______________________________
        / \                             \.
        |   |                            |.
         \_ |                            |.
            | I know im either dead or   |.
            | i have escaped this place  |.
            | but if youve found this    |.
            | note youre looking in the  |.
            | right places. The code you |.
            | seek is hidden in a riddle |.
            | inside the juniors room    |.
            | but to make it easy i      |.
            | thought id give it to you  |.
            | straight, the code is ONE, |.
            WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
            
        The note ends abruptly, it seems the parhment was torn and seems like drops of blood stain the eges.
        
        You place the note back in its place, incase anyone else could use the note.
        
        Pick Your next action:
        ***********************************
        1) Search the Snug for clues.
        3) Go back into the Tavern Mess Hall.
        ***********************************
        
"""
door1 = "You walk back into the Tavern Hall."

class tavernSnug:
    def __init__(self):
        self.description = """
        *********************************** TAVERN SNUG ***********************************
        The snug has a fireplace on the eastern wall, roaring and keeping the snug warm.
        You see a round table big enough to host a large meeting and above the the table on
        the northern wall hung a larger taxidermied bears head in mid roar. 
        ***********************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Search the Snug for clues.
        2) Investigate the bear head on the wall.
        3) Go back into the Tavern Mess Hall.
        ***********************************
        
        """
        
        self.story = ""
        self.bearheadcount = 0

        

    def perform_action(self, game, action):
        if action == '1':
            self.story = story1
            return 'story'
        elif action == '2':
            if self.bearheadcount < 1:
                    self.story = story2
                    self.bearheadcount += 1
                    return 'story'
            else:
                self.story = story3
                return 'story'
        elif action == '3':
            print (door1)
            return 'Tavern Hall'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
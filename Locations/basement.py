story1 = """
---------------------------------------------------------------------------------------------------------------
        The only thing to search is the old barrels. Most of which are empty, the last one you search contains 
        a skeleton, you see its holding a torn peice of parchment and open it up, it reads:
        
             /\/\/\/|
            | FOUR, >
            |       >
            | Good L> 
            |      >
             WWWWWW>
             
        Seems like its been torn from a larger peice of parchment.
        Pick Your next action:
        ***********************************3
        
        2) Go back up to the kitchen.
        ***********************************

"""
door1 = "You walk back up the stairs to the kitchen."

class basement:
    def __init__(self):
        self.description = """
        *********************************** BASEMENT ***********************************
        The Basement is dark but a single candle lit the square damp room. The room is 
        empty other than a few rotting barrels and a few metal pots. 
        ********************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Search the basement.
        2) Go back up to the kitchen.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            self.story = story1
            return 'story'
        elif action == '2':
            print (door1)
            return 'Kitchen'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
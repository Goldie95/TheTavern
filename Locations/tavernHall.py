story1 = """
---------------------------------------------------------------------------------------------------------------
        You search the room from top to bottom, under the tables and around the fireplace on the western wall. Theres
        nothing of use in here, you may have to search more of the tavern.
        
        Pick Your next action:
        ***********************************
        2) Go to the Bar Area.
        3) Walk up the stairs.
        4) Go into the taverns snug.
        ***********************************
"""
door1 = """
---------------------------------------------------------------------------------------------------------------
        You walk over to the bar and leap over it.
"""
door2 = """
---------------------------------------------------------------------------------------------------------------
        You start creeping up the stairs, they wind left upwards.
"""
door3 = """
---------------------------------------------------------------------------------------------------------------
        You walk through a small archway to the east.
"""

class tavernHall:
    def __init__(self):
        self.description = """
        *********************************** TAVERN MESS HALL ***********************************
                    
        To the North of the Hall is the bar, with a curtain drawn shut behind it, which you think may lead somehwere. To the
        east you see a stairway that must lead upstairs and beyond that it seems another room, maybe a 
        tavern snug of somekind. You see there is a banister above you, which you assume the stairway will
        take you, but cannot see whats beyond the banister. The western wall there is a fireplace.

        ****************************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Search the tavern hall for clues.
        2) Go to the Bar Area.
        3) Walk up the stairs.
        4) Go into the taverns snug.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            self.story = story1
            return 'story'
        elif action == '2':
            print (door1)
            return 'Bar Area'
        elif action == '3':
            print (door2)
            return 'Upstairs Hall'
        elif action == '4':
            print (door3)
            return 'Tavern Snug'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
story1 = """
---------------------------------------------------------------------------------------------------------------
        The heater has a dial and as you turn it a flame ignites, however this flame isnt usual, it flickers an
        unusual yellow and blue. You look aroudn the greenhouse and see it started to mist and water droplets
        have started to form on the glass. 
        
        You see an arrow formed in an area where condensation seems to have not affected the glass,pointing 
        towards a patch of dirt. You grab the spade and begin to dig and find an old bottle and a peice of
        parchment inside. You remove the cork stopper from the bottle and read:
        
            "THREE. Luck traveller."
        
        There was also another note, that seems to have been scribbled in red ink, probably blood in addition
        to the orginal note.
        
            "I've had to hide the last clue in here, i think hes on to me, but how can we escape with the clue
            destroyed? I cant tell you where the rest of the code is, i fear he may find them."
            
        You place the note back into the bottle and bury it again, it seems more than just yourself have been in
        this place. 
        
        You turn off the heater. 
        
        Pick Your next action:
        ***********************************
        2) Try digging around the greenhouse.
        3) Back back into the East yard.
        ***********************************
        
"""
story2 = """
---------------------------------------------------------------------------------------------------------------
        You grab the spade and dig in several places, but theres no sign of anything. You may need to find a 
        specific place to dig. 
        
        Pick Your next action:
        ***********************************
        1) Investigate the heater.
        3) Back back into the East yard.
        ***********************************
"""
door1 = "You exit the greenhouse."

class greenHouse:
    def __init__(self):
        self.description = """
        *********************************** GREENHOUSE ***********************************
        The greenhouse is small and shades of  green is reflected through the opaque glass.
        There is pots and piles of dirt everywhere, though someone has been rummaging 
        through here. 
        
        You see a small parafin heater on a bench and a small hand shovel placed next to it.
        **********************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Investigate the heater.
        2) Try digging around the greenhouse.
        3) Back back into the East yard.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            self.story = story1
            return 'story'
        elif action == '2':
            self.story = story2
            return 'story'
        elif action == '3':
            print (door1)
            return 'diningRoom'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
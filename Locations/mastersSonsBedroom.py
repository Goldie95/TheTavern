story1 = """
---------------------------------------------------------------------------------------------------------------
        Theres nothing worth noting about the room, the cage is birdless and the drawers it sits on are empty.
        Shifting the books doesnt do anything, they just seem to crumble. The bed has no mattress, theres no
        chance of nay sleep in here. 
        
        Pick Your next action:
        ***********************************
        2) Investigate the book.
        3) Go back into the kitchen.
        ***********************************
"""
story2 = """
---------------------------------------------------------------------------------------------------------------
        You go to pick up the book, but it seems the back cover has been bolted to the desk. the title on the 
        spine reads "MY DIARY", the rest of the cover is a faint green fabirc.
        
        You open the book to find a very boring and mundane diary, it includes snippets such as:
        
            "Helped father with the shopping today, so yet another boring day."
        
            "Mr Symbone was rather rude today, think i might slip him a sleeping pill in his mead."
        
            "Why is my father obssesed with keeping people happy? escpecially when the guests are so arrogant."
        
        The rest of the book is empty after around half way through apart form the last page. A sentence that 
        was written in dark red ink, probably dried blood. It reads:
        
            "The last clue is in the greenhouse, i buried it, i hope they dont see me doing this, good luck."
        
        You close the book.
        
        Pick Your next action:
        ***********************************
        1) Search the room further.
        3) Go back into the kitchen.
        ***********************************
"""
door1 = "You open the door and walk back into the kitchen, closing the door behind you."

class mastersSonsBedroom:
    def __init__(self):
        self.description = """
        *********************************** HALOTHANE JNR BEDROOM ***********************************
        This room is dark and dingy, a small bed sit in the corner, the room feels cold. Theres some
        drawers in the corner and an old brass bird cage sitting on top. There is a book shelf, with
        a lot of books, but they seem to have been eaten by some sort of mite. 
        
        Theres a book you notice that hasnt been touched by mites, sitting upon the desk. 
        *********************************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Search the room further.
        2) Investigate the book.
        3) Go back into the kitchen.
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
            return 'Kitchen'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
story1 = """
---------------------------------------------------------------------------------------------------------------
        You search the room, including the cabinet, but all you find is dust. The bed has no mattress, so 
        that rules out any sleep.
        
        Pick Your next action:
        ***********************************
        2) Investigate the jewellry box.
        3) Investigate the picture.
        4) Leave the room, into the kitchen.
        ***********************************
"""
story2 = """
---------------------------------------------------------------------------------------------------------------
        You reach for the jewellry box and open it. The box contains a small wooden tablet, with a message
        inscribed upon it.
        
        /-----------/
        / SORRY,THE /
        / CLUE WAS  /
        / DESTROYED /
        /___________/
            
        You put the wooden tablet back into the jewellry box and place it back upon the shelf. 
        
        Pick Your next action:
        ***********************************
        1) Search the Room for clues.
        3) Investigate the picture.
        4) Leave the room, into the kitchen.
        ***********************************

"""
story3 = """
---------------------------------------------------------------------------------------------------------------
        What does this picture mean? You try to move it off the wall but its glued tight up against it. You
        look at the images. The abstarct shapes must mean something? 
        ._______.
        |       |
        | ✴ ■ ▲ |
        |_______|
        
        Pick Your next action:
        ***********************************
        1) Search the Room for clues.
        2) Investigate the jewellry box.
        4) Leave the room, into the kitchen.
        ***********************************

"""
door1 = "You open the door and leave the room."

class masterBedroom:
    def __init__(self):
        self.description = """
        *********************************** HALOTHANE SNR BEDROOM ***********************************
        The room seems brighter than the rest of the tavern, you look around and see a small bed, a
        cabinet and a desk. Above the desk it a large picture in an old frame. In the frame is a 
        picture of an 8 pointed star, a square and a triangle lined up in a row.
        
        There was a small shelf below the frame, where stood a small jewelry box, it seems to have
        been wipied clean, there was no dust on the object. 
        ********************************************************************************************* 
        
        Pick Your next action:
        ***********************************
        1) Search the Room for clues.
        2) Investigate the jewellry box.
        3) Investigate the picture.
        4) Leave the room, into the kitchen.
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
            self.story = story3
            return 'story'
        elif action == '4':
            print (door1)
            return 'Kitchen'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
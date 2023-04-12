
story1 = """
---------------------------------------------------------------------------------------------------------------
        You search the kitchen and there is no food. You turn the tap at the sink, but nothing happens.
        Theres nothing worth noting in the kitchen, but the lock on the door to the outside looks odd, 
        the keyhole isnt a typical keyhole, but int he shape of a 8 pointed star.
        
        Pick Your next action:
        ***********************************
        2) Go down to the basement.
        3) Try the door to the north that leads outside again.
        4) Open the north door in the nook.
        5) Open the south door in the nook.
        6) Go to the bar area.
        ***********************************
"""
door1 = """
---------------------------------------------------------------------------------------------------------------
        You start walking down the steps.
"""
door2 = """
---------------------------------------------------------------------------------------------------------------
        You use the key you obtaned earlier, it slides in and unlocks the door. It opens on its own acccord.
"""
story2 = """
---------------------------------------------------------------------------------------------------------------
        You need a key to open this door.The lock on the door looks odd, the keyhole isnt a typical keyhole, but int 
        the shape of a 8 pointed star.

        Pick Your next action:
        ***********************************
        1) Search the Kitchen for Clues.
        2) Go down to the basement.
        3) Try the door to the north that leads outside again.
        4) Open the north door in the nook.
        5) Open the south door in the nook.
        6) Go to the bar area.
        ***********************************
"""
door3 = """
---------------------------------------------------------------------------------------------------------------
        You open the door and enter the room.
"""
door4 = """
---------------------------------------------------------------------------------------------------------------
        You open the door and enter the room.
"""
door5 = """
---------------------------------------------------------------------------------------------------------------
        You go back through the red curtains, drawing them shut behind you.
"""
lockedoorstory = """
---------------------------------------------------------------------------------------------------------------
        The door is locked. You need a key to open it.

        Pick Your next action:
        ***********************************
        1) Search the Kitchen for Clues.
        2) Go down to the basement.
        3) Open the door to the north that leads outside.
        4) Open the north door in the nook.
        5) Open the south door in the nook.
        6) Go to the bar area.
        ***********************************
"""

class kitchen:
    def __init__(self):
        self.description = """
        *********************************** KITCHEN ***********************************
        To the west you see a stairway, that leads down a dark passage you assume is a basement. The the right of the 
        stairway is a butcher block with a knife pretuding it. Along the wall follows a kitchenette and sink area. To
        the north is a door that seems to lead outdoors, the door seems to have 1 keyhole. 
        
        To the east is a small nook which leads to two doors, one leading north and the other leading south. The northern
        door has a plate that reads 'Halothane Senior' and the otherto the south had a similar plate that reads
        'Halothane Jnr'.
        ******************************************************************************* 
        
        Pick Your next action:
        ***********************************
        1) Search the Kitchen for Clues.
        2) Go down to the basement.
        3) Open the door to the north that leads outside.
        4) Open the north door in the nook.
        5) Open the south door in the nook.
        6) Go to the bar area.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            self.story = story1
            return 'story'
        elif action == '2':
            print (door1)
            return 'basement'
# I need this section to unlock the door if they have the key (self.key (star key = Y))
        elif action == '3':
            if game.keys['starKey'] == 'Y':
                print (door2)
                return 'Yard North'
            else:
                self.story = lockedoorstory
                return 'story'
        elif action == '4':
            print (door3)
            return 'Masters Bedroom'
        elif action == '5':
            print (door4)
            return 'Masters Sons Bedroom'
        elif action == '6':
            print (door5)
            return 'Bar Area'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
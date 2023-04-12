story1 = """
---------------------------------------------------------------------------------------------------------------
        You search the yard but theres nothing of interest, the greenhouse may be interesting. You see the 
        keyhole is a funny shape like the last one. Maybe another puzzle will grant me a key to open this?
        
        Pick Your next action:
        ***********************************
        2) Go into the greenhouse.
        3) Open the gate.
        4) Go back to the northern yard.
        ***********************************
"""
door1 = "You open the greenhouse door and step inside."
door2 = "You push in the triangle key and the gate swings open."
door3 = "You walk back to the northern yard."
lockedoorstory = """
---------------------------------------------------------------------------------------------------------------
        The gate is locked, you need a key to open this.
        
        Pick Your next action:
        ***********************************
        1) Search the Yard.
        2) Go into the greenhouse.
        4) Go back to the northern yard.
        ***********************************
        
"""

class yardEast:
    def __init__(self):
        self.description = """
        *********************************** YARD EAST ***********************************
        The eastern yard contains a intricate greenhouse, which you reliase its green
        glass is almost opaque, the door is slightly adjar. To the east of the yard is a 
        gate exiting the yard, though it seems to have the same strange lock mechanism
        as the door to the northern yard.
        
        The eastern yard is still blocked by a large wooden wall, the only way out it 
        seems is through the gate.
        *********************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Search the Yard.
        2) Go into the greenhouse.
        3) Open the gate.
        4) Go back to the northern yard.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            self.story = story1
            return 'story'
        elif action == '2':
            print (door1)
            return 'Greenhouse'
        elif action == '3':
            if game.keys['triangleKey'] == 'Y':
                print (door2)
                return 'End Game Puzzle'
            else:
                self.story = lockedoorstory
                return 'story'
        elif action == '4':
            print (door3)
            return 'Yard North'    
        elif action == "stats":
            return 'stats'
        else:
            return None
        
story1 = """
---------------------------------------------------------------------------------------------------------------
You search the North Yard and find nothing. Its muddy and derelict. Theres an empty barrel falling to peices, 
rotten to the eat of the yard. Beyond that you see the eastern yard.

        Pick Your next action:
        ***********************************
        2) Go to the eatern yard.
        3) Go back into the kitchen.
        ***********************************

"""
door1 = "You walk to the east into the the yard east of the tavern."
door2 = "You go through the door to the kitchen."

class yardNorth:
    def __init__(self):
        self.description = """
        *********************************** YARD NORTH ***********************************
        The yard is enclosed in a tall wooden fence, almost three times as tall as you 
        and topped with razor wire. There isnt much that you can see thats worth any
        interest, but there seems to be a yard to the east, on the east side of the
        tavern.
        **********************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Search the northern yard.
        2) Go to the eatern yard.
        3) Go back into the kitchen.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            self.story = story1
            return 'story'
        elif action == '2':
            print (door1)
            return 'Yard East'
        elif action == '3':
            print (door2)
            return 'Kitchen'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
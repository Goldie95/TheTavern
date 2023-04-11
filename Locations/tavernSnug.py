story1 = "Nothing happens, the Garage is quiet and its dark and silent."
story2 = "You try to open the garage door but it doesnt budge, looks like its seized shut."
door1 = "You suxessfully open the door to your left revealing another room."

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
        
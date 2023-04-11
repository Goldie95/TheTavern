story1 = "Nothing happens, the Garage is quiet and its dark and silent."
story2 = "You try to open the garage door but it doesnt budge, looks like its seized shut."
door1 = "You suxessfully open the door to your left revealing another room."

class puzzleRoom2:
    def __init__(self):
        self.description = """
        You are in a dark Garage you look around and there isnt much to see. Yooy do however see a light seeping
        through the door to your left. You c an also see the outline of the garage door hehind you lit by moon light.
        
        Pick Your next action:
        1) Do Nothing.
        2) Try the garage door.
        3) Try and open the door on your left.
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
        
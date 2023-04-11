

class endGameDeath:
    def __init__(self):
        self.description = """
        A ghostly figure rises through the floor in front of you and you feel your soul leaving your body until.
        
        YOU ARE DEAD.
        
        Thank you for playing.
        
        Enter 'q' to quit the game.
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == 'q':
            return None
        else:
            return None
        
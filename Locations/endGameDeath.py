

class endGameDeath:
    def __init__(self):
        self.description = """
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        A ghostly figure rises through the floor in front of you and you feel your soul leaving your body until.
        
        YOU ARE DEAD.
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        
        Thank you for playing.
        
        Enter 'q' to quit the game.
        """
        
        self.story = ""

        3

    def perform_action(self, game, action):
        if action == 'q':
            return None
        else:
            return None
        
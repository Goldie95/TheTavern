door1 = """
---------------------------------------------------------------------------------------------------------------
        You drawn the curtains to reveal another archway and see another room, you walk through and candles light
        up on their own revealing the room.
"""
door2 = """
---------------------------------------------------------------------------------------------------------------
        You Jump back over the bar.
"""

class barArea:
    def __init__(self):
        self.description = """
        *********************************** BAR AREA ***********************************
        
        The bar in empty, aside from a few empty beer horns and clay mugs. The shalves are lined with dust
        and the only thing worth investigating is a deep red curtain that is drawn shut. It seems to be
        concealing another archway.
        
        ********************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Open the curtains.
        2) Jump back over the bar, back to the Tavern Hall.
        ***********************************
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == '1':
            print (door1)
            return 'Kitchen'
        elif action == '2':
            print (door2)
            return 'Tavern Hall'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
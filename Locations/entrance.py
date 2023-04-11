story1 = """
---------------------------------------------------------------------------------------------------------------
        You hear the singing much louder and seems like a normal tavern. You cant make anything out other than drunken
        singing and the strumming of what seems to be a Lute playing a fast paced drinking jig.
    
        ***********************************
        Pick Your next action:
        2) Peer through the stained glass window to the side of the taverns doors.
        3) Enter the tavern.
        ***********************************
"""
story2 = """
---------------------------------------------------------------------------------------------------------------
        You peer through the stained glass windows, its bright but the window distorts the images in the tavern. 
        You can make out drinkers dancing and the ficker of a large fire to the left. It looks warm and inviting.

        ***********************************
        Pick Your next action:
        1) Press your ear to the door and listen in.
        3) Enter the tavern.
        ***********************************
"""
door1 = """
---------------------------------------------------------------------------------------------------------------
        
        You push open the Taverns entrance doors and enter the tavern to find its completley empty! The Doors slam shut
        behind you and you hear the lock seal your exit. Suddenly the candles and fire light up in flame, exposing 
        a large room.

        There is no sound of the lute and no sign of life. What has just happened? 
                
        You look around and see that the place has been deserted for maybe years. Dust convered the tables
        and it smelled like a mixture of damp and dust. 

        The mess hall of the tavern was as tall as it was wide. Large open ceiling and a large iron chandelier
        swining from the eaves, lit by small candles lit the dusty wooden beams above your head.

        A deep cracking voice rose up through the floors of the tavern and vibrated through your mind;

        'Welcome to the Halothane Tavern, you have entered looking for warmth and food but first you must
        complete my trial. In this tavern i have hidden 3 keys, all of which are secured and guarded
        by challanges. You have 3 chances at completing the challanges, if you fail, you will perish in
        this taven, locked forever in this souless darkness. Good Luck traveller.'
"""

class entrance:
    def __init__(self):
        self.description = """
        *********************************** START OF GAME ***********************************
        
        The Tavern stood, towering above your head in the misty darkness. Candle Light flickered through the
        stained glass windows and the hustle and bustle of drinkers and minstrels singing to a tune
        echoed through the air to the sound of stringed instruments. You feel your stomach rumble and decide
        that this Tavern is the best oppertunity to get food and rest for the night. The sign above the door read
        "The Halothane Tavern" and underneath, swining in the breeze was another sing that read "Vacancies".
        
        *************************************************************************************
        
        Pick Your next action:
        ***********************************
        1) Press your ear to the door and listen in.
        2) Peer through the stained glass window to the side of the taverns doors.
        3) Enter the tavern.
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
            return 'Tavern Hall'
        elif action == "stats":
            return 'stats'
        else:
            return None
        
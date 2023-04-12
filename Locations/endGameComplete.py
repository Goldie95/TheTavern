

class endGameComplete:
    def __init__(self):
        self.description = """
        You walk down the street and find everything back to normal, the door to the tavern is open and 
        you enter to demand the owner explains themselves. The drunken folk are still singing and 
        dancing. You recognise it familiarity as you walk towards the bar. You demand you speak to 
        Mr Halothane. The Barman raises his eyebrows,
        
        "Mr Halothane? Ah you must mean becuase of the name outside. No, Mr Halthone has been dead 
        for many years son. Im the owner now, have been for about 15 years. Kept the name because it
        was well know."
        
        You stare at the inn keeper and look around, it seemed strange to see it so full of light. 
        
        "What happened to Mr Halothane?" You ask the man.
        
        "Ah well theres many theories, but some say he went mad, hung his own father, poisened a 
        regular customer and then suffocated his own daughter with her dolly. But you know rumours
        ey. No, i think he just died a regular old man, though it wasnt here, he was long gone 
        before i bought this place. They say he just vanished, along with his family. I think he
        ran out of money, this place was a right mess when i bought it."
        
        You try to think of whats just happened and try to make out if youd just dreamed it, did you
        pass out on the floor outdoor. 
        
        "How about a room traveller? Got some hot stew bubbling over the fire, over there."
        
        You shake your head and give thanks. You decide you arent so tired and hungry afterall,
        at least not until you reach the next tavern. 
        
        ████████ ██   ██ ███████     ███████ ███    ██ ██████  
           ██    ██   ██ ██          ██      ████   ██ ██   ██ 
           ██    ███████ █████       █████   ██ ██  ██ ██   ██ 
           ██    ██   ██ ██          ██      ██  ██ ██ ██   ██ 
           ██    ██   ██ ███████     ███████ ██   ████ ██████
           
           Thanks for playing.
           
           'q' and ENTER to quit.
        """
        
        self.story = ""

        

    def perform_action(self, game, action):
        if action == 'q':
            return None
        else:
            return None
        
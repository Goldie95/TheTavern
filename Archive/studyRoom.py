story1 = """
You inspect every aspect of the bear for a speaker or some sort of device and find nothing. Until you check the bears open mouth
and find a rolled up not inside that reads, "To whomeevr finds this note, DO NOT enter the door witht he tred cross, i ahve covered
it in my blood to warn others. Also the answer to the bears question is.........." The not ends smeared in blood and the rest is 
unreadable. You roll it back up and place it back into the bears mouth.
"""
story2 = "You try to open the garage door but it doesnt budge, looks like its seized shut."
door1 = "You suxessfully open the door to your left revealing another room."
numberGuess = ""

class studyRoom:
    def __init__(self):
        self.description = """
        The dining room is large and in the centre of the room is a large dining table. In the corner there is a large taxidermied brown bear
        actioning a visicious growl. There is a white door to your left and on the right is a nother white door but this one has a red 'X' 
        painted acrross it in what looks like red paint. A voice suddenly echoes from the bear, "Push the button beneath my stare and answer
        the questions if you dare. If you answer correctly you you gain a key, if not ill take a life from thee."
        
        Pick Your next action:
        1) Inspect the bear.
        2) Try the door on your Left.
        3) Try the door on your Right.
        4) Push the button on the stand beneath the bear.
    
        """
        
        self.story = ""
        self.puzzleResult = False
        self.puzzleCount = 0

    def diningRoom_puzzle(self):
        if self.puzzleResult == False:
            print("Enter Number 5")
            numberGuess = input("> ")
            if numberGuess == "5":
                self.puzzleResult = True
            else:
                self.puzzleResult = False
        self.puzzleCount +=1 

    def perform_action(self, game, action):
        if action == '1':
            self.story = story1
            return 'story'
        elif action == '2':
            print (door1)
            return "kitchenClosetSideRoom"
        elif action == '3':
            print (door2)
            return 'studyRoom'
        elif action =="4":
            diningRoom.diningRoom_puzzle(self)
            return 'puzzleAttempt'
        else:
            return None
        
    
        
    
        
        
#Import the Rooms
import Locations.entrance
import Locations.tavernHall
import Locations.tavernSnug
import Locations.barArea
import Locations.kitchen
import Locations.masterBedroom
import Locations.mastersSonsBedroom
import Locations.yardNorth
import Locations.yardEast
import Locations.greenHouse
import Locations.upstairsHall
import Locations.puzzleRoom1
import Locations.puzzleRoom2
import Locations.puzzleRoom3
import Locations.basement
import Locations.endGameDeath
        
class Game:
    def __init__(self):
        self.lives = 3
        self.keys = {
            'starKey': 'N',
            'triangleKey': 'N',
            'squareKey': 'N',
        }
        self.name = None
        self.rooms = {
            'Entrance': Locations.entrance.entrance(),
            'Tavern Hall': Locations.tavernHall.tavernHall(),
            'Tavern Snug': Locations.tavernSnug.tavernSnug(),
            'Bar Area': Locations.barArea.barArea(),
            'Kitchen': Locations.kitchen.kitchen(),
            'Master Bedroom': Locations.masterBedroom.masterBedroom(),
            'Masters Sons Bedroom': Locations.mastersSonsBedroom.mastersSonsBedroom(),
            'Yard North': Locations.yardNorth.yardNorth(),
            'Yard East': Locations.yardEast.yardEast(),
            'Greenhouse': Locations.greenHouse.greenHouse(),
            'Upstairs Hall': Locations.upstairsHall.upstairsHall(),
            'Puzzle Room One': Locations.puzzleRoom1.puzzleRoom1(),
            'Puzzle Room Two': Locations.puzzleRoom2.puzzleRoom2(),
            'Puzzle Room Three': Locations.puzzleRoom3.puzzleRoom3(),
            'Basement': Locations.basement.basement(),
            'End Game Death': Locations.endGameDeath.endGameDeath(),
        }
        self.current_room = 'Entrance'
        self.just_entered = True

    def start_menu(self):
            welcome = """
            ************************************************************************************
            * ████████ ██   ██ ███████     ████████  █████  ██    ██ ███████ ██████  ███    ██ *     
            *    ██    ██   ██ ██             ██    ██   ██ ██    ██ ██      ██   ██ ████   ██ *    
            *    ██    ███████ █████          ██    ███████ ██    ██ █████   ██████  ██ ██  ██ *    
            *    ██    ██   ██ ██             ██    ██   ██  ██  ██  ██      ██   ██ ██  ██ ██ *    
            *    ██    ██   ██ ███████        ██    ██   ██   ████   ███████ ██   ██ ██   ████ * 
            ************************************************************************************

                              _   _._
                             |_|-'_~_`-._
                          _.-'-_~_-~_-~-_`-._
                      _.-'_~-_~-_-~-_~_~-_~-_`-._
                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                       |  []  []   []   []  [] |
                       |           __    ___   |   
                     ._|  []  []  | .|  [___]  |_._._._._._._._._._._._._._._._._.  
                     |=|________()|__|()_______|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=| 
                   ^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
                                      Created by: Louis Goldsbrough
                                      
                                         Please select an option:
            
                           1|START GAME          2|INSTRUCTIONS           3|QUIT
            """
            print(welcome)
            option = input("> ")

            if option == '1':
                self.name = input("Enter your name: ")
                self.play()
            elif option == '2':
                print("""Instructions:
                      This game will provide a mixture of story telling and puzzles to solve. Instructions
                      will be provided to you throughout the game.
                      
                      To access your stats at any time, simply type 'stats' into the command line and hit enter.
                      
                      To quit the game simply type 'q' into the command line and hit enter.
                    
                      """)
                instruction_choice = input("Would you like to play? (Y/N): ")
                
                if instruction_choice == "Y".lower:
                     self.name = input("Enter your name: ")
                     self.play()
                elif instruction_choice == "N".lower:
                    exit()              
            elif option == '3': 
                exit()
            else:
                print("Invalid option. Please try again.")
                self.start_menu()
    
    def track_keys(self, key):
            if key in self.keys:
                if self.keys[key] == 'N':
                    self.keys[key] = 'Y'
                    print("You found a {}!".format(key))
                else:
                    print("You already have the {} key.".format(key))
            else:
                print("Invalid key.")

    def play(self):
            while True:
                room = self.rooms[self.current_room]
                if self.just_entered:
                    print(room.description)
                    self.just_entered = False
                action = input("> ")
                if action == 'q':
                    break
                result = room.perform_action(self, action)
                # Descriptive Story
                if result == 'story':
                    print(room.story)
                # Puzzle Attempt    
                elif result == 'puzzleAttempt':
                    print("LOG:",room.puzzleResult)
                    print("LOG:",room.puzzleCount)
                    if room.puzzleResult == True:
                        if room.puzzleCount > 1:
                            print ("You have already completed this puzzle.")
                        else:
                            print("Well done you completed the puzzle.")
                            self.keys +=1
                            print("You have gained an extra Key! you now have", self.keys, "Keys!")                        
                    else:
                        print("Incorrect.")
                        self.lives -= 1
                        print ("You now have",self.lives, "lives.")
                # Write Stats        
                elif result == 'stats':
                    print(self.name,"'s Currents Stats")
                    print("---------------")
                    print("Lives Left:", self.lives)
                    print("Keys Obtained:", self.keys)
                # Move Room        
                elif result in self.rooms:
                    self.current_room = result
                    self.just_entered = True
                    print("You moved to the {}.".format(self.current_room))
                else:
                    print("Invalid action.")

game = Game()
game.start_menu()
game.play()
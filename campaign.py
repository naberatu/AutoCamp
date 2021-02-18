from main import CELoop
class Campaign:

    def __init__(self, name, encs=list()):
        self.name = name
        self.encs = encs
        self.current_location = None # stored as encounter object
        self.playing = True

    def change_location(self):
        moving = True
        while moving:
            for location in self.encs:
                print("> {:<3}: {}".format(self.encs.index(location) + 1, location.name))
            next_location = input("> ")
            if next_location == "cancel":
                return False
            else:
                try:
                    next_location = int(next_location) - 1
                    if self.current_location == self.encs[next_location]:
                        print("[ER] You're already here! Please pick another location!")
                    elif 0 <= next_location < len(self.encs):
                        moving = False
                        if self.current_location is not None and not self.current_location.is_combat:
                            self.current_location.running_loop = False
                        self.current_location = self.encs[next_location]
                        return True
                except ValueError:
                    print(
                        "[ER] invalid input! Please select a new location by inputting a number or enter 'cancel' to return")
                except IndexError:
                    print(
                        "[ER] invalid input! Please select a valid location or enter 'cancel' to return")

    def run_campaign(self):
        while self.playing:
            print("Hello adventurer! Where would you like to go?")
            handled = self.change_location()
            if handled == "exit":
                exit()
            elif not handled:
                if self.current_location.is_shop:
                    self.current_location.vendLoop()
                elif not self.current_location.is_combat:
                    self.current_location.genLoop()
                else:
                    CELoop(self.current_location.currentEntity)
                continue
            elif self.current_location.is_shop:
                self.current_location.vendLoop()
            elif not self.current_location.is_combat:
                self.current_location.genLoop()
            else:
                CELoop(self.current_location.currentEntity)
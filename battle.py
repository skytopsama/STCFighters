import operator

class Battle(object):
    "object used to run a battle between two (or more) fighters"

    def __init__(self, fighter_list = []):
        self.fighters = fighter_list
        self.turn = 0
        #environment

    #introduce the fight
    def battle_intro(self):
        reply = "It's a battle!!!\n"
        for fighter in self.fighters:
            reply += fighter.name + "\n"
            #if fighter not last in list
            if fighter != self.fighters[-1]:
                reply += "\nVS\n\n"

    #increment turn
    def increment_turn(self):
        self.turn += 1
        reply = "Turn " + str(self.turn) + "\n"
    #check initiative (attack speed) function
    def check_fighter_initiative(self):
        fighter_order = []
        dex_list = [fighter.dex for fighter in self.fighters]
        fighter_initiative_dict = {k:v for k, v in zip(self.fighters, dex_list)}
        sorted_fighter_initiative = sorted(fighter_initiative_dict.items(), key=operator.itemgetter(1), reverse=True)
#         print(sorted_fighter_initiative)
        for fighter, initiative in sorted_fighter_initiative:
            fighter_order.append(fighter)
        return fighter_order

    def run(self):
        print(self.battle_intro())
        fighter_order = self.check_fighter_initiative()
        print(self.increment_turn())

    #per fighter per turn while fighter is alive (hp > 0):
        #check status
            #can fighter use a move?
        #player selects a move for fighter to use
        #move use is validated
            #can fighter use selected move?
                #if yes proceed
                #if no select a different move
        #fighter uses move
        #check all fighters status
            #all fighters alive?
    #^^^return to increment turn at top^^^

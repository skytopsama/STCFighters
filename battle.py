import operator

class Battle(object):
    "object used to run a battle between two (or more) fighters"

    def __init__(self):
        fighters = []
        turn = 0
        #environment
        
    #introduce the fight
    #increment turn
    #check initiative (attack speed) function
    def check_fighter_initiative(self):
        fighter_order = []
        dex_list = [fighter.dex for fighter in self.fighters]
        fighter_initiative_dict = {k:v for k, v in zip(self.fighters, dex_list)}
        sorted_fighter_initiative = sorted(fighter_initiative_dict.items(), key=operator.itemgetter(1), reverse=True)
        for fighter in sorted_fighter_initiative.keys():
            fighter_order.append(fighter)
        return fighter_order
    #per fighter per turn while fighter is alive (hp > 0):
        #check status
            #can fighter use a move?
        #fighter uses a move
    
            
    
        

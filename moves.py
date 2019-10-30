import random

### MOVE CLASS

class Move(object):
    "A Virtual Move. Can be used to influence different fighter attributes."
    fighter_move_list = []

    #Default Move initiation
    def __init__(self, name):
        #move info
        self.name = name
        self.move_type = "Default"
        self.hit_chance = 1.0
        self.hit_times = 1
        self.effects = []
        self.move_cost = {}
        self.move_changes = {}

        self.description = "None\n"
        self.hit_text = "Hit confirmed.\n"

        #initiation actions
        Move.fighter_move_list.append(self)

    #Default move string method
    def __str__(self):
        reply =  "\n" + self.name + "\n"
        reply +=  self.description + "\n"
        reply += "-" * 20 + "\n"
        reply += "Move type: " + str(self.move_type) + "\n"
        reply += "Hit%: " + str(self.hit_chance) + "\n"
        reply += "Hit Count: " + str(self.hit_times) + "\n"
        reply += "Cost:\n"
        for cost in self.move_cost.keys():
            reply += str(cost) + " : " + str(self.move_cost[cost]) + "\n"
        reply += "Target changes: \n"
        for change in self.move_changes.keys():
            reply += change + " : " + str(self.move_changes[change]) + "\n"
        for effect in self.effects:
            reply += effect  + "\n"
        return reply

    #reassign multiple move attributes
    def setup_move(self, **meta):
        self.name = meta.get('name', self.name)
        self.description = meta.get('description', self.description)
        self.move_type = meta.get('move_type', self.move_type)
        self.hit_chance = meta.get('hit_chance', self.hit_chance)
        self.hit_times = meta.get('hit_times', self.hit_times)
        self.effects = meta.get('effects', self.effects)
        self.move_cost = meta.get('move_cost', self.move_cost)
        self.move_changes = meta.get('move_changes', self.move_changes)

    #check if fighter can use a move
    def evaluate_move_cost(self, fighter):
        attr_changes = {}
        cost_dict = self.move_cost
        for cost_type in cost_dict.keys(): #what if there is no cost/multuple costs
            #if fighter stats/attributes is valid
            if hasattr(fighter, cost_type) is True:
                #once validated, check if there is enough
                selected_attr = getattr(fighter, cost_type)
                cost_amount = cost_dict[cost_type]
                if selected_attr >= cost_amount:
                    # add attribute and new amount to attr_changes dictionary
                    attr_changes[cost_type] = selected_attr - cost_amount
                #end process if fighter cannot pay cost
                else:
                    print("Not enough") #expand string later
                    break
            #end process if invalid attribute
            else:
                print(str(cost_type) + " is an invalid attribute.")
                break

        return attr_changes

    def ready_change_statement(self, attr_key, attr_value):
        reply = ""
        if type(attr_value) is int:
            #handle if pos or neg
            if attr_value > 0:
                reply += attr_key.upper() + " increased by " + str(abs(attr_value)) + ".\n"
            elif attr_value < 0:
                reply += attr_key.upper() + " decreased by " + str(abs(attr_value)) + ".\n"
            else:
                pass
        if type(attr_value) is str:
            reply += attr_key.upper() + " set to " + attr_value + ".\n"
        else:
            pass

        return reply

    #move method to execute itself from fighter to a target
    def execute(self, fighter, target):
        #check if fighter can pay cost of move
        attr_changes = self.evaluate_move_cost(fighter)
        #if attribute cost exist
        if len(attr_changes) > 0:
            ##print("Cost passed")
            #update fighter attributes with subtracted cost
            for cost_attr in attr_changes.keys():
                setattr(fighter, cost_attr, attr_changes[cost_attr])
                ##print(str(getattr(fighter, cost_attr)))

            #for moves that have multiple actions
            for time in range(self.hit_times):
                ##print("hit " + str(time))
                #if action is in hit chance
                roll = random.uniform(0,1)
                if self.hit_chance >= random.uniform(0,1):
                    ##print(str(self.hit_chance) + " > " + str(roll))
                    modded_attr_dict = self.move_changes
                    ##print(modded_attr_dict)
                    for modded_attr in modded_attr_dict.keys():
                        #if target stat/attribute is valid
                        ##print(modded_attr)
                        if hasattr(target, modded_attr) is True:
                            ##print(target.name + " has attr " + modded_attr)
                            #once validated, modify target's associated attr amount
                            current_stat = getattr(target, modded_attr)
                            setattr(target, modded_attr, current_stat + modded_attr_dict[modded_attr])
                            statement  = target.name + " " + self.ready_change_statement(modded_attr, modded_attr_dict[modded_attr])
                            print(statement)

                        #if target stat/attribute is not valid
                        else:
                            print("Invalid attribute")

                    #after move hits, chance for effect to activate should start
                    #for effect in effectdict.keys():
                        #if effect is valid:
                            #if effectdict[effect] <= random.uniform(1, 100):
                                #perform effect - how are effects performed though?

                #if action not in hit chance, end
                else:
                    print(fighter.name + " missed.\n")
        #if attribute cost do not exist
        else:
            print(fighter.name + " cannot execute " + self.name + " .\n")

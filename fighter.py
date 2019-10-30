###FIGHTER CLASS

class Fighter(object):
    "A Virtual Fighter"
    roster = []

#Default Fighter initiation

    def __init__(self, name):
        #personal info
        self.name = name

        #base stats
        self.max_hp = 100
        self.hp = self.max_hp
        self.max_sp = 100
        self.sp = self.max_sp
        self.max_mp = 100
        self.mp = self.max_mp

        #attributes
        self.base_con = 1
        self.con = self.base_con
        self.base_str = 1
        self.str = self.base_str
        self.base_int = 1
        self.int = self.base_int
        self.base_agi = 1
        self.agi = self.base_agi
        self.base_dex = 1
        self.dex = self.base_dex

        #attack set
        self.attacks = []
        #move set
        self.moves = []
        #equips - not designed yet
        #self.weapon=
        #self.armor=
        #current status
        self.status = "Normal"

        #initiation actions
        Fighter.roster.append(self)
        print(self.name, "is ready to fight!!!")

#Default fighter string method

    def __str__(self):
        reply =  "\n" + self.name + "\n"
        reply += "-" * 20 + "\n"
        reply += "Attributes\n"
        reply += "HP: " + str(self.max_hp) + "\n"
        reply += "SP: " + str(self.max_sp) + "\n"
        reply += "MP: " + str(self.max_mp) + "\n"
        reply += "CON: " + str(self.base_con) + "\n"
        reply += "STR: " + str(self.base_str) + "\n"
        reply += "INT " + str(self.base_int) + "\n"
        reply += "AGI: " + str(self.base_agi) + "\n"
        reply += "DEX: " + str(self.base_dex) + "\n"
        return reply


    #Method for getting current stats
    def current_stats(self):
        reply =  "\n" + self.name + "\n"
        reply += "-" * 20 + "\n"
        reply += "Attributes\n"
        reply += "HP: " + str(self.hp) + "\n"
        reply += "SP: " + str(self.sp) + "\n"
        reply += "MP: " + str(self.mp) + "\n"
        reply += "CON: " + str(self.con) + "\n"
        reply += "STR: " + str(self.str) + "\n"
        reply += "INT " + str(self.int) + "\n"
        reply += "AGI: " + str(self.agi) + "\n"
        reply += "DEX: " + str(self.dex) + "\n"
        print(reply)

#Stat relationship reset

    def update_base_stats(self):
        self.max_hp = 100 + 10*self.con #formula for hp should incorporate CON
        self.hp = self.max_hp
        self.max_sp = 100 + 10*self.agi#formula for hp should incorporate AGI
        self.sp = self.max_sp
        self.max_mp = 100 + 10*self.int#formula for hp should incorporate INT
        self.mp = self.max_mp

#Base Attribute change function

    def set_base_attrs(self, attr_dict):
        for attr in attr_dict.keys():
            if attr == "con":
                self.base_con = attr_dict[attr]
                self.con = self.base_con
            if attr == "str":
                self.base_str = attr_dict[attr]
                self.str = self.base_str
            if attr == "int":
                self.base_int = attr_dict[attr]
                self.int = self.base_int
            if attr == "agi":
                self.base_agi = attr_dict[attr]
                self.agi = self.base_agi
            if attr == "dex":
                self.base_dex = attr_dict[attr]
                self.dex = self.base_dex
        self.update_base_stats()

#Current Attribute change function

    def set_attrs(self, attr_dict):
        for attr in attr_dict.keys():
            if attr == "con":
                self.con = attr_dict[attr]
            if attr == "str":
                self.str = attr_dict[attr]
            if attr == "int":
                self.int = attr_dict[attr]
            if attr == "agi":
                self.agi = attr_dict[attr]
            if attr == "dex":
                self.dex = attr_dict[attr]
            print(str(attr) + "modified by" + attr_dict[attr])
        self.update_base_stats()

#Current Attribute reset function

    def reset_current_attr_to_base(self):
        self.con = self.base_con
        self.str = self.base_str
        self.int = self.base_int
        self.agi = self.base_agi
        self.dex = self.base_dex

    #check if fighter can use a move (rewrite as fighter method returning true or false)
    def can_use_move(self, move):
        #attr_changes = {}
        cost_dict = move.move_cost
        for cost_type in cost_dict.keys():
            #if fighter stats/attributes is valid
            if hasattr(self, cost_type) is True:
                #once validated, check if there is enough
                selected_attr = getattr(self, cost_type)
                cost_amount = cost_dict[cost_type]
                if selected_attr >= cost_amount:
                    # continue
                    continue
                #end process if fighter cannot pay cost
                else:
                    print("Not enough") #expand string later
                    return False
            #end process if invalid attribute
            else:
                print(str(cost_type) + " is an invalid attribute.")
                return False

        return True

    def use_move(self, move_name, target):
        #if move_name is equipped to fighter
            x = [move for move in self.moves if move.name == move_name]
            if len(x) == 1:
                #if fighter can use the move
                if self.can_use_move(x[0]):
                    #execute move
                    print(self.name +  " used " + x[0].name)
                    x[0].execute(self, target)
                else:
                    #reject use move (exception)
                    pass
            else:
                pass

            #execute move


# #Weapon change function

#     def change_weapon(self, newWeapon):
#         self.weapon = newWeapon

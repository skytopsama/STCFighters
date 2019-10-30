four = Fighter("4.0")
four.set_base_attrs({"con":10, "int":10, "str":8, "agi":11, "dex":12})

tula = Fighter("Tula")
tula.set_base_attrs({"con":11, "int":10, "str":14, "agi":9, "dex":10})

Blitz = Move('Blitz')
Blitz.setup_move(move_type = "Melee", hit_chance = 0.8, move_cost = {"sp":10}, move_changes = {'hp':-15})

four.moves = [Blitz]
four.use_move("Blitz", tula)

test = Battle([tula, four])
test.run()

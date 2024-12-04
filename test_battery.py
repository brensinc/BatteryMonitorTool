from battery import battery

battery1 = battery(3, 2, 1)

battery1.random_discharge(current_limit = 0.1, dashboard = True)

battery2 = battery(3, 2, 1)
battery2.constant_discharge(discharge_rate = 0.01, dashboard = True)
import numpy as np
import plotly.graph_objects as go
from status_monitor import monitor

class battery(object):
    def __init__(self, V_ocv, C_bat, soc, temp = 25):
        """
        self.V_ocv : 
        self.soc :
        self.C_bat : 
        self.R_s
        self.R
        """
        self.V_ocv = V_ocv
        self.C_bat = C_bat
        self.soc = soc
        self.temp = temp
   

    # Simple charge/discharge model without aging dynamics
    def discharge(self, I):
        self.soc += -(1/self.C_bat) * I

        if self.soc > 1:
            self.soc = 1
        elif self.soc < 0.2:
            self.soc = 0.2


    def random_discharge(self, time = 3600, current_limit = 0.1, notification_cooldown = 600, plot = True, dashboard = False):
        # Generate random charge/discharge sequence
        discharge_series_random = np.random.uniform(-current_limit, current_limit, time)
        battery_soc_random = []


        for discharge_step in discharge_series_random:
            self.discharge(discharge_step)
            battery_soc_random.append(self.soc)

        charge_monitor = monitor()
        charge_cooldown = notification_cooldown

        for soc in battery_soc_random:
            if soc <= 0.20 and not charge_cooldown:
                message = "🚨 Alert: Battery SOC Below 20%!"
                username = "SOC Bot"
                charge_monitor.send_discord_alert(message, username)
                charge_cooldown = notification_cooldown
            elif charge_cooldown > 0:
                charge_cooldown -= 1

        if plot:
            # Create the initial figure
            fig = go.Figure()

            # Add the SOC line
            fig.add_trace(go.Scatter(
                y=battery_soc_random, 
                mode='lines',
                name='Battery SOC',

            ))

            # Add the discharge series line
            fig.add_trace(go.Scatter(
                y=discharge_series_random, 
                mode='lines',
                name='Discharge Series',
                line=dict(color='red')  # Optional styling
            ))

            # Update layout with titles
            fig.update_layout(
                xaxis_title="Time (seconds)", 
                yaxis_title="SOC"
            )

            # Show the figure
            # fig.show()
        
        if dashboard:
            charge_monitor.dash_app(battery_soc_random, discharge_series_random)


    def constant_discharge(self, time = 3600, discharge_rate = 0.1, notification_cooldown = 600, plot = True, dashboard = False):
        # Generate constant charge/discharge sequence
        discharge_series_constant = [discharge_rate for i in range(time)]
        battery_soc_constant = []

        for discharge_step in discharge_series_constant:
            self.discharge(discharge_step)
            battery_soc_constant.append(self.soc)


        charge_monitor = monitor()
        charge_cooldown = notification_cooldown

        for soc in battery_soc_constant:
            if soc <= 0.20 and not charge_cooldown:
                message = "🚨 Alert: Battery SOC Below 20%!"
                username = "SOC Bot"
                charge_monitor.send_discord_alert(message, username)
                charge_cooldown = notification_cooldown
            elif charge_cooldown > 0:
                charge_cooldown -= 1

        if plot:
            # Create the initial figure
            fig = go.Figure()

            # Add the SOC line
            fig.add_trace(go.Scatter(
                y=battery_soc_constant, 
                mode='lines',
                name='Battery SOC'
            ))

            # Add the discharge series line
            fig.add_trace(go.Scatter(
                y=discharge_series_constant, 
                mode='lines',
                name='Discharge Series',
                line=dict(color='red')  # Optional styling
            ))

            # Update layout with titles
            fig.update_layout(
                xaxis_title="Time (seconds)", 
                yaxis_title="SOC"
            )

            # Show the figure
            # fig.show()

        if dashboard:
            charge_monitor.dash_app(battery_soc_constant, discharge_series_constant)


    ### WRITE CODE TO ENCORPORATE AGING DYNAMICS ###
            
    # def __init__(self, V_ocv, C_bat, soc, temp):
    #     """
    #     self.V_ocv : 
    #     self.soc :
    #     self.C_bat : 
    #     self.R_s
    #     self.R
    #     """
    #     self.V_ocv = V_ocv
    #     self.soc = soc
    #     self.C_bat = C_bat

    #     self.T_s = temp
    #     self.T_c = temp


    # def electrical_model(self, I):
    #     self.V = []
    #     self.R = __
    #     self.C = __

    #     if I >= 0:
    #         R_s = __
    #         R_u = __
    #         C_s = __

    #     else:
    #         R_s = __
    #         R_u = __
    #         C_s = __

    #     # Terminal voltage of electrical model
    #     V_t = self.V_ocv - I * R_s - sum(self.V)
        
    #     # Update soc of the battery
    #     self.soc += (-1/self.C_bat) * I
        
    #     # Update voltage drops of RC pairs
    #     self.V = [-1/(self.R[i] * self.C[i]) * self.V + (1/self.C[i]) * I for i in range(len(self.V))]
        

    # def thermal_model(self):
    #     Q = I * (self.V_ocv - V_t)

    #     self.T_c += Q/C_c + (self.T_s - self.T_c) / (self.R_c * self.C_c)
    #     self.T_s += (self.T_f - self.T_s) / (R_u * C_s) - (self.T_s - self.T_c) / (R_c * C_s)

import numpy as np
import plotly.graph_objects as go
from status_monitor import monitor
import matplotlib.pyplot as plt

class Battery:
    def __init__(self, capacity, initial_soc=100, initial_soh=100):
        # Battery parameters
        self.capacity = capacity
        self.soc = initial_soc
        self.soh = initial_soh

        # Equivalent circuit model parameters
        self.R0 = 0.05  
        self.R1_charge = 0.02 
        self.C1_charge = 1000  
        self.R2_charge = 0.05
        self.C2_charge = 5000 

        self.R1_discharge = 0.03  
        self.C1_discharge = 1200 
        self.R2_discharge = 0.06  
        self.C2_discharge = 5500  
        
        # Thermal parameters
        self.temperature = 25 

        # State variables for RC pairs
        self.V1 = 0  
        self.V2 = 0 

        # Voltage output
        self.voltage = 0

    def update_soc(self, current, duration):
        # Ah consumed = current (A) × time (hours)
        ah_consumed = current * (duration / 3600)
        self.soc -= (ah_consumed / self.capacity) * 100
        self.soc = max(0, min(100, self.soc)) 
        
    def equivalent_circuit_model(self, current, charge_mode=True):
        # Select parameters based on charge/discharge
        if charge_mode:
            R1, C1, R2, C2 = self.R1_charge, self.C1_charge, self.R2_charge, self.C2_charge
        else:
            R1, C1, R2, C2 = self.R1_discharge, self.C1_discharge, self.R2_discharge, self.C2_discharge

        # RC dynamics update
        tau1 = R1 * C1
        tau2 = R2 * C2

        self.V1 += (current / C1 - self.V1 / tau1)
        self.V2 += (current / C2 - self.V2 / tau2)

        # Calculate terminal voltage
        open_circuit_voltage = 3.7 + (self.soc / 100) * 0.5
        self.voltage = open_circuit_voltage - self.R0 * current - self.V1 - self.V2

    def simulate_step(self, current, charge_mode=True):
        # Simulate a single 1-second step
        self.update_soc(current, 1)
        self.equivalent_circuit_model(current, charge_mode)

    def run_simulation(self, current_profile, charge_mode_profile, dashboard=True, notification_cooldown=600):
        """
        Run an iterative simulation for a time-varying current profile.

        Parameters:
        - current_profile: List of currents (A) for each second.
        - charge_mode_profile: List of booleans indicating charge (True) or discharge (False).

        Returns:
        - results: A dictionary with time-series data for SOC, SOH, voltage, and temperature.
        """
        results = {
            "time": [],
            "soc": [],
            "soh": [],
            "voltage": [],
            "temperature": []
        }

        charge_monitor = monitor(notification_cooldown)
        

        for t, (current, charge_mode) in enumerate(zip(current_profile, charge_mode_profile)):
            self.simulate_step(current, charge_mode)
            results["time"].append(t)
            results["soc"].append(self.soc)
            results["soh"].append(self.soh)
            results["voltage"].append(self.voltage)
            results["temperature"].append(self.temperature)
            charge_monitor.check_soc(self.soc) # Check to see soc is above 20%

        if dashboard:
            charge_monitor.dash_app(results, current_profile)

        return results

    def __repr__(self):
        return (f"Battery(SOC={self.soc:.2f}%, SOH={self.soh:.2f}%, "
                f"Voltage={self.voltage:.2f}V, Temperature={self.temperature:.2f}°C)")
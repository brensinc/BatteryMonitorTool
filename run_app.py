from status_monitor import monitor
from battery import Battery
import pandas as pd
import numpy as np
import dash
from dash import dcc, html
import plotly.express as px

# Create battery instance
battery = Battery(capacity=2.6, initial_soc=100)

# Define a current profile
current_profile = [np.sin(i * np.pi/4) * 5 + 5 for i in range(3600)]
charge_mode_profile = [False if t % 2 == 0 else True for t in range(3600)]  # Alternate between charge and discharge

# Run the simulation
results = battery.run_simulation(current_profile, charge_mode_profile, dashboard = True, notification_cooldown=600)
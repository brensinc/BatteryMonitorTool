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
current_profile = [50 if t % 2 == 0 else -30 for t in range(3600)]  # Alternating currents
charge_mode_profile = [False if t % 2 == 0 else True for t in range(3600)]  # Alternate modes

# Run the simulation
results = battery.run_simulation(current_profile, charge_mode_profile, dashboard = True, notification_cooldown=600)
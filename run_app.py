from status_monitor import monitor
import pandas as pd
import numpy as np
import dash
from dash import dcc, html
import plotly.express as px

# Simulate 96 timesteps
data = pd.DataFrame({
    "time": pd.date_range(start="2024-01-01", periods=96, freq="H"),
    "voltage": np.random.uniform(3.5, 4.2, 96),
    "charge": np.random.uniform(20, 100, 96),
    "temperature": np.random.uniform(20, 40, 96),
})

charge_cooldown = False
temp_cooldown = False

monitor = monitor()

for index, row in data.iterrows():
    if row["charge"] < 20 and not charge_cooldown:
        message = "🚨 Alert: Battery SOC Below 20%!"
        username = "SOC Bot"
        monitor.send_discord_alert(message)
        charge_cooldown = True

    if row["temperature"] > 35 and not temp_cooldown:
        message = "🚨 Alert: Battery temperature Above 35 deg celcius!"
        username = "Temp bot"
        monitor.send_discord_alert(message)
        temp_cooldown = True



app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(
        id="voltage-chart",
        figure=px.line(data, x="time", y="voltage", title="Battery Voltage Over Time")
    ),
    dcc.Graph(
        id="charge-chart",
        figure=px.line(data, x="time", y="charge", title="Battery Charge Over Time")
    ),
    dcc.Graph(
        id="temperature-chart",
        figure=px.line(data, x="time", y="temperature", title="Battery Temperature Over Time")
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
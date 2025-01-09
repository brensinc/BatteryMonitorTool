import pandas as pd
import numpy as np
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests


class monitor(object):
    def __init__(self, notification_cooldown):
        self.notification_cooldown = notification_cooldown
        self.remaining_cooldown = notification_cooldown

    def check_soc(self, soc):
        if soc <= 0.20 and not self.remaining_cooldown:
                    message = "🚨 Alert: Battery SOC Below 20%!"
                    username = "SOC Bot"
                    self.send_discord_alert(message, username)
                    self.remaining_cooldown = self.notification_cooldown
        elif self.remaining_cooldown > 0:
            self.remaining_cooldown -= 1

    # As reading in battery data, send notification if SOC below 20%
    def send_discord_alert(self, message, username="Alert Bot", avatar_url=None):
        """
        Sends an alert to a Discord webhook.

        :param webhook_url: Discord webhook URL
        :param message: Message content for the alert
        :param username: Optional: Username to appear as the sender
        :param avatar_url: Optional: URL for the sender's avatar
        """

        webhook_url = "https://discord.com/api/webhooks/1312833846370242710/GCjXQufs558Toa_28wupSSpuaUg1G4J9SdOqpYljEAqQ-aqVeTsgPjJE89V--G3Kr2UA"

        payload = {
            "content": message,
            "username": username,
        }
        if avatar_url:
            payload["avatar_url"] = avatar_url
        try:
            response = requests.post(webhook_url, json=payload)
            response.raise_for_status()
            print(f"Message sent successfully: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send message: {e}. Check webhook_url.")

    def dash_app(self, results, current_profile):
    # Create the Dash app
        app = dash.Dash(__name__)

        # Define a single layout containing both graphs
        app.layout = html.Div([
            dcc.Graph(
                id="SOC-Current",
                figure=go.Figure(
                    data=[
                        go.Scatter(y=results["soc"], mode="lines", name="SOC"),
                        go.Scatter(y=results["measured_soc"], mode="lines", name="Measured SOC"),
                        go.Scatter(y=results["estimated_soc"], mode="lines", name="Estimated SOC"),

                        go.Scatter(y=current_profile, mode="lines", name="Current (A)")
                    ]
                ).update_layout(
                    title="Battery SOC and Current Over Time",
                    xaxis_title="Time (seconds)",
                    yaxis_title="SOC"
                )
            )
            # ,dcc.Graph(
            #     id="SOC-Voltage",
            #     figure=go.Figure(
            #         data=[
            #             go.Scatter(x=results["voltage"], y=results["soc"], mode="lines", name="SOC")
            #         ]
            #     ).update_layout(
            #         title="Battery SOC and Voltage Over Time",
            #         xaxis_title="Voltage",
            #         yaxis_title="SOC"
            #     )
            # )
        ])

        # Run the app
        app.run_server(debug=True)
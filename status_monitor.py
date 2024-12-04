import pandas as pd
import numpy as np
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests


class monitor(object):
    def __init__(self):
        pass

    # As reading in battery data, send notification if SOC below 20%
    def send_discord_alert(self, message, username="Alert Bot", avatar_url=None):
        """
        Sends an alert to a Discord webhook.

        :param webhook_url: Discord webhook URL
        :param message: Message content for the alert
        :param username: Optional: Username to appear as the sender
        :param avatar_url: Optional: URL for the sender's avatar
        """

        webhook_url = "{Your webhook URL}"

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


    def dash_app(self, soc_data, current_data):
        # Create the Dash app
        app = dash.Dash(__name__)

        # Layout
        # app.layout = html.Div([
        #     dcc.Graph(
        #         id="SOC-chart",
        #          figure=px.line(
        #     y=soc_data, 
        #     title="Battery SOC Over Time",
        #     labels={"index": "Time (seconds)", "x" : "Time (Seconds)", "y": "State of Charge (SOC)"}
        #     ))])

        app.layout = html.Div([
            dcc.Graph(
                id="SOC-chart",
                figure=go.Figure(
                    data=[
                        go.Scatter(y=soc_data, mode="lines", name="State of Charge (SOC)"),
                        go.Scatter(y=current_data, mode="lines", name="Current (A)")
                    ]
                ).update_layout(
                    title="Battery SOC and Current Over Time",
                    xaxis_title="Time (seconds)",
                    yaxis_title="Values"
                )
            )
        ])

        # Run the app
        app.run_server(debug=True)
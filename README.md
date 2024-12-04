# Battery SOC Monitor with Discord Notifications

This project provides a comprehensive solution for monitoring a battery's **State of Charge (SOC)** using Coulomb counting and displaying the results in an interactive dashboard. Additionally, it integrates an alert system using Discord to notify users of critical battery states in real time.

## Features
- **Battery SOC Simulation**: Accurately tracks and simulates the SOC using Coulomb counting.
- **Interactive Dashboard**: Visualize SOC data and battery current trends using an intuitive Dash-based web interface.
- **Real-time Alerts**: Sends Discord notifications when specific battery thresholds (e.g., low SOC) are reached.
- **Customizable Parameters**: Easily configure threshold values for alerts and data sampling intervals.

## How It Works
1. **Coulomb Counting**: Tracks charge and discharge currents to calculate the battery's SOC dynamically.
2. **Dashboard Visualization**: Uses Plotly and Dash to provide real-time SOC plots and current data over time.
3. **Discord Integration**: Alerts are sent via a Discord bot when SOC falls below or exceeds preset limits, ensuring proactive battery management.

## Technologies Used
- **Python** for the core functionality and simulation.
- **Dash and Plotly** for the interactive web dashboard.
- **Discord API** for real-time alert notifications.
- **pandas** for efficient data handling and processing.

## Setup and Installation
1. Clone this repository: <br>
   ```bash
   git clone https://github.com/brensinc/BatteryMonitorTool.git
   cd BatteryMonitorTool


2. Install dependencies: <br>
   pip install -r requirements.txt
   
3. Set up Discord integration:

4. Create a Discord webhook. <br>
   Add the webhook url as variable webhook_url in status_monitor.py:

## Test the application:
- Modify test_battery.py to create battery object to your specifications. <br>
   python test_battery.py
   Access the dashboard at http://127.0.0.1:8050/.

## Dashboard Preview
- **State of Charge Over Time:** Visualize the battery's SOC dynamically.
- **Current Data Trends:** View charge and discharge trends alongside SOC.
- **Notifications:** Receive timely alerts directly on Discord.

## Customization
- Dashboard Features: Update run_app.py to include additional plots or data points.

## Contribution
- Feel free to submit issues or create pull requests for new features, bug fixes, or enhancements.

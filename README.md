# Battery State of Charge (SOC) Monitor with Discord Notifications

This project provides a comprehensive solution for simulating, monitoring, and analyzing a battery's State of Charge (SOC) and State of Health (SOH). It **electro-thermal modeling** for performance and SOC analysis, and an **interactive dashboard** for visualization. Additionally, the system integrates **Discord notifications** to alert users in real time about critical battery states.

---

## Features

### Battery SOC Simulation and Monitoring
- **Accurate SOC Estimation**: Implements SOC tracking methodology from the literature to calculate the battery's SOC dynamically.
- **SOH Simulation**: Models the State of Health to analyze long-term battery performance and degradation.

### Interactive Dashboard
- Visualize SOC and current data trends in real time using a **Dash-based web interface**.
- SOC vs. Voltage Visualization: Understand battery dynamics with intuitive graphs.
- Customizable plots: Easily extend and add data points for enhanced analysis.

### Environmental Impact Simulation
- Incorporates **electro-thermal modeling** to simulate the effect of temperature on battery behavior.
- Robust SOC and voltage estimation under varying operational and environmental conditions.

### Real-time Alerts with Discord Integration
- Sends Discord notifications when battery SOC falls below or exceeds **configurable thresholds**.
- Proactively monitor critical battery states to avoid unexpected failures.

---

## How It Works
1. **Electro-Thermal Modeling**  
   Models the impact of current and temperature on battery performance based on research-backed methods.

2. **Dashboard Visualization**  
   - Uses **Plotly** and **Dash** to display SOC, current, and voltage data trends over time.  
   - Access the interactive web interface to monitor battery states.  

3. **Discord Integration**  
   - A Discord bot sends alerts to a server or channel when critical SOC thresholds are met.

---

## Technologies Used
- **Python**: Core functionality and simulation.
- **Dash & Plotly**: Interactive web-based dashboard for visualization.
- **Discord API**: Real-time notifications through a webhook.
- **pandas**: Efficient data handling and processing.
- **NumPy**: Mathematical computations for battery modeling.

---

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/brensinc/BatteryMonitorTool.git
cd BatteryMonitorTool

## Steps to use
- pip install -r requirements.txt
- Add the webhook URL as a variable webhook_url in the status_monitor.py file
- Run the file python test_battery.py

## Dashboard Preview

### Graphs Included:

1. **State of Charge (SOC) Over Time**  
   Visualizes SOC changes dynamically as the battery charges and discharges.

2. **Current Trends**  
   Displays current inflow/outflow alongside SOC for detailed analysis.

3. **SOC vs. Voltage**  
   Provides insights into battery behavior across different charge levels.

---

### Notifications  
Real-time Discord alerts notify users when:  
- SOC drops below critical thresholds (e.g., 20%).  
- SOC exceeds maximum charge levels.

---

## Customization

### Parameters:
- Adjust SOC thresholds, sampling intervals, and other parameters in the simulation files.  
- Update `run_app.py` to include additional plots or customized visualizations.

---

## References

This project incorporates modeling concepts and methods from the following research:

1. **Lin, X., et al. (2014)**  
   *A lumped-parameter electro-thermal model for cylindrical batteries.*  
   *Journal of Power Sources, 257, 1-11.*

2. **Perez, H. E., et al. (2017)**  
   *Optimal charging of Li-Ion batteries with coupled electro-thermal-aging dynamics.*  
   *IEEE Transactions on Vehicular Technology, 66(9), 7761-7770.*

3. **Perez, H. E., et al. (2012)**  
   *Parameterization and validation of an integrated electro-thermal cylindrical LFP battery model.*  
   *ASME Dynamic Systems and Control Conference.*

---

## Contribution  
We welcome contributions for new features, bug fixes, and improvements!  
Feel free to submit issues or open pull requests.

---

## Future Work

- Improved SOC estimation using **Kalman Filters** or **Machine Learning techniques**.  
- Expanded thermal modeling for real-world scenarios.  
- Enhanced notification features for additional platforms like **Slack** or **Email**.

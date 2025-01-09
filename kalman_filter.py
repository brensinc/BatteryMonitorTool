import numpy as np
    
class KalmanFilter:
    def __init__(self, initial_state, process_var, measurement_var):
        self.state = np.array(([[initial_state]]))
        self.P = np.array([[1]])
        self.Q = np.array([[process_var]])
        self.R = np.array([[measurement_var]])
        self.K = None 

    def predict(self, control_input=0):
        self.state = self.state + control_input
        self.P = self.P + self.Q 

    def update(self, measurement):
        self.K = self.P / (self.P + self.R)
        self.state = self.state + self.K * (measurement - self.state)
        self.P = (1 - self.K) * self.P

    def get_state(self):
        return self.state[0, 0]
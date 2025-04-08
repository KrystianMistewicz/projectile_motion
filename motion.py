import math
import numpy as np
import pandas as pd


class ProjectileMotion():

    def __init__(self, height: float, velocity: float, angle: float, points_number: int=100):
        """
        height : initial height for t=0, should be expressed in [m]
        velocity: initial value of body velocity for t=0, should be expressed in [m/s]
        angle: angle between velocity vector and x axis, must be in range from -90 to +90 degrees
        """
        self.h0 = height
        self.V0 = velocity
        self.alpha = angle
        self.n = points_number
        self.g = 9.81 # The value of Earth gravitation acceleration
        try:
            assert self.alpha >= -90 and self.alpha <= 90, "The value of angle must be in range from -90 to +90 degrees"
        except AssertionError as err:
            print(err)
        else:
            self.Vy0 = math.sin(self.alpha*math.pi/180)*self.V0
            self.tf = (self.Vy0 + math.sqrt(self.Vy0**2 + 2*self.g*self.h0))/self.g
            self.t_array = np.linspace(0, self.tf, self.n)
            self.y_array = self.h0 + self.Vy0*self.t_array - 0.5*self.g*self.t_array**2
            self.x_array = math.cos(self.alpha*math.pi/180)*self.V0*self.t_array
            self.Vx_array = np.ones(self.n)*math.cos(self.alpha*math.pi/180)*self.V0
            self.Vy_array = self.Vy0 - self.g*self.t_array
            self.V_array = (self.Vx_array**2 + self.Vy_array**2)**0.5
            self.V0_array = np.ones(self.n)*self.V0
            self.alpha_array = np.ones(self.n)*self.alpha
            self.data_dict = {
                't [s]': self.t_array,
                'x [m]': self.x_array,
                'y [m]': self.y_array,
                'Vx [m/s]': self.Vx_array,
                'Vy [m/s]': self.Vy_array,
                'V [m/s]': self.V_array,
                'V0 [m/s]': self.V0_array,
                'alpha [degree]': self.alpha_array
            }
            self.data = pd.DataFrame(data=self.data_dict)


if __name__ == '__main__':
    pm1 = ProjectileMotion(1, 1, -60, points_number=10)
    pm2 = ProjectileMotion(1, 1, -30, points_number=10)
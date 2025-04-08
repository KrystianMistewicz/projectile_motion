from motion import ProjectileMotion
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Graph():

    def __init__(self, projectile_motion, palette='Paired', **kwargs):
        self.projectile_motion = projectile_motion
        self.palette = palette
        self.kwargs = kwargs
        self.hue = None
        if type(self.projectile_motion) == ProjectileMotion:
            self.data = self.projectile_motion.data
        elif type(self.projectile_motion) == list or type(self.projectile_motion) == tuple:
            self.data_list = [pm.data for pm in self.projectile_motion]
            self.data = pd.concat(self.data_list)
            if 'parameter' in self.kwargs:
                self.hue = self.kwargs['parameter']
    
    def make_plot(self):
        sns.set_theme()
        plt.tight_layout()
        if 'title' in self.kwargs:
            plt.suptitle(self.kwargs['title'])
        plt.subplot(2, 2, 1)
        sns.lineplot(data=self.data, x='x [m]', y='y [m]', hue=self.hue, palette=self.palette)
        plt.subplot(2, 2, 2)
        sns.lineplot(data=self.data, x='t [s]', y='V [m/s]', hue=self.hue, palette=self.palette)
        plt.subplot(2, 2, 3)
        sns.lineplot(data=self.data, x='t [s]', y='Vx [m/s]', hue=self.hue, palette=self.palette)
        plt.subplot(2, 2, 4)
        sns.lineplot(data=self.data, x='t [s]', y='Vy [m/s]', hue=self.hue, palette=self.palette)
        plt.show()


if __name__ == '__main__':
    
    # title = 'Dane z zadania nr 5 z zestawu nr 2 (h0=1.5 m, V0=10 m/s, alfa=0)'
    # pm = ProjectileMotion(1.5, 10, 0)
    # Graph(pm, title=title).make_plot()

    # title = 'Wykresy dla h=1 m, alfa=0 i różnych prędkości V0'
    # pm_list = [ProjectileMotion(1, velocity, 0) for velocity in np.linspace(1, 10, 10)]
    # graph = Graph(pm_list, parameter='V0 [m/s]', title=title).make_plot()

    # title = 'Wykresy dla h0=0 m, V0=10 m/s i różnych wartości kąta alfa'
    # pm_list = [ProjectileMotion(0, 10, alpha) for alpha in np.linspace(15, 90, 6)]
    # graph = Graph(pm_list, palette='tab10', parameter='alpha [degree]', title=title).make_plot()

    title = 'Wykresy dla h0=1 m, V0=10 m/s i różnych wartości kąta alfa'
    pm_list = [ProjectileMotion(1, 10, alpha) for alpha in np.linspace(-75, 75, 11)]
    graph = Graph(pm_list, parameter='alpha [degree]', palette='Paired', title=title).make_plot()

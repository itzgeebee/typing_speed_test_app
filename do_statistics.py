import pandas as pd
from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# A feature to graphically display the user's typing speed over time
class PlotGraph:
    def __int__(self):
        x = ""

    def plot_data(self, window, row, column):
        """ plots a graph of the wpm stats against time"""

        stats = pd.read_csv("statistics.csv")
        avg = stats.groupby(by='Date').agg({'score': pd.Series.mean})
        moving_average = avg.rolling(window=6).mean()
        y = (stats["score"])
        fig = Figure(figsize=(5, 5), dpi=100.)
        plot1 = fig.add_subplot(111)
        fig.suptitle("Word per minute over time")
        fig.supxlabel("months")
        fig.supylabel("wpm")
        plot1.plot(moving_average.index, moving_average.values)

        canvas = FigureCanvasTkAgg(fig,
                               master = window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=row, column=column)




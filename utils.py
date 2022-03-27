from termcolor import colored
import pandas as pd
import plotly.graph_objects as go
from matplotlib import pyplot as plt

def printGreen(string):
    """
    Print a string in green in the terminal
    :param string: (str)
    """
    print(colored(string, 'green'))


def printYellow(string):
    """
    :param string: (str)
    """
    print(colored(string, 'yellow'))


def printRed(string):
    """
    :param string: (str)
    """
    print(colored(string, 'red'))


def printBlue(string):
    """
    :param string: (str)
    """
    print(colored(string, 'blue'))

def plot_plotly(df, x=None, mode='plot', width=600, height=300, plot=True):
    """
    Plot a dataframe with plotly

    x: the name of the x-axis, it is by default the index of dataframe 
    """
    fig = go.Figure()
    fontdict = {'family':'monospace','size':13}
    x_name = df.index.name if df.index.name else 'index'
    if isinstance(df, pd.Series):
        df = pd.DataFrame(df)
    x = df.index if not x else x
    mode = {
        'plot': 'lines',
        'plot_s': 'markers',
        'plot_s2': 'lines+markers'
    }[mode]
    ys_name = [str(x) for x in df.columns]
    for y_name in ys_name:
        fig.add_trace(go.Scatter(x=x, y=df[y_name], mode=mode, name=y_name))
    legend_width = 65+8*max(map(len,ys_name))
    margin = go.layout.Margin({'l':0, 't':25, 'b':0, 'r':legend_width})
    fig.update_layout(width=width, height=height, margin=margin)
    if plot:
        fig.show()
    else:
        return fig

def plot_matplotlib(data, height=300, width=800):
    plt.figure(figsize=[width/60, height/60])
    plt.plot(data)
    plt.show()
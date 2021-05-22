# pwplot.py - quick plotting utilities for my WUT needs.
# github.com/m-luk - 2021

import pandas as pd
import numpy as np
from numpy.polynomial import Polynomial
from matplotlib import pyplot as plt
import matplotlib as mpl
from pyutils import dotdict

# matplotlib style
mpl.rcParams['savefig.dpi'] = 300
plt.style.use('seaborn-white')
plt.rcParams["figure.figsize"] = (25/3.25, 15/3.25)
plt.rcParams["font.size"] = 11


def plot(traces, **kwargs):
    '''
    Basic plot, created from data provided as a list of dictionaries:

        Parameters:
            traces (list): List of dicts with plot data and config like:
                [dict(
                    x = <x values>,
                    y = <y values>,
                    name = <trace name>,
                    color = <color>
                    style = <basic style such as 'o' or '--'>,
                    markersize = <size of the marker>,
                    trendline = <trendline polynomial degree>,
                    xerr = <value of x error lines>,
                    yerr = <value of y error lines>,
                    params = <dict with additional parameteres> 
                ), ...]
            title (string): Figure title,
            xlabel (string): Figure xlabel,
            ylabel (string): Figure ylabel,
            xlim (tuple): (x_min, x_max),
            ylim (tuple): (y_min, y_max),
            legend (bool): Show legend, default False,
            savefig (string): if path provided save to <savefig> - user specifies extension,
            show (bool): Show figure, default True

        Retruns:
            Figure (by gcf)
    '''

    # create plot objects
    fig, ax = plt.subplots()

    # evaluate traces
    for trace in traces:
        trace = dotdict(trace)

        # if none supply default params
        if trace.x is None or trace.y is None:
            return
        if trace.style is None:
            trace.style = 'o'
        if trace.params == None:
            trace.params = {}

        # main plot
        ax.plot(trace.x, trace.y, trace.style, color=trace.color,
                 label=trace.name, markersize=trace.markersize, **trace.params)

        # TODO: trendline style params
        # trendline (currently only polynomial approximation)
        if trace.trendline is not None and trace.trendline > 0:
            p = Polynomial.fit(trace.x, trace.y, trace.trendline)
            xx, yy = p.linspace()
            ax.plot(xx, yy, '--', color=trace.color, alpha=0.6)

        # error bars
        if trace.xerr or trace.yerr:
            ax.errorbar(
                trace.x, trace.y, xerr=trace.xerr, yerr=trace.yerr, fmt='none',
                color=trace.color
            )

    # evaluate figure params
    for key, value in kwargs.items():
        if key == 'xlabel':
            ax.set_xlabel(value)
        elif key == 'ylabel':
            ax.set_ylabel(value)
        elif key == 'title':
            ax.set_title(value)
        elif key == 'xlim':
            ax.set_xlim(value)
        elif key == 'ylim':
            ax.set_ylim(value)

    # show legend, default no
    if 'legend' in kwargs.keys():
        if kwargs['legend']:
            ax.legend()

    # show grid, default yes
    if 'grid' in kwargs.keys():
        if kwargs['grid']:
            ax.grid()
    else:
        ax.grid()

    # show figure, default no
    if 'show' in kwargs.keys():
        if kwargs['show']:
           fig.show()
    
    # savefig, default no, user provides full path with extension
    if 'savefig' in kwargs.keys():
        if kwargs['savefig']:
            fig.savefig('{}'.format(kwargs['savefig']))


    # return figure
    return (fig, ax)
# pwplot.py - quick plotting utilities for my WUT needs.
# github.com/m-luk - 2021

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.polynomial import Polynomial

from pyutils import dotdict

# matplotlib style
mpl.rcParams['savefig.dpi'] = 300
plt.style.use('seaborn-white')
plt.rcParams["figure.figsize"] = (25/3.25, 15/3.25)
plt.rcParams["font.size"] = 11


def plot(traces, **kwargs):
    '''
#<Esc>    Basic plot, created from data provided as a list of dictionaries:

        Parameters:
            traces (list): List of dicts with plot data and config like:
                [dict(
                    x = <x values>,
                    y = <y values>,
                    label = <trace name>,
                    color = <color>
                    style = <basic style such as 'o' or '--'>,
                    markersize = <size of the marker>,
                    trendline = <trendline polynomial degree>,
                    xerr = <value of x error lines>,
                    yerr = <value of y error lines>,
                    params = <dict with additional parameteres> 
                    name = <backwards compatibility label>
                ), ...]
            title (string): Figure title,
            xlabel (string): Figure xlabel,
            ylabel (string): Figure ylabel,
            xlim (tuple): (x_min, x_max),
            ylim (tuple): (y_min, y_max),
            legend (bool): Show legend, default False,
            savefig (string): if path provided save to <savefig> - user specifies extension,
            show (bool): Show figure, default True,
            font_size (int): Defines font size

        Retruns:
            Figure (by gcf)
    '''

    # change defaults
    if 'font_size' in kwargs.keys():
        plt.rcParams["font.size"] = kwargs['font_size']
    else:
        plt.rcParams["font.size"] = 11

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
        if trace.label is None and trace.name is not None:
            trace.label = trace.name

        # main plot
        ax.plot(trace.x, trace.y, trace.style, color=trace.color,
                label=trace.label, markersize=trace.markersize, **trace.params)

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


def set_size_cm(mpl_fig, width, height):
    ''' Damns those imperial units '''
    mpl_fig.set_size_inches(width/2.54, height/2.54)


# This part is CC BY-SA 3.0
# From HYRY's answer: https://stackoverflow.com/a/10482477
def align_yaxis(ax1, v1, ax2, v2):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _, y1 = ax1.transData.transform((0, v1))
    _, y2 = ax2.transData.transform((0, v2))
    inv = ax2.transData.inverted()
    _, dy = inv.transform((0, 0)) - inv.transform((0, y1-y2))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy)
# end of CC BY-SA 3.0

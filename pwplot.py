# pwplot.py - quick plotting utilities for my WUT needs.
# github.com/m-luk - 2021

import pandas as pd
import numpy as np
from numpy.polynomial import Polynomial
from matplotlib import pyplot as plt
import matplotlib as mpl
from pyutils import dotdict

# matplotlib styling
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
                    styling = <basic styling such as 'o' or '--'>,
                    markersize = <size of the marker>,
                    trendline = <trendline polynomial degree>,
                    xerr = <value of x error lines>,
                    yerr = <value of y error lines>,
                ), ...]
            title (string): Figure title,
            xlabel (string): Figure xlabel,
            ylabel (string): Figure ylabel,
            legend (bool): Show legend, default False,
            savefig (string): if name provided save to <savefig>.png,
            show (bool): Show figure, default True

        Retruns:
            Figure (by gcf)
    '''

    # evaluate traces
    for trace in traces:
        # print(trace)
        # trace = trace_dict_fill_empty(trace)
        trace = dotdict(trace)

        # if none supply default params
        if trace.x is None or trace.y is None:
            return
        if trace.styling is None:
            trace.styling = 'o'
        if trace.color is None:
            trace.color = 'tab:blue'

        # main plot
        plt.plot(trace.x, trace.y, trace.styling, color=trace.color,
                 label=trace.name, markersize=trace.markersize)

        # TODO: trendline styling params
        # trendline (currently only polynomial approximation)
        if trace.trendline is not None and trace.trendline > 0:
            p = Polynomial.fit(trace.x, trace.y, trace.trendline)
            xx, yy = p.linspace()
            plt.plot(xx, yy, '--', color=trace.color, alpha=0.6)

        # error bars
        if trace.xerr or trace.yerr:
            plt.errorbar(
                trace.x, trace.y, xerr=trace.xerr, yerr=trace.yerr, fmt='none',
                color=trace.color
            )

    # evaluate figure params
    for key, value in kwargs.items():
        if key == 'xlabel':
            plt.xlabel(value)
        elif key == 'ylabel':
            plt.ylabel(value)
        elif key == 'title':
            plt.title(value)
        # FIXME: this is not good, empty argument does the thing but it shouldn't
        elif key == 'legend' and value == True:
            plt.legend()
        elif key == 'grid' and value == True:
            plt.grid()

    kwargs = dotdict(kwargs)

    if 'show' in kwargs.keys():
        if kwargs['show']:
           plt.show()
    else:
        plt.show()
    
    # FIXME: saves empty figure
    if 'savefig' in kwargs.keys():
        if kwargs['savefig']:
            plt.savefig('{}.png'.format(kwargs['savefig']))


    # TODO: switch all plt. to fig, ax syntax
    # return figure
    return plt.gcf()


def trace_dict_fill_empty(trace):
    ''' 
    Returns trace dict with None filled empty positions, if mandatory arguments
    not submitted returns False 
    '''
    trace_keys = set(trace.keys())
    keys_mandatory = set(['x', 'y'])
    keys_additional = [
        "name", "color", "styling", "markersize", "trendline", "xerr", "yerr"
    ]

    if not trace_keys.issubset(keys_mandatory):
        return False

    for key in keys_additional:
        if key not in trace_keys:
            trace[key] = None

    return trace

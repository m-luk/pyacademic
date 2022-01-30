# pyutils.py: Python utils for other utilities
# github.com/m-luk - 2021

class dotdict(dict):
	''' Create dict with dot access '''
	__getattr__ = dict.get
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__
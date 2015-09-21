__author__ = 'veradocs-web'

 # bisect module with functions for manipulating sorted lists
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print scores

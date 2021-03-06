#! /usr/bin/python

# Boilerplate
import sys
from rxnlvl import *

# Plot
p = plot([15.0,10.0],vbuf=10.0,hbuf=10.0,bgcolour=None, qualified='sortof', font_size_energy='8pt', font_size_name='8pt', dy_name='-4pt', dy_energy='-4pt', drawAxis=True)

p +  level(energy(   00, 'kjmol'),  1,    '1',        0x0, drawName=False)
p +  level(energy(  -85.5, 'kjmol'),  2,  'EC1(2)',   0x0)
p +  level(energy(  144, 'kjmol'),  3, 'TS(1)a', 0xFF4444)
p +  level(energy(   51, 'kjmol'),  3, 'TS1b',        0x0)
p +  level(energy( -102, 'kjmol'),  4,  'DC1',        0x0)
p +  level(energy(  -82, 'kjmol'),  5,    '2',        0x0)
p +  level(energy( -111, 'kjmol'),  6,  'EC2',        0x0)
p +  level(energy(  -83, 'kjmol'),  7, 'TS2b',        0x0)
p +  level(energy(   18, 'kjmol'),  7, 'TS2a',   0x44FF44)
p +  level(energy( -103, 'kjmol'),  8,  'DC2',        0x0)
p +  level(energy(   85, 'kjmol'),  9,    '3',        0x0)
p +  level(energy(  185, 'kjmol'), 10,    '4',        0x0)
p +  level(energy(   25, 'kjmol'), 11,    '5',        0x0)

p +  edge(    '1',  'EC1(2)', 0x0, 0.4, 'normal')
p +  edge(  'EC1(2)', 'TS(1)a', 0x0, 0.2, 'normal')
p +  edge(  'EC1(2)', 'TS1b', 0x0, 0.4, 'normal')
p +  edge( 'TS(1)a',  'DC1', 0x0, 0.2, 'normal')
p +  edge( 'TS1b',  'DC1', 0x0, 0.4, 'normal')
p +  edge(  'DC1',    '2', 0x0, 0.4, 'normal')
p +  edge(    '2',  'EC2', 0x0, 0.4, 'normal')
p +  edge(  'EC2', 'TS2b', 0x0, 0.4, 'normal')
p +  edge(  'EC2', 'TS2a', 0x0, 0.2, 'normal')
p +  edge( 'TS2a',  'DC2', 0x0, 0.2, 'normal')
p +  edge( 'TS2b',  'DC2', 0x0, 0.4, 'normal')
p +  edge(  'DC2',    '3', 0x0, 0.4, 'normal')
p +  edge(    '3',    '4', 0x0, 0.4, 'normal')
p +  edge(    '4',    '5', 0x0, 0.4, 'normal')

baselines = [i*20 for i in range(-9,9)]
for base in baselines:
  p + baseline(energy( base, 'kjmol'),colour=0x0,mode='dashed',opacity=0.1)

svg = p.write((-200,200))
with open('test2.svg', 'w') as f:
  f.write(svg)
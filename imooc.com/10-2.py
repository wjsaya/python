#!/usr/bin/env python3
# coding: utf-8
'''
from: https://www.imooc.com/code/3542
    d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
    def generate_tr(name, score):
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

    tds = [??? for name, score in d.iteritems()]
    print '<table border="1">'
    print '<tr><th>Name</th><th>Score</th><tr>'
    print '\n'.join(tds)
    print '</table>'
'''

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.items()]
print(tds)
print('<table border="1">')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')
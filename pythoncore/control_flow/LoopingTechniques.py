__author__ = 'veradocs-web'


for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v


questions = ['name', 'quest', 'favorite color',"banda"]
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

for i in reversed(xrange(1,10,2)):
    print i


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v


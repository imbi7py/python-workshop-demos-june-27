cal = dict()
cal['Monday'] = ['lunch', 'training', 'meeting']
cal['Tuesday'] = []
cal['Wednesday'] = ['lunch n learn']

max_meeting_num = max([
     len(day)
     for day in cal.values()
    ])

w = 15
for k in cal:
    print('{0: <{width}}'.format(k, width=w), end='|')
print()
print('-'*50)
for n in range(0, max_meeting_num):
    for day in cal.keys():
        meetings = cal[day]
        if len(meetings) > n:
            print('{0: <{width}}'.format(meetings[n], width=w), end='|')
        else:
            print('{0: <{width}}'.format(' ', width=w), end='|')
    print()


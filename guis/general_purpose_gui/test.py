from praytimes import *

PT = PrayTimes('MWL')
times = PT.getTimes((2019, 1, 6), (30, 97), -2)
print('''
Sunrise: {}
Sunset: {}
'''.format(times['sunrise'], times['sunset']))

#시계열 데이터 만들기

import  pandas as pd

ts_ms = pd.date_range(start = '2019-01-01',
                      end = None,
                      periods= 6,
                      freq='MS',
                      tz='Asia/Seoul')
# print(ts_ms)

ts_me = pd.date_range(start = '2019-01-01',
                      periods= 6,
                      freq='M', #월말
                      tz = 'Asia/Seoul')
# print(ts_me)

ts_3m = pd.date_range(start= '2019-01-01',
                      periods= 6,
                      freq='3M', #3개월 ,월말
                      tz = 'Asia/Seoul')
# print(ts_3m)

pr_m = pd.period_range(start = '2019-01-01',
                       end=None,
                       periods= 3,
                       freq = 'M')
# print(pr_m)


pr_h = pd.period_range(start= '2019-01-01',
                       end=None,
                       periods=3,
                       freq='H')
print(pr_h)

pr_2h = pd.period_range(start= '2019-01-01',
                       end=None,
                       periods=3,
                       freq='2H')
print(pr_2h)

import datetime,time
# a='2018-4-18 16:30:22'
# r=datetime.datetime.strftime(2018-4-18,"%Y-%m-%d")
# t=datetime.datetime.now().strftime("%Y-%m-%dz %H:%M:%Sz")
# print(t,r)

str = '2012-11-19 16:30:22'

date_time = datetime.datetime.strptime(str,'%Y-%m-%d  %H:%M:%S').strftime('%Y-%m-%dZ%H:%M:%SZ')
print(date_time)

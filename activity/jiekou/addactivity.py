import requests,xlrd,datetime

name_td=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M')
td1=datetime.timedelta(hours=-7)
td2=datetime.timedelta(hours=-6)
td3=datetime.timedelta(hours=-1)#自定义签到开始时间差
newtd1=td1+datetime.datetime.now()
newtd2=td2+datetime.datetime.now()
newtd3=td3+datetime.datetime.now()
dt1=datetime.datetime.strftime(newtd1,'%Y-%m-%dT%H:%MZ')
dt2=datetime.datetime.strftime(newtd2,'%Y-%m-%dT%H:%MZ')
dt3=datetime.datetime.strftime(newtd3,'%Y-%m-%d %H:%M')
print(dt1,dt2,dt3,newtd1)
req=requests.session()

def login():
    url='http://admin2.join-inapp.com/api/main/loginData'
    data={
        'login_name':'13418914293',
        'password':'00000000'
    }
    response=req.post(url,data)
    f=response.text
    print(f)


def add(dataadd):
    urladd='http://admin2.join-inapp.com/api/activitybaseinfo/addData/0'
    f=req.post(urladd,dataadd)
    text=f.text
    print(text)


login()
add(adddata)

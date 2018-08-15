import requests,time

import datetime
#from jiekou.data import adddata
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
# print(dt1,dt2,dt3)

name_td=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M')
td1=datetime.timedelta(hours=-7)
td2=datetime.timedelta(hours=-6)
td3=datetime.timedelta(hours=-1)#自定义签到开始时间差
newtd1=td1+datetime.datetime.now()
newtd2=td2+datetime.datetime.now()
newtd3=td3+datetime.datetime.now()
dt1=datetime.datetime.strftime(newtd1,'%Y-%m-%dT%H:%MZ')
dt2=datetime.datetime.strftime(newtd2,'%Y-%m-%dT%H:%MZ')
dt3=datetime.datetime.strftime(newtd3,'%Y-%m-%dT%H:%MZ')

# print(dt1)
def data(abiSignOpen=0):

    adddata={"signStart": 0,
    "signEnd": 0,
    "bannerUrl": "/uploads/2017/10/20/9299e925-09ac-470f-8d1c-8f64734641fe.jpg",
    "cosponsorIds": "10002305",
    "aciUserId": "10015499",
    "abiWeightDate": "",
    "signinStartTime": "",
    "signinEndTime": "",
    "signoutStartTime": "",
    "signoutEndTime": "",
    "signStartTime": "",
    "abiRegistrationDeadline": "",
    "abiName": name_td,
    "activitySponsors": "10000102",
    "activityOrganizers": "10000712",
    "abiRangeId": "10000002",
    "abiDescription": "<p>pppp</p>",
    "abiPurpose": "jjjjjjj",
    "imgUrl": ["/uploads/2017/10/20/a8d64ad8-3158-44af-957c-a86c3e655c10.jpg"],
    "fileUrl": [],
    "abiSignOpen": abiSignOpen,
    "abiStartTime": dt1,
    "abiEndTime": dt2,
    "signinType": 0,
    "signoutType": 0,
    "haveExpenses": 0,
    "abiGpsPlace": "广东省深圳市福田区农轩路55号",
    "maxSignTimes": 0,
    "isArtificialMark": 0,
    "abiWeight": 0,
    "allowComment": 2,
    "commentAudit": 1,
    "abiChargeName": "t1",
    "abiChargeNo": "t2",
    "abiChargeMobile": "t3",
    "abiSupervisorName": "t4",
    "abiSupervisorMobile": "t5",
    "isCanCancel": 0,
    "remindContent": "",
    "sortno": 1,
    "abiSignRequire": "",
    "creditFlag": 0,
    "abiPublishId": "10001112",
    "abiRangeId2": "10000002",
    "abiValidHour": 20,
    "limitSignNum": 22,
    "abiGpsLat": 22.542695,
    "abiGpsLng": 114.014493,
    "cosponsorNames": "666",
    "cosponsorNos": "12112",
    "aciUserName": "111",
    "aciUserNo": "1199653",
    "abiSponsor": "校学生会",
    "abiOrganizer": "校学生会",
    "mustSignTimes": 0,
    "activityCategorys": "10000704,10000703",
    "abiCategory": "文艺体育类",
    "abiType": 0,
    "remindTimes": 0,
    "remindTime": ""
    }
    return adddata

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

a=input('请输入报名方式，0为公开，1为审核')



def audit1():
    listurl='http://admin2.join-inapp.com/api/activitybaseinfo/getData/0'
    getlist=req.get(listurl)
    a=getlist.json()
    id=a['data']['queryData'][0]['id']
    urlaudit1='http://admin2.join-inapp.com/api/activitybaseinfo/auditData/1'
    urlauditdata={
    'id':id,
    'abiWeight':0,
    'haveExpenses':	0,
    'allowComment':	2,
    'commentAudit':	1,
    'abiChargeName':'',
    'abiChargeNo':'',
    'abiChargeMobile':'',
    'abiSupervisorName':'',
    'abiSupervisorMobile':'',
    'isCanCancel':'0',
    'isArtificialMark':'0',
    'abiWeightDate':'',
    'auditContent':'',
    'aalState':'2',
    'activityCategorys':'10000703',
    'abiCategory':'综合实践类',
    'abiType':'0',
    'remindTimes':'0',
    'remindTime':''
    }
    audit=req.post(urlaudit1,urlauditdata)
    print(audit.text)
    # time.sleep(3)
def audit2():
    listurl='http://admin2.join-inapp.com/api/activitybaseinfo/getData/0'
    getlist=req.get(listurl)
    a=getlist.json()
    id=a['data']['queryData'][0]['id']
    urlaudit1='http://admin2.join-inapp.com/api/activitybaseinfo/auditData/2'
    urlauditdata={
    'id':id,
    'abiWeight':0,
    'haveExpenses':	0,
    'allowComment':	2,
    'commentAudit':	1,
    'abiChargeName':'',
    'abiChargeNo':'',
    'abiChargeMobile':'',
    'abiSupervisorName':'',
    'abiSupervisorMobile':'',
    'isCanCancel':'0',
    'isArtificialMark':'0',
    'abiWeightDate':'',
    'auditContent':'',
    'aalState':'2',
    'activityCategorys':'10000703',
    'abiCategory':'综合实践类',
    'abiType':'0',
    'remindTimes':'0',
    'remindTime':''
    }
    audit=req.post(urlaudit1,urlauditdata)
    print(audit.text)
    time.sleep(3)
login()
add(data(a))
audit1()
audit2()
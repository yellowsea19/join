import requests,time

import datetime

name_td=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M')
td1=datetime.timedelta(hours=-7)
td2=datetime.timedelta(hours=-6)
td3=datetime.timedelta(hours=-1)#自定义签到开始时间差
td4=datetime.timedelta(minutes=15)
newtd4=''
newtd1=td1+datetime.datetime.now()
newtd2=td2+datetime.datetime.now()
newtd3=td3+datetime.datetime.now()
dt1=datetime.datetime.strftime(newtd1,'%Y-%m-%dT%H:%MZ')
dt2=datetime.datetime.strftime(newtd2,'%Y-%m-%dT%H:%MZ')
dt3=datetime.datetime.strftime(newtd3,'%Y-%m-%dT%H:%MZ')
print(dt1,dt2,dt3)
print(dt3)
def data():

    dataadd={
        "abiRangeId": "10000206",
"abiPublishId": "10001112",
"sortno": 1756,
"id": "994411462078369795",
"abiName": datetime.datetime.now(),
"abiSponsor": "校学生会",
"abiPurpose": "",
"abiDescription": "<p>对大学生而言，就业是人生一次重要的选择。每个大学生都希望找到一份好工作，为社会做贡献，实现自身价值。面对艰难的就业形势，我们应当培养&ldquo;生于忧患&rdquo;和&ldquo;居安思危&rdquo;的意识，提前做好自己的职业规划。此次第八届模拟招聘会决赛，我们将会有数家企业HR作为评委莅临现场。他们分别是 \\n白艺雄 中建一局西北分公司人力资源部经理\\n李强 &nbsp; 中建一局西北分公司招聘经理\\n董德北 智联招聘校园及海外事业部西北区域负责人\\n刘荣荣 德邦物流西北事业部人事部总监\\n宋玲 &nbsp; 荣盛房地产开发有限公司招聘培训负责人\\n 杨芳 &nbsp; &nbsp; 西安学而思培优选聘部面试负责人\\n张晓娟 银泰百货西安区人力资源负责人\\n同时将会有6位选手带上他们在求职岗位上所做出的努力和取得的成就来接受各个企业HR评委的招聘</p><p><br></p>",
"imgUrl": ["/uploads/2017/10/20/185b986f-eaaa-46ec-b7f4-d4c91a17058b.jpg", "/uploads/2017/10/20/39b2c0cb-f3f9-4fef-a55a-df5607fb530d.jpg", "/uploads/2017/10/20/0aadfffb-2bb6-4dc7-9201-12ea63a5dfd2.jpg", "/uploads/2017/10/20/5107ed93-ce44-45e4-b4af-1c0c260c9b22.jpg", "/uploads/2017/10/20/5281cf54-c773-4dda-bd14-da402e329a00.png", "/uploads/2017/10/20/cc41f705-07db-477e-9195-6e44006a36af.jpg", "/uploads/2017/10/20/a8d64ad8-3158-44af-957c-a86c3e655c10.jpg", "/uploads/2017/10/20/9299e925-09ac-470f-8d1c-8f64734641fe.jpg", "/uploads/2017/10/20/5fa5517b-fca0-4f49-92ef-d8b0c1680e8f.jpg"],
"bannerUrl": "/uploads/2018/05/14/5af9580a-4c90-9c79-f8c7-1b27622a0a66.jpg",
"fileUrl": "",
"abiStartTime": dt1,
"abiEndTime": dt2,
"limitSignNum": 20,
"abiGpsPlace": "广东省深圳市福田区农轩路55号",
"abiGpsLng": "114.014493",
"abiGpsLat": "22.542695",
"abiWeight": 0,
"haveExpenses": 0,
"allowComment": 2,
"commentAudit": 1,
"abiSignOpen": 0,
"abiStatus": 0,
"sriId": "0",
"abiChargeName": "",
"abiChargeNo": "",
"abiChargeMobile": "",
"abiSupervisorName": "",
"abiSupervisorMobile": "",
"isCanCancel": 0,
"signinType": 0,
"signoutType": 0,
"isArtificialMark": 0,
"maxSignTimes": 0,
"mustSignTimes": 0,
"abiValidHour": 1440,
"abiSignRequire": "",
"creditFlag": 0,
"activitySponsors": "10000102",
"activityOrganizers": [],
"signStart": 0,
"signEnd": 0,
"cosponsorIds": "986459886701383681",
"aciUserId": [],
"abiRangeId2": "10000206",
"abiWeightDate": "",
"signinStartTime": "",
"signinEndTime": "",
"signoutStartTime": "",
"signoutEndTime": "",
"signStartTime": "",
"abiRegistrationDeadline": "",
"remindContent": "",
"cosponsorNames": "19920180003",
"cosponsorNos": "061516551",
"activityCategorys": "10000700,10000700",
"abiCategory": "学术科技类",
"abiType": 0,
"remindTimes": 0,
"remindTime": ""
    }
    return dataadd

data_223={"signStart":0,"signEnd":0,"bannerUrl":"/uploads/2018/04/08/25788d5f-669a-4f6d-b92b-6f596dba124f.jpg","cosponsorIds":"10003907","aciUserId":"10004836","abiWeightDate":"","signinStartTime":"","signinEndTime":"","signoutStartTime":"","signoutEndTime":"","signStartTime":"","abiRegistrationDeadline":"","abiName":datetime.datetime.now(),"activitySponsors":"10000102","activityOrganizers":"10000711","activityCosponsors":"1002023603400740866","abiRangeId":"10002800","abiDescription":"<p>在</p>","abiPurpose":"城","imgUrl":["/uploads/2018/04/08/25788d5f-669a-4f6d-b92b-6f596dba124f.jpg"],"fileUrl":[],"abiSignOpen":0,"abiStartTime":dt1,"abiEndTime":dt2,"signinType":0,"signoutType":0,"haveExpenses":0,"abiGpsPlace":"广东省深圳市福田区农轩路55号","maxSignTimes":0,"isArtificialMark":0,"abiWeight":0,"allowComment":2,"commentAudit":1,"abiChargeName":"","abiChargeNo":"","abiChargeMobile":"","abiSupervisorName":"","abiSupervisorMobile":"","isCanCancel":0,"remindContent":"","sortno":1,"abiSignRequire":"","creditFlag":0,"abiPublishId":"10001519","auditId":"10003600","abiRangeId2":"10002800","abiValidHour":22,"limitSignNum":22,"abiGpsLat":22.542695,"abiGpsLng":114.014493,"cosponsorNames":"王五","cosponsorNos":"7401118","aciUserName":"法海","aciUserNo":"1111111111","abiSponsor":"校学生会","abiOrganizer":"校研究生会","abiCosponsor":"协办方","mustSignTimes":0,"activityCategorys":"10000705","abiCategory":"公益志愿类","abiType":0,"remindTimes":0,"remindTime":""}

req=requests.session()

def login():
    url='http://admin2.join-inapp.com/api/main/loginData'
    # url='http://10.0.0.223:8001/api/main/loginData'

    data={
        'login_name':'13418914293',
        'password':'00000000'
    }

    response=req.post(url,data)
    f=response.text
    print(f)


def add(dataadd):
    urladd='http://admin2.join-inapp.com/api/activitybaseinfo/addData/0'
    # urladd='http://10.0.0.223:8001/api/activitybaseinfo/addData/0'
    f=req.post(urladd,dataadd)
    d=req.post(urladd,dataadd)
    a=req.post(urladd,dataadd)
    text=f.text
    print(f.text,d.text,a.text)

# a=input('请输入报名方式，0为公开，1为审核  默认公开')
# credit_flag=input('请输入是否开启信用  0为关闭，1为开启')

def edit():
    listurl='http://admin2.join-inapp.com/api/activitybaseinfo/getData/0'
    getlist=req.get(listurl)
    a=getlist.json()
    id=a['data']['queryData'][0]['id']
    print(id)
    data={"abiRangeId":"10000206","abiPublishId":"10001112","sortno":1822,"id":id,"abiName":"2018-06-01 16:32:29","abiSponsor":"校学生会","abiPurpose":"","abiDescription":"<p>对大学生而言，就业是人生一次重要的选择。每个大学生都希望找到一份好工作，为社会做贡献，实现自身价值。面对艰难的就业形势，我们应当培养&ldquo;生于忧患&rdquo;和&ldquo;居安思危&rdquo;的意识，提前做好自己的职业规划。此次第八届模拟招聘会决赛，我们将会有数家企业HR作为评委莅临现场。他们分别是 \\n白艺雄 中建一局西北分公司人力资源部经理\\n李强 &nbsp; 中建一局西北分公司招聘经理\\n董德北 智联招聘校园及海外事业部西北区域负责人\\n刘荣荣 德邦物流西北事业部人事部总监\\n宋玲 &nbsp; 荣盛房地产开发有限公司招聘培训负责人\\n 杨芳 &nbsp; &nbsp; 西安学而思培优选聘部面试负责人\\n张晓娟 银泰百货西安区人力资源负责人\\n同时将会有6位选手带上他们在求职岗位上所做出的努力和取得的成就来接受各个企业HR评委的招聘</p><p><br></p>","imgUrl":["/uploads/2017/10/20/185b986f-eaaa-46ec-b7f4-d4c91a17058b.jpg","/uploads/2017/10/20/39b2c0cb-f3f9-4fef-a55a-df5607fb530d.jpg","/uploads/2017/10/20/0aadfffb-2bb6-4dc7-9201-12ea63a5dfd2.jpg","/uploads/2017/10/20/5107ed93-ce44-45e4-b4af-1c0c260c9b22.jpg","/uploads/2017/10/20/5281cf54-c773-4dda-bd14-da402e329a00.png","/uploads/2017/10/20/cc41f705-07db-477e-9195-6e44006a36af.jpg","/uploads/2017/10/20/a8d64ad8-3158-44af-957c-a86c3e655c10.jpg","/uploads/2017/10/20/9299e925-09ac-470f-8d1c-8f64734641fe.jpg","/uploads/2017/10/20/5fa5517b-fca0-4f49-92ef-d8b0c1680e8f.jpg"],"bannerUrl":"/uploads/2018/05/14/5af9580a-4c90-9c79-f8c7-1b27622a0a66.jpg","fileUrl":"","abiStartTime":"2018-06-01T09:32:00.000Z","abiEndTime":"2018-06-01T10:32:00.000Z","limitSignNum":20,"abiGpsPlace":"广东省深圳市福田区农轩路55号","abiGpsLng":"114.014493","abiGpsLat":"22.542695","abiWeight":0,"haveExpenses":0,"allowComment":2,"commentAudit":1,"abiSignOpen":0,"abiStatus":0,"sriId":"0","abiChargeName":"","abiChargeNo":"","abiChargeMobile":"","abiSupervisorName":"","abiSupervisorMobile":"","isCanCancel":0,"signinType":0,"signoutType":0,"isArtificialMark":0,"maxSignTimes":0,"mustSignTimes":0,"abiValidHour":22,"abiSignRequire":"","creditFlag":0,"activitySponsors":"10000102","activityOrganizers":[],"signStart":0,"signEnd":0,"cosponsorIds":"986459886701383681,999917216981979140","aciUserId":[],"abiRangeId2":"10000206","abiWeightDate":"","signinStartTime":"","signinEndTime":"","signoutStartTime":"","signoutEndTime":"","signStartTime":"","abiRegistrationDeadline":"","remindContent":"","cosponsorNames":"19920180003","cosponsorNos":"061516551","abiType":0,"activityCategorys":"10000700","abiCategory":"学术科技类","remindTimes":0,"remindTime":""}
    url='http://admin2.join-inapp.com/api/activitybaseinfo/editData/0'
    Edit=req.post(url,data)
    print(Edit.text)

def audit1():
    listurl='http://admin2.join-inapp.com/api/activitybaseinfo/getData/0'
    getlist=req.get(listurl)
    a=getlist.json()
    id=a['data']['queryData'][0]['id']
    urlaudit1='http://admin2.join-inapp.com/api/activitybaseinfo/auditData/1'
    urlauditdata={
    'id':id,'abiWeight':0, 'haveExpenses':	0,'allowComment':	2,'commentAudit':	1,'abiChargeName':'','abiChargeNo':'','abiChargeMobile':'','abiSupervisorName':'','abiSupervisorMobile':'','isCanCancel':'0','isArtificialMark':'0','abiWeightDate':'','auditContent':'','aalState':'2','activityCategorys':'10000703','abiCategory':'综合实践类','abiType':'0','remindTimes':'0','remindTime':''
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
    urlauditdata={'id':id,'abiWeight':0,'haveExpenses':	0,'allowComment':	2,'commentAudit':	1,'abiChargeName':'','abiChargeNo':'','abiChargeMobile':'','abiSupervisorName':'','abiSupervisorMobile':'','isCanCancel':'0','isArtificialMark':'0','abiWeightDate':'', 'auditContent':'', 'aalState':'2', 'activityCategorys':'10000703','abiCategory':'综合实践类','abiType':'0', 'remindTimes':'0','remindTime':''
    }
    audit=req.post(urlaudit1,urlauditdata)
    print(audit.text)
    time.sleep(3)


def api_login():
    api_url='http://api2.join-inapp.com/api/user/loginData'
    data={"access_token": "",
    "appKey": "10000304",
    "loginName": "13418914293",
    "password": "00000000",
    "platformType": "Android",
    "ubiId": 10000002}
    response=req.post(api_url,data=data)
    print(response.text)
    return  response.text
def api_add():

    url='http://api2.join-inapp.com/api/activitybaseinfo/addData'
    response=req.post(url,data=data)
    print(response.text)
    return response.text

if __name__=='__main__':
    #
    login()
    add(data())
    # edit()
    # add(data_223)
    # api_login()
    # api_add()

    audit1()
    audit2()




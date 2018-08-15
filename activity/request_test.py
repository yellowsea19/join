import requests
url='http://admin2.join-inapp.com/api/main/loginData'
data={
    'login_name':'13111111111',
    'password':'Jy123456'
}
dataadd={'signStart':0,
'signEnd':0,
'bannerUrl':'/uploads/2017/10/20/9299e925-09ac-470f-8d1c-8f64734641fe.jpg',
'abiWeightDate':'',
'signinEndTime':'',
'signoutStartTime':'',
'signoutEndTime':'',
'signStartTime':'',
'abiRegistrationDeadline':'',
'abiName':'0305003',
'activitySponsors':'10000102',
'abiDescription':'<p>123啊啊</p>',
'abiPurpose':'456哎哎哎',
'imgUrl[]':'/uploads/2017/10/20/9299e925-09ac-470f-8d1c-8f64734641fe.jpg',
'imgUrl[]':'/uploads/2017/10/20/a8d64ad8-3158-44af-957c-a86c3e655c10.jpg',
'abiSignOpen':0,
'abiStartTime':'2018-03-06T16:00:00.000Z',
'abiEndTime':'2018-03-07T16:00:00.000Z',
'signinType':0,
'signoutType':0,
'haveExpenses':0,
'abiGpsPlace':'北京市北京市东城区中华路甲10号',
'maxSignTimes':0,
'isArtificialMark':0,
'abiWeight':0,
'allowComment':2,
'commentAudit':1,
'abiChargeName':'',
'abiChargeNo':'',
'abiChargeMobile':'',
'abiSupervisorName':'',
'abiSupervisorMobile':'',
'isCanCancel':0,
'remindContent':'',
'sortno':1,
'abiSignRequire':'',
'abiPublishId':	10001112,
'limitSignNum':	10,
'abiValidHour':	20,
'abiGpsLat':	39.90726,
'abiGpsLng':	116.391393,
'abiSponsor':	'校学生会',
'mustSignTimes':	0,
'abiRangeId1[0][uoiId]':	10001302,
'abiRangeId1[0][uoiName]':	'脚印学生会',
'abiRangeId1[0][uoiType]':	7,
'abiRangeId1[0][allowCount]':	5,
'abiRangeId1[0][$$hashKey]':	'object:5036',
'abiRangeId1[1][uoiId]':	10000205,
'abiRangeId1[1][uoiName]':	'少年班学院',
'abiRangeId1[1][uoiType]':	4,
'abiRangeId1[1][allowCount]':	5,
'abiRangeId1[1][$$hashKey]':	'object:5037',
'activityCategorys':	10000704,
'abiCategory':	'文艺体育类',
'abiType':	0,
'remindTimes':	0,
'remindTime':''
}
req=requests.session()
response=req.post(url,data)
f=response.text
print(f)
urladd='http://admin2.join-inapp.com/api/activitybaseinfo/addData/0'
f=req.post(urladd,dataadd)
text=f.text
print(text)
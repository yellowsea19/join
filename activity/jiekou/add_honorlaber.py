import requests

data2={'dataAry':[{"sdiName":"test001","scdId":10000500,"pid":0,"path":",0,","isShow":1,
	   "sdiValue":"[{\"name\":\"分类名称\",\"value\":[\"001\",\"002\"]},"
				  "{\"name\":\"类别二\",\"value\":[\"003\",\"004\",\"005\"]}]",
	   "sortno":10,"children":[{"sdiName":"[\"001\",\"003\"]","scdId":10000500,"isShow":1,"sortno":1,"sdiValue":"[1,1,1]"},
							   {"sdiName":"[\"001\",\"004\"]","scdId":10000500,"isShow":1,"sortno":2,"sdiValue":"[1,1,1]"},
							   {"sdiName":"[\"001\",\"005\"]","scdId":10000500,"isShow":1,"sortno":3,"sdiValue":"[1,1,1]"},
							   {"sdiName":"[\"002\",\"003\"]","scdId":10000500,"isShow":1,"sortno":4,"sdiValue":"[1,1,1]"},
							   {"sdiName":"[\"002\",\"004\"]","scdId":10000500,"isShow":1,"sortno":5,"sdiValue":"[1,1,1]"},
							   {"sdiName":"[\"002\",\"005\"]","scdId":10000500,"isShow":1,"sortno":6,"sdiValue":"[1,1,1]"}]}],
	   "delIdAry":"",
	   'optDataType':2
	   }

data1={'dataAry':{"sdiName":"6r3","scdId":10000500,"pid":0,"path":",0,","isShow":1,"sdiValue":"","sortno":23,"children":[]}}
req=requests.session()
def login():
    # url='http://admin2.join-inapp.com/api/main/loginData'
    # url='http://admin2.join-inapp.com/api/main/loginData'
    url='http://10.0.0.223:8001/api/main/loginData'

    data={ 'login_name':'13499999999',
             'password':'11111111'    }
    response=req.post(url,data)
    f=response.text
    print(f)
def add(data):
    url='http://10.0.0.223:8001/api/sysdictionaryinfo/skueditData/10000500'
    response=req.post(url=url,data=data)
    print(response.text)

login()
add(data1)
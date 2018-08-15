
import requests
req=requests.session()
url='http://admin2.join-inapp.com'
def login():

    url='http://admin2.join-inapp.com/api/main/loginData'
    data={
        'login_name':'13418914293',
        'password':'00000000'
    }
    response=req.post(url,data)
    f=response.status_code
    print(f)
def get_activity_list():
    urllist=url+'/api/activitybaseinfo/getData/0'
    data={
        # 'abiName_0': 21,
        # 'abiOrganizer_0': 21,
        # 'abiSponsor_0': 21,
        # 'access_token': "createDate: ",
        'limit': 18,
        # 'offset': 0,
        'page': 1,
        # 'search_select_type': 0,
        # 'sort': "createDate,desc",
        # 'updateDate': ""
    }
    response=req.post(urllist,data=data)
    f=response.json()
    for i in f['data']['queryData']:
        print(i)
login()
get_activity_list()
def read_idlist():
    '''从idlist.txt中获取活动ID值'''
    idlist=[]
    with open (r'e:\activity\testcase\idlist.txt','r+') as f:
        number=f.readlines()
        for id in number:
            newid=id.replace("\n",'')
            idlist.append(newid)
        f.close()
    return idlist


if __name__=='__main__':
    id_list=read_idlist()
    print(id_list)
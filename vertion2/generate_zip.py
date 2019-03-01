import os
import shutil
import zipfile


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

def zipDir(dirpath,outFuilName):
    zip = zipfile.ZipFile(outFuilName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')
        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()


def get_zip(user):
    #获取主路径
    father_path = os.getcwd()
    print(father_path)

    #获取导出的文件的路劲
    result_path = os.path.join(father_path, "result")

    #删除整个result的原来的文件
    del_file(result_path)

    #删除result的文件夹
    ls = os.listdir(result_path)
    for element in ls:
        path = os.path.join(result_path, element)
        print(path)
        os.removedirs(path)
    os.makedirs(result_path)

    #获取Media 的路径
    static_path = os.path.join(father_path,"static")
    media_path = os.path.join(static_path,"media")
    user_passport = os.path.join(media_path,"user_passport")
    user_photo = os.path.join(media_path,"user_photo")

    #创建文件夹
    for element in user:
        path = os.path.join(result_path,element["First_Name"]+" "+element["Last_Name"])
        os.makedirs(path)
        split1 = element["photo"].split(".")
        split2 = element["Passport_Information_Page"].split(".")

        #复制头像文件
        oldname = os.path.join(user_photo,element["photo"])
        newname = os.path.join(path,"photo"+"."+split1[-1])
        f = open(newname, 'w+')
        f.close()
        shutil.copyfile(oldname, newname)

        # 复制护照文件
        oldname = os.path.join(user_passport, element["Passport_Information_Page"])
        newname = os.path.join(path, "passport" + "."+split2[-1])
        f = open(newname, 'w+')
        f.close()
        shutil.copyfile(oldname, newname)

    #复制excel文件
    excel_path = os.path.join(father_path,"result.xls")
    new_excel_path = os.path.join(result_path,"result.xls")

    shutil.copyfile(excel_path, new_excel_path)

    zip_path = os.path.join(father_path,"result.zip")
    zipDir(result_path,zip_path)




# alllist=os.listdir(u"D:\\notes\\python\\资料\\")
# for i in alllist:
#     aa,bb=i.split(".")
#     if 'python' in aa.lower():
#         oldname= u"D:\\notes\\python\\资料\\"+aa+"."+bb
#         newname=u"d:\\copy\\newname"+aa+"."+bb
#         shutil.copyfile(oldname,newname)



#
# user =  [{"First_Name":"lily","Last_Name":"Kaka","Passport_Information_Page":"1@bjtu.edu.cndcgan_network.jpg","photo":"1@bjtu.edu.cn未命名文件.jpg"},
#          {"First_Name": "Dave","Last_Name":"mama", "Passport_Information_Page": "1@bjtu.edu.cn皇族.png","photo": "1@bjtu.edu.cn背景图片.jpg"}]
#
# get_zip(user)
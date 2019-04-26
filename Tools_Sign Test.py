# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 9:36
# @Author  : B2e4i
# @Email   : admin@Blcat.cn
# @File    : Tools_Sign

#测试版需要手动提交自己的用户名和密码字段等等信息
import requests
import re

print("\n[*]..........Tools土司论坛自动签到工具.........[*]")
print("[*]...............By Be24i.....................[*]")
print("[*]..........Email：admin@Blcat.cn.............[*]")
print("[*]......学习Python版本，不喜勿喷大牛们！......[*]\n")

s = requests.Session()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
           "Referer": "www.baidu.com",
           "X-Requested-With": "XMLHttpRequest"
           }
#自主抓包提交参数
formdata1={'formhash':'XXXX',
          'referer':'https://www.t00ls.net/index.php',
          'loginfield':'XXXX',
          'username':'XXXX',
          'password':'XXXXXX',
          'questionid':'XXXX',
          'answer':'XXXX',
          'cookietime':'XXXX'
          }
url ="https://www.t00ls.net/logging.php?action=login&loginsubmit=yes&floatlogin=yes&inajax=1"
url2 ="https://www.t00ls.net/ajax-sign.json"
tools =s.post(url,data =formdata1,headers=headers)

headers2={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5773.400 QQBrowser/10.2.2059.400',
          'Referer':'https://www.t00ls.net/members-profile-120032.html',
          'X-Requested-With': 'XMLHttpRequest',
          }
formdata={'formhash':'2a6af27a',
          'signsubmit':'apply',
          }
Tools =s.post(url2,data=formdata,headers=headers2)

ToolsPOC=Tools.text
lang =tools.text
res_th =r'<p>(.*?)<font color=".*?">(.*?)</font>(.*?)</p>'
m_tr = re.findall(res_th, lang, re.S | re.M)
for line in m_tr:
    print(line)

ToRe =ToolsPOC[28:39]

if ToRe !='alreadysign':
    print("\n[*]Hei Boy，签到成功了！！")
else:
    print("\n[*]签到失败可能是已经签到了也或许是程序Bug，请手动签到！")

exit()
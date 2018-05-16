import requests
from mail import send_mail

url = 'http://www.allcpp.cn/allcpp/ticket/getTicketTypeList.do'
data = {
    'eventmainid': 450
}
headers = {
    'Host': 'www.allcpp.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Origin': 'http://www.dianping.com',
    'Referer': 'http://www.allcpp.cn/m/e/450/ticket.do',
    'Cookie': 'JALKSJFJASKDFJKALSJDFLJSF=183122104165daf6d371580142f7b1f56a76ee3de0d1223.167.62.204_633965124; JSESSIONID=62BD4B0BF9CF566CA3A9B4A7EADA11CD; token=43971884377E14018B997B6E1D68B491F94562BE594902C018D5EF13DB98C7FC201246381685EC74E9DA49E909D70E3993D20802E4DE09A74B320C73A2A0D4F3; Hm_lvt_75e110b2a3c6890a57de45bd2882ec7c=1526484787; Hm_lpvt_75e110b2a3c6890a57de45bd2882ec7c=1526484787'
}
r = requests.post(url, headers=headers, data=data)

value = []
flag = False
for item in r.json()['ticketTypeList']:
    value.append(item['ticketTypeName'] + str(item['remainCount']))
    print(value)
    if item['ticketTypeName'] == 'D1-CP22普通票' and item['remainCount'] > 0:
        flag = True

if flag:
    status = send_mail('\n'.join(value), '1101022351@qq.com')
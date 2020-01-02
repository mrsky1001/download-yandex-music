import requests

url = 'https://music.yandex.ru/users/Nikita.nk16/playlists/101'
headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en;q=0.9,la;q=0.8',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '68',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Host': 'mc.yandex.ru',
    'Origin': 'https://music.yandex.ru',
    'Referer': 'https://music.yandex.ru/users/Nikita.nk16/playlists/101',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 YaBrowser/19.12.3.320 Yowser/2.5 Safari/537.36',
    'Cookie': "yandexuid=2846864621566360018; _ym_uid=1566360030901213383; mda=0; my=Yy4BAQA=; yandex_gid=66; yuidss=2846864621566360018; L=eQ10AgJFf0FSW015TWFxCQBjY0pgVFtKGFA9PQQPWgVSQ3E=.1577605077.14094.348300.2932acb082e2bb69ab510881382876c2; yandex_login=Nikita.nk16; i=GBWGD8R+Z+BjOO9O1L/UQmy/GaoaDe3+zmj2l251KvIeB2kTDSfeqdNaSzFc5B9ji5AsAcUvGSycWHfjZ+QaagQYUwc=; zm=m-white_bender.webp.css-https%3As3home-static_ZQ44p_Cgt35Ibd2eEt3hqtZfkcc%3Al; Session_id=3:1577864329.5.0.1566360119803:6QleAg:6.1|130658527.0.2|291579288.463060.2.2:463060|210383.839713.pRYnJA_h5zMZsFFufAXqSIaNuDQ; sessionid2=3:1577864329.5.0.1566360119803:6QleAg:6.1|130658527.0.2|291579288.463060.2.2:463060|210383.678022.QqHm_nWviSHO8Q6jI2NXWw9zeDk; _ym_isad=1; yc=1578216290.zen.cach%3A1577960687; HgGedof=1; cycada=1RdNBZjMbizIbB8Jd87uTAO8m17c1SJbhV7GNJFEFQA=; lastVisitedPage=%7B%22130658527%22%3A%22%2Fusers%2FNikita.nk16%2Fplaylists%2F101%22%7D; _ym_d=1577982426; instruction=1; device_id=\"a7edb7cc1002e009b71d292a38d63095433254e0b\"; active-browser-timestamp=1577982650312; ys=ead.C5C8A923#def_bro.1#svt.1#ymrefl.6B2BA9E9873F5851#mclid.2270456#wprid.1577984856537396-322231475364339298700124-man1-4034#ybzcc.ru; yabs-frequency=/4/2G0A05aZ3bv4FWXU/nEHoS1Gv8RFjSd0KEK7-xN9m53aXUl8zRHGv9r21Fcq8EITyyZrj13adU_8zRGGv9vXCFcqKEI0bKR1m53aW/; yp=1608819031.brd.0500000134#1608819031.cld.2270452#1881720029.yrtsi.1566360029#1597896057.p_sw.1566360056#1593548142.szm.1%3A1280x1024%3A1280x912#1892965077.udn.cDpOaWtpdGEubmsxNg%3D%3D#1599324616.ygu.1#1882183179.multib.1#1578236044.csc.2#1603622389.stltp.serp_bk-map_1_1572086389#1892224675.sad.1573739089%3A1576864675%3A2#1579677232.nps.15410233%3Aclose#1578056779.zmblt.1462#1578056779.zmbbr.yandexbrowser%3A19_12_3_320#1578241626.clh.2270456"
}

r = requests.get(url, headers=headers)
with open('test.html', 'w') as output_file:
    output_file.write(r.text)

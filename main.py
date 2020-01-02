import requests
url = 'https://music.yandex.ru/users/Nikita.nk16/playlists/101'
r = requests.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text.encode('cp1251'))
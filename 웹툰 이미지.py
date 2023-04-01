import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

for q in range(1, 11, 1):
      url = 'https://comic.naver.com/webtoon/detail?titleId=648419&no={0}'.format(q)
      site = requests.get(url, headers=headers)
      source_data = site.text

      pos1 = source_data.find('<meta property="og:title" content="')+ len('<meta property="og:title" content="')
      source_data = source_data[pos1:]

      pos2 = source_data.find('">')
      a_data = source_data[: pos2].strip()
      source_data = source_data[pos2+1:]
      
      count2 = source_data.count(' alt="comic content')

      for u in range(count2):

            pos3 = source_data.find('background:#FFFFFF">')+ len('background:#FFFFFF">')
            source_data = source_data[pos3:]

            pos4 = source_data.find('<img src="')+ len('<img src="')
            source_data = source_data[pos4:]

            pos5 = source_data.find('"')
            b_data = source_data[: pos5]
                        
            source_data = source_data[pos5+1:]
            print(u+1, a_data, b_data)
            try:
                  file_name = './webtoon2/{0}{1}.{2}'.format(a_data, u+1, b_data[-3:])
                  ss = requests.get(b_data, headers=headers)
                  file = open(file_name, 'wb')
                  file.write(ss.content)
                  file.close()
            except Exception as e:
                  print('에러발생 : ', e)
           

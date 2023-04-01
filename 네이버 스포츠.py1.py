import requests


headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

for date in range(4, 70, 1):
      url = 'https://sports.news.naver.com/news?oid=109&aid=000481981{0}'.format(date)
      site = requests.get(url, headers = headers)
      source_data = site.text

      count = source_data.count('<h4 class="title">')

      for i in range(count):

            pos1 = source_data.find('<h4 class="title">')+ len('<h4 class="title">')
            source_data = source_data[pos1:]

            pos2 = source_data.find('</h4>')
            a_data = source_data[: pos2]

            pos3 = source_data.find('<a target="_blank" href="')+ len('<a target="_blank" href="')
            source_data = source_data[pos3:]

            pos4 = source_data.find('" class="press_link">기사원문</a>')
            b_data = source_data[: pos4]

            pos5 = source_data.find('class="end_photo_org"><img src="')+ len('class="end_photo_org"><img src="')
            source_data = source_data[pos5:]

            pos6 = source_data.find('" alt="" />')
            c_data = source_data[: pos6]

            source_data = source_data[pos6+1:]
            print(i+1, a_data, b_data, c_data)
            try:
                  file_name = './webtoon2/{0}{1}{2}.{3}'.format('야구', a_data, i+1, c_data[-14:])
                  ss = requests.get(a_data, headers=headers)
                  file = open(file_neme, 'wb')
                  file.write(ss.content)
                  file.close()
            except Exception as e:
                  print('에러발생 : ', e)

            
      

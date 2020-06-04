import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)


# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# 지니차트의 읽어오고자 하는 부분을 크롬 검사 -> copy -> copy selector 로 복사하여 괄호 안의 부분을 아래처럼 하고 
# chart_infos 변수에 집어넣음
chart_infos = soup.select('#body-content > div.newest-list > div > table > tbody > tr')                                                      

for chart_info in chart_infos :

    #순위 스크래핑
    #rank = tr.select_one('td.number').text[0:2].strip()
    rank = chart_info.select_one('td.number')       
    rank = rank.text.strip().split('\n')[0]
    

    #제목 스크래핑
    title = chart_info.select_one('td.info > a.title.ellipsis')
    title = title.text.strip()
    # print(title)

    #가수 스크래핑
    singer = chart_info.select_one('td.info > a.artist.ellipsis')
    singer = singer.text.strip()

    print(rank,'-',title,'-',singer)

     
import requests
from bs4 import BeautifulSoup
import re
def film_pars(film_name):

    session = requests.Session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Accept-Language': 'en-US',
    }
    #https://habr.com/ru/post/337420/
    #https://www.avito.ru/sankt-peterburg/avtomobili?q=bmw+525
    #film_name='godzilla'
    url = f'https://www.imdb.com/find?q={film_name}&ref_=nv_sr_sm'#делаем поиск film_name всех похожих фильмов 
    #print(url)
    r = session.get(url)
    #print(r.text)
    #print(r.text)
    soup = BeautifulSoup(r.content, 'html.parser')



    ###думаю лучше забирать название и год прямо из списка фильмов ---------
    #print(soup.prettify())
    quotes = soup.find('td', class_='result_text')#забираем первый попавшийся фильм из поиска
    print(quotes)
    print('huy'+quotes.text)
    filter = re.compile(r'[(]\d\d\d\d[)]')
    year = filter.search(quotes.text)
    year = year.group(0)

    text = quotes.text.replace(' '+year, '')
    year = year[1:-1]
   # text_year=quotes.text.split('(')
   # print(text_year)
    #text=text_year[0]
    if text[0]==' ':
        text=text[1:]
    if text[-1]==' ':
        text=text[:-1]
    print(text)
    #year = text_year[1].split(')')[0]


   # print(year.group(0))
    print(year)
    quotes = quotes.find('a')
    print(quotes)
    
    film_name1=text
    str_year=year
    #for tag in quotes:
        #print(tag.get('href'))
    link=quotes.get('href')#берём на него ссылку
    #link =quotes.find('a')
    #print(link)
    last_url='https://www.imdb.com/'+link
    print(last_url)
    r = session.get(last_url)#и теперь парсим уже страничку с этим фильмом
    soup = BeautifulSoup(r.content, 'html.parser')
    #try:
    rating_parse = soup.find('span', class_='AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV')#Название    фильма god na samom dele
    rating=rating_parse.text
    print(rating)
   # print(quotes)
   # print(quotes.text)

    #тут ищем #+год
    #quotes = quotes.find('h1',)#--------------
    #print(quotes.text)
    #year = quotes.text[-7:]
   # film_name1=str(quotes.text[:-7])#-------------

   # print('ИМЯ ИМЯ'+str(film_name1))
    #print(film_name1)



    #subtext
    '''
    year=soup.find('div', class_='subtext')
    year = year.find_all('a')
    year=year[-1].text
    counter=4
    print(year)
    str_year=''
    for i in year:
        if counter==0:
            break
        try:
            int(i)+1
            str_year+=i
            counter-=1
        except:
            counter=4
            str_year=''
            pass

    print(year)
    '''
    '''
    try:
        quotes = soup.find('div', class_='ratingValue')#рейтинг
        rating=quotes.text.split()[0][:-3]
        print(rating)
    except:
        rating=0
        print(rating)
    '''
  #  quotes = soup.find('div', class_='ratingValue')#рейтинг
  #  rating=quotes.text.split()[0][:-3]
   # print(rating)

    
    '''
    quotes = soup.find_all('div', class_='credit_summary_item')#парсим актёров

    print(quotes[2].text)
    stars= quotes[2].text.split('\n')
    stars_1=stars[2]
    stars_1 = re.sub('[| ]', '', stars_1)
    stars_1=stars_1.split(',')#массив с актёрами

    print(stars_1)
    '''

    #СТАРЫЕ ЖАНРЫ
 #   ipc-metadata-list-item__content-container
    genres_parse = soup.find('div', class_='ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL')
    genres_parse = genres_parse.find_all('span', class_='ipc-chip__text')
    print(genres_parse)
   # genres_parse = genres_parse.split(',')
    mass_genres=[]
    for i in genres_parse:
        mass_genres.append(i.text)
    print(mass_genres)
    #genres_parse
    genres=mass_genres
    '''
    genres_parse = soup.find_all('div', class_='ipc-metadata-list-item__content-container')#парсим жанры
    genres_parse = soup.find_all('ul', class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base')
    genres = genres_parse[4].text
    print(genres)
    '''
    #print(genres_parse)
  #  mass_all_p=[]
  #  for i in genres_parse:
    #    print(i.text)
      #  mass_all_p.append(i.text)
  #  print(mass_all_p)
    #print(genres_parse.text)
    '''
    quotes = soup.find_all('div', class_='see-more inline canwrap')#парсим жанры
    #quotes = quotes.find_all('a', class_='see-more inline canwrap')
    #quotes[-1].text
    #print(quotes[-1])
    quotes = quotes[-1].find_all('a')
    #print(quotes.text)
    mass=[]
    for i in quotes:
        #print(i.text)
        i=i.text[1:]
        mass.append(i)
    #print(mass)#МАССИВ С ЖАНРАМИ
    genres = mass
    print(genres)
    '''
    ######описание
    descr_parse = soup.find('div', class_='GenresAndPlot__ContentParent-cum89p-8 bFvaWW Hero__GenresAndPlotContainer-kvkd64-11 twqaW')
    descr_parse = descr_parse.find('span', class_='GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD')
    print('------------------------')
    print(descr_parse.text)
    string = descr_parse.text
   # print(quotes.prettify())
    #GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD
    '''
    descr_parse = soup.find('span', class_='GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD')
    print(descr_parse.text)
    descr=descr_parse.text
    quotes = soup.find('div', class_='plot_summary')
    quotes = soup.find('div', class_='summary_text')
    string=quotes.text
    string=string.replace("                    ", "")
    print(string)
    '''
    '''
    quotes = soup.find('div', class_='inline canwrap')#описание
    #print(quotes.text)
    string=quotes.text
    while "  " in str(string):
        string= str(string).replace("  ", " ")
    #string=string.replace('\n', '')
    string=string.replace('\n\n', '')[1:]
    print(string)#переменная с описанием
    '''
    quotes = soup.find_all('img')#ФОТКА
    #for i in quotes:
    #   print(i.text)
    #print(quotes)

    quotes=quotes[1]
    photo1=quotes.get('src')
    print(photo1)

    direc_parse = soup.find('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
    print(quotes)
    direc=direc_parse.text
    print(direc)
    #quotes = quotes.find_all('a', class_='see-more inline canwrap')
    #quotes[-1].text
    #print(quotes[-1])
   # quotes = quotes.find_all('a')
    #print(quotes[0].text)
   # direc = quotes[0].text
    #direc=direc.replace("'", "''")
    #tr
    '''
    mass=[]

    quotes = soup.find_all('tr', class_='odd')#парсим жанры
    for i in quotes:
        mass.append(i.find_all('td'))
    '''
    #quotes = quotes.find_all('a')
    #print(quotes.text)
    #print(mass)
    '''
    quotes = soup.find_all('td', class_='primary_photo')
    mass2=[]
    for i in quotes:
        mass2.append(i.find_all('img'))
        
    #print(mass2)
    mass=[]
    for i in mass2:
        print(i[0].get('title'))
        mass.append(i[0].get('title'))
    print(mass)
    string_stars=''
    for i in mass:
        string_stars+=i+','
    string_stars=string_stars[:-1]
    string_stars=string_stars.replace("'", "''")
    '''
    #ipc-metadata-list-item__content-container
    stars_parse = soup.find('li', class_='ipc-metadata-list__item ipc-metadata-list-item--link')
    stars_parse = stars_parse.find('div', class_='ipc-metadata-list-item__content-container')
    stars_parse = stars_parse.find_all('li', class_='ipc-inline-list__item')
    mass_stars=[]
    mass_lastst=[]
    string_stars=''
    for i in stars_parse:
        mass_stars.append(i.text)
    for i in mass_stars:
        string_stars+=i+','
    string_stars=string_stars[:-1]
    print(string_stars)
    #print(stars_parse.text)
    #stars=stars_parse.text
    return [film_name1, str_year, rating, genres, string, photo1, direc, string_stars]
    #quotes = quotes.find('itemprop')
    #print(quotes)


    #выведет <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>

    #print(quotes.)
    #for quote in quotes:
    #    print(quote.text.strip())


def film_parse_for_name(film_name):
    session = requests.Session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Accept-Language': 'en-US',
    }
    #https://habr.com/ru/post/337420/
    #https://www.avito.ru/sankt-peterburg/avtomobili?q=bmw+525
    #film_name='godzilla'
    url = f'https://www.imdb.com/find?q={film_name}&ref_=nv_sr_sm'#делаем поиск film_name всех похожих фильмов 
    #print(url)
    r = session.get(url)
    #print(r.text)
    #print(r.text)
    soup = BeautifulSoup(r.content, 'html.parser')

    quotes = soup.find('td', class_='result_text')#забираем первый попавшийся фильм из поиска
    #print(quotes)
   # print('huy'+quotes.text)
    text_year=quotes.text.split('(')
    #print(text_year)
    text=text_year[0]
    if text[0]==' ':
        text=text[1:]
    if text[-1]==' ':
        text=text[:-1]
    film_name1=text
    print(text)
    return film_name1
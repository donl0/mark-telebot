from .dbcommands import genre_create, film_create, stars_create, directors_create, push_video_link
from .imdb_film_pars import film_pars
import re


async def film_filler(film_name, link):

    if film_name[0]=='-':
        film_name=film_name[1:]
        film_data=film_pars(film_name)
        print(link)
        link=str(link)
        await push_video_link(film_name, link)
     #   cursor.execute(f"UPDATE films_list SET `full link`='{link}' WHERE instr(name_film, '{film_data[0]}')")
       
    else:
        film_data=film_pars(film_name)
        

        #print(film_data)
        #print(film_data[0])
        print(film_data)
        film_data[0]=film_data[0].replace('\xa0', ' ')
        film_data[3]=str(film_data[3]).replace("[","")
        film_data[3]=str(film_data[3]).replace("]","")

        #film_data[4]=film_data[4].replace('\n', '  ')
        #film_data[4]=film_data[4].replace('\n', ' ')
        film_data[3]=str(film_data[3])
        
        film_data[4]=str(film_data[4])
        film_data[4]=str(film_data[4]).replace("<","''")
        film_data[4]=str(film_data[4]).replace(">","''")
        nameD = re.compile(r'(Written by)[\s\S]+')
        film_data[4] = nameD.sub('', film_data[4])

        film_data[7] = film_data[7].split(',')#to make mass

        film_data[3] = film_data[3].split(',')
        i = 0
        for genre in film_data[3]:
            if genre[0] == ' ':
                film_data[3][i] = genre[1:]

            i += 1
    # print(film_data)
        #film_data[0]=film_data[0].encode('utf8')
        #return [film_name, year, rating, mass, string] 0,3
        #cursor.execute(f"UPDATE `films_list` SET name_film='Harry Potter and the Sorcerer''s Stone\xa0' WHERE id = 5")

        # film_data[0] - film name - string
        # film_data[1] str_year - int
        # film_data[2] - rating float
        # film_data[3]  genres	text
        #сейчас жанры это тупо строка, нужно на самом деле
        # делать get_or_create в бд с жанрами, чтобы создать все новые забранные жанры
        # после чгео помещать в жанры фильма все связаные с ним жанры
        # для этого нужно сделать из строки массив, после чего создание всех жанров в бд жанров
        # и теперь уже привязывать фильму
        # то же самое со актёрами и директором
        # film_data[4] descriotion	text


        # film_data[5] photo str
        # film_data[6] dictor str
        # film_data[7] stars str

       #film_name = models.CharField(verbose_name="name", max_length=100, default="NULL")
        #year = models.CharField(max_length=5, default="NULL")
       # rating = models.CharField(max_length=5, default="NULL")
       # genres = models.ManyToManyField(Genres, blank=True)

       # description = models.CharField(max_length=1500, default="NULL")

       # director = models.ManyToManyField(Director, blank=True)
        #stars = models.ManyToManyField(Stars, blank=True)

        #video_link = models.CharField(verbose_name="video link", max_length=200, default="NULL")
       # video_file = models.FileField(verbose_name='video', upload_to='videos/', default="NULL")

        film_info={'film_name': film_data[0],
                   'year': film_data[1],
                   'rating': film_data[2],
                   'description': film_data[4],
                   'photo': film_data[5],
                   'trailer_link': link}

        await genre_create(film_data[3])
        await stars_create(film_data[7])
        await directors_create(film_data[6])
        await film_create(film_info, film_data[3], film_data[7], film_data[6])


      #  cursor.execute(f"INSERT INTO `films_list` (`name_film`, `year`, `rating`, `genres`, `descriotion`, `link`, `top_24`, `top_7`, `top_mounth`,  `likes`,  `dislikes`, `comments`, `comments counter`, `full link` ,`all views`, `photo`, `Director`, `Stars`, `id`) VALUES ('{film_data[0]}', {film_data[1]}, '{film_data[2]}', '{film_data[3]}', '{film_data[4]}', '', 0,0,0,0,0,'', 0, '',0,'{film_data[5]}', '{film_data[6]}', '{film_data[7]}',NULL);")
      #  cursor.execute(f"UPDATE films_list SET `link`='{link}' WHERE name_film = '{film_data[0]}'")



        #cursor.execute(f"INSERT INTO `films_list` (`name_film`, `year`, `rating`, `genres`, `descriotion`, `link`, `id`) VALUES ('{film_data[0]}', {film_data[1]}, '{film_data[2]}', '{film_data[3]}', '{film_data[4]}', '{link}', NULL);")
        #cursor.execute(f"INSERT INTO `films_list` (`name_film`, `year`, `rating`, `genres`, `descriotion`, `link`, `id`) VALUES ('{film_data[0]}', '{film_data[1]}', '{film_data[2]}', '{str(film_data[3])}', '{film_data[4]}', 'ссфлк сюда', NULL);")
   # conn.commit()

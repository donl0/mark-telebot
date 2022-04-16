from asgiref.sync import sync_to_async







@sync_to_async
def get_from_user_counter_to_mark(user):
    return user[0].manyToMark

@sync_to_async
def get_from_user_counter_marked(user):
    return user[0].markCounter

@sync_to_async
def get_from_user_marked_by_someone(user):
    return user[0].markBySomeone


@sync_to_async
def get_from_film_requests(list):
    mass_films = []
    mass_process = []
    print(list)
    list = tuple(reversed(list))
    for i in range(len(list)):
        mass_films.append(list[i].film_name)
        mass_process.append(list[i].verification_process)
    return mass_films, mass_process

@sync_to_async
def get_from_user_counter_marked_me(user):
    return user[0].counterMarkedMe

@sync_to_async
def get_id_from_user(user):
    return user[0].id_tele

@sync_to_async
def get_phone_num_from_user(user):
    return user[0].phone_num

@sync_to_async
def get_fio_num_from_user1(user):
    return user[0].fio

@sync_to_async
def plus_all_from_different_models(mass1, mass2, mass3):
    mass1=list(mass1)
    mass2=list(mass2)
    mass3=list(mass3)



    return mass1+mass2+mass3


@sync_to_async
def get_only_names_from_users(list):
    new_list=[]
    for user in list:
        new_list.append(user.fio.fio)
    return new_list


@sync_to_async
def get_only_dead_line_from_users(list):
    new_list=[]
    for user in list:
        try:
            new_list.append(str(user.dead_line)[:-6])
        except:
            new_list.append('Дедлайн не установлен')
    return new_list



def get_only_id_from_users_bo_async(list):
    new_list=[]
    for user in list:
        new_list.append(user.id_tele)
    return new_list



@sync_to_async
def get_only_id_from_users(list):
    new_list=[]
    for user in list:
        new_list.append(user.fio.id_tele)
    return new_list

@sync_to_async
def get_list_len(list):
    return len(list)

def get_list_len_no_asycn(list):
    return len(list)

@sync_to_async
def ret_list(vars):
    return list(vars)


def get_comments(list):
    new_list=[]
    for comment in list:
        new_list.append(comment.text)
    return new_list


def get_only_names2(list):
    new_list=[]
    for value in list:
        new_list.append(value.film_name)
    return new_list


@sync_to_async
def get_only_names(list):
    new_list=[]
    for value in list:
        new_list.append(value.film_name)
    return new_list

@sync_to_async
def get_job_type_from_user(user):

    return user.job_type

def get_only_fio(list):
    new_list=[]
    for value in list:
        new_list.append(value.fio)
    return new_list

def get_only_fio_from_user(user):

    return user.fio

def do_with_3_10_8_film_info(film_info3, film_info10, film_info8):
    if film_info3 != '':
        film_info3 = do3(film_info3)
    if film_info10 != '':
        film_info10 = fo10(film_info10)
    if film_info8 != '':
        film_info8 = do8(film_info8)
    return {'film_info3': film_info3,
            'film_info10': film_info10,
            'film_info8': film_info8}


# genres
def do3(film3):
    film_info = [0, 1, 2,4]
    film_info[3] = film3

    len_f_l = len(film_info[3])
    if len_f_l > 2:
        film_info[3] = str(film_info[3][0]) + ', ' + str(film_info[3][1]) + ', ' + str(film_info[3][2])
    elif len_f_l == 2:
        film_info[3] = str(film_info[3][0]) + ', ' + str(film_info[3][1])
    elif len_f_l == 1:
        film_info[3] = str(film_info[3][0])
    else:
        film_info[3] = ''
    return film_info[3]


# description
def do8(film8):
    if len(film8) > 550:
        film8 = str(film8[0:550]) + '...'
    return film8


# stars
def fo10(film_info10):
    film_info = []

    if len(film_info10) > 2:
        film_info10 = str(film_info10[0]) + ', ' + str(film_info10[1]) + ', ' + str(film_info10[2])
    elif len(film_info[10]) == 2:
        film_info10 = str(film_info10[0]) + ', ' + str(film_info10[1])
    elif len(film_info[10]) == 1:
        film_info10 = str(film_info10[0])
    else:
        film_info10 = ''
    return film_info10

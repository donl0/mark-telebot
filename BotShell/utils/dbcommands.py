from aiogram import Bot

from markBot import settings
from .tools import get_only_fio, ret_list, get_only_id_from_users
from ..models import Employment, Hr, TeamLeader, Message, AllEmployment, TopManager, Manager, Specialist, MailingRate

from asgiref.sync import sync_to_async
from django.db.models import F, Q

from ..models.colleague import Сolleague

@sync_to_async
def update_start_mark(user):
    user.update(markStart=True)


@sync_to_async
def user_exist_check_with_dict(dict):
    user = AllEmployment.objects.filter(**dict)
    print(user)
    if len(user) == 0:
        return False
    else:
        return True



@sync_to_async
def get_all_users():
    users_mass = AllEmployment.objecs.fileter()
    return users_mass

@sync_to_async
def mailing_start(message, id_users_mass):
    bot = Bot(token=settings.TG_TOKEN, parse_mode='HTML', loop=None)


    for id_tele in id_users_mass:
        print(id_tele)

        try:
            bot.send_message(id_tele, message)
        except:
            pass



@sync_to_async
def notification_rate():
    mail_info =  MailingRate.objects.filter()[0]
    return mail_info.mail_rate

@sync_to_async
def match_last_time_with_mail_rate_sync():
    mail_object = MailingRate.objects.filter()
    if mail_object[0].mail_rate==mail_object[0].time_from_last_mail+1:
        mail_object.update(time_from_last_mail=0)
        return True
        #инициировать рассыку
    else:
        mail_object.update(time_from_last_mail=F('time_from_last_mail')+1)
        return False


@sync_to_async
def get_mess_from_mail_rate_sync():
    mail_object = MailingRate.objects.filter()
    return mail_object[0].text



def match_last_time_with_mail_rate():
    mail_object = MailingRate.objects.filter()
    if mail_object[0].mail_rate==mail_object[0].time_from_last_mail:
        mail_object.update(time_from_last_mail=0)
        return True
        #инициировать рассыку
    else:
        mail_object.update(time_from_last_mail=F('time_from_last_mail')+1)
        return False

def try_to_delete_from_Manager(dict):
    instance = Manager.objects.get(**dict)
    instance.delete()



def try_to_delete_from_Spec(dict):
    instance = Specialist.objects.get(**dict)
    instance.delete()



def try_to_delete_from_Top_M(dict):
    instance = TopManager.objects.get(**dict)
    instance.delete()


@sync_to_async
def get_employers_list():
    all_employers = AllEmployment.objects.filter()
    return list(all_employers)


@sync_to_async
def get_employers_list_with_rafy_report():
    from_top_m = TopManager.objects.filter(reportIsReady=True)
    from_spec = Specialist.objects.filter(reportIsReady=True)
    from_manager = Manager.objects.filter(reportIsReady=True)
    return [from_top_m, from_spec, from_manager]






@sync_to_async
def get_employers_list_with_end_record():
    from_top_m = TopManager.objects.filter(markEnd=True)
    from_spec = Specialist.objects.filter(markEnd=True)
    from_manager = Manager.objects.filter(markEnd=True)
    return [from_top_m, from_spec, from_manager]


@sync_to_async
def get_employers_list_with_no_rady_report():
    from_top_m = TopManager.objects.filter(reportIsReady=False)
    from_spec = Specialist.objects.filter(reportIsReady=False)
    from_manager = Manager.objects.filter(reportIsReady=False)
    return [from_top_m, from_spec, from_manager]
#эту тройку надо первратить в
#reportIsReady


@sync_to_async
def get_employers_list_with_start_record():
    from_top_m = TopManager.objects.filter(markStart=True, markEnd=False)
    from_spec = Specialist.objects.filter(markStart=True, markEnd=False)
    from_manager = Manager.objects.filter(markStart=True, markEnd=False)
    return [from_top_m, from_spec, from_manager]


@sync_to_async
def get_employers_list_with_no_start_record():
    from_top_m = TopManager.objects.filter(markStart=False, markEnd=False)
    from_spec = Specialist.objects.filter(markStart=False, markEnd=False)
    from_manager = Manager.objects.filter(markStart=False, markEnd=False)
    return [from_top_m, from_spec, from_manager]

'''@sync_to_async
def make_from_models_to_main_model(users_list):
    mass_fio=[]
    for user in users_list:
        print(user)
        print(user.fio)
    
    return mass_fio'''






@sync_to_async
def user_report_is(dict_user):
    user = user_find_from_jоb_with_id_no_async(dict_user)
    user.update(reportIsReady=True)



'''  if (await many_mark_me(dict) == 0) and (await user_get_many_marked_me(dict) > 0) and (
            await marked_by_someone(dict)):
'''

def many_mark_me_no_asyns_with_user(user):
    #объект алл эмплоера
    len_from_topM=len(TopManager.objects.filter(teamLeader=user))+len(TopManager.objects.filter(colleagues=user))++len(TopManager.objects.filter(employers=user))
    len_from_M = len(Manager.objects.filter(teamLeader=user)) + len(
        Manager.objects.filter(colleagues=user)) + +len(Manager.objects.filter(employers=user))
    len_from_S =len(
        Specialist.objects.filter(colleagues=user)) +len(Specialist.objects.filter(teamLeader=user))


def many_mark_me_no_asyns(dict):
    user = user_find_get(dict)
    len_from_topM=len(TopManager.objects.filter(teamLeader=user))+len(TopManager.objects.filter(colleagues=user))++len(TopManager.objects.filter(employers=user))
    len_from_M = len(Manager.objects.filter(teamLeader=user)) + len(
        Manager.objects.filter(colleagues=user)) + +len(Manager.objects.filter(employers=user))
    len_from_S =len(
        Specialist.objects.filter(colleagues=user)) +len(Specialist.objects.filter(teamLeader=user))


@sync_to_async
def end_or_not_marking_after_yourself(dict):
    user = user_find_from_jоb_with_id_no_async(dict)
    if (user[0].markCounter > 0) and (user[0].markByHimSelf == True) and (user[0].manyToMark == 0):
        user.update(markEnd=True)

@sync_to_async
def all_user_empl(dict):
    user = user_find_from_jоb_with_id_no_async(dict)[0]
    return user.all_employers

@sync_to_async
def mark_yourself(dict):
    user = user_find_from_jоb_with_id_no_async(dict)
    user.update(markByHimSelf=True)

@sync_to_async
def increase_counter_marked_user(dict):
    user = user_find_from_jоb_with_id_no_async(dict)
    user.update(counterMarkedMe=F('counterMarkedMe')+1)


@sync_to_async
def many_mark_me(dict):
    user = user_find_get(dict)
    len_from_topM=len(TopManager.objects.filter(teamLeader=user))+len(TopManager.objects.filter(colleagues=user))++len(TopManager.objects.filter(employers=user))
    len_from_M = len(Manager.objects.filter(teamLeader=user)) + len(
        Manager.objects.filter(colleagues=user)) + +len(Manager.objects.filter(employers=user))
    len_from_S =len(
        Specialist.objects.filter(colleagues=user)) +len(Specialist.objects.filter(teamLeader=user))
    return len_from_topM+len_from_M+len_from_S



@sync_to_async
def increase_to_count(dict):
    user = user_find_from_jоb_with_id_no_async(dict)
    user.update(markCounter=F('markCounter')+1)





@sync_to_async
def remove_from_manyomany_colleagues(user_id, user_id_to_remove):
    dict_user = {'id_tele':user_id}
    user = user_find_from_jоb_with_id_no_async(dict_user)[0]
    user_to_delete = {'phone_num': user_id_to_remove}
    user.colleagues.remove(user_find_get(user_to_delete))


@sync_to_async
def remove_from_manyomany_teamLeader(user_id, user_id_to_remove):
    dict_user = {'id_tele':user_id}
    user = user_find_from_jоb_with_id_no_async(dict_user)[0]
    user_to_delete = {'phone_num': user_id_to_remove}
    user.teamLeader.remove(user_find_get(user_to_delete))


@sync_to_async
def remove_from_manyomany_employers(user_id, user_id_to_remove):
    dict_user = {'id_tele':user_id}
    user = user_find_from_jоb_with_id_no_async(dict_user)[0]
    user_to_delete = {'phone_num': user_id_to_remove}
    user.employers.remove(user_find_get(user_to_delete))


@sync_to_async
def add_to_user_teamLeader(user_name, team_lead_nme):
    dict_user = {'fio':user_name}
    user = user_find_from_jоb_with_id_no_async(dict_user)[0]
    dict_user_to_add = {'fio':team_lead_nme}
    user.teamLeader.add(user_find_get(dict_user_to_add))

@sync_to_async
def add_to_user_empl(user_name, team_lead_nme) -> object:
    dict_user = {'fio':user_name}
    user = user_find_from_jоb_with_id_no_async(dict_user)[0]
    dict_user_to_add = {'fio':team_lead_nme}
    user.employers.add(user_find_get(dict_user_to_add))

@sync_to_async
def add_to_user_coll(user_name, team_lead_nme):
    dict_user = {'fio':user_name}
    user = user_find_from_jоb_with_id_no_async(dict_user)[0]
    dict_user_to_add = {'fio':team_lead_nme}
    user.colleagues.add(user_find_get(dict_user_to_add))


@sync_to_async
def get_teamleaders_from_user(dict):
    user = user_find_from_jоb_with_id_no_async(dict)[0]
    teamLeaders = user.teamLeader.all()
    teamLeaders_fio = get_only_fio(teamLeaders)
    return teamLeaders_fio


@sync_to_async
def get_employers_from_user(dict):
    user = user_find_from_jоb_with_id_no_async(dict)[0]
    employers = user.employers.all()
    employers_fio = get_only_fio(employers)
    return employers_fio


@sync_to_async
def get_collegaues_from_user(dict):
    user = user_find_from_jоb_with_id_no_async(dict)[0]
    colleagues = user.colleagues.all()
    colleagues_fio = get_only_fio(colleagues)
    return colleagues_fio



@sync_to_async
def get_teamLeaders_from_user(dict):
    user = user_find_from_jоb_with_id_no_async(dict)[0]
    teamLeaders = user.teamLeader.all()
    teamLeaders_fio = get_only_fio(teamLeaders)
    return teamLeaders_fio


def user_find_from_jоb_with_id_no_async(dict):
    print(dict)
    user = TopManager.objects.filter(fio=AllEmployment.objects.filter(**dict)[0])
    if len(user) == 0:
        user = Manager.objects.filter(fio=AllEmployment.objects.filter(**dict)[0])
        if len(user) != 0:
            return user
        if len(user) == 0:
            user = Specialist.objects.filter(fio=AllEmployment.objects.filter(**dict)[0])
            if len(user) != 0:
                return user
    return user
#comments = user_data['comments'].append('-'+mess+'\n\n')
       # await state.update_data(comments=comments)
#answers = user_data['answers'].append(mess[0])
#await state.update_data(answers=answers)
@sync_to_async
def mark_someone(dict):
    user = user_find_from_jоb_with_id_no_async(dict)
    mark = user[0].markBySomeone
    return mark

@sync_to_async
def marked_by_someone(dict):
    user = user_find_from_jоb_with_id_no_async(dict)
    mark = user[0].markByHimSelf
    return mark
'''
def user_find_from_jоb_with_id_no_async(dict):
    user = TopManager.objects.filter(fio=AllEmployment.objects.get(**dict))
    if len(user) == 0:
        user = Manager.objects.filter(fio=AllEmployment.objects.get(**dict))
        if len(user) != 0:
            return user
        if len(user) == 0:
            user = Specialist.objects.filter(fio=AllEmployment.objects.get(**dict))
            if len(user) != 0:
                return user
    return user
'''
@sync_to_async
def user_find_from_jоb_with_id(dict):
    user = TopManager.objects.filter(fio=AllEmployment.objects.get(**dict))
    if len(user) == 0:
        user = Manager.objects.filter(fio=AllEmployment.objects.get(**dict))
        if len(user) != 0:
            return user
        if len(user) == 0:
            user = Specialist.objects.filter(fio=AllEmployment.objects.get(**dict))
            if len(user) != 0:
                return user
    return user

@sync_to_async
def get_hr_ids():
    hrs = AllEmployment.objects.filter(HR=True)
    mass_id_he=[]
    for hr in hrs:
        mass_id_he.append(hr.id_tele)
    return mass_id_he

@sync_to_async
def get_job_type2(dict):
    hr = AllEmployment.objects.get(**dict)
    return hr.job_type


@sync_to_async
def get_job_type3(dict):
    user = AllEmployment.objects.get(**dict)
    return user.HR


@sync_to_async
def get_hr(dict):
    hr = AllEmployment.objects.filter(**dict)
    if len(hr) ==0:
        return False
    else:
        return True


@sync_to_async
def type_of_job(dict):
    user = TopManager.objects.filter(fio=AllEmployment.objects.get(**dict))
    if len(user) == 0:
        user = Manager.objects.filter(fio=AllEmployment.objects.get(**dict))
        if len(user) != 0:
            return 'Manager'
        if len(user) == 0:
            user = Specialist.objects.filter(fio=AllEmployment.objects.get(**dict))
            if len(user) != 0:
                return 'Specialist'
    return 'TopManager'



@sync_to_async
def user_get_name(dict):
    user_name = user_find_async(dict)[0].name_tele
    return user_name

@sync_to_async
def user_get_many_marked_me(dict):
   # user = AllEmployment.objects.get(**dict)
    user = user_find_from_jоb_with_id_no_async(dict)
    cpunter_merked_me = user[0].markByHimSelf
    return cpunter_merked_me

@sync_to_async
def user_get_mark_myself(dict):
    user = user_find_from_jоb_with_id_no_async(dict)
    mark=user[0].markByHimSelf
    return mark


@sync_to_async
def user_find_async(dict):
    user = user_find(dict)
    return user


def user_find(dict):
    user = AllEmployment.objects.filter(**dict)

    return user

@sync_to_async
def user_find_fio(dict):
    user = AllEmployment.objects.filter(**dict)

    return user[0].fio

@sync_to_async
def get_user_fio(dict):
    user = AllEmployment.objects.get(**dict)

    return user.fio

def user_find_get(dict):
    user = AllEmployment.objects.get(**dict)

    return user

@sync_to_async
def user_start_update(phone_number, id_tele, user_name):

    dict = {'phone_num':phone_number}
    user = user_find(dict)
    if len(user) != 0:
        user.update(id_tele=id_tele,name_tele=user_name)

@sync_to_async
def user_start_update_true(phone_number, id_tele, user_name):

    dict = {'phone_num':phone_number}
    user = user_find(dict)
    print('----------')
    print(user)
    if len(user) != 0:
        user.update(id_tele=id_tele,name_tele=user_name)



@sync_to_async
def get_massage_for_question(job_type, message_id):
    if job_type=='Manager':
        pass
    elif job_type=='Specialist':
        message_id+=100
    elif job_type == 'TopManager':
        message_id += 200
    return message_id


@sync_to_async
def get_message(msg_id, base_message):
    text = Message.objects.filter(msg_id=msg_id)
    if len(text)==0:
        return base_message
    return text[0].text


def get_message_no_async(msg_id, base_message):
    text = Message.objects.filter(msg_id=msg_id)
    if len(text)==0:
        return base_message
    return text[0].text


@sync_to_async
def create_user_to_AllEmployment(dict):
   AllEmployment.objects.create(**dict)


'''
@sync_to_async
def clear24h_watches():
    Films.objects.filter().update(watches24h=0)


@sync_to_async
def clear7d_watches():
    Films.objects.filter().update(watches7d=0)


@sync_to_async
def clear1m_watches():
    Films.objects.filter().update(watches1m=0)


@sync_to_async
def add_new_requests(text, id_tele):
    Requests.objects.create(film_name=text,id_tele=int(id_tele))


@sync_to_async
def get_user_requests(id_tele):
    film_requests = Requests.objects.filter(id_tele=id_tele)
    return list(film_requests)


@sync_to_async
def get_all_last_search():
    all_search = LastSearch.objects.filter()
    return list(all_search)


@sync_to_async()
def add_to_all_last_search(film_name):
    LastSearch.objects.filter(film_name=Films.objects.get(film_name=film_name)).delete()
    LastSearch.objects.create(film_name=Films.objects.get(film_name=film_name))


@sync_to_async
def get_search_way(user_id):
    search_way = Users.objects.get(id_tele=user_id).search_way
    return search_way


@sync_to_async
def create_comment(film_name, user_id, text):
    Comments.objects.create(text=text, film_name=Films.objects.get(film_name=film_name), author=Users.objects.get(id_tele=user_id))


@sync_to_async
def get_comments_film(film_name):
    comments = Comments.objects.filter(film_name__film_name=film_name)
    return list(comments)

@sync_to_async
def get_films_by_year(year):
    films = Films.objects.filter(year=year)
    return list(films)


@sync_to_async
def get_films_by_genres(genre):
    films = Films.objects.filter(genres=Genres.objects.get(genre_name=genre))
    return list(films)

@sync_to_async
def test1(genre):
    films = Films.objects.filter(genres=Genres.objects.get(genre_name=genre))
    return list(films)


@sync_to_async
def year_genre_filter(year, genre):
    films = Films.objects.filter(year=year, genres=Genres.objects.get(genre_name=genre))
    return list(films)


@sync_to_async
def get_user_history(id_tele):
    history = Users.objects.get(id_tele=id_tele)
    print(history)
    history = list(history.history.all())
    return history


@sync_to_async
def delete_user_history(id_tele):
    Users.objects.get(id_tele=id_tele).history.clear()

@sync_to_async
def films_top_rating():
    all_films = list(Films.objects.order_by('rating'))
    return all_films


@sync_to_async
def films_top_mouth():
    all_films = list(Films.objects.order_by('watches1m'))
    return all_films


@sync_to_async
def films_top_24():
    all_films = list(Films.objects.order_by('watches24h'))
    return all_films



@sync_to_async
def get_all_films():
    all_films = list(Films.objects.filter())
    return all_films

@sync_to_async
def create_user(info):
    Users.objects.get_or_create(**info)


@sync_to_async
def user_info_by_id(user_id):
    user_info = Users.objects.get(id_tele=user_id)
    return user_info


@sync_to_async
def update_all_watches(film_name):
    film_info = Films.objects.filter(film_name=film_name)
    film_info.update(watches_all=F('watches_all') + 1)
    film_info.update(watches7d=F('watches7d') + 1)
    film_info.update(watches1m=F('watches1m') + 1)
    film_info.update(watches24h=F('watches24h') + 1)
    #Films.objects.filter(film_name=film_name).update(watches_all=F('watches_all') + 1)
    #Films.objects.filter(film_name=film_name).update(watches7d=F('watches7d') + 1)
    #Films.objects.filter(film_name=film_name).update(watches1m=F('watches1m') + 1)
    #Films.objects.filter(film_name=film_name).update(watches24h=F('watches24h') + 1)


@sync_to_async
def update_user_history(film_name, user_id):
    try:
        Users.objects.get(id_tele=user_id).history.remove(Films.objects.get(film_name=film_name))
    except:
        pass
    Users.objects.get(id_tele=user_id).history.add(Films.objects.get(film_name=film_name))


@sync_to_async
def update_general_history(film_name):
    GeneralHistory.objects.get_or_create(film_name=Films.objects.get(film_name=film_name))


@sync_to_async
def remove_new_favourite_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).favourite.remove(Films.objects.get(film_name=film_name))


@sync_to_async
def add_new_favourite_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).favourite.add(Films.objects.get(film_name=film_name))


@sync_to_async
def get_favourite_user(user_id):
    favourite_list = Users.objects.get(id_tele=user_id).favourite.all()
    favourite_list = list(favourite_list)
    return favourite_list


@sync_to_async
def remove_liked_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).liked_films.remove(Films.objects.get(film_name=film_name))


@sync_to_async
def remove_disliked_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).disliked_films.remove(Films.objects.get(film_name=film_name))


@sync_to_async
def add_new_liked_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).liked_films.add(Films.objects.get(film_name=film_name))


@sync_to_async
def add_new_disliked_film_user(film_name, user_id):
    Users.objects.get(id_tele=user_id).disliked_films.add(Films.objects.get(film_name=film_name))


@sync_to_async
def inc_comments(film_name):
    Films.objects.filter(film_name=film_name).update(comments_counter=F('comments_counter')+1)


@sync_to_async
def decrease_film_likes(film_name):
    Films.objects.filter(film_name=film_name).update(likes=F('likes') - 1)


@sync_to_async
def decrease_film_dislikes(film_name):
    Films.objects.filter(film_name=film_name).update(dislikes=F('dislikes') - 1)


@sync_to_async
def increase_film_likes(film_name):
    Films.objects.filter(film_name=film_name).update(likes=F('likes') + 1)


@sync_to_async
def increase_film_dislikes(film_name):
    Films.objects.filter(film_name=film_name).update(dislikes=F('dislikes') + 1)


@sync_to_async
def get_dislikes_from_user(user_id):
    dislikes = Users.objects.get(id_tele=user_id).disliked_films
    dislikes = list(dislikes.all())
    return dislikes


@sync_to_async
def get_likes_from_user(user_id):
    likes = Users.objects.get(id_tele=user_id).liked_films
    likes = list(likes.all())
    return likes


@sync_to_async
def update_paper_count(count_value, id_person):
    user = Users.objects.filter(id_tele=id_person)
    user.update(paper_count=count_value)


@sync_to_async
def update_search_way(search_way, id_person):
    user = Users.objects.filter(id_tele=id_person)
    user.update(search_way=search_way)


@sync_to_async
def get_all_by_all_preference_search(filter_value):
    film_info = Films.objects.filter(Q(film_name=filter_value) | Q(director__name__contains=filter_value) | Q(stars__name__contains=filter_value))
    return list(film_info)


@sync_to_async
def get_all_by_director_film(director):
    film_info = Films.objects.filter(director__name__contains=director)
    return list(film_info)


@sync_to_async
def get_all_by_star(star_name):
    film_info = Films.objects.filter(stars__name__contains=star_name)
    return list(film_info)


@sync_to_async
def get_all_by_contain_film(film_name):
    film_info = Films.objects.filter(film_name__contains=film_name)
    return list(film_info)


@sync_to_async
def get_all_by_film_name(film_name):
    film_info = Films.objects.get(film_name=film_name)
    return film_info


@sync_to_async
def get_genres_by_film_name(film_name):
    genres = Films.objects.get(film_name=film_name)
    genres = genres.genres.all()
    genres = list(genres)
    return genres


@sync_to_async
def push_video_link(film_name, link):
    Films.objects.filter(film_name=film_name).update(video_link=link)


@sync_to_async
def get_paper_count(user_id):
    paper_counter = Users.objects.get(id_tele=user_id).paper_count
    return paper_counter


@sync_to_async
def get_trending_films():
    trending = TrendingFilms.objects.filter()
    print(trending)
    print(len(trending))
    trending = list(trending)
    print(len(trending))
    return trending

@sync_to_async
def get_all_general_history():
    all_g_history = GeneralHistory.objects.filter()
    all_g_history = list(all_g_history)
    return all_g_history


@sync_to_async
def get_all_info():
    info = Films.objects.filter()
    info = list(info)
    return info[0]


@sync_to_async
def get_message(msg_id):
    text = Message.objects.filter(msg_id=msg_id)
    return text[0].text


@sync_to_async
def genre_create(genres):
    for genre in genres:
        Genres.objects.get_or_create(genre_name=genre)


@sync_to_async
def stars_create(stars):
    for star in stars:
        Stars.objects.get_or_create(name=star)


@sync_to_async
def directors_create(director):
    Directors.objects.get_or_create(name=director)


@sync_to_async
def film_create(info, genres, stars, director):
#def film_create(info):
    film = Films.objects.get_or_create(**info)
   # film = Films.objects.create(**info)
    #film_name
    #film = Films.objects.get_or_create(film_name=info['film_name'])
   # film = Films.objects.get_or_create(film_name='1')
    print(film)
  #  print(film[0])
    for genre in genres:
        #film[0].objects.update(genres=Genres.objects.filter(genre_name=genre))
        #film2 = Films.objects.filter(film_name=film[0].film_name)
       # for film_ in film2:
     #       film_.genres.add(Genres.objects.get(genre_name=genre))
        film[0].genres.add(Genres.objects.get(genre_name=genre))
    for star in stars:
        film[0].stars.add(Stars.objects.get(name=star))

    film[0].director.add(Directors.objects.get(name=director))

       # film[0].genres.add(genres=Genres.objects.filter(genre_name=genre))


@sync_to_async
def get_admin():
    admins = Admins.objects.filter()
    mass_admins = []
    for admin in admins:
        mass_admins.append(admin.admin_id)
    print(mass_admins)
   # admins = list(admins)
   # print(admins)
    return mass_admins
    #marker tools base_m
'''
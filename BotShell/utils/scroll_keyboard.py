#from handlers import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from config import admin_id
from asgiref.sync import sync_to_async

from .dbcommands import get_admin, get_trending_films, get_genres_by_film_name, get_all_by_film_name
from .tools import ret_list


async def next_page_info1(counter, film_list, len_l, open_count, id_person):
    num=0
    text=''
    #keyboard_film_list= InlineKeyboardMarkup(row_width=5)

    #film_list_trending = await get_trending_films()

    x=False
    admin_id = await get_admin()
    if id_person in admin_id:
        x=True
#нынешнее количество =  общая длинна 
#к примеру у нас длинна 25 а всего 25
    coef=open_count
    keyboard_film_list= InlineKeyboardMarkup(row_width=18)
    print(counter, open_count)
    for i in range(counter*open_count, counter*open_count+open_count):
        try:
            print(film_list[i])
            num=i+1
            film=film_list[i]

            film_j = await get_genres_by_film_name(film)

            for n in range(3):
                try:
                    film_j[n] = str(film_j[n])
                except:
                    break


            if len(film_j)>2:
                film_j=film_j[0]+', '+film_j[1]+', '+film_j[2]
            elif len(film_j)==2:
                film_j=film_j[0]+', '+film_j[1]
            elif len(film_j)==1:
                film_j=film_j[0]
            else:
                film_j=''


            text+=str(num)+') '+str(film.film_name)+'('+str(film.year)+')\nIMBb: '+str(film.rating)+' | '+film_j+'\n\n'
            print(text)
            item_f = InlineKeyboardButton(text=num, callback_data='find film_'+str(film.film_name))
            if num%7==0:
                keyboard_film_list.row(item_f)
            else:
                keyboard_film_list.insert(item_f)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            
            coef=1
            #await state.finish()
        # await bot.send_video(chat_id = id_person, video=film[-2], caption=str(film[0]) + ' ('+str(film[1])+')\n\n'+str(film[3])+'\n\n'+film[4]+'\nRatng: '+str(film[2])+'\10',reply_markup=watch_keyboard)
    #keyboard_for_next_films = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    
    item_page = InlineKeyboardButton(text='Page: '+str(counter+1), callback_data='11111')
    #print(num, len(film_list))
    #наш нам =11 
    if num>open_count:
      #  print('ДЕЛАЮ ЭТО')
        item_back = InlineKeyboardButton(text='⏮', callback_data='previous_page')
        keyboard_film_list.add(item_back)
    #item_next_page = InlineKeyboardButton(text='Next page👉', callback_data='next_page')
        keyboard_film_list.insert(item_page)
    else:
        keyboard_film_list.add(item_page)
    #user_data['counter']=user_data['counter']+1
    
    #await state.update_data(counter=user_data['counter'])
    if not coef==1 and num!=len(film_list):
      #  print('это..')
        #item_yars_f = InlineKeyboardButton(text='Years filter⚙️', callback_data='Years_filter')
        item_next_page = InlineKeyboardButton(text='⏭', callback_data='next_page')
        #keyboard_film_list.insert(item_yars_f).insert(item_next_page)#item_yars_f
        keyboard_film_list.insert(item_next_page)#item_yars_f
        #user_data['counter']=user_data['len_list']-1
        #text =str((counter+1)*coef)+'/'+str(len_l)
        
        #await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=str((user_data['counter']+1)*coef)+'/'+str(user_data['len_list']), reply_markup=keyboard_film_list)
    else:
        counter1=len_l
        #text = text=str((counter1)*coef)+'/'+str(len_l)
    
        #await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=str((user_data['counter'])*coef)+'/'+str(user_data['len_list']), reply_markup=keyboard_film_list)
    #print('всё:'+str(counter) + str(text) + str(keyboard_film_list))
  #  print('COUNTER:'+str(counter))
    return [counter, text, keyboard_film_list]


async def previous_page_info1(counter, film_list, len_l, open_count, id_person):
    keyboard_film_list= InlineKeyboardMarkup(row_width=18)
    x=False
    num=0
    text=''



    admin_id = await get_admin()
    if id_person in admin_id:
        x=True

    #counter=counter-1
    #await OrderDataUser.sanding_films.set()
    coef=open_count
   # print('counter: '+str(counter))
    #print()
    for i in range(counter*open_count,counter*open_count+open_count):
        #print(i)
        num=i+1

        film = film_list[i]

        film_j = await get_genres_by_film_name(film)

        for n in range(3):
            try:
                film_j[n] = str(film_j[n])
            except:
                break

        if len(film_j)>2:
            film_j=film_j[0]+', '+film_j[1]+', '+film_j[2]
        elif len(film_j)==2:
            film_j=film_j[0]+', '+film_j[1]
        elif len(film_j)==1:
            film_j=film_j[0]
        else:
            film_j=''


        text+=str(num)+') '+str(film.film_name)+'('+str(film.year)+')\nIMBb: '+str(film.rating)+' | '+film_j+'\n\n'

        item_f = InlineKeyboardButton(text=num, callback_data='find film_'+str(film.film_name))
        if num%7==0:
            keyboard_film_list.row(item_f)
        else:
            keyboard_film_list.insert(item_f)
            #await state.finish()
        # await bot.send_video(chat_id = id_person, video=film[-2], caption=str(film[0]) + ' ('+str(film[1])+')\n\n'+str(film[3])+'\n\n'+film[4]+'\nRatng: '+str(film[2])+'\10',reply_markup=watch_keyboard)
    #keyboard_for_next_films = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    
    item_page = InlineKeyboardButton(text='Page: '+str(counter+1), callback_data='11111')
    #item_back = InlineKeyboardButton(text='👈 Previous page', callback_data='previous_page')
    #item_next_page = InlineKeyboardButton(text='Next page👉', callback_data='next_page')
    #keyboard_film_list.add(item_page)

    #user_data['counter']=user_data['counter']+1
    if counter==0:
        coef=1
    #await state.update_data(counter=counter)
    if coef==1:
        #item_page = InlineKeyboardButton(text='Page: 1', callback_data='11111')
        #item_yars_f = InlineKeyboardButton(text='Years filter', callback_data='Years_filter')
        item_next_page = InlineKeyboardButton(text='⏭', callback_data='next_page')
        keyboard_film_list.add(item_page, item_next_page)

        '''   
        #item_yars_f = InlineKeyboardButton(text='Years filter⚙️', callback_data='Years_filter')
        item_next_page = InlineKeyboardButton(text='Next page👉', callback_data='next_page')
        #keyboard_film_list.insert(item_yars_f).insert(item_next_page)#item_yars_f
        keyboard_film_list.insert(item_next_page)#item_yars_f
        #user_data['counter']=user_data['len_list']-1
        '''
        
        #text=str((counter+5)*coef)+'/'+str(len_l)
        #await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=str((user_data['counter']+5)*coef)+'/'+str(user_data['len_list']), reply_markup=keyboard_film_list)
    else:
        item_back_page = InlineKeyboardButton(text='⏮', callback_data='previous_page')
        item_next_page = InlineKeyboardButton(text='⏭', callback_data='next_page')
        keyboard_film_list.add(item_back_page, item_page, item_next_page)
        
        
        #text=str((counter+1)*coef)+'/'+str(len_l)
        #user_data['counter']=user_data['len_list']
        #await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=str((user_data['counter']+1)*coef)+'/'+str(user_data['len_list']), reply_markup=keyboard_film_list)
        #await bot.send_message(chat_id=id_person, text='Select one genre', reply_markup=Genre_keyboard)
        #await OrderDataUser.waiting_for_Genres.set()
 #   print('COUNTER:'+str(counter))
    return [counter, text, keyboard_film_list]


async def page_open(film_list, open_count, id_person):
    len_list=len(film_list)
    #print('len2: '+str(len_list))
    text = ''
    num=0
    keyboard_film_list= InlineKeyboardMarkup(row_width=18)
    x=False

    film_list_trending = await get_trending_films()

    admin_id = await get_admin()
    if id_person in admin_id:
        x=True

    print('open_count: '+str(open_count))
    if len(film_list)<open_count:
        len_list=len(film_list)
    else:
        len_list=open_count
    #keyboard_film_list= InlineKeyboardMarkup(row_width=3)
    print('------------------')
   # print(film_list)
    for i in range(len_list):
        num += 1
        film = film_list[i]

        #genres_str = ''
        film_info = await get_all_by_film_name(film)
        film_genres = film_info.genres.all()
        film_genres = await ret_list(film_genres)
       # film_genres = list(film_genres)
       # film_genres = await get_genres_by_film_name(film)
        print(film_genres)
      #  for genre in film_genres:
        #    film_genres.append(genre)
         #   print(genre)
       # print('mass: '+str(film_genres))
        if len(film_genres) > 2:
            film_genres = str(film_genres[0])+', '+str(film_genres[1])+', '+str(film_genres[2])
        elif len(film_genres) == 2:
            film_genres = str(film_genres[0])+', '+str(film_genres[1])
        elif len(film_genres) == 1:
            film_genres = str(film_genres[0])
        else:
            film_genres = ''
        print(film_genres)

        text += str(num)+') '+str(film_info.film_name)+'('+str(film_info.year)+')\nIMBb: '+str(film_info.rating)+' | '+film_genres+'\n\n'
        item_f = InlineKeyboardButton(text=num, callback_data='find film_'+str(film_info.film_name))
        if num % 7 == 0:
            keyboard_film_list.row(item_f)
        else:
            keyboard_film_list.insert(item_f)

    item_page = InlineKeyboardButton(text='Page: 1', callback_data='11111')
    item_next_page = InlineKeyboardButton(text='⏭', callback_data='next_page')
   # print('open_count:'+str(open_count))
   # print(num, open_count)
    if num<open_count or len(film_list)<open_count+1:
       # item_next_page = InlineKeyboardButton(text='⏭', callback_data='next_page')
        keyboard_film_list.add(item_page)
    else:
      #  print('это')
        keyboard_film_list.add(item_page, item_next_page)
    #text=str(len_list)+'/'+str(len(film_list))

    return [text, keyboard_film_list]

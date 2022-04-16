from .dbcommands import get_all_by_film_name, get_admin, get_favourite_user
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from asgiref.sync import sync_to_async
#from db_cursor import cursor, conn
#from config import admin_id
from .tools import get_only_names, get_only_names2, ret_list


async def film_create(film_name, id_person):
  admin_id = await get_admin()
  #film_name=film_name.replace("'", "''")
  film_inf = await get_all_by_film_name(film_name)

  #film_inf
  mass_counter_values = [film_inf.likes, film_inf.dislikes, film_inf.comments_counter]
  print('-----------')
  print(mass_counter_values)
 # cursor.execute(f"SELECT * from `films_list` WHERE name_film='{film_name}'")
  #comm = cursor.fetchone()
  # comm вся информация об одном фильме
  favorurite_list = await get_favourite_user(id_person)
 # cursor.execute(f"SELECT favourite FROM `user_info` WHERE id_tele={id_person}")
 # comm_list = cursor.fetchone()[0]
 # mass_i=[9, 10, 12]
 # list2=list(comm)
  for i in range(3):
    if mass_counter_values[i]>1000:
      
    #  print(list2[i])
      mass_counter_values[i]=mass_counter_values[i]/1000
      
      mass_counter_values[i]=round(mass_counter_values[i],1)
      mass_counter_values[i]=str(mass_counter_values[i])
      if mass_counter_values[i][-1]=='0':
        mass_counter_values[i]=mass_counter_values[i][:-2]
      #list2[i]=int(list2[i])

   #   print(comm[i], mass_counter_values[i])
    #  comm_int=comm[i]
      list_int=mass_counter_values[i]
      list_int+='K'
      #comm=list(comm)
      mass_counter_values[i]=list_int
  next_step_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
  item_film_like = InlineKeyboardButton(text='😍 ' + str(mass_counter_values[0]), callback_data='like video')
  item_film_dislike = InlineKeyboardButton(text='🤬 ' + str(mass_counter_values[1]), callback_data='dislike video')
  item_comm = InlineKeyboardButton(text='💬 ' + str(mass_counter_values[2]), callback_data='comment video')
  item_watch_f = InlineKeyboardButton(text='▶️ Watch now', callback_data='start watching')
  item_searc_an = InlineKeyboardButton(text='🔍 Search another', switch_inline_query_current_chat='')
  # next_step_keyboard.add(item_film_like, item_film_dislike, item_comm).row(item_fav, item_watch_f).row(item_searc_an)

  if not film_name in get_only_names2(favorurite_list):
    item_fav = InlineKeyboardButton(text='🧡 Favourite', callback_data='add favourite')
  else:
    item_fav = InlineKeyboardButton(text='🚫 Remove', callback_data='add favourite')
  next_step_keyboard.add(item_film_like, item_film_dislike, item_comm).row(item_watch_f, item_searc_an).row(item_fav)
  #  print('----------COMM------')
    #print(comm)
  # print(comm[0], comm[1], comm[2], comm[3], comm[5], comm[11], comm[12])
  return [film_inf.film_name, film_inf.year, film_inf.rating, await ret_list(film_inf.genres.all()), film_inf.trailer_link, film_inf.director.all(), mass_counter_values[2], next_step_keyboard, film_inf.description, (await ret_list(film_inf.director.all()))[0], await ret_list(film_inf.stars.all())]


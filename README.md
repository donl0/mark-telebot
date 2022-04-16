Film library Telegram bot with users system.
Admin should uploat film with this plan(add your tele id in admin model):
  1)send trailer with film name(like in IMDB)
  2)wait for approval from bot
  3)send '-'+film name with film file
  Enother data (actors, genres etc.) will parse from IMDB

User system are realized with history, favourite, comments and requests functions for every own person.

'🔥 Popular' button contains films that admin will add from admin model.

Every text in bot you can change with Messages from admin panel(Messages have their own id).

To start bot you should run 2 commadns(you can do this from 2 consoles).
pytohn manage.py runserver
pytohon manage.py run_bot

To connect to admin panel:
Go url+/admin (check from pytohn manage.py runserver).

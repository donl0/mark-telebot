from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
#from main import dp

class OrderDataUser(StatesGroup):

    wait_for_empl_name_to_take_excel = State()

    waiting_for_name_to_excel = State()

    get_name = State()

    start_marking_a = State()
    mark_a1 = State()
    mark_a2 = State()
    mark_a3 = State()
    mark_a4 = State()
    mark_a5 = State()
    mark_a_comment = State()

    mark_b1 = State()
    mark_b2 = State()
    mark_b3 = State()
    mark_b4 = State()
    mark_b5 = State()
    mark_b_comment = State()

    mark_c1 = State()
    mark_c2 = State()
    mark_c3 = State()
    mark_c4 = State()
    mark_c5 = State()
    mark_c6 = State()
    mark_c_comment = State()

    mark_d1 = State()
    mark_d2 = State()
    mark_d3 = State()
    mark_d4 = State()
    mark_d5 = State()
    mark_d_comment = State()

    mark_e1 = State()
    mark_e2 = State()
    mark_e3 = State()
    mark_e4 = State()
    mark_e5 = State()
    mark_e6 = State()
    mark_e_comment = State()


    mark_begin = State()
    get_telephone_num = State()
    favorite_st =State()
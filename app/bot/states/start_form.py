from aiogram.fsm.state import StatesGroup, State


class StartForm(StatesGroup):
    first_name = State()
    last_name = State()
    middle_name = State()
    phone_number = State()
    email = State()
    speciality = State()
    study_type = State()
    payment_type = State()
    study_form = State()
    dorm = State()
    confirm_edbo = State()
    print_edbo = State()

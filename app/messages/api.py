from app.messages.environment import environment

CONTRACT_INFO = environment.from_string("""
<b>ПІБ:</b> {{ contract.last_name }} {{ contract.first_name }} {{ contract.middle_name }}
<b>Спеціальність:</b> {{ contract.speciality }}
<b>Номер контракту:</b> {{ contract.contract_number }}
<b>Конкурсний бал:</b> {{ contract.competitive_point }}
<b>Дата:</b> {{ contract.date }}
""")

REGISTER_USER = environment.from_string("""
<b>ПІБ:</b> {{ user.last_name }} {{ user.first_name }} {{ user.surname }}
<b>Юзернейм:</b> @{{ user.username }} ({{ user.telegram_id }})
<b>Телефон:</b> {{ user.phone }}
<b>Пошта:</b> {{ user.email }}
<b>Спеціальність:</b> {{ user.speciality }}
<b>Гуртожиток:</b> {{ 'Так' if user.is_dorm else 'Ні' }}
<b>Роздрукував заяву:</b> {{ 'Так' if user.printed_edbo else 'Ні' }}
""")

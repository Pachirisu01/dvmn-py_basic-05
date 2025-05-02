import random
import file_operations
from faker import Faker
import os


RUNIC_LETTERS = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠', 
    'м': 'м͒͠', 
    'н': 'н͒',
    'о': 'о̋', 
    'п': 'п̋͠', 
    'р': 'р̋͠',
    'с': 'с͒', 
    'т': 'т͒', 
    'у': 'у͒͠',
    'ф': 'ф̋̋͠', 
    'х': 'х͒͠', 
    'ц': 'ц̋',
    'ч': 'ч̋͠', 
    'ш': 'ш͒͠', 
    'щ': 'щ̋',
    'ъ': 'ъ̋͠', 
    'ы': 'ы̋͠', 
    'ь': 'ь̋',
    'э': 'э͒͠͠', 
    'ю': 'ю̋͠', 
    'я': 'я̋',
    'А': 'А͠', 
    'Б': 'Б̋', 
    'В': 'В͒͠',
    'Г': 'Г͒͠', 
    'Д': 'Д̋', 
    'Е': 'Е',
    'Ё': 'Ё͒͠', 
    'Ж': 'Ж͒', 
    'З': 'З̋̋͠',
    'И': 'И', 
    'Й': 'Й͒͠', 
    'К': 'К̋̋',
    'Л': 'Л̋͠', 
    'М': 'М͒͠', 
    'Н': 'Н͒',
    'О': 'О̋', 
    'П': 'П̋͠', 
    'Р': 'Р̋͠',
    'С': 'С͒', 
    'Т': 'Т͒', 
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 
    'Х': 'Х͒͠', 
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 
    'Ш': 'Ш͒͠', 
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 
    'Ы': 'Ы̋͠', 
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 
    'Ю': 'Ю̋͠', 
    'Я': 'Я̋',
    ' ': ' '
}



SKILLS = [
"Стремительный прыжок",
"Электрический выстрел",
"Ледяной удар",
"Стремительный удар",
"Кислотный взгляд",
"Тайный побег",
"Ледяной выстрел",
"Огненный заряд"
]


def generate_random_skills():
	return random.sample(SKILLS, 3)


def runic_skills(text):
	result = ""
	for char in text:
		if char in RUNIC_LETTERS:
			result += RUNIC_LETTERS[char]
	return result


def generate_character():
	fake = Faker("ru_RU")
	skills = random.sample(SKILLS, 3)

	context = {
	        "first_name": fake.first_name(),
	        "last_name": fake.last_name(),
	        "job": fake.job(),
	        "town": fake.city(),
	        "strength": random.randint(3, 18),
	        "agility": random.randint(3, 18),
	        "endurance": random.randint(3, 18),
	        "intelligence": random.randint(3, 18),
	        "luck": random.randint(3, 18),
	        "skill_1": runic_skills(skills[0]),
	        "skill_2": runic_skills(skills[1]),
	        "skill_3": runic_skills(skills[2])
	    }
	    
	return context


def generate_cards():
	for i in range(10):
		context = generate_character()
		name_file =f'card{i}.svg'
		folder = "characters"
		os.makedirs(folder, exist_ok=True)
		output_path = os.path.join(folder,name_file)
		file_operations.render_template("charsheet.svg", output_path, context)


if __name__ == '__main__':
    generate_cards()

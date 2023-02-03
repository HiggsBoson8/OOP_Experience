import requests
import os
os.system("clear")

class RickAndMorty:
    def __init__(self):
        self.url = "https://rickandmortyapi.com/api/"

    def get_info(self, gets):
        response = requests.get(f"{self.url}/{gets}")
        data = response.json()
        return data

    def get_episode(self, gets):
        get_id_episode = self.get_info(f"character/{gets}")

        for i in get_id_episode["episode"]:
            response = requests.get(i)
            episode = response.json()
            information_episode = f"""
Эпизод где учвствует персонаж
    Название эпизода: {episode["name"]}
    Дата релиза: {episode["air_date"]}
    Эпизод: {episode["episode"]}
    Дата создания: {episode["created"]}"""
        return information_episode

    def get_location(self, gets):
        get_id = self.get_info(f"character/{gets}")
        
        for i in get_id["location"]:
            name_location = get_id["location"]["name"]
            url_location = get_id["location"]["url"] 
            
            if url_location:
                id_url = url_location.split('/')[-1]
                location = self.get_info(f"location/{id_url}")
                name_dimension = location['dimension']
                type_location = location['type']
            
                information_location = f"""
Локация персонажа
    Название локации: {name_location}
    Тип локации: {type_location}
    Изменение локации: {name_dimension}"""
                return information_location
            else: 
                information_location = f"""
Локация персонажа
    Название локации: {name_location}
    Тип локации: Unknown
    Измерение локации: Unknown"""
                return 

    def get_character(self, gets):
        if gets <= 826:
            character = self.get_info(f"character/{gets}")
            information = f"""
Идектификатор персонажа: {character["id"]}
    Имя персонажа: {character["name"]}
    Пол персонажа: {character["gender"]}
    Жизненное положение: {character["status"]}
    Какой расе относится: {character["species"]} 
    Личность: {character["type"]} 
    Дата создания: {character["created"]}

{self.get_location(gets)}"""            

            return information
        return "Неправильный ID персонажа"

    def __str__(self):
        return f"Вы забыли вызвать у экземпляра метод get_character_info" 

s = RickAndMorty()
print(s.get_character(1)) 
# print(s.__doc__) 
# print(s.__dict__()) 
# print(s.__hash__()) 
# print(s.__dir__()) 
# print(s.get_location(9)) 
# print(s.get_episode(9)) 

# print(s.get_character(1)) 




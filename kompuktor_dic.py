# import os
# import time
# import pprint
# os.system("clear")

# class Computer():
#     """docstring for Computer"""

#     def __init__(self, notebook, ssd, os, size, mother_board):
#         self.notebook = notebook
#         self.ssd = ssd
#         self.os = os
#         self.size = size
#         self.mother_board = mother_board
#         self.comp = {}

#     def updates(self): 
#         self.comp.update({
#             "f{self.notebook}": {
#                 'операционная система': self.os,
#                 'накопитель': self.ssd,
#                 'размер экрана': self.size,
#                 'материнская плата': self.mother_board
#             }}) 
#         return self.comp

#     def __str__(self):
#         return self.notebook

# note1  = Computer('HP', '512gb', 'macOS', '15.6', 'Intel')
# note2 = Computer('Asus', '512gb', 'linux', '15.6', 'AMD')
# pprint.pprint(note1.updates())
# pprint.pprint(note2.updates())


#-----------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------

import os 
import time 
import os
import pprint
os.system('clear')


class Computer:
    """
    Собираем игровое железо для задрота
    """

    def __init__(self, kompuktor, video_card, central_processing_unit, ssd_harddisk, random_access_memory, motherboard, monitor_size): 
        self.kompuktor = kompuktor
        self.video_card = video_card 
        self.central_processing_unit = central_processing_unit 
        self.ssd_harddisk = ssd_harddisk 
        self.random_access_memory = random_access_memory 
        self.motherboard = motherboard 
        self.monitor_size = monitor_size 
        self.comp = {}

    def update(self): 
        self.comp.update({ 
            f"{self.kompuktor}": { 
            'Видеокарта': f"Мощная видюха {self.video_card} для задрота", 
            'Процессор': f"Мощный процессор для GAYmera {self.central_processing_unit}", 
            'Накопитель': f"По больше памяти для игр, потому что мальчишка будет качать много игр, поэтому и {self.ssd_harddisk}", 
            'Оперативка': f"И конечно же побольше оперативной памяти, потому что игры требуют много памяти { self.random_access_memory}\
            для задрота! Ведь мальчишка будет играть сразу в несколько игр одновременно!", 
            'Материнская плата': f"Мамку для маленького задротика {self.motherboard}", 
            'Монитор': f"Зачем для gayмера личная жизнь, когда есть несколько штук здоровенных мониторов: {self.monitor_size}?" 
            }}) 
        return self.comp 

    def __str__(self):
        return self.kompuktor 

zadrot = Computer("", "NVIDIA Geforce RTX 5080ti super nerd", "AMD RYZEN 10 9800x super nerd edition", "SSD 10tb", "64gb RAM", "MSI B250M Gaming Pro",\
"изогнутые игровые мониторы GYFOMA, 27 дюймов, 240 Гц,  8k дисплеи, игровые ЖК-мониторы HD для игрового компьютера, для настольного ПК, совместимые с HDMI мониторы")

print("И так, давайте соберем мощный игровой компуктор для малолетнего задрота! Что мы ему дадим? ")
time.sleep(4)
pprint.pprint(zadrot.update())
time.sleep(4)
print("?????????????????????????????????????? \nPROFIT")
time.sleep(4)
print("Gaymer доволен!")
# print(zadrot.update()) 


#-----------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------

# import os 
# import time 
# import os
# import pprint
# os.system('clear')


# class Computer:
#     """
#     Собираем игровое железо для задрота
#     """

#     def __init__(self, kompuktor, video_card, central_processing_unit, ssd_harddisk, random_access_memory, motherboard, monitor_size): 
#         self.kompuktor = kompuktor 
#         self.video_card = video_card 
#         self.central_processing_unit = central_processing_unit 
#         self.ssd_harddisk = ssd_harddisk 
#         self.random_access_memory = random_access_memory 
#         self.motherboard = motherboard 
#         self.monitor_size = monitor_size 
#         self.comp = {} 

#     def update(self): 
#         self.comp.update({ 
#             f"{self.kompuktor}": { 
#             'Видеокарта': self.video_card, 
#             'Процессор': self.central_processing_unit, 
#             'Накопитель': self.ssd_harddisk, 
#             'Оперативка':  self.random_access_memory, 
#             'Материнская плата': self.motherboard, 
#             'Монитор': self.monitor_size 
#             }}) 
#         return self.comp 
        

#     def __str__(self): 
#         return self.kompuktor 

# zadrot = Computer("", "NVIDIA Geforce RTX 5080ti super nerd", "AMD RYZEN 10 9800x super nerd edition", "SSD 10tb", "64gb RAM", "MSI B250M Gaming Pro",\
# "изогнутые игровые мониторы GYFOMA, 27 дюймов, 240 Гц,  8k дисплеи, игровые ЖК-мониторы HD для игрового компьютера, для настольного ПК, совместимые с HDMI мониторы") 

# pprint.pprint(zadrot.update()) 
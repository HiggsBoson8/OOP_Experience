# Собрать железо?

import os 
import time 
import os
os.system('clear')


class Computer:
    """
    Собираем игровое железо для задрота
    """

    def __init__(self, video_card, central_processing_unit, ssd_harddisk, random_access_memory, motherboard, monitor_size): 
        self.video_card = video_card 
        self.central_processing_unit = central_processing_unit 
        self.ssd_harddisk = ssd_harddisk 
        self.random_access_memory = random_access_memory 
        self.motherboard = motherboard 
        self.monitor_size = monitor_size 
       
    def video(self):
        return f"Мощная видюха {self.video_card} для задрота" 
    
    def CPU(self):
        return f"Мощный процессор для GAYmera + {self.central_processing_unit}"

    def SSD(self):
        return f"По больше памяти для игр, потому что мальчишка будет качать много игр, поэтому и {self.ssd_harddisk}"
    
    def RAM(self):
        return f"И конечно же побольше оперативной памяти, потому что игры требуют много памяти + {self.random_access_memory} для задрота! Ведь мальчишка будет играть сразу в несколько игр одновременно!"

    def MOTHERBOARD(self):
        return f"Мамку для маленького задротика {self.motherboard}"

    def MONITOR(self):
        return f"Зачем для gayмера личная жизнь, когда есть несколько штук здоровенных мониторов: {self.monitor_size}?" 

    def __str__(self):
        return f"hmmmmmmmm"

zadrot = Computer("NVIDIA Geforce RTX 5080ti super nerd", "AMD RYZEN 10 9800x super nerd edition", "SSD 10tb", "64gb RAM", "MSI B250M Gaming Pro",\
"изогнутые игровые мониторы GYFOMA, 27 дюймов, 240 Гц,  8k дисплеи, игровые ЖК-мониторы HD для игрового компьютера, для настольного ПК, совместимые с HDMI мониторы")

print("И так, давайте соберем мощный игровой компуктор для малолетнего задрота! Что мы ему дадим? ")
time.sleep(4)
print(zadrot.video()) 
time.sleep(4)
print(zadrot.CPU())
time.sleep(4)
print(zadrot.RAM())
time.sleep(4)
print(zadrot.SSD())
time.sleep(6)
print(zadrot.MOTHERBOARD())
time.sleep(4)
print(zadrot.MONITOR())
print("?????????????????? \nPROFIT \nМальчишка счастлив!") 


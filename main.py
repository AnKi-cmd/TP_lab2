import time

all_ways = {}
counter = 0

def create_map():
    map = {
        "Беговая":{"Зенит":8},  #НАЧАЛО ЗЕЛЕНОЙ ВЕТКИ
        "Зенит":{"Беговая":8, "Приморская":2},
        "Приморская":{"Зенит":2, "Василеостровская":6},
        "Василеостровская":{"Приморская":6, "Гостиный двор":6},
        "Гостиный двор":{"Василеостровская":6, "Маяковская":5, "Невский проспект":4},
        "Маяковская":{"Гостиный двор":5, "Площадь Александра Невского 1":5, "Площадь Восстания":3},
        "Площадь Александра Невского 1": {"Маяковская": 5, "Елизаровская": 6, "Площадь Александра Невского 2":2},
        "Елизаровская": {"Площадь Александра Невского 1": 6, "Ломоносовская": 5},
        "Ломоносовская": {"Елизаровская": 5, "Пролетарская": 6},
        "Пролетарская": {"Ломоносовская": 6, "Обухово": 5},
        "Обухово": {"Пролетарская": 5, "Рыбацкое": 6},
        "Рыбацкое": {"Обухово": 6},  #КОНЕЦ ЗЕЛЕНОЙ ВЕТКИ

        "Комендантский проспект": {"Старая деревня": 6}, #НАЧАЛО ФИОЛЕТОВОЙ ВЕТКИ
        "Старая деревня": {"Комендантский проспект": 6, "Крестовский остров": 5},
        "Крестовский остров": {"Старая деревня": 5, "Чкаловская": 5},
        "Чкаловская": {"Крестовский остров": 5, "Спортивная": 4},
        "Спортивная": {"Чкаловская": 4, "Адмиралтейская": 5},
        "Адмиралтейская": {"Спортивная": 5, "Садовая": 4},
        "Садовая": {"Адмиралтейская": 4, "Звенигородская": 5, "Спасская":3, "Сенная площадь":4},
        "Звенигородская": {"Садовая": 5, "Обводной канал": 7, "Пушкинская":3},
        "Обводной канал": {"Звенигородская": 7, "Волковская": 5},
        "Волковская": {"Обводной канал": 5, "Бухарестская": 5},
        "Бухарестская": {"Волковская": 5, "Международная": 5},
        "Международная": {"Бухарестская": 5, "Проспект славы": 4},
        "Проспект славы": {"Международная": 4, "Дунайская": 5},
        "Дунайская": {"Проспект славы": 5, "Шушары": 5},
        "Шушары": {"Дунайская": 5},  #КОНЕЦ ФИОЛЕТОВОЙ ВЕТКИ

        "Парнас": {"Проспект просвещения": 5},     #НАЧАЛО СИНЕЙ ВЕТКИ
        "Проспект просвещения": {"Парнас": 5, "Озерки": 4},
        "Озерки": {"Проспект просвещения": 4, "Удельная": 5},
        "Удельная": {"Озерки": 5, "Пионерская": 5},
        "Пионерская": {"Удельная": 5, "Черная речка": 5},
        "Черная речка": {"Пионерская": 5, "Петроградская": 6},
        "Петроградская": {"Черная речка": 6, "Горьковская": 4},
        "Горьковская": {"Петроградская": 4, "Невский проспект": 6},
        "Невский проспект": {"Горьковская": 6, "Сенная площадь": 2, "Гостиный двор": 4},
        "Сенная площадь": {"Невский проспект": 2, "Технологический институт 2": 4, "Садовая": 3, "Спасская": 4},
        "Технологический институт 2": {"Сенная площадь": 4, "Фрунзенская": 4, "Технологический институт 1":1},
        "Фрунзенская": {"Технологический институт 2": 4, "Московские ворота": 5},
        "Московские ворота": {"Фрунзенская": 5, "Электросила": 4},
        "Электросила": {"Московские ворота": 4, "Парк Победы": 4},
        "Парк Победы": {"Электросила": 4, "Московская": 5},
        "Московская": {"Парк Победы": 5, "Звездная": 7},
        "Звездная": {"Московская": 7, "Купчино": 5},
        "Купчино": {"Звездная": 5},       #КОНЕЦ СИНЕЙ ВЕТКИ

        "Девяткино": {"Гражданский проспект": 4},     #НАЧАЛО КРАСНОЙ ВЕТКИ
        "Гражданский проспект": {"Девяткино": 4, "Академическая": 4},
        "Академическая": {"Гражданский проспект": 4, "Политехническая": 2},
        "Политехническая": {"Академическая": 2, "Площадь мужества": 2},
        "Площадь мужества": {"Политехническая": 2, "Лесная": 3},
        "Лесная": {"Площадь мужества": 3, "Выборгская": 3},
        "Выборгская": {"Лесная": 3, "Площадь Ленина": 3},
        "Площадь Ленина": {"Выборгская": 3, "Чернышевская": 3},
        "Чернышевская": {"Площадь Ленина": 3, "Площадь Восстания": 3},
        "Площадь Восстания": {"Чернышевская": 3, "Владимирская": 2, "Маяковская":3},
        "Владимирская": {"Площадь Восстания": 2, "Пушкинская": 2, "Достоевская":3},
        "Пушкинская": {"Владимирская": 2, "Технологический институт 1": 4, "Звенигородская":3},
        "Технологический институт 1": {"Пушкинская": 4, "Балтийская": 4, "Технологический институт 2": 1},
        "Балтийская": {"Технологический институт 1": 4, "Нарвская": 5},
        "Нарвская": {"Балтийская": 5, "Кировский завод": 6},
        "Кировский завод": {"Нарвская": 6, "Автово": 4},
        "Автово": {"Кировский завод": 4, "Ленинский проспект": 5},
        "Ленинский проспект": {"Автово": 5, "Проспект ветеранов": 4},
        "Проспект ветеранов": {"Ленинский проспект": 4}, #КОНЕЦ КРАСНОЙ ВЕТКИ

        "Спасская": {"Достоевская": 6, "Садовая": 3, "Сенная площадь": 4},   #НАЧАЛО ОРАНЖЕВОЙ ВЕТКИ
        "Достоевская": {"Спасская": 6, "Лиговский проспект": 4, "Владимирская": 3},
        "Лиговский проспект": {"Достоевская": 4, "Площадь Александра Невского 2": 4},
        "Площадь Александра Невского 2": {"Лиговский проспект": 4, "Новочеркасская": 5, "Площадь Александра Невского 1":2},
        "Новочеркасская": {"Площадь Александра Невского 2": 5, "Ладожская": 5},
        "Ладожская": {"Новочеркасская": 5, "Проспект Большевиков": 5},
        "Проспект Большевиков": {"Ладожская": 5, "Улица Дыбенко": 5},
        "Улица Дыбенко": {"Проспект Большевиков": 5}                   #КОНЕЦ ОРАНЖЕВОЙ ВЕТКИ

    }
    return map

def get_start_station(stations):
    while(True):
        print("Выберите стартовую станцию: (При помощи порядкового номера или названия)")
        for i in range(1, 73, 1):
            print(str(i) + " : " + stations[i - 1])
        try:
            input_value = input()
            start_station = int(input_value)
            if (start_station>72)or(start_station<1):
                print("Станции с таким номером нет.")
                time.sleep(3)
                continue
        except:
            if not input_value in stations:
                print("Вы ввели некорректное значение.")
                time.sleep(3)
                continue
            return input_value
        return stations[start_station-1]

def get_end_station(stations):
    while(True):
        print("Выберите станцию назначения: (При помощи порядкового номера или названия)")
        for i in range(1, 73, 1):
            print(str(i) + " : " + stations[i - 1])
        try:
            input_value = input()
            end_station = int(input_value)
            if (end_station>72)or(end_station<1):
                print("Станции с таким номером нет.")
                continue
        except:
            if not input_value in stations:
                print("Вы ввели некорректное значение.")
                time.sleep(3)
                continue
            return input_value
        return stations[end_station-1]

def search_for_best_way(cur_station, end_station, prev_station = None, time = 0, way_list=None):
    stations_map = create_map()
    if time==0:
        way_list = list()
        prev_station = list()
        way_list.append(cur_station)
    if cur_station==end_station:
        global counter
        global all_ways
        all_ways[counter] = {str(way_list):time}
        counter+=1
        # print("Маршрут: "+str(way_list))
        # print("Приблизительное время: "+str(time)+" минуты")
    else:
        possible_ways = stations_map[cur_station]
        for way in possible_ways.keys():
            if way not in prev_station:
                new_time = time + possible_ways[way]
                new_list = way_list.copy()
                prev_list = prev_station.copy()
                new_list.append(way)
                prev_list.append(cur_station)
                search_for_best_way(way,
                                    end_station,
                                    prev_station = prev_list,
                                    time=new_time,
                                    way_list=new_list)

def main():
    stations = list(create_map().keys())
    start_station = get_start_station(stations)
    end_station = get_end_station(stations)
    search_for_best_way(start_station, end_station)
    print("Найдено "+str(counter)+" путей")
    best_time = [99999,99999,99999]
    best_ways = ["","",""]
    for variants in all_ways.keys():
        cur_dict = all_ways[variants]
        for times in range(3):
            if best_time[times] > list(cur_dict.values())[0]:
                for i in range(2,times,-1):
                    best_time[i]=best_time[i-1]
                    best_ways[i]=best_ways[i-1]
                best_time[times] = list(cur_dict.values())[0]
                best_ways[times] = list(cur_dict.keys())[0]
                break
    for i in range(3):
        if (best_time[i]!=99999):
            print("\nПуть "+str(i+1)+":")
            print("Время: "+str(best_time[i]))
            print("Маршрут:")
            print(best_ways[i])

main()
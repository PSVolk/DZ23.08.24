import json


music_groups_albums = {}

def add_music_group_album(group, album):
    """Добавление данных о группе и альбоме"""
    if group in music_groups_albums:
        music_groups_albums[group].append(album)
    else:
        music_groups_albums[group] = [album]
    print(f"Добавлена группа '{group}' с альбомом '{album}'.")

def remove_music_group_album(group, album):
    """Удаление данных о группе и альбоме"""
    if group in music_groups_albums:
        if album in music_groups_albums[group]:
            music_groups_albums[group].remove(album)
            if not music_groups_albums[group]:
                del music_groups_albums[group]
            print(f"Удален альбом '{album}' у группы '{group}'.")
        else:
            print(f"Альбом '{album}' не найден в группе '{group}'.")
    else:
        print(f"Группа '{group}' не найдена.")

def find_albums(group):
    """Поиск альбомов по названию группы"""
    if group in music_groups_albums:
        albums = ", ".join(music_groups_albums[group])
        print(f"Альбомы группы '{group}': {albums}")
    else:
        print(f"Группа '{group}' не найдена.")

def update_album(group, old_album, new_album):
    """Обновление данных об альбоме"""
    if group in music_groups_albums:
        if old_album in music_groups_albums[group]:
            index = music_groups_albums[group].index(old_album)
            music_groups_albums[group][index] = new_album
            print(f"Альбом '{old_album}' группы '{group}' обновлен на '{new_album}'.")
        else:
            print(f"Альбом '{old_album}' не найден в группе '{group}'.")
    else:
        print(f"Группа '{group}' не найдена.")

def save_data():
    """Сохранение данных в файл"""
    with open("music_groups_albums.json", "w") as file:
        json.dump(music_groups_albums, file)
    print("Данные успешно сохранены.")

def load_data():
    """Загрузка данных из файла"""
    try:
        with open("music_groups_albums.json", "r") as file:
            global music_groups_albums
            music_groups_albums = json.load(file)
        print("Данные успешно загружены.")
    except FileNotFoundError:
        print("Файл с данными не найден.")

# Пример использования функций
add_music_group_album("Metallica", "Master of Puppets")
add_music_group_album("Metallica", "Ride the Lightning")
add_music_group_album("Linkin Park", "Hybrid Theory")
add_music_group_album("Linkin Park", "Meteora")

find_albums("Metallica")
find_albums("Queen")

update_album("Metallica", "Master of Puppets", "Kill 'Em All")

remove_music_group_album("Linkin Park", "Meteora")

save_data()
load_data()

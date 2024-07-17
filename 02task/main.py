import cats_information as cat_info

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                cat_id, name, age = line.strip().split(',')
                cat_data = {"id" : cat_id, "name" : name, "age" : age}
                cats_info.append(cat_data)
        return cats_info
    except FileNotFoundError:
        return "Файл не знайдено"
    except Exception as e:
        return f"Сталася помилка: {e}"
    
cats_info = get_cats_info(cat_info)
print(cats_info)
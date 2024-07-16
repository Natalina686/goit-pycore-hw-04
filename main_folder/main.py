from main_folder import salary_file


def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            total = 0
            for line in lines:
                name, salary = line.strip().split(",")
                total += int(salary)
                average_salary = total / len(lines)
                return (total, average_salary)
    except FileNotFoundError:
        return "Файл не знайдено"
    except Exception as e:
        return f"Сталася помилка: {e}"
    
total, average_salary = total_salary(salary_file.txt)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average_salary}")
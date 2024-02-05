from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Настройка параметров Chrome и инициализация WebDriver
custom_options = Options()
custom_options.add_argument("--start-maximized")
path_driver = "/usr/local/bin/chromedriver"  # Замените на путь к вашему исполняемому файлу chromedriver
service = Service(path_driver)
driver = webdriver.Chrome(service=service, options=custom_options)

# Переход на целевой веб-сайт
link = "https://www.flashscore.com.ua/"
driver.get(link)

# Поиск элементов на веб-странице
driver_m = driver.find_elements(By.CLASS_NAME, 'event__match.event__match--twoLine')

# Извлечение данных с веб-страницы и сохранение в списке
results = []
for match in driver_m:
    result = match.text.splitlines()
    results.append(result)

# Определение названий столбцов для DataFrame
columns_name = ['status', 'team_1', 'team_2', 'g_1', 'g_2', 'first_time_1', 'first_time_2', 'sl_1', 'sl_2']

# Создание DataFrame с использованием библиотеки pandas
df = pd.DataFrame(results, columns=columns_name)

# Удаление ненужных столбцов
drop_col = ['sl_1', 'sl_2']
df = df.drop(drop_col, axis=1)

# Фильтрация строк, где статус матча 'Завершен' (Completed)
df = df.loc[df['status'] == 'Завершен']

# Определение имени выходного Excel файла
excel_filename = "output_data.xlsx"

# Сохранение DataFrame в Excel файл
df.to_excel(excel_filename, index=False)

# Закрытие WebDriver
driver.quit()




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидание, пока цена не станет $100
    price_condition = EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    WebDriverWait(driver, 12).until(price_condition)

    # Нажатие на кнопку "Book"
    book_button = driver.find_element(By.ID, "book")
    book_button.click()

    # Решение математической задачи
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    # Ввод ответа
    answer_field = driver.find_element(By.ID, "answer")
    answer_field.send_keys(answer)

    # Нажатие на кнопку для отправки формы
    submit_button = driver.find_element(By.ID, "solve")
    submit_button.click()

    # Считывание числа из alert
    alert = driver.switch_to.alert
    result = alert.text.split()[-1]
    print(result)

finally:
    # Закрытие браузера
    driver.quit()
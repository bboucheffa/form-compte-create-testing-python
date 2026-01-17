from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from manageData.read_data import ReadData

URL = "https://sendform.nicepage.io/?version=13efcba7-1a49-45a5-9967-c2da8ebdd189&uid=f7bd60f0-34c8-40e3-8e2c-06cc19fcb730"

read_data = ReadData()

def test_man(driver):
    client = read_data.read_Client("Client1")
    #wait = WebDriverWait(driver, 100)

    driver.get(URL)

    driver.find_element(By.ID, "field-2688").click()
    Select(driver.find_element(By.ID, "select-9648")).select_by_value("FR")

    #breakpoint()
    driver.find_element(By.ID, "email-c6a3").send_keys(client["email"])
    driver.find_element(By.ID, "name-c6a3").send_keys(client["name"])
    driver.find_element(By.ID, "phone-84d9").send_keys(client["phone"])
    driver.find_element(By.ID, "address-be2d").send_keys(client["adresse"])
    driver.find_element(By.ID, "message-c6a3").send_keys(client["message"])

    Select(driver.find_element(By.ID, "select-c283")).select_by_value("mot")

    driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        driver.find_element(By.ID, "checkbox-8214")
    )
    driver.find_element(By.ID, "checkbox-8214").click()

    driver.find_element(By.CSS_SELECTOR, "form a").click()

def test_women(driver):
    client = read_data.read_Client("Client2")
    wait = WebDriverWait(driver, 50)

    driver.get(URL)

    driver.find_element(By.ID, "field-aa6c").click()
    Select(driver.find_element(By.ID, "select-9648")).select_by_value("ES")

    driver.find_element(By.ID, "email-c6a3").send_keys(client["email"])
    driver.find_element(By.ID, "name-c6a3").send_keys(client["name"])
    driver.find_element(By.ID, "phone-84d9").send_keys(client["phone"])
    driver.find_element(By.ID, "address-be2d").send_keys(client["adresse"])
    driver.find_element(By.ID, "message-c6a3").send_keys(client["message"])

    Select(driver.find_element(By.ID, "select-c283")).select_by_value("car")

    driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        driver.find_element(By.ID, "checkbox-1848")
    )
    driver.find_element(By.ID, "checkbox-1848").click()

    driver.find_element(By.XPATH, "//form/div[12]/a").click()

def test_man_with_condition(driver):
    client = read_data.read_Client("Client3")
    wait = WebDriverWait(driver, 50)

    driver.get(URL)

    genre = driver.find_element(By.ID, "field-2688")
    genre.click()

    select_pays = Select(driver.find_element(By.ID, "select-9648"))
    select_pays.select_by_value("FR")

    driver.find_element(By.ID, "email-c6a3").send_keys(client["email"])
    driver.find_element(By.ID, "name-c6a3").send_keys(client["name"])
    driver.find_element(By.ID, "phone-84d9").send_keys(client["phone"])
    driver.find_element(By.ID, "address-be2d").send_keys(client["adresse"])
    driver.find_element(By.ID, "message-c6a3").send_keys(client["message"])

    pays = select_pays.first_selected_option.text
    genre_value = genre.get_attribute("value")

    #breakpoint()
    select_product = Select(driver.find_element(By.ID, "select-c283"))

    if genre_value == "man" and pays == "France":
        select_product.select_by_value("mot")
        checkbox = "checkbox-8214"
    else:
        select_product.select_by_value("vel")
        checkbox = "checkbox-1848"

    driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        driver.find_element(By.ID, checkbox)
    )
    driver.find_element(By.ID, checkbox).click()

    driver.find_element(By.CSS_SELECTOR, "form a").click()

def test_women_with_condition(driver):
    client = read_data.read_Client("Client4")
    wait = WebDriverWait(driver, 50)

    driver.get(URL)

    genre = driver.find_element(By.ID, "field-aa6c")
    genre.click()

    select_pays = Select(driver.find_element(By.ID, "select-9648"))
    select_pays.select_by_value("IT")

    driver.find_element(By.ID, "email-c6a3").send_keys(client["email"])
    driver.find_element(By.ID, "name-c6a3").send_keys(client["name"])
    driver.find_element(By.ID, "phone-84d9").send_keys(client["phone"])
    driver.find_element(By.ID, "address-be2d").send_keys(client["adresse"])
    driver.find_element(By.ID, "message-c6a3").send_keys(client["message"])

    pays = select_pays.first_selected_option.text
    genre_value = genre.get_attribute("value")

    #breakpoint()
    select_product = Select(driver.find_element(By.ID, "select-c283"))

    if genre_value == "women" and pays == "Italie":
        select_product.select_by_value("vel")
        checkbox = "checkbox-1848"
    else:
        select_product.select_by_value("mot")
        checkbox = "checkbox-3250"

    driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        driver.find_element(By.ID, checkbox)
    )
    driver.find_element(By.ID, checkbox).click()

    driver.find_element(By.XPATH, "//form/div[12]/a").click()

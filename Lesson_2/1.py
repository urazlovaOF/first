from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_class_name("trollface.btn.btn-primary").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_id("input_value").text
    result_x = calc(x)
    browser.find_element_by_id("answer").send_keys(result_x)

    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()
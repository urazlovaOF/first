from selenium import webdriver
import time
import math
import pytest

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_answer(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)

    answer = math.log(int(time.time()))
    answer_input = browser.find_element_by_tag_name("textarea")
    answer_input.send_keys(str(answer))
    browser.find_element_by_tag_name("button").click()

    correct_answer = browser.find_element_by_css_selector(".smart-hints__hint")
    correct_answer_text = correct_answer.text

    assert correct_answer_text == "Correct!", f"The hint is {correct_answer_text}"






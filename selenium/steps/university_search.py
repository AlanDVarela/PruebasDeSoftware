# -*- coding: utf-8 -*-
# pylint: disable=import-error,no-name-in-module
"""
Module for university search step definitions using Behave and Selenium.
"""
import time

from behave import then, when
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@when("I click the first result")
def click_first_link(context):
    """Clicks the first search result in Google."""
    wait = WebDriverWait(context.driver, 15)
    first_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div#search h3"))
    )
    first_link.click()


@then('I should be on "{expected_domain}"')
def verify_domain(context, expected_domain):
    """Verifies that the current URL contains the expected domain."""
    wait = WebDriverWait(context.driver, 20)
    try:
        wait.until(lambda d: expected_domain in d.current_url.lower())
    except TimeoutException:
        actual_url = context.driver.current_url
        assert (
            expected_domain in actual_url.lower()
        ), f"Esperaba {expected_domain} pero estoy en {actual_url}"


@when('I search "{term}" inside the site')
def internal_search(context, term):
    """Searches for a specific term inside the university's site."""
    for trigger_id in ["icon-search", "buscar_front"]:
        triggers = context.driver.find_elements(By.ID, trigger_id)
        if triggers and triggers[0].is_displayed():
            context.driver.execute_script("arguments[0].click();", triggers[0])
            time.sleep(1)
            break

    search_css = (
        "input[name='search'], input[name='s'], input#gsc-i-id1, input[type='search']"
    )

    search_input = None
    inputs = context.driver.find_elements(By.CSS_SELECTOR, search_css)

    for element in inputs:
        if element.is_displayed() and element.is_enabled():
            search_input = element
            break

    if not search_input:
        inputs = context.driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        for element in inputs:
            if element.is_displayed() and element.is_enabled():
                search_input = element
                break

    if not search_input:
        raise RuntimeError("No hay campo de texto para buscar")

    context.driver.execute_script("arguments[0].focus();", search_input)
    search_input.send_keys(Keys.COMMAND + "a")
    search_input.send_keys(Keys.CONTROL + "a")
    search_input.send_keys(Keys.BACKSPACE)
    search_input.send_keys(term + Keys.RETURN)


@then('I should see results related to "{term}"')
def verify_results(context, term):
    """Verifies that the given term appears in the search results page."""
    try:
        time.sleep(4)

        if len(context.driver.window_handles) > 1:
            context.driver.switch_to.window(context.driver.window_handles[-1])
            time.sleep(2)

        wait = WebDriverWait(context.driver, 15)

        for _ in range(3):
            try:
                body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                content = body.text.lower()
                assert (
                    term.lower() in content
                ), f"Termino '{term}' no encontrado en pagina"
                break
            except StaleElementReferenceException:
                time.sleep(1)
                continue

    except Exception as exc:
        context.driver.save_screenshot(f"error_{term}.png")
        raise exc

    finally:
        context.driver.quit()

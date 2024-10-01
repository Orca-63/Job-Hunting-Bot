from job_results import job_results
from Jobs.constants import BASE_URL
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from prettytable import PrettyTable
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class jobs(webdriver.Chrome):
    def __init__(self, teardown=False):

        service = Service(path='chromedriver.exe')

        self.teardown = teardown
        super(jobs, self).__init__(service=service, options=chrome_options)
        self.maximize_window()
        time.sleep(2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)

    def choose_Job_Title(self, title):

        title_element = self.find_element(By.ID, 'text-input-what')
        title_element.send_keys(title)

        title_element.send_keys(Keys.ENTER)
        time.sleep(2)

    def choose_Job_Location(self, location):

        location_element = self.find_element(By.ID, 'text-input-where')
        location_element.send_keys(location)

        location_element.send_keys(Keys.ENTER)

    def close_Pop_Up(self):

        try:
            cross = self.find_element(By.CSS_SELECTOR, 'button.css-yi9ndv')
            cross.click()

        except:
            pass

    def close_suggestion(self):
        try:
            cross = self.find_element(By.CSS_SELECTOR, 'button.css-k6r5io')
            cross.click()
        except:
            pass

    def choose_Education_Level(self, level):

        education_button = self.find_element(By.ID, "filter-taxo1")
        education_button.click()

        labels = self.find_elements(By.XPATH, "//fieldset//label")

        for label in labels:
            span = label.find_element(By.TAG_NAME, 'span')
            if span.text == level:
                checkbox = label.find_element(By.TAG_NAME, 'input')
                if not checkbox.is_selected():
                    checkbox.click()
                    break

        submit_element = self.find_element(
            By.CSS_SELECTOR, "button.css-4of6ml")

        submit_element.click()

    def choose_Salary(self, salary):
        salary_button = self.find_element(By.ID, 'filter-salary-estimate')
        salary_button.click()
        time.sleep(2)
        salary_menu = self.find_element(By.ID, 'filter-salary-estimate-menu')

        salary_options = salary_menu.find_elements(By.TAG_NAME, 'li')

        for option in salary_options:
            option_text = option.text
            salary_string = ''
            for j in option_text:
                if j == '₹' or j == ',':
                    continue
                elif j == '.':
                    break
                else:
                    salary_string += j

            offered_salary = int(salary_string)
            expected_salary = int(salary)

            if offered_salary >= expected_salary:
                option.click()
                time.sleep(2)
                break

    def choose_Job_Type(self, job_type):
        type_button = self.find_element(By.ID, 'filter-jobtype')
        type_button.click()
        time.sleep(2)
        filter_job_type = self.find_element(By.ID, 'filter-jobtype-menu')
        filter_job_type_options = filter_job_type.find_elements(
            By.TAG_NAME, 'li')
        for types in filter_job_type_options:
            if types.text == job_type:
                types.click()
                time.sleep(2)
                break
            else:
                continue

    def choose_industry(self, preferred_industry):
        industry_button = self.find_element(By.ID, 'filter-taxo2')
        industry_button.click()
        time.sleep(2)
        parent_element = self.find_element(
            By.CSS_SELECTOR, 'fieldset.css-1hyl41o')
        labels = parent_element.find_elements(By.TAG_NAME, 'label')

        for i in labels:
            span_element = i.find_element(By.TAG_NAME, 'span')
            checkbox = i.find_element(By.TAG_NAME, 'input')
            if span_element.text == preferred_industry:
                checkbox.click()
                submit_button = self.find_element(
                    By.CSS_SELECTOR, "button.css-4of6ml")
                submit_button.click()
                break

    def display_results(self):
        all_jobs = self.find_element(
            By.CSS_SELECTOR, 'ul.css-zu9cdh')

        results = job_results(all_jobs)

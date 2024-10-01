from selenium.webdriver.common.by import By
from prettytable import PrettyTable


class job_results:
    def __init__(self, selected_elements):
        self.selected_elements = selected_elements
        self.job_boxes = self.get_all_jobs()

    def get_all_jobs(self):
        company_name_list = []
        job_position_list = []
        location_list = []
        job_description_list = []

        for boxes in self.selected_elements.find_elements(By.TAG_NAME, 'li'):
            try:
                e = boxes.find_element(
                    By.CSS_SELECTOR, 'h2.jobTitle')
                job_position_list.append(e.text.strip())
                f = boxes.find_element(By.CSS_SELECTOR, 'span.css-63koeb')
                company_name_list.append(f.text.strip())
                g = boxes.find_element(By.CSS_SELECTOR, 'div.css-1p0sjhy')
                location_list.append(g.text.strip())
                h = boxes.find_element(
                    By.CSS_SELECTOR, 'div.css-9446fg').find_element(By.TAG_NAME, 'li')
                job_description_list.append(h.text[:10])

            except:
                pass
        try:
            table = PrettyTable()
            table.add_column('Company_Name', company_name_list)
            table.add_column('Job_Position', job_position_list)
            table.add_column('Location', location_list)

            print(table)
        except:
            pass

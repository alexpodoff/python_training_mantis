from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def home_page(self):
        wd = self.app.wd
        wd.find_element_by_id("logo-image").click()

    def project_page(self):
        wd = self.app.wd
        #self.home_page()
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_project(self, project):
        wd = self.app.wd
        self.project_page()
        wd.find_element_by_css_selector("input.button-small").click()
        self.fill_project_form(project)

    def confirm(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[@class='submit-button']/input[@class='button']").click()
        self.project_page()

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.desc)

    def get_project_list(self):
        wd = self.app.wd
        project_list = []
        self.project_page()
        rows = wd.find_elements_by_xpath("//div/div[4]/div[2]/table/tbody/tr")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            desc = cells[4].text
            project_list.append(Project(name=name, desc=desc))
        return list(project_list)

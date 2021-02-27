from base.base import Base
import page
import allure


class PageAddress(Base):

    @allure.step(title="点击添加联系人按钮")
    def page_click_add_contacts(self):
        self.base_click(page.add_contacts_button)

    @allure.step(title="输入联系人姓名")
    def page_input_name(self, name):
        allure.attach(name, "名字", allure.attachment_type.TEXT)
        self.base_input(page.input_name, name)

    @allure.step(title="输入联系人电话号码")
    def page_input_phone_number(self, phone):
        allure.attach(phone, "电话", allure.attachment_type.TEXT)
        self.base_input(page.input_phone_number, phone)

    @allure.step(title="输入联系人姓名和电话号码")
    def page_address(self, name, phone):
        self.page_input_name(name)
        self.page_input_phone_number(phone)

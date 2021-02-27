from base.base import Base
import page


class PageMessage(Base):

    def page_click_new_message(self):
        self.base_click(page.new_message)

    def page_input_message_recipient(self, name):
        self.base_input(page.message_recipient, name)

    def page_input_message_text(self, text):
        self.base_input(page.message_text, text)

    def page_click_message_send(self):
        self.base_click(page.message_send)

    def page_message(self, name, text):
        self.page_click_new_message()
        self.page_input_message_recipient(name)
        self.page_input_message_text(text)
        self.page_click_message_send()

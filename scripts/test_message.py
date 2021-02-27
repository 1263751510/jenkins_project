from base.get_driver import get_driver
from page.page02_message import PageMessage
import time
import pytest

from tool.read_txt import read_txt


def get_data():
    arrs = []
    for data in read_txt("message.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs


class TestMessage:

    def setup(self):
        self.driver = get_driver()
        self.message = PageMessage(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize(("name", "text"), get_data())
    def test_message(self, name, text):
        self.message.page_message(name, text)

import pytest
from base.get_driver import get_driver
from page.page01_address import PageAddress
from tool.read_txt import read_txt
import time


def get_data():
    arrs = []
    for data in read_txt("address.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs


class TestAddress:

    def setup(self):
        self.driver = get_driver()
        self.address = PageAddress(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize(("name", "phone"), get_data())
    def test_address(self, name, phone):
        self.address.page_click_add_contacts()
        self.address.page_address(name, phone)

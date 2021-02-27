from selenium.webdriver.common.by import By

"""以下为联系人功能配置信息"""
add_contacts_button = By.ID, "com.android.contacts:id/floating_action_button"
input_name = By.XPATH, "//*[@text='姓名']"
input_phone_number = By.XPATH, "//*[@text='电话']"

"""以下为短信功能配置信息"""
new_message = By.ID, "com.android.mms:id/action_compose_new"
message_recipient = By.XPATH, "//*[@text='接收者']"
message_text = By.XPATH, "//*[@text='键入信息']"
message_send = By.ID, "com.android.mms:id/send_button_sms"

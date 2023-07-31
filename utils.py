from aiogram.utils.helper import Helper, HelperMode, ListItem


class TestStates(Helper):
    mode = HelperMode.snake_case
    TEST_STATE_7 = ListItem()
    W_SEND_CONTACT = ListItem()
    TEST_STATE_RENAME = ListItem()
    TEST_STATE_PHOTO = ListItem()


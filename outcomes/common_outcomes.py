def assert_equal(actual, expected, message=None):
    if message:
        assert actual == expected, message
    else:
        assert actual == expected


def assert_not_equal(actual, expected, message=None):
    if message:
        assert actual != expected, message
    else:
        assert actual != expected


def assert_true(value, message=None):
    if message:
        assert value is True, message
    else:
        assert value is True


def assert_false(value, message=None):
    if message:
        assert value is False, message
    else:
        assert value is False


def assert_is_none(value, message=None):
    if message:
        assert value is None, message
    else:
        assert value is None


def assert_is_not_none(value, message=None):
    if message:
        assert value is not None, message
    else:
        assert value is not None


def assert_contains(collection, value, message=None):
    if message:
        assert value in collection, message
    else:
        assert value in collection


def assert_not_contains(collection, value, message=None):
    if message:
        assert value not in collection, message
    else:
        assert value not in collection


def assert_element_displayed(element, message=None):
    is_displayed = element.is_displayed()
    if message:
        assert is_displayed, message
    else:
        assert is_displayed


def assert_element_not_displayed(element, message=None):
    is_displayed = element.is_displayed()
    if message:
        assert not is_displayed, message
    else:
        assert not is_displayed


def assert_element_disabled(element, message=None):
    is_enabled = element.is_enabled()
    if message:
        assert not is_enabled, message
    else:
        assert not is_enabled


def assert_element_selected(element, message=None):
    is_selected = element.is_selected()
    if message:
        assert is_selected, message
    else:
        assert is_selected


def assert_element_not_selected(element, message=None):
    is_selected = element.is_selected()
    if message:
        assert not is_selected, message
    else:
        assert not is_selected


def assert_element_text(element, expected_text, message=None):
    actual_text = element.text
    if message:
        assert actual_text == expected_text, message
    else:
        assert actual_text == expected_text

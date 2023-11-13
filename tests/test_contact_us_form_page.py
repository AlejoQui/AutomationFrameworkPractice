from pages.contact_us_from_page import ContactUsFromPage
from pages.homefeed_page import HomefeedPage

homefeed_page = HomefeedPage()
contact_us_form_page = ContactUsFromPage()


def test_user_submits_contact_information():
    homefeed_page.choose_contact_us_from()
    contact_us_form_page.send_keys_enter_name()
    contact_us_form_page.send_keys_enter_email()
    contact_us_form_page.send_keys_enter_address()
    contact_us_form_page.send_keys_enter_mobile_no()

    contact_us_form_page.choose_contact_us_form_submit_button()

    contact_us_form_page.check_output_entered_name()
    contact_us_form_page.check_output_entered_email()
    contact_us_form_page.check_output_entered_address()
    contact_us_form_page.check_output_entered_mobile_no()


def test_check_header_name_in_contact_us_form_page():
    homefeed_page.choose_enter_value()
    contact_us_form_page.check_header_name()


def test_check_title_name_in_contact_us_form_page():
    homefeed_page.choose_enter_value()
    contact_us_form_page.check_title_name()

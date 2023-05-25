from behave import *


@given("I am logged into my account")
def step_impl(context):
    context.home_page.open_home_page()
    context.home_page.click_login_button()
    context.home_page.insert_email()
    context.home_page.insert_password()
    context.home_page.click_singin_button()


@when("I see the upgrade offer modal")
def step_impl(context):
    context.my_dashboard.i_see_the_offer()


@when("I click on x button")
def step_impl(context):
    context.my_dashboard.close_offer()


@then("The offer doesn't appear anymore")
def step_impl(context):
    context.my_dashboard.offer_is_closed()


@when("I click on add button")
def step_impl(context):
    context.my_dashboard.add_button()


@when("I insert my workspace name")
def step_impl(context):
    context.my_dashboard.name_your_space()


@when("I push the Create button")
def step_impl(context):
    context.my_dashboard.create_your_space()


@then("My new workspace is created")
def step_impl(context):
    context.my_dashboard.my_new_space()


@when("I see the DesignSpace tour overlay")
def step_impl(context):
    context.my_dashboard.i_see_design_tour()


@when("I close the DesignSpace tour")
def step_impl(context):
    context.my_dashboard.close_design_tour()


@then("The DesignSpace tour should be closed")
def step_impl(context):
    context.my_dashboard.design_tour_is_closed()


@when("I chose the UI drawing add icon")
def step_impl(context):
    context.my_dashboard.myfirst_create()


@when("I insert my Wireframe name")
def step_impl(context):
    context.my_dashboard.wireframe_name()


@when("I search for my desired UI pack and i select it")
def step_impl(context):
    context.my_dashboard.ui_pack()


@then("My Wireframe is created")
def step_impl(context):
    context.my_dashboard.my_new_wireframe()


@when("From navigation bar i click on store icon")
def step_impl(context):
    context.my_dashboard.store_icon()


@when("I am in store and i click on Templates bar")
def step_impl(context):
    context.my_dashboard.template_tab()


@when("I click on the desired template and import it")
def step_impl(context):
    context.my_dashboard.marketing_pack_email()


@then("I can save my customized Wireframe")
def step_impl(context):
    context.my_dashboard.save_changes()


@when("I select from space settings the option Rename")
def step_impl(context):
    context.my_dashboard.settings_in_wireframe()


@when("I put the new name")
def step_impl(context):
    context.my_dashboard.rename_name()


@when("I confirm the rename")
def step_impl(context):
    context.my_dashboard.confirm_rename()


@then("My Wireframe is renamed")
def step_impl(context):
    context.my_dashboard.check_the_rename()
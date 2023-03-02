from behave import given, when, then

@given(u'I navigate to the index pages')
def nav(context):
    context.browser.get('http://127.0.0.1:5000/')
    assert context.browser.find_element_by_id("artist_num").text == "717"
    assert context.browser.find_element_by_id("mbtag_num").text == "1997"
    assert context.browser.find_element_by_id("term_num").text == "2000"

@when(u'I click on the link to mdtag details')
def click(context):
    a_link = context.browser.find_element_by_xpath('//a[1]')
    a_link.click()
    print("ok")

@then(u"Madtag's data statistics and analysis page should be displayed")
def details(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/artist_mgtag'
    assert 'Back' in context.browser.page_source
from poium import Page, PageElement

class BBSPage(Page):
    load_page = PageElement(id_="android:id/navigationBarBackground")
    search_box = PageElement(id_="com.meizu.flyme.flymebbs:id/nx")
    search_button = PageElement(id_="com.meizu.flyme.flymebbs:id/o2")
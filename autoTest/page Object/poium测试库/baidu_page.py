from poium import Page, Element, Elements   # 一组元素时用Elements
# 支持八种定位


class BaiduPage(Page):
    """
    百度page层，可以封装页面上的元素
    """

    search_input = Element(id_='kw', timeout=2, describe='搜索框')   # 注意: id_
    search_button = Element(id_='su', timeout=2, describe='搜索按键')
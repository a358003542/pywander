from pywander.text.country_zh_abbr import get_country_zh_abbr


def test_get_country_zh_abbr():
    assert get_country_zh_abbr('巴西') == '巴西'
    assert get_country_zh_abbr('奥地利') == '奥'
    assert get_country_zh_abbr('澳大利亚') == '澳'
    assert get_country_zh_abbr('比利时') == '比利时'
    assert get_country_zh_abbr('德国') == '德'
    assert get_country_zh_abbr('俄罗斯') == '俄'
    assert get_country_zh_abbr('法国') == '法'
    assert get_country_zh_abbr('荷兰') == '荷'
    assert get_country_zh_abbr('美国') == '美'
    assert get_country_zh_abbr('日本') == '日'
    assert get_country_zh_abbr('意大利') == '意'
    assert get_country_zh_abbr('印度') == '印'
    assert get_country_zh_abbr('英国') == '英'
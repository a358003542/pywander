
def test_stopwords():
    from pywander.nlp.stopwords import multiple_stopwords
    result = multiple_stopwords('english', 'chinese')
    assert len(result) > 0
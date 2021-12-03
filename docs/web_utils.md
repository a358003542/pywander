## crawler
need the `requests` and `beautifulsoup4` and `my_fake_useragent` and `diskcache` modules.

### URLType
define four type of URL:

```
class URLType(Enum):
    """
    refUrl: 除了Absolute URL，其他URL都需要根据本URL所在的文章的refUrl才能得到绝对URL
    """
    Absolute = 1
    # 'https://www.cis.rit.edu/htbooks/nmr/chap-10/chap-10.htm'
    MissScheme = 2
    # ’//www.cis.rit.edu/htbooks/nmr/chap-10/chap-10.htm‘ refUrl
    RelativeSite = 3
    # ’/htbooks/nmr/chap-10/chap-10.htm‘ refUrl
    RelativeFolder = 4
    # ’chap-10.html‘ refUrl
    RelativeArticle = 5
    # ’#sec1‘
    InValid = 6
```


### to_absolute_url
```python
def to_absolute_url(url, refUrl):
    """
    给定好refUrl，利用urljoin就能得到绝对url
    refUrl: 除了绝对URL，其他URL都需要根据本URL所在的文章的Url也就是refUrl
            才能得到绝对URL

    如果是爬虫，一开始就将遇到的URL转成绝对URL可能是一个好的选择，但其他文档处理情况则
    不能这样简单处理，需要小心地根据URL的各种类型来采取不同的处理策略。
    """
    return urljoin(refUrl, url)
```



### is_url_inSite
```python
def is_url_inSite(url, refUrl):
    """
    is the url in site.
    the judgement is based on the refUrl's netloc.

>>> is_url_inSite('https://code.visualstudio.com/docs',
    'https://code.visualstudio.com/docs/python/linting')
True
    """
    p = urlsplit(url)
    if p.netloc == urlsplit(refUrl).netloc:
        return True
    else:
        return False
```


    
### is_url_inArticle

```python
def is_url_inArticle(url, refUrl):
    """

    """
    p = urlsplit(url)
    if p.fragment:
        return True
    else:
        return False
```

### check_url_type
```python

def check_url_type(url):
    """
    这里只是对URL类型进行判断，从网络下或的HTML文件需要分辨各种URL类型并采取相应的策略
    """
    p = urlsplit(url)
    if p.scheme and p.netloc and p.path:
        return URLType.Absolute

    if not p.scheme and p.netloc and p.path:
        return URLType.MissScheme

    if not p.scheme and not p.netloc and p.path:
        if p.path.startswith('/'):
            return URLType.RelativeSite
        else:
            return URLType.RelativeFolder
    if not p.scheme and not p.netloc and not p.path:
        if p.fragment:
            return URLType.RelativeArticle
        else:
            return URLType.InValid

```
### get_url_fragment
```python
def get_url_fragment(url):
    """
    please notice the fragment not include the symbol #
    """
    p = urlsplit(url)
    return p.fragment
```
### remove_url_fragment
```python
def remove_url_fragment(url):
    """
    remove url fragment like `#sec1` and the parameters on url will
    keeped still.
    """
    defragmented, frag = urldefrag(url)
    return defragmented
```
### get_webpage_links
```python
def get_webpage_links(html, name='a', id="", class_="", **kwargs):
    """
    :param html: 目标网页的text内容

    input html content, and use the beautifulsoup parse it, get all the
    <a href="link"> and return the link.

    sometime you may want the specific  <a href="link"> which is in where id
    or where class etc.

    you can set `name="div" id="what"'` to narrow the url target into
    the SoupStrainer for the first filter,
    so you can specific which url you want to collect.

    this function will return:
    (
        soup,
        {
            ‘href’: [beatifulsoup4 Tag object, ...]
        }
    )
    """
```
### get_webpage_images
```python
def get_webpage_images(html, name="img", id="", class_="", **kwargs):
    """
    :param html: 目标网页的text内容

    input a html content , and use the beautifulsoup parse it, get all the
    <img src="link"> and return the link.

    sometime you may want the specific  <img src="link"> which is in where id
    or where class etc.

    you can set `name="div" id="what"'` to narrow the url target
    into the SoupStrainer for the first filter,
    so you can specific which url you want to collect.

    this function will return:
    (
        soup,
        {
            ‘src’: [beatifulsoup4 Tag object, ...]
        }
    )
    """
```
```
def parse_webpage_links(url, html, name='a', id="", class_="", **kwargs):
    """
    :param url: 目标网页的url（或者该网站的base url也是可以的）
    :param html: 目标网页的text内容

    input html content, and use the beautifulsoup parse it, get all the
    <a href="link"> and return the link.

    we will do the extrawork: to_absolute_url and remove_url_fragment.

    sometime you may want the specific  <a href="link"> which is in where id
    or where class etc.

    you can set `name="div" id="what"'` to narrow the url target into the SoupStrainer for the first filter, so you can specific which url you want to collect.

    this function will return a set of links.

    """
```


### download
比如下载图片
```
def download(url, filename, download_timeout=30, override=False, **kwargs):
    """
    High level function, which downloads URL into tmp file in current
    directory and then renames it to filename autodetected from either URL
    or HTTP headers.
    :param out: output filename or directory
    :return:    filename where URL is downloaded to
    """
```

### requests_web
除了随机的UserAgent之外，网络请求结果会缓存，也就是同样的URL不会再请求两次了。

```python
@func_cache(use_cache_callback=use_cache_callback_requests_web)
def requests_web(url):
    """
    有数据则直接使用 没有数据则试着从网络上请求
    直接使用数据的时候会根据数据的时间戳来判断新旧，如果数据过旧则启动后台更新线程

    :param url:
    :return:
    """
```
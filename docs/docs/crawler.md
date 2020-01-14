## crawler
need the `requests` and `beautifulsoup4` module.

### is_relative_url

is the url a relative url (including the `/what` )

### to_absolute_url
use the baseurl and the target url generate the target absolute url, no matter of the target url is relative url or absolute url. just make sure the baseurl is definitely in this site domain.
```text
to_absolute_url(baseurl, url)
```

### remove_url_fragment
remove the target url fragment like `#sec1` and the parameters on url will keeped still.
    
### parse_webpage_links

input html content, and use the beautifulsoup parse it, get all the
`<a href="link">` and return the link.

we will do the extrawork: to_absolute_url and remove_url_fragment.

sometime you may want the specific  `<a href="link">` which is in where id
or where class etc.

you can set `name="div" id="what"'` to narrow the url target into the SoupStrainer for the first filter, so you can specific which url you want to collect.

this function will return a set of links.

### parse_webpage_images
input a html content , and use the beautifulsoup parse it, get all the
    `<img src="link">` and return the link.

we will do the extrawork: to_absolute_url.

sometime you may want the specific  `<img src="link">` which is in where id
or where class etc.

you can set `name="div" id="what"'` to narrow the url target into the SoupStrainer for the first filter, so you can specific which url you want to collect.

this function will return a set of image links.

### download
High level function, which downloads URL into tmp file in current
directory and then renames it to filename autodetected from either URL
or HTTP headers.
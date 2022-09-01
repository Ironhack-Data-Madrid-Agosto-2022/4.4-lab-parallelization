def index_page(url):
    import requests as req
    from slugify import slugify
    texto=req.get(url).text
    r = slugify(texto)
    url=slugify(url)
    f = open(url+'.html', "w")
    f.write(r)
    f.close()
    pass
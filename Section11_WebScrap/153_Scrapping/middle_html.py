from bs4 import BeautifulSoup
import re

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

parser = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_item_name():
    locator = 'article.product_pod h3 a'
    item_link = parser.select_one(locator)
    item_name = item_link.attrs['title']
    print(item_name)


def find_item_link():
    locator = 'article.product_pod h3 a'
    item_link = parser.select_one(locator)
    item_name = item_link.attrs['href']
    print(item_name)


def find_item_price():
    locator = 'article.product_pod p.price_color'
    item_price = parser.select_one(locator).string  # £51.77
    pattern = '£([0-9]+\.[0-9]+)'
    matcher = re.search(pattern, item_price)
    print(float(matcher.group(1)))


def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_tag = parser.select_one(locator)
    classes = star_rating_tag.attrs['class']
    rating_class = [r for r in classes if r != 'star-rating']
    # rating_class = filter(lambda x: x != 'star-rating', classes)
    print(rating_class[0])



find_item_name()
find_item_link()
find_item_price()
find_item_rating()
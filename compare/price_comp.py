from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def flipkart(name):
    price = '0'
    title = ""
    url = "https://www.flipkart.com"
    image = ""

    try:
        # global flipkart
        name1 = name.replace(" ", "+")  # iphone x  -> iphone+x
        res = requests.get(f'https://www.flipkart.com/search?q={name1}', headers=headers)

        print("\nSearching in flipkart....")
        soup = BeautifulSoup(res.text, 'html.parser')
        div_type_1 = soup.find_all('div', attrs={'class': '_4ddWXP'})
        div_type_2 = soup.find_all('div', attrs={'class': '_2kHMtA'})

        if len(div_type_1) > 1:
            # New Class For Product Name
            print("div_type_1")
            for i in range(0, len(soup.select('.s1Q9rs'))):
                title = soup.select('.s1Q9rs')[i].getText().strip()
                title = title.upper()
                if name.upper() in title:
                    # New Class For Product Price
                    price = soup.select('._30jeq3')[i].getText().strip()
                    title = soup.select('.s1Q9rs')[i].getText().strip().upper()
                    url += soup.select('.s1Q9rs')[i]['href'].strip()
                    image = soup.select('._396cs4')[i + 1]['src'].strip()
                    if image.find("placeholder_fcebae.svg") != -1:
                        image = "https:" + image
                        print(image)
                    print("Flipkart:")
                    print(title)
                    print(price)
                    print(image)
                    print(url)
                    print("-----------------------")
                    break
                else:
                    print("Flipkart:No product found!")
                    print("-----------------------")
                    title = "No product found"
                    price = '-'

        elif len(div_type_2) > 1:
            print("div_type_2")
            for i in range(0, len(soup.select('._4rR01T'))):
                title = soup.select('._4rR01T')[i].getText().strip()
                title = title.upper()
                if name.upper() in title:
                    # New Class For Product Price
                    price = soup.select('._30jeq3')[i].getText().strip()
                    title = soup.select('._4rR01T')[i].getText().strip().upper()
                    url += soup.select('._1fQZEK')[i]['href'].strip()
                    image = soup.select('._396cs4')[i + 1]['src'].strip()
                    if image.find("placeholder_fcebae.svg") != -1:
                        image = "https:" + image
                        print(image)
                    print("Flipkart:")
                    print(title)
                    print(price)
                    print(image)
                    print(url)
                    print("-----------------------")
                    break
                else:
                    print("Flipkart:No product found!")
                    print("-----------------------")
                    title = "No product found"
                    price = '-'
        else:
            print("Flipkart:No product found!")
            print("-----------------------")
            title = "No product found"
            price = '-'

    except:
        print("Flipkart:No product found!")
        print("-----------------------")
        title = "No product found"
        price = '0'

    product = {"title": title, "price": price, "url": url, "image": image, "site": "Flipkart"}
    return product


def amazon(name):
    title = ""
    url = "https://www.amazon.in"
    price = "0"
    image = ""
    try:
        # global amazon
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)
        print("\nSearching in amazon:")
        soup = BeautifulSoup(res.text, 'html.parser')
        title_list = soup.select('.a-color-base.a-text-normal')
        # print(title_list)
        amazon_page_length = int(len(title_list))
        # print(amazon_page_length)
        for i in range(0, amazon_page_length):
            name = name.upper()
            title = soup.select(
                '.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in title:
                title = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                price = "₹" + soup.select('.a-price-whole')[i].getText().strip()
                url += soup.select(".a-link-normal.a-text-normal.s-no-hover.a-text-normal")[i]['href'].strip()
                image = soup.select("div.a-section.aok-relative.s-image-fixed-height img")[i]['src'].strip()
                print("Amazon:")
                print(title)
                print(price)
                print(url)
                print(image)
                print("-----------------------")
                break
            else:
                i += 1
                i = int(i)
                if i == amazon_page_length:
                    print("amazon : No product found!")
                    print("-----------------------")
                    title = "No product found"
                    price = '-'
                    break
        product = {"title": title, "price": price, "url": url, "image": image, "site": "Amazon"}
        return product
    except:
        print("amazon: No product found!")
        print("-----------------------")
        title = "No product found"
        price = '-'
    product = {"title": title, "price": price, "url": url, "image": image, "site": "Amazon"}
    return product


def convert(a):
    b = a.replace(" ", '')
    c = b.replace("INR", '')
    d = c.replace(",", '')
    f = d.replace("₹", '')
    g = int(float(f))
    return g


def price_comp(search_string):
    filpkart_product = flipkart(search_string)
    amazon_product = amazon(search_string)

    if filpkart_product["price"] == '-':
        print("No product found!")
    else:
        print("\nFLipkart Price:", filpkart_product)
    if amazon_product["price"] == '-':
        print("No Product found!")
    else:
        print("\namazon price:", amazon_product)

    return {
        "Amazon": filpkart_product,
        "Flipkart": amazon_product,
    }

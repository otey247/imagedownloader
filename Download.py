from imgdl import download

urls = [
    'https://cdn.shopify.com/s/files/1/0227/0581/products/Good-News-The-End-Is-Near-So-Lets-Drink-Beer-Lager-16OZ-CAN_2000x.jpg?v=1662202922'
]

paths = download(urls, store_path='~/.datasets/images', n_workers=50)

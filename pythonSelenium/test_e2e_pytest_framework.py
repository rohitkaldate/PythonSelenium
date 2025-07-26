import os
import sys

from Pages.purchase import Purchase

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Pages.launch import Launch
from Pages.shop import Shop

def test_e2e(browserInstance):
    driver = browserInstance

    ##Launch the website to automate
    launch = Launch(driver)
    launch.launchPage()

    ## Further actions to add the product to cart and purchase product and validate the success mesaage
    shop = Shop(driver)
    shop.shopItems("Blackberry")
    shop.checkout()
    purchase = Purchase(driver)
    purchase.purchase_product()
    purchase.delivery_address("ind")
    purchase.validate_result()
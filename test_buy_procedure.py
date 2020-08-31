from pages.drivers import Drivers
from pages.alza_page import AlzaPage
from pages.dph_count import count_dph
import time

browser = Drivers('--start-maximized').chrome()

ap = AlzaPage(driver=browser)
checkmark = '✓'
# test start
ap.go()
# go to mobile phones
ap.mobile_phones.move_to()
# click Iphone 11 pro link and get the name price
ap.iphone11pro_link.click()
ip_name1 = ap.product1.text
ip_price1 = ap.price_product1.format_price()

# go to product's page, get name and price and price excl.vat
ap.product1.click()
ip_name2 = ap.product_name.text
ip_price2 = ap.product_price.format_price()
exvat_price = ap.product1_exc_vat.format_price()
assert ip_price1 == ip_price2
# calculate vat
my_vat = count_dph(exvat_price)

# select all the additional items and get price
ap.checkbox_1.click()
price_item1 = ap.price_checkbox_1.format_price()
ap.checkbox_2.click()
price_item2 = ap.price_checkbox_2.format_price()
ap.checkbox_3.click()
price_item3 = ap.price_checkbox_3.format_price()
ap.checkbox_4.click()
price_item4 = ap.price_checkbox_4.format_price()
# accept protection glass warning dialog
ap.glass_dialog.click()
# go to proceed page and get the name
ap.add_to_card.click()
ip_name3 = ap.product_name_checkout.format_name()
# go to basket and get the name
ap.proceed_checkout.click()
ip_name4 = ap.product_name_basket.format_name()
# compare all product names through out the procedure
assert ip_name1 == ip_name2 == ip_name3 == ip_name4
# get total price using calculated vat tax for the main item
my_total = int(my_vat) + int(price_item1) + int(price_item2) + int(price_item3) + int(price_item4)
# get total price with vat and without vat
browser.refresh()
ttl_vat = ap.total_vat.format_price()
# validate correct price with vat calculation on the main item
assert str(ttl_vat) == str(my_total)
print(f'expected total price: {my_total}')
print(f'real total price:     {ttl_vat} {checkmark}')
print('test passed')
browser.quit()






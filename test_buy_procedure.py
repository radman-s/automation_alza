from pages.drivers import Drivers
from pages.alza_page import AlzaPage
from pages.dph_count import count_dph
import time

browser = Drivers('--start-maximized').chrome()

ap = AlzaPage(driver=browser)
checkmark = '✓'
# test start
ap.go()
ap.mobile_phones.move_to()

ap.iphone11pro_link.click()
# get first name and price
name1 = ap.product_name1.text()
# with dph
price1 = ap.product_price1.format_price()
# no dph
no_dph = ap.product_price_nodph.format_price()
# calculate dph
my_dph = count_dph(no_dph)
round_dph = round(float(my_dph))

print(f'price with dph:   {price1}')
print(f'price no dph:     {no_dph}')
print(f'calculate dph:    {round_dph}{checkmark}')
# validate dph is calculated correctly
assert str(price1) == str(round_dph)

ap.iphone11pro_pic.click()
# get second name and price
name2 = ap.product_name2.text()
price2 = ap.product_price2.format_price()
# validate product's name and price corresponds
assert name1 == name2
assert str(price1) == str(price2)
# select case checkbox and get price
ap.case_check.click()
case = ap.case_price.format_price()
# select warranty checkbox and get price
ap.warranty_check.click()
warranty = ap.warranty_price.format_price()
# select insurance checkbox and get price
ap.insurance_check.click()
insurance = ap.insurance_price.format_price()
# select protection glass checkbox and get price
ap.protect_glass_price.click()
glass = ap.protect_glass_price.format_price()
# calculate total price with all the items included
all = int(warranty) + int(insurance) + int(glass) + int(my_dph) + int(case)

ap.protect_glass_button.click()
# proceed to the shopping basked
ap.buy_button.click()
ap.basked.click()
# get total price
ttl1 = ap.total_price.format_price()
# validate correct total price
assert str(all) == str(ttl1)
print(f'case:             {case}')
print(f'waranty:          {warranty}')
print(f'insurance:        {insurance}')
print(f'protection glass: {glass}')
print(f'calculate total:  {all}')
print(f'price basked:     {ttl1}{checkmark}')

browser.quit()





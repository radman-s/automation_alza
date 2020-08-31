from pages.drivers import Drivers
from pages.alza_page import AlzaPage
from pages import info

browser = Drivers('--start-maximized').chrome()
ap = AlzaPage(driver=browser)

# test start
ap.go()
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
ap.careers.click()
ap.it.click()
ap.qa.click()
browser.refresh()
ap.name.input_text(info.nm)
ap.email.input_text(info.em)
ap.phone.input_text(info.ph)
ap.link.input_text(info.lk)
ap.cover_letter.input_text(info.cov_letter)
ap.upload_cv.upload(info.path)
ap.send.click()
print('test passed')


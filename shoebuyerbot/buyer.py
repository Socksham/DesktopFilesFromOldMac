# import mechanize

# br = mechanize.Browser()

# page = br.open("https://www.yeezysupply.com/delivery")
# br.addheaders = [("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15")]
# br.set_all_readonly(False)
# br.set_handle_robots(False)
# br.set_handle_refresh(False)
# for form in br.forms():
#     print(form)


from selenium import webdriver

browser = webdriver.Chrome("/Users/sakshamgupta/Desktop/Quizlet Bot/chromedriver")
browser.get("https://www.yeezysupply.com/delivery")




import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)

br.open("https://quizlet.com/live")
print(br.forms())

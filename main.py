import webbrowser

url = 'https://twitter.com/'

username = input("Please enter your twitter email:\n")
password = input("Please enter your twitter password: \n")

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open(url)




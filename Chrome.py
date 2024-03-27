from selenium import webdriver
# Importing options for the Opera module
#from selenium.webdriver.opera.options import Options

print ('hello')

print ('hello from Dima')
executable_path="C:\\Users\\Андрей\\AppData\\Local\\Programs\\Opera\\operadriver.exe"
from selenium.webdriver import Opera, OperaOptions
#Set the path to the Opera driver executable
#executable_path = ‘/path/to/operadriver’
#Set the options for the Opera browser
options = OperaOptions()
options.add_argument("–disable-gpu")
options.add_argument("–no-sandbox")
#Create a new instance of the Opera driver
driver = Opera(executable_path,options)

browser = webdriver.Opera('C:/Users/Андрей/AppData/Local/Programs/Opera')
#browser = webdriver.Opera(options=options, executable_path=r'location_of_operadriver.exe'
browser.get('https://vk.com')


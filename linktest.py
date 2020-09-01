
# Fill username and pwd in the script 
# Run on terminal 
# enter string to be searched in groups
# wait for the completion, out excel file will be generated 


from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import datetime
import pandas as pd
from getpass import getpass
from IPython import embed 
path_to_chromedriver = os.path.join(
    os.getcwd(), 'chromedriver_linux64/chromedriver')
#username = input('Enter your UserName : ')
#
#username = 'gabhishek339@gmail.com'
#username = 'adit.mishra.7'

#password = getpass()
#password = 'mnbvcxz@123'
#password = 'adit@123'

#username = input('Enter your UserName : ')
#password = input('Enter your Password : ')
#input_search = input(
 #   "Entert the String to be Searched by ',' seprate like name1, name2, name3 : ")
#input_search_list = input_search.split(',')
#print('input_search_list', input_search_list)
group_detail = []


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)


class Account:
    def __init__(self, driver, Username, Password):
        self.driver = driver
        self.login(Username, Password)

    def login(self, Username, Password):
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(Username)
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Password)
        #driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
        time.sleep(10)
        # driver = webdriver.Chrome()
        time.sleep(5)

    def get_group_detail(self):
            group_url =  ['https://www.facebook.com/groups/calcuttaribbon/about','https://www.facebook.com/groups/PrintingTec/about','https://www.facebook.com/groups/1070775659679708/about','https://www.facebook.com/groups/328405567316494/about','https://www.facebook.com/groups/374069602640035/about','https://www.facebook.com/groups/printingpackagingprocurement/about','https://www.facebook.com/groups/1564373077166019/about','https://www.facebook.com/groups/284766135328401/about','https://www.facebook.com/groups/326808834051057/about','https://www.facebook.com/groups/432193520721793/about','https://www.facebook.com/groups/371910553537399/about','https://www.facebook.com/groups/1222023914585187/about','https://www.facebook.com/groups/1185548018256792/about','https://www.facebook.com/groups/1694219247302338/about','https://www.facebook.com/groups/494289550630177/about','https://www.facebook.com/groups/tshirtsprintinguae/about','https://www.facebook.com/groups/1413017012121168/about','https://www.facebook.com/groups/390120691404773/about','https://www.facebook.com/groups/963185413758575/about','https://www.facebook.com/groups/1994919184107634/about','https://www.facebook.com/groups/digitaldukaandaar/about','https://www.facebook.com/groups/532006920541178/about','https://www.facebook.com/groups/600355670095727/about','https://www.facebook.com/groups/flexnbannerprinting/about','https://www.facebook.com/groups/PrintingMineOfficial/about','https://www.facebook.com/groups/314625318735268/about','https://www.facebook.com/groups/1415752075365954/about','https://www.facebook.com/groups/572656103248090/about','https://www.facebook.com/groups/342796603123432/about','https://www.facebook.com/groups/424339394602319/about','https://www.facebook.com/groups/823338217676835/about','https://www.facebook.com/groups/976659505855137/about','https://www.facebook.com/groups/150339565609409/about','https://www.facebook.com/groups/685960758909509/about','https://www.facebook.com/groups/604598940277585/about','https://www.facebook.com/groups/266759453871780/about','https://www.facebook.com/groups/PrusaOfficial/about','https://www.facebook.com/groups/201640394116441/about','https://www.facebook.com/groups/938761639501149/about','https://www.facebook.com/groups/183844835602741/about','https://www.facebook.com/groups/130171211162356/about','https://www.facebook.com/groups/175859466291744/about','https://www.facebook.com/groups/557076824412030/about','https://www.facebook.com/groups/539601019547548/about','https://www.facebook.com/groups/186745281749052/about','https://www.facebook.com/groups/offsetmachinery/about','https://www.facebook.com/groups/printpackclub/about','https://www.facebook.com/groups/165238450197656/about','https://www.facebook.com/groups/172064452838986/about','https://www.facebook.com/groups/jobsprintingandpackaging/about','https://www.facebook.com/groups/495454250956001/about','https://www.facebook.com/groups/403468603037372/about','https://www.facebook.com/groups/1626153940993309/about','https://www.facebook.com/groups/Buyers.and.Suppliers/about','https://www.facebook.com/groups/872081146614429/about','https://www.facebook.com/groups/NAIJAPRINTINGCOMMUNITY/about','https://www.facebook.com/groups/962941437053445/about','https://www.facebook.com/groups/621747335300332/about','https://www.facebook.com/groups/1377257752302022/about','https://www.facebook.com/groups/541187252603075/about','https://www.facebook.com/groups/philippineprintingentrepreneurs/about','https://www.facebook.com/groups/1841053396013739/about','https://www.facebook.com/groups/laserbiz/about','https://www.facebook.com/groups/871943369856941/about','https://www.facebook.com/groups/2071870216372483/about','https://www.facebook.com/groups/144202299407592/about','https://www.facebook.com/groups/541153152702914/about','https://www.facebook.com/groups/348656502458738/about','https://www.facebook.com/groups/270664767463482/about','https://www.facebook.com/groups/483988309123382/about','https://www.facebook.com/groups/908073522669931/about','https://www.facebook.com/groups/405230376479052/about','https://www.facebook.com/groups/244710969012255/about','https://www.facebook.com/groups/886397661438693/about','https://www.facebook.com/groups/1951975891692906/about','https://www.facebook.com/groups/570197899811720/about','https://www.facebook.com/groups/xeroapp/about','https://www.facebook.com/groups/1145966129107311/about','https://www.facebook.com/groups/736463586492450/about','https://www.facebook.com/groups/1802190430050935/about','https://www.facebook.com/groups/copiertechclubindia/about','https://www.facebook.com/groups/2732932513646409/about','https://www.facebook.com/groups/551762948599343/about','https://www.facebook.com/groups/1874269179477471/about','https://www.facebook.com/groups/1105162399884004/about','https://www.facebook.com/groups/103580426342481/about','https://www.facebook.com/groups/585996068709263/about','https://www.facebook.com/groups/1687001171610217/about','https://www.facebook.com/groups/511506489535626/about']
            for group in group_url:
                driver.get(group)
                time.sleep(2)
                try:
                    driver.find_element_by_xpath(
                        '//*[@id="u_0_v"]/div[1]/a/span[1]').click()
                    time.sleep(3)
                    group_name = driver.find_element_by_xpath(
                        '//*[@id="seo_h1_tag"]/a').get_attribute('innerHTML')
                    group_member = driver.find_element_by_xpath(
                        '//*[@id="pagelet_group_about"]/div[2]/div[1]/span').get_attribute('innerHTML')
                    group_admin_url = []
                    group_admin_div_number = len(driver.find_elements_by_xpath(
                        '//*[@id="pagelet_group_about"]/div[2]/div[2]/div'))
                    group_admin_list = driver.find_elements_by_xpath(
                        '//*[@id="pagelet_group_about"]/div[2]/div[2]/div[{0}]/span/a'.format(group_admin_div_number))
                    for elm in group_admin_list:
                        group_admin_url.append(elm.get_attribute('href'))

                    group_detail.append({"group_name": group_name, "group_url": group,
                                        "group_member": group_member, "group_admin": " ".join(group_admin_url)})

                except:
                    try:
                        group_name = driver.find_element_by_xpath(
                        '//*[@id="seo_h1_tag"]/a').get_attribute('innerHTML')
                        group_member = driver.find_element_by_xpath(
                            '//*[@id="pagelet_group_about"]/div[2]/div[1]/span').get_attribute('innerHTML')
                        group_admin_url = []
                        group_admin_div_number = len(driver.find_elements_by_xpath(
                            '//*[@id="pagelet_group_about"]/div[2]/div[2]/div'))
                        group_admin_list = driver.find_elements_by_xpath(
                            '//*[@id="pagelet_group_about"]/div[2]/div[2]/div[{0}]/span/a'.format(group_admin_div_number))
                        for elm in group_admin_list:
                            group_admin_url.append(elm.get_attribute('href'))

                        group_detail.append({"group_name": group_name, "group_url": group,
                                            "group_member": group_member, "group_admin": ",".join(group_admin_url)})
                    except Exception as e:
                        print("Error : ", e)
            return group_detail



def launchfirefox(driverLocation, url):
    # for crome browser
    driver = webdriver.Chrome(
        executable_path=path_to_chromedriver, options=chrome_options)

    # for fire fox
    # driver = webdriver.Firefox(executable_path=driverLocation)

    driver.implicitly_wait(20)
    driver.get(url)
    return driver


def make_file(group_detail):
    #save in file
    file_path = os.path.join(os.getcwd(), '{0}_{1}.xlsx'.format('printing', datetime.datetime.now()))
    df = pd.DataFrame(group_detail)
    writer = pd.ExcelWriter(file_path,engine='xlsxwriter',options={'strings_to_urls': False})
    time.sleep(2)
    df.to_excel(writer, 'Sheet1')
    time.sleep(2)
    writer.save()
    time.sleep(2)

    print('your file path is {}'.format(file_path))



driver = launchfirefox(path_to_chromedriver, 'https://www.facebook.com')
ACC = Account(driver, username, password)
#time.sleep(25)
#for group_name in input_search_list:
group_details = ACC.get_group_detail()
make_file(group_detail)
driver.close()



from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
import os

opts = Options()
opts.set_headless()
assert opts.headless

### In this example i will use a range of numbered pages to extract info

def scrapper(path, rangeofnumbered, iplist, geckopath, waitingtime = 1, interestedpattern, vpnon, vpnoff):

    '''

    This Web Scrapper is useful even with Distil Network protection


    :param path: str the domain of the page of interested
    :param rangeofnumbered: range Range of the numbered pages of interested
    :param dateobtained: tuple The data of interested
    :param iplist: list list of ips that you want to use
    :param geckopath: str the gecko driver path in your computer
    :param waitingtime: int seconds to wait for any visit default = 1
    :param interestedpattern: str the data that you are looking for
    :param vpnon: str command in shell to start vpn
    :param vpnoff: str command in shell to finished vpn
    :return:
    '''

    dataobtained =[]


    for i in rangeofnumbered:

        # Use a vpn to use a new ip for example vpn
        count = [0]
        os.system(vpnon + str(iplist[count]%len(iplist)))

        # Create the profile with user-agent random
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", UserAgent().random)
        profile.update_preferences()

        # The page of interest
        interestedpath= path + rangeofnumbered

        # Create the web driver
        driver = webdriver.Firefox(executable_path=geckopath, options=opts,
                                   firefox_profile=profile)


        print("good connection for " + interestedpath )
        driver.implicitly_wait(waitingtime)  # seconds
        driver.get(interestedpath)

        lookfor = driver.find_elements_by_class_name(interestedpattern)
        for item in lookfor:
            dataobtained.append(item.text)

        os.system(vpnoff)

    return dataobtained
from modules import *







global _
with open('account.txt') as db:
    account = db.readlines()
    account = [info.strip() for info in account]
    _ = {
        'email':account[0],
        'password':account[1]
        #'displayName':names.get_first_name()
    }
    
seleniumwire_options = {
    'proxy':{
        'http':f'{proxy["type"]["http"]}://{proxy["user"]}:{proxy["pass"]}@{proxy["host"]}:{proxy["port"]}',
        'https':f'{proxy["type"]["https"]}://{proxy["user"]}:{proxy["pass"]}@{proxy["host"]}:{proxy["port"]}',
        'no_proxy':'localhost,127.0.0.1'
    }
}
options = uc.ChromeOptions()
#options.add_argument('--headless')

driver = uc.Chrome(
        options=options,
        seleniumwire_options=seleniumwire_options
    )


def checkExistByXPATH(xpath):
    try:
        sleep(uniform(3.5,5))
        #WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,xpath)))
        driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:# or TimeoutException:
        return False
    return True



def signin2Google(account):
    try:
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Logging-in to Google account {account["email"]}:{account["password"]}')
        driver.get('https://accounts.google.com')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_SIGNIN_PAGE['emailInput']))).send_keys(account['email'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_SIGNIN_PAGE['nextButton']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_SIGNIN_PAGE['passwordInput']))).send_keys(account['password'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_SIGNIN_PAGE['loginButton']))).click()
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Successfuly signed in to Google account {account["email"]}:{account["password"]}')
        #sleep(2)
        return 0
    except:
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - ERROR! An exception occured when logging in to Google account. Retrying...')
        return signin2Google(account)



def launchAd(infos): # WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,))).click()
    try:
        sleep(uniform(10,15))
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Ad phase..')
        driver.get('https://ads.google.com/intl/en/home')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['startNow']))).click()
        sleep(uniform(8,10))
        # IMPORTANT: ADD CHECK CONDITION FOR MANAGER!!
        """
            >>> manager2 = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'//material-list/material-list-item[2]')))
            >>> manager2.text
            'Armando\nManager\n364-788-7744'
            >>> manager2.text.split('\n')
            ['Armando', 'Manager', '364-788-7744']
            >>> manager2.text.split('\n')[0]
            'Armando'
        """
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - chosing Manager {infos["managerName"].title()}')
        if(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','1')))).text.split('\n')[0].lower() == infos['managerName'].lower()):
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','1')))).click()
        elif(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','2')))).text.split('\n')[0].lower() == infos['managerName'].lower()):
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','2')))).click()
        elif(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','3')))).text.split('\n')[0].lower() == infos['managerName'].lower()):
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','3')))).click()
        #WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager']))).click()
        sleep(uniform(0.5,1.5))
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Launching new campaign')
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['newCampaign']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['pickManager']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['managerOne']))).click()
        sleep(uniform(0.5,1.5))
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Configuring ad...')
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['websiteTrafficCard']))).click()
        sleep(uniform(0.5,1.5))
        #WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['continue1']))).click()
        #sleep(uniform(2,4))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['searchCard']))).click()
        sleep(uniform(0.5,1.5))
        # !!check if website input exists or not
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['websiteInput']))).send_keys(infos['site'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['campaignName']))).clear()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['campaignName']))).send_key(f'{infos["managerName"]}{infos["site"]}{randint(1001,9999)}')
        sleep(uniform(1,2))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['continue1']))).click()
        sleep(uniform(0.5,1.5))
        #WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['continue1']))).click()
        # !!!There is a next button here, where you enter Bidding Clicks. Name is next0
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['next0']))).click()
        sleep(uniform(0.5,1.5))
        # check tuto if exist leave
        # some
        # code
        # here
        if(checkExistByXPATH(GOOGLE_ADS_PAGE['tuto']['close']['2'])): # checking for tuto
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['tuto']['close']['2']))).click()
            sleep(uniform(0.5,1.5))
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['tuto']['leave']['2']))).click()
            sleep(uniform(0.5,1.5))
        else:
            pass
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['includeGoogleDisplayNetworkCheckBox']))).click() # exclude Google Display Network
        sleep(uniform(0.5,1.5)) # enterOtherLocation
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['enterOtherLocation']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['locationInput']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['locationInput']))).send_keys(infos['country'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['targetButton']))).click() # target the country !!iframe
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['next1']))).click()
        sleep(uniform(0.5,1.5))
        # check tuto if exist leave
        # some
        # code
        # here
        if(checkExistByXPATH(GOOGLE_ADS_PAGE['tuto']['close']['2'])): # checking for tuto
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['tuto']['close']['2']))).click()
            sleep(uniform(0.5,1.5))
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['tuto']['leave']['2']))).click()
            sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['keywordsTextarea']))).clear()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['keywordsTextarea']))).send_keys(infos['keywords'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['paths']['1']))).send_keys(infos['paths']['1'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['paths']['2']))).send_keys(infos['paths']['2'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['headlines']['1']))).clear()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['headlines']['1']))).send_keys(infos['headlines']['1'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['headlines']['2']))).clear()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['headlines']['2']))).send_keys(infos['headlines']['2'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['headlines']['3']))).clear()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['headlines']['3']))).send_keys(infos['headlines']['3'])
        sleep(uniform(1,2))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['descriptions']['1']))).clear()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['descriptions']['1']))).send_keys(infos['descriptions']['1'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['descriptions']['2']))).clear()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['descriptions']['2']))).send_keys(infos['descriptions']['2'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['next2']))).click()
        sleep(uniform(0.5,1.5))
        #WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['next2']))).click()
        sleep(uniform(0.5,1.5))
        if(checkExistByXPATH(GOOGLE_ADS_PAGE['setCustomBudget'])): # checking for tuto
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['setCustomBudget']))).click()
            sleep(uniform(0.5,1.5))
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['budgetInput']))).click()
            sleep(uniform(0.5,1.5))
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['budgetInput']))).clear()
            sleep(uniform(0.5,1.5))
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['budgetInput']))).send_keys(infos['adBudget'])
        else:
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['budgetInput2']))).click()
            sleep(uniform(0.5,1.5))
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['budgetInput2']))).clear()
            sleep(uniform(0.5,1.5))
            WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['budgetInput2']))).send_keys(infos['adBudget'])
        sleep(uniform(1,2))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['next3']))).click()
        sleep(uniform(2,5))
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['publishCampaign']))).click()
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Done.')
    except:
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - ERROR! An exception occured when launching ad. Retrying...')
        sleep(5)
        launchAd(infos)









def main():
    signin2Google(_)
    launchAd(ad_infos)











if __name__ == '__main__':
    main()
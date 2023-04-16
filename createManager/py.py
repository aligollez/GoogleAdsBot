from modules import *







global _
with open('account.txt') as db:
    account = db.readlines()
    account = [info.strip() for info in account]
    _ = {
        'email':account[0],
        'password':account[1],
        'displayName':names.get_first_name()
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
pluginfile = 'proxy_auth_plugin.zip'
with zipfile.ZipFile(pluginfile,'w') as zp:
    zp.writestr('manifest.json',manifest_json)
    zp.writestr('background.js',background_js)
options.add_extension(pluginfile)

driver = uc.Chrome(
        options=options,
        #seleniumwire_options=seleniumwire_options
    )




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
        sleep(3)
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Successfuly signed in to Google account {account["email"]}:{account["password"]}')
        #sleep(2)
        return 0
    except:
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - ERROR! An exception occured when logging in to Google account. Retrying...')
        return signin2Google(account)




def createManagerAccount(account):
    sleep(uniform(10,15))
    try:
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Creating Google Ads Manager account {account["displayName"]}.')
        #driver.switch_to.new_window() # not necessary
        driver.get('https://ads.google.com/intl/en/home/tools/manager-accounts/')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['createMAButton']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['accountDisplayName']))).send_keys(account['displayName'])
        sleep(uniform(0.5,1.5))
        # configuring country, timezone and currency
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['countrySelect']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,DATABASES['countries'][country]['countryXPath']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['currencySelect']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,DATABASES['countries'][country]['currencyXPath']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['submitButton']))).click()
        #print('Submited')
        sleep(uniform(3,5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['exploreAccountButton']))).click()
        sleep(uniform(10,15))
        # !!!Setup
        # ADD LAST
        #
        #
        #sleep(uniform(5,10)) Accounts
        if(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['settingsButton']['1']))).text == 'arrow_right\nAccounts'):
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['settingsButton']['2']))).click()
        else:
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['settingsButton']['1']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['subAccountSettingsButton']))).click()
        sleep(uniform(2,5))
        #driver.execute_script(f'{GOOGLE_ADS_PAGE["+"]["jsElement"]}.click()')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['+']['fullXPath']))).click() # so far so good
        sleep(uniform(0.5,1.5))
        #driver.execute_script(f'{GOOGLE_ADS_PAGE["+NewManager"]["jsElement"]}.click()')
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Creating Account Manager.')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['+NewManager']['fullXPath']))).click() # this changes # FIXED.
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['+NewManager']['accountName']))).send_keys(account['displayName'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['+NewManager']['Save&Continue']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['+NewManager']['doneButton']))).click()
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Account Manager created.')
        sleep(uniform(2,5))
        #driver.execute_script(f'{GOOGLE_ADS_PAGE["+"]["jsElement"]}.click()')
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['+']['fullXPath']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['+CreateAccount']['fullXPath']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['+CreateAccount']['accountName']))).send_keys(account['displayName'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['+CreateAccount']['Save&Continue']))).click()
        sleep(uniform(10,15))
        #WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['tools&settings']))).click()
        driver.get('https://ads.google.com/aw/preferences')
        sleep(uniform(5,10))
        if(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','1')))).text.split('\n')[0].lower() == account['displayName'].lower()):
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','1')))).click()
        elif(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','2')))).text.split('\n')[0].lower() == account['displayName'].lower()):
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','2')))).click()
        elif(WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','3')))).text.split('\n')[0].lower() == account['displayName'].lower()):
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['choiceManager'].replace('position','3')))).click()
        else:
            pass
        #WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['setup']))).click()
        #sleep(uniform(0.5,1.5))
        #WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['preferences']))).click()
        #sleep(uniform(1.5,3))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['contactInformation']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['nameInput']))).send_keys(account['displayName'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['emailInput']))).send_keys(account['email'])
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['sameCheck']))).click()
        sleep(uniform(0.5,1.5))
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,GOOGLE_ADS_PAGE['saveButton']))).click()
        sleep(uniform(1,2))
        #while(True):
        #    sleep(1)
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - Done.')
        sleep(10)
        return 0
    except:
        log(f'[{str(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))}] - ERROR! An exception occured in creating Google AM. Retrying...')
        sleep(5)
        return createManagerAccount(account)











def main():
    signin2Google(_)
    createManagerAccount(_)
    









if __name__ == '__main__':
    main()
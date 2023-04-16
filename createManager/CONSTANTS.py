#/!/bin/python3.9.2



# ------------------------------ GENERAL VARIABLES ------------------------------#




#------------------------------ DB SECTION ------------------------------#
DATABASES = {
    'testAccount':{
        'email':'hamza@gmail.com',
        'password':'password'
    },
    'countries':{
        'Argentina':{
            'countryXPath':'//material-select-dropdown-item[10]',
            'currencyXPath':'//material-select-dropdown-item[1]'
            },
        'Australia':{
            'countryXPath':'//material-select-dropdown-item[13]',
            'currencyXPath':'//material-select-dropdown-item[2]'
        },
        'Belgium':{
            'countryXPath':'//material-select-dropdown-item[21]',
            'currencyXPath':'//material-select-dropdown-item[15]' # euro
        },
        'Canada':{
            'countryXPath':'//material-select-dropdown-item[37]',
            'currencyXPath':'//material-select-dropdown-item[7]'
        },
        'Switzerland':{
            'countryXPath':'//material-select-dropdown-item[210]',
            'currencyXPath':'//material-select-dropdown-item[41]'
        },
        'Germany':{
            'countryXPath':'//material-select-dropdown-item[81]',
            'currencyXPath':'//material-select-dropdown-item[15]' # euro
        },
        'Denmark':{
            'countryXPath':'//material-select-dropdown-item[58]',
            'currencyXPath':'//material-select-dropdown-item[13]'
        },
        'Spain':{
            'countryXPath':'//material-select-dropdown-item[202]',
            'currencyXPath':'//material-select-dropdown-item[15]' # euro
        },
        'Finland':{
            'countryXPath':'//material-select-dropdown-item[73]',
            'currencyXPath':'//material-select-dropdown-item[15]' # euro
        },
        'Israel':{
            'countryXPath':'//material-select-dropdown-item[103]',
            'currencyXPath':'//material-select-dropdown-item[20]'
        },
        'Netherlands':{
            'countryXPath':'//material-select-dropdown-item[149]',
            'currencyXPath':'//material-select-dropdown-item[15]' # euro
        },
        'Russia':{
            'countryXPath':'//material-select-dropdown-item[177]',
            'currencyXPath':'//material-select-dropdown-item[34]'
        },
        'Sweden':{
            'countryXPath':'//material-select-dropdown-item[209]',
            'currencyXPath':'//material-select-dropdown-item[40]'
        },
        'France':{
            'countryXPath':'//material-select-dropdown-item[74]',
            'currencyXPath':'//material-select-dropdown-item[15]' # euro
        },
        'Norway':{
            'countryXPath':'//material-select-dropdown-item[159]',
            'currencyXPath':'//material-select-dropdown-item[28]'
        }
    }
}




#------------------------------ PATH SECTION ------------------------------#





#------------------------------ XPATH SECTION ------------------------------#
GOOGLE_SIGNIN_PAGE = {
    'emailInput':'//*[@id="identifierId"]',
    'nextButton':'//*[@id="identifierNext"]/div/button',
    'passwordInput':'//*[@id="password"]/div[1]/div/div[1]/input',
    'loginButton':'//*[@id="passwordNext"]/div/button'
}

GOOGLE_ADS_PAGE = {
    'createMAButton':'//*[@id="jump-content"]/div[2]/section[1]/div/div/div[2]/div/a',
    'choiceManager':'//material-list/material-list-item[position]',
    'accountDisplayName':'//signup-subapp-root//input', # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div/cm-editing-root/deferred-component/signup-subapp-root/base-root/div/div[2]/div[1]/view-loader/manager-view/div/material-input/div[1]/div[1]/label/input
    'countrySelect':'//country-select/material-dropdown-select/dropdown-button', # 
    #'timezoneSelect':'//time-zone-select/material-dropdown-select/dropdown-button', #
    'currencySelect':'//currency-select/material-dropdown-select/dropdown-button',
    'submitButton':'//signup-subapp-root//material-button', # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div/cm-editing-root/deferred-component/signup-subapp-root/base-root/div/div[2]/div[1]/view-loader/manager-view/div/div[6]/material-button
    'exploreAccountButton':'//signup-subapp-root//material-button', # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div/cm-editing-root/deferred-component/signup-subapp-root/base-root/div/div[2]/div[1]/view-loader/congrats-view/div/div[1]/div[1]/material-button
    'tools&settings':'//deferred-app-menus//div[2]/material-button', # 
    'setup':'//material-expansionpanel[2]',
    'preferences':'//app-menu-item[6]//material-list-item',
    'contactInformation':'//data-protection-contacts-editor//material-expansionpanel',
    'nameInput':'//div[1]/data-protection-contact-detail/div/div/div[1]//input',
    'emailInput':'//div[1]/data-protection-contact-detail/div/div/div[2]//input',
    'sameCheck':'//material-checkbox',
    'saveButton':'//root//material-yes-no-buttons/material-button[2]',
    'backButton':'//awsm-app-bar/div/div[2]/material-button',
    'settingsButton':{
        '1':'//div[3]/awsm-skinny-nav-item/a',
        '2':'//div[4]//a'
    }, # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-skinny-nav/nav/div[1]/div[3]/awsm-skinny-nav-item/a # /html/body/div[2]/root/div/div[1]/div/div/div[3]/div/div/awsm-skinny-nav/nav/div[1]/div[4]/awsm-skinny-nav-item/a # //div[4]//a only if insights exist Accounts
    'subAccountSettingsButton':'//awsm-skinny-nav-item[3]/a', # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-skinny-nav/nav/div[1]/div[3]/awsm-skinny-nav-item/div/awsm-skinny-nav-item[3]/a
    '+':{
            'fullXPath':'//material-fab', # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div[3]/customersettings-root/base-root/div/div[2]/div[1]/view-loader/all-account-settings-view/tableview/div[4]/div/section/toolbelt/toolbelt-bar[1]/div[1]/div[1]/element/fab/material-fab-menu/material-fab
            'jsElement':'document.querySelector("#aB920AE78-9B6F-4858-A599-577EC8A955FD--0 > div.content._ngcontent-whi-36 > material-icon > i")' # ignore
        },
    '+NewManager':{
        'fullXPath':'//material-select-item[1]',# /html/body/div[7]/div[8]/div/div/div[2]/div[2]/div/div/focus-trap/div[2]/menu-item-groups/div/material-select-item[1]
        'jsElement':'document.querySelector("#a7C06EB5F-F1DE-4351-B596-B8C6F20F1B50--0 > material-icon > i")', # ignore
        'accountName':'//material-expansionpanel[1]//input', # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div[4]/mcc-root/base-root/div/div[2]/div[1]/view-loader/new-submanager-account-view/mcc-create-account-stepper/div/ess-stepper/material-stepper/div[2]/div/step-loader/submanager-account-creation-step/div/div[1]/material-expansionpanel[1]/div/div[2]/div/div[1]/div/div/span[2]/account-name-input/material-input/div[1]/div[1]/label/input
        'Save&Continue':'//view-loader//material-button[1]', # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div[4]/mcc-root/base-root/div/div[2]/div[1]/view-loader/new-submanager-account-view/mcc-create-account-stepper/div/ess-stepper/material-stepper/div[2]/div/step-loader/submanager-account-creation-step/div/div[2]/material-yes-no-buttons/material-button[1]
        'doneButton':'//view-loader//material-yes-no-buttons/material-button[1]' # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div[4]/mcc-root/base-root/div/div[2]/div[1]/view-loader/new-submanager-account-view/mcc-create-account-stepper/div/ess-stepper/material-stepper/div[2]/div/step-loader/link-accounts-step/div/div[3]/material-yes-no-buttons/material-button[1]
    },
    '+CreateAccount':{
        'fullXPath':'//material-select-item[1]', # /html/body/div[7]/div[8]/div/div/div[2]/div[2]/div/div/focus-trap/div[2]/menu-item-groups/div/material-select-item[1]
        'accountName':'//account-name-input/material-input//input', # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div[4]/mcc-root/base-root/div/div[2]/div[1]/view-loader/new-account-view/mcc-create-account-stepper/div/ess-stepper/material-stepper/div[2]/div/step-loader/account-creation-step/div/div[1]/material-expansionpanel[1]/div/div[2]/div/div[1]/div/div/span[2]/account-name-input/material-input/div[1]/div[1]/label/input
        'Save&Continue':'//view-loader//material-button[1]' # /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div[4]/mcc-root/base-root/div/div[2]/div[1]/view-loader/new-account-view/mcc-create-account-stepper/div/ess-stepper/material-stepper/div[2]/div/step-loader/account-creation-step/div/div[2]/material-yes-no-buttons/material-button[1]
    }
}



#------------------------------ COMMENT SECTION ------------------------------#

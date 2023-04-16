#/!/bin/python3.9.2



# ------------------------------ GENERAL VARIABLES ------------------------------#




#------------------------------ DB SECTION ------------------------------#
DATABASES = {
    'testAccount':{
        'email':'hamza@gmail.com',
        'password':'password'
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
    'startNow':'//*[@id="jump-content"]/div[2]/section[1]/div/div/div[2]/div/a',
    'choiceManager':'//material-list/material-list-item[position]',
    'newCampaign':'//material-extended-fab-menu/button',
    'pickManager':'//customer-picker',
    'managerOne':'//customer-picker-cell[1]',
    'tuto':{
        'close':{
            '1':'/html/body/div[4]/div[12]/material-dialog/focus-trap/div[2]/div/div[2]/focus-trap/div[2]/div[1]/div/div[2]/material-button',
            '2':'//focus-trap//focus-trap//div[1]//material-button'
        },
        'leave':{
            '1':'/html/body/div[4]/div[11]/material-dialog/focus-trap/div[2]/div/div[2]/div[3]/material-button[1]',
            # //*[@id="default-acx-overlay-container"]/div[11]/material-dialog/focus-trap/div[2]/div/div[2]/div[3]/material-button[1] # leave button
            # //*[@id="default-acx-overlay-container"]/div[11]//material-button[1] # leave button
            '2':'//div[11]//material-button[1]'
        }
    },
    'websiteTrafficCard':'//dynamic-component[3]/marketing-objective-card-v2/selection-card', # /html/body/div[2]/root/div/div[1]/div/div/div[3]/div/div[2]/awsm-child-content/div/div[2]/cm-editing-root/deferred-component/construction-root/base-root/div/div[2]/div[1]/view-loader/campaign-construction-selection/guided-selection-engine/div/marketing-objective-selection-view-v4/div/div[2]/fieldset/selection-view/div/dynamic-component[3]/marketing-objective-card-v2/selection-card
    'searchCard':'//dynamic-component[1]/channel-selection-card-v2/selection-card',
    'websiteInput':'//detail-text-input//input', # /html/body/div[2]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div/cm-editing-root/deferred-component/construction-root/base-root/div/div[2]/div[1]/view-loader/campaign-construction-selection/guided-selection-engine/div/tactics-selection/div/div/fieldset/div/div/div/detail-url-input/div/detail-text-input/material-input/div[1]/div[1]/label/input # IMPORTANT: most times it doesn't even show
    'campaignName':'//campaign-name-view//input',
    'continue1':'//continue-cancel-selection-view/material-yes-no-buttons/material-button[1]', # /html/body/div[2]/root/div/div[1]/div/div/div[3]/div/div[2]/awsm-child-content/div/div[2]/cm-editing-root/deferred-component/construction-root/base-root/div/div[2]/div[1]/view-loader/campaign-construction-selection/guided-selection-engine/div/continue-cancel-selection-view/material-yes-no-buttons/material-button[1]
    'next0':'//div[1]/dynamic-component//material-button',
    'next1':'//div[1]/div[1]/div[2]//div/div/material-button', # /html/body/div[2]/root/div/div[1]/div/div/div[3]/div/div[2]/awsm-child-content/div/div[2]/cm-editing-root/deferred-component/construction-root/reconstruction-base-root/view-loader/search-campaign-flow-root/base-campaign-flow-root/left-stepper/div[1]/div[1]/div[2]/dynamic-component/layout-driven-view/construction-layout/div/div/div/material-button
    'includeGoogleDisplayNetworkCheckBox':'//network-editor/div/div[2]//material-checkbox',
    'enterOtherLocation':'//div[3]/material-radio',
    'locationInput':'//location-with-options//input',
    'targetButton':'//material-list/div[1]//div[1]/location-data-suggestion-entry//div[1]/material-button', # /html/body/div[6]/div[20]/div/div/div[2]/div[2]/material-list/div[1]/div/div[1]/location-data-suggestion-entry/div/div/div[1]/material-button
    'languageInput':'//language-picker//input',
    'keywordsTextarea':'//standard-ad-group-editor/material-expansionpanel[1]//textarea',
    'paths':{
        '1':'//span[2]/rsa-text-input[1]//input',
        '2':'//span[2]/rsa-text-input[2]//input'
    },
    'headlines':{
        '1':'//div[1]/rsa-text-input/material-input//input',
        '2':'//div[2]/rsa-text-input/material-input//input',
        '3':'//div[3]/rsa-text-input/material-input//input'
    },
    'descriptions':{
        '1':'//div[1]/rsa-text-input//textarea',
        '2':'//div[2]/rsa-text-input//textarea'
    },
    'next2':'//div[2]//div/div[3]/div/material-button',
    'setCustomBudget':'//material-expansionpanel-set/material-expansionpanel[4]//material-radio',
    'budgetInput':'//material-expansionpanel[4]//input', # ORR /html/body/div[1]/root/div/div[1]/div/div/div[3]/div/div/awsm-child-content/div/div[2]/cm-editing-root/deferred-component/construction-root/reconstruction-base-root/view-loader/search-campaign-flow-root/base-campaign-flow-root/left-stepper/div[1]/div[1]/div[4]/dynamic-component/layout-driven-view/construction-layout/div/construction-layout-engine/div/div/div[3]/div/lazy-plugin/div/dynamic-component/budget/material-expansionpanel/div/div[2]/div/div[1]/div/div/div/div/div[1]/budget-editor-wrapper/budget-base-edit/div[2]/material-input/div/div[1]/label/input
    # //budget-base-edit//input
    'budgetInput2':'//budget-base-edit//input',
    'next3':'//div[2]//div[4]//material-button',
    'publishCampaign':'//search-review/div/div/div[1]//material-button'
}





#------------------------------ COMMENT SECTION ------------------------------#

ad_infos = {
    'managerName':'', # manager which will run ads...
    'country':'', # country you want to target, example: "USA" or "UK". the bot will always choose the first option
    'site':'',
    'keywords':'', # keywords like this : "keyword1,keyword2,keyword3....
    'paths':{ # site.com / path 1 / path 2
        '1':'',
        '2':''
    },
    'headlines':{
        '1':'', # headline 1
        '2':'', # headline 2
        '3':'' # headline 3
    },
    'descriptions':{
        '1':'', # description 1
        '2':'' # description 2
    },
    'adBudget':'' # budget
}
proxy = {
    'location':'Unknown', # change it if you want
        'type':{
            'http':'http', # leave it
            'https':'https' # leave it
        },
        'host':'', # enter either host or IP, host example: iproyal.com.., IP example: 58.128.96.1
        'port':'', # enter port, port example: 8080
        'user':'', # enter user
        'pass':'', # enter pass
}



manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """
background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (proxy['host'],proxy['port'],proxy['user'],proxy['pass'])
# -*- coding: utf-8 -*-

from selenium import webdriver 
from time import sleep 

options = webdriver.ChromeOptions()

options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\\hiranokentaro\\Documents\\Python\\amazon_voucheres"
})
options.add_argument('--kiosk-printing')

browser = webdriver.Chrome(options=options)
# browser = webdriver.Chrome()


url = "https://www.amazon.co.jp/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fgp%2Fhelp%2Fcustomer%2Fdisplay.html%3FnodeId%3DG985MC479RA4YQRL%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
browser.get(url)

elem_username = browser.find_element_by_id('ap_email') 
elem_username.send_keys("yakyukentaro@icloud.com")
# sleep(1)

elem_next_btn = browser.find_element_by_class_name('a-button-input')
elem_next_btn.click()
# sleep(2)

elem_password = browser.find_element_by_id('ap_password') 
elem_password.send_keys("Kiraritown2024")
elem_login_btn = browser.find_element_by_class_name('a-button-input')
elem_login_btn.click()

sleep(2)
elem_order_histroy = browser.find_element_by_id('nav-orders')
elem_order_histroy.click()

element_order_filter = browser.find_element_by_id('orderFilter')
element_entry_year = element_order_filter.find_element_by_id('orderFilterEntry-year-2020')
element_entry_year.click()


element_voucheres = browser.find_elements_by_class_name('hide-if-no-js')

while True:
    for num in range(len(element_voucheres)):
        print(num)
        # print(len(element_voucheres))
        element_voucheres = browser.find_elements_by_class_name('hide-if-no-js')
        # print(element_voucheres)
        element_voucheres[num].click()
        sleep(4)
        element_get_ul = browser.find_element_by_class_name('a-nowrap') # 領収書リンク内のul取得
        element_get_li = element_get_ul.find_elements_by_tag_name('li') # ulの中のliすべて取得
        element_get_li[-1].click() # liの中の領収書リンク押下
        browser.execute_script('window.print();') # 自動でPDF保存
        browser.back() # 前のページに戻る
        if num == len(element_voucheres) -1:
            # print("最後の要素です")
            element_nxt_btn = browser.find_element_by_class_name('a-last')
            if len(element_nxt_btn.find_elements_by_tag_name('a')) == 0:
                print("nextボタンはありません")   
                print("終了しました")
                break
    else:
        element_nxt_btn.click()
        continue
    break

browser.quit()
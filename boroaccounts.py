import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
from reader import Reader


driver = webdriver.Chrome()

def boro_fnl_form(size, firstname, lastname, middleinitial, zipcode, gender, num_entries):
    driver.get('https://accounts.boroinc.com/products/fnl')
    try:
        shoe_size = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/form/div[2]/div[1]/select')
        shoe_size.send_keys(size)
        time.sleep(.25)
    except:
        print('Size Box Not Found Retrying')
        print('Waiting Two Seconds')
        shoe_size = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/form/div[2]/div[1]/select')
        shoe_size.send_keys(size)
    try:
        first_name = driver.find_element_by_name('properties[firstname]')
        first_name.send_keys(firstname)
        time.sleep(.25)
    except:
        print('First Name Box Not Found Retrying')
        print('Waiting Two Seconds')
        time.sleep(2)
        first_name = driver.find_element_by_name('properties[firstname]')
        first_name.send_keys(firstname)
    try:
        last_name = driver.find_element_by_name('properties[lastname]')
        last_name.send_keys(lastname)
        time.sleep(.25)
    except:
        print('Last Name Box Not Found Retrying')
        print('Waiting Two Seconds')
        time.sleep(2)
        last_name = driver.find_element_by_name('properties[lastname]')
        last_name.send_keys(lastname)
    try:
        full_name = driver.find_element_by_name('properties[middle]')
        full_name.send_keys(middleinitial)
        time.sleep(.25)
    except:
        print('Name Box Not Found Retrying')
        print('Waiting Two Seconds')
        time.sleep(2)
        full_name = driver.find_element_by_name('properties[middle]')
        full_name.send_keys(middleinitial)
    try:
        zip_code = driver.find_element_by_name('properties[Zipcode]')
        zip_code.send_keys(zipcode)
        time.sleep(.25)
    except:
        print('Zip Not Found Retrying')
        print('Waiting Two Seconds')
        time.sleep(2)
        zip_code = driver.find_element_by_name('properties[Zipcode]')
        zip_code.send_keys(zipcode)
    try:
        gender_form = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/form/div[2]/div[3]/select')
        gender_form.send_keys(gender)
        time.sleep(.25)
    except:
        print('Gender Box Not Found Retrying')
        print('Waiting Two Seconds')
        time.sleep(2)
        gender_form = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/form/div[2]/div[3]/select')
        gender_form.send_keys(gender)
    try:
        agreement1 = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/li[1]/label')
        agreement1.click()
        time.sleep(.25)
    except:
        print('Agreement 1 Not Found Retrying')
        print('Waiting Two Seconds')
        time.sleep(2)
        agreement1 = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/li[1]/label')
        agreement1.click()
    else:
        print('Skipped Agreement')
    try:
        agreement2 = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/li[2]/label')
        agreement2.click()
        time.sleep(.25)
    except:
        print('Agreement 2 Not Found Retrying')
        print('Waiting Two Seconds')
        time.sleep(2)
        agreement2 = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/li[2]/label')
        agreement2.click()
    else:
        print('Skipped Agreement')
    try:
        number_entry = driver.find_element_by_name('quantity')
        number_entry.send_keys('\ue017' + num_entries)
        time.sleep(.25)
    except:
        print('Entries Not Found Retrying')
        print('Waiting Two Seconds')
        time.sleep(2)
        number_entry = driver.find_element_by_name('quantity')
        number_entry.send_keys('\ue017' + num_entries)

    try:
        time.sleep(.5)
        add_to_cart = driver.find_element_by_name('add')
        add_to_cart.click()
        time.sleep(.5)
    except:
        time.sleep(.5)
        add_to_cart = driver.find_element_by_name('add')
        add_to_cart.click()
        time.sleep(.5)
     

with open ("input.txt", newline = '') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        boro_fnl_form(row[0],row[1],row[2],row[3],row[4],row[5],row[6])


def checkout(email, first, last, address1, city, state, zipcode):
    driver.get('https://accounts.boroinc.com/cart')
    time.sleep(.5)
    driver.find_element_by_name('checkout').click()
    time.sleep(1)
    try:
        driver.find_element_by_name('checkout[email]').send_keys(email)
    except:
        print('email error')
        time.sleep(.5)
        driver.find_element_by_name('checkout[email]').send_keys(email)
    try:
        driver.find_element_by_name('checkout[billing_address][first_name]').send_keys(first)
    except:
        print('email error')
        time.sleep(.5)
        driver.find_element_by_name('checkout[billing_address][first_name]').send_keys(first)
    try:
        driver.find_element_by_name('checkout[billing_address][last_name]').send_keys(last)
    except:
        print('email error')
        time.sleep(.5)
        driver.find_element_by_name('checkout[billing_address][last_name]').send_keys(last) 
    try:
        driver.find_element_by_name('checkout[billing_address][address1]').send_keys(address1)
    except:
        print('email error')
        time.sleep(.5)
        driver.find_element_by_name('checkout[billing_address][address1]').send_keys(address1) 
    try:
        driver.find_element_by_name('checkout[billing_address][city]').send_keys(city)
    except:
        print('email error')
        time.sleep(.5)
        driver.find_element_by_name('checkout[billing_address][city]').send_keys(city)
    try:
        driver.find_element_by_name('checkout[billing_address][province]').send_keys(state)
    except:
        print('email error')
        time.sleep(.5)
        driver.find_element_by_name('checkout[billing_address][province]').send_keys(state)
    try:
        driver.find_element_by_name('checkout[billing_address][zip]').send_keys(zipcode)
    except:
        print('email error')
        time.sleep(.5)
        driver.find_element_by_name('checkout[billing_address][zip]').send_keys(zipcode)
    try:
        driver.find_element_by_name('checkout[reduction_code]').send_keys('VIPONLY30')
        time.sleep(.5)
        driver.find_element_by_xpath('/html/body/div/div/aside/div[2]/div[1]/div/div[2]/form[2]/div/div/div/button').click()
        time.sleep(3)
    except:
        print('code Error')
        time.sleep(.5)
        driver.find_element_by_name('checkout[reduction_code]').send_keys('VIPONLY30')
        time.sleep(.5)
        driver.find_element_by_xpath('/html/body/div/div/aside/div[2]/div[1]/div/div[2]/form[2]/div/div/div/button').click()
        time.sleep(3)
    try:
        driver.find_element_by_name('button').click()
    except:
        print('email error')
        time.sleep(.5)
        driver.find_element_by_name('button').click()
        
checkout('camden.fritz123@gmail.com', 'Camden', 'fritz', '30 Manchester Rd', 'Amherst', 'New Hampshire', '03031') #edit this line of code to fit your own billing
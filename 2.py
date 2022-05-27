# 动态页面的爬虫 selenium phantomJs FireFox

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()  # 将火狐地址写在系统path中
driver.get("https://weibo.com/")

searchWhat=driver.find_element(By.ID,"kw") # 搜索框的元素id
searchWhat.clear() # 清空输入框
searchWhat.send_keys("python") # 通过send_keys方法把'python'传递给serchWhat元素，即id叫做'kw'的元素

searchBtn=driver.find_element(By.CLASS_NAME,"s_btn") # 通过类名找到按钮
searchBtn.click() # 点击
#
# xpath
#
# find_element_by_xpath("//*[@id='search']")
#
# find_element(By.XPATH, "//*[@id='search']")
#
# class_name
#
# find_element_by_class_name("element_class_name")
#
# find_element(By.CLASS_NAME, "element_class_name")
#
# id
#
# find_element_by_id("element_id")
#
# find_element(By.ID,"element_id")
#
# name
#
# find_element_by_name("element_name")
#
# find_element(By.NAME, "element_name")
#
# link_text
#
# find_element_by_link_text("element_link_text")
#
# find_element(By.LINK_TEXT,"element_link_text")
#
# css_selector
#
# find_element_by_css_selector("element_css_selector")
#
# find_element(By.CSS_SELECTOR, "element_css_selector")
#
# tag_name
#
# find_element_by_tag_name("element_tag_name")
#
# find_element(By.TAG_NAME, "element_tag_name")
#
# partial_link_text
#
# ind_element_by_partial_link_text("element_partial_link_text")
#
# find_element(By.PARTIAL_LINK_TEXT, "element_partial_link_text")


# 有些需要滚动才能加载的
# js="document.documentElement.scrollTop=10000" #拖动滚动条到屏幕底端
#
# driver.execute_script(js)

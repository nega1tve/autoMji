from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)

    login_input = driver.find_element(By.ID, 'userid')
    login_input.clear()
    login_input.send_keys(login)
    time.sleep(1)
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)
    time.sleep(2)
    driver.find_element(By.NAME, 'submit').click()
    driver.implicitly_wait(12)
    frame_0 = driver.find_element(By.NAME, 'formCanvas')
    driver.switch_to.frame(frame_0)

    # INPUT

    ti1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')

    ti2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[3]/td[3]/textarea').get_attribute(
        'value')

    ti3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[4]/td[3]/textarea').get_attribute(
        'value')

    ti4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[5]/td[3]/textarea').get_attribute(
        'value')
    ti5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[6]/td[3]/textarea').get_attribute(
        'value')

    ti6 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]/textarea').get_attribute(
        'value')

    ti11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')

    ti21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[3]/td[4]/input').get_attribute(
        'value')

    ti31 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[4]/td[4]/input').get_attribute(
        'value')

    ti41 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[5]/td[4]/input').get_attribute(
        'value')
    ti51 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[6]/td[4]/input').get_attribute(
        'value')

    ti61 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[7]/td[4]/input').get_attribute(
        'value')

    ti12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')

    ti22 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[3]/td[5]/input').get_attribute(
        'value')

    ti32 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[4]/td[5]/input').get_attribute(
        'value')

    ti42 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[5]/td[5]/input').get_attribute(
        'value')
    ti52 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[6]/td[5]/input').get_attribute(
        'value')

    ti62 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[7]/td[5]/input').get_attribute(
        'value')

    ti13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    ti23 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[3]/td[6]/input').get_attribute(
        'value')

    ti33 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[4]/td[6]/input').get_attribute(
        'value')

    ti43 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[5]/td[6]/input').get_attribute(
        'value')
    ti53 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[6]/td[6]/input').get_attribute(
        'value')

    ti63 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[7]/td[6]/input').get_attribute(
        'value')

    # to1 = driver.find_element(By.XPATH,
    #                            '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
    #     'value')
    # to11 = driver.find_element(By.XPATH,
    #                            '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
    #     'value')
    # to12 = driver.find_element(By.XPATH,
    #                            '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
    #     'value')
    # to13 = driver.find_element(By.XPATH,
    #                            '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
    #     'value')

    # водоотвод

    tp1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    tp11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    tp12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    tp13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Герметизация

    ta1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[6]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    ta11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[6]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    ta12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[6]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    ta13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[6]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Фасад
    td1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[8]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    td11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[8]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    td12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[8]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    td13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[8]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Балконы
    tf1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')

    tf2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[3]/td[3]/textarea').get_attribute(
        'value')

    tf3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[4]/td[3]/textarea').get_attribute(
        'value')

    tf4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[5]/td[3]/textarea').get_attribute(
        'value')
    tf5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[6]/td[3]/textarea').get_attribute(
        'value')

    tf11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')

    tf21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[3]/td[4]/input').get_attribute(
        'value')

    tf31 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[4]/td[4]/input').get_attribute(
        'value')

    tf41 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[5]/td[4]/input').get_attribute(
        'value')
    tf51 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[6]/td[4]/input').get_attribute(
        'value')


    tf12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')

    tf22 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[3]/td[5]/input').get_attribute(
        'value')

    tf32 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[4]/td[5]/input').get_attribute(
        'value')

    tf42 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[5]/td[5]/input').get_attribute(
        'value')
    tf52 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[6]/td[5]/input').get_attribute(
        'value')

    tf13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    tf23 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[3]/td[6]/input').get_attribute(
        'value')

    tf33 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[4]/td[6]/input').get_attribute(
        'value')

    tf43 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[5]/td[6]/input').get_attribute(
        'value')
    tf53 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[6]/td[6]/input').get_attribute(
        'value')

    # Стены
    tg1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[16]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    tg11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[16]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    tg12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[16]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    tg13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[16]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Подвал
    th1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[20]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    th11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[20]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    th12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[20]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    th13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[20]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Тех.подполье
    tj1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[22]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    tj11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[22]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    tj12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[22]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    tj13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[22]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Тех.этаж
    tk1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[24]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    tk11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[24]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    tk12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[24]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    tk13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[24]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Гараж стоянка (подземный)
    tl1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[26]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    tl11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[26]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    tl12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[26]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    tl13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[26]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Места
    # общего
    # пользования

    tz1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')

    tz2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[3]/td[3]/textarea').get_attribute(
        'value')

    tz3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[4]/td[3]/textarea').get_attribute(
        'value')

    tz4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[5]/td[3]/textarea').get_attribute(
        'value')
    tz5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[6]/td[3]/textarea').get_attribute(
        'value')
    tz6 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[7]/td[3]/textarea').get_attribute(
        'value')
    tz7 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[8]/td[3]/textarea').get_attribute(
        'value')
    tz8 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[9]/td[3]/textarea').get_attribute(
        'value')

    tz101 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')

    tz211 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[3]/td[4]/input').get_attribute(
        'value')

    tz311 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[4]/td[4]/input').get_attribute(
        'value')

    tz411 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[5]/td[4]/input').get_attribute(
        'value')
    tz511 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[6]/td[4]/input').get_attribute(
        'value')
    tz611 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[7]/td[4]/input').get_attribute(
        'value')
    tz711 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[8]/td[4]/input').get_attribute(
        'value')
    tz811 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[9]/td[4]/input').get_attribute(
        'value')

    tz12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')

    tz22 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[3]/td[5]/input').get_attribute(
        'value')

    tz32 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[4]/td[5]/input').get_attribute(
        'value')

    tz42 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[5]/td[5]/input').get_attribute(
        'value')
    tz52 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[6]/td[5]/input').get_attribute(
        'value')
    tz62 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[7]/td[5]/input').get_attribute(
        'value')
    tz72 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[8]/td[5]/input').get_attribute(
        'value')
    tz82 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[9]/td[5]/input').get_attribute(
        'value')

    tz13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    tz23 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[3]/td[6]/input').get_attribute(
        'value')

    tz33 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[4]/td[6]/input').get_attribute(
        'value')

    tz43 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[5]/td[6]/input').get_attribute(
        'value')
    tz53 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[6]/td[6]/input').get_attribute(
        'value')
    tz63 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[7]/td[6]/input').get_attribute(
        'value')
    tz73 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[8]/td[6]/input').get_attribute(
        'value')
    tz83 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[9]/td[6]/input').get_attribute(
        'value')

    # Лестницы
    tx1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[30]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    tx11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[30]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    tx12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[30]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    tx13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[30]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Перекрытия
    tc1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[32]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    tc11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[32]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    tc12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[32]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    tc13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[32]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Система отопления
    tv1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')

    tv2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[3]/td[3]/textarea').get_attribute(
        'value')

    tv3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[4]/td[3]/textarea').get_attribute(
        'value')

    tv4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[5]/td[3]/textarea').get_attribute(
        'value')
    tv5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[6]/td[3]/textarea').get_attribute(
        'value')
    tv12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')

    tv22 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[3]/td[4]/input').get_attribute(
        'value')

    tv32 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[4]/td[4]/input').get_attribute(
        'value')

    tv42 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[5]/td[4]/input').get_attribute(
        'value')
    tv52 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[6]/td[4]/input').get_attribute(
        'value')
    tv121 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')

    tv221 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[3]/td[5]/input').get_attribute(
        'value')

    tv321 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[4]/td[5]/input').get_attribute(
        'value')

    tv421 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[5]/td[5]/input').get_attribute(
        'value')
    tv521 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[6]/td[5]/input').get_attribute(
        'value')

    tv13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    tv23 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[3]/td[6]/input').get_attribute(
        'value')

    tv33 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[4]/td[6]/input').get_attribute(
        'value')

    tv43 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[5]/td[6]/input').get_attribute(
        'value')
    tv53 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[6]/td[6]/input').get_attribute(
        'value')

    # ГВС
    tb1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')

    tb2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[3]/td[3]/textarea').get_attribute(
        'value')

    tb3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[4]/td[3]/textarea').get_attribute(
        'value')

    tb4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[5]/td[3]/textarea').get_attribute(
        'value')
    tb5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[6]/td[3]/textarea').get_attribute(
        'value')
    tb11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')

    tb21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[3]/td[4]/input').get_attribute(
        'value')

    tb31 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[4]/td[4]/input').get_attribute(
        'value')

    tb41 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[5]/td[4]/input').get_attribute(
        'value')
    tb51 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[6]/td[4]/input').get_attribute(
        'value')
    tb12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')

    tb22 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[3]/td[5]/input').get_attribute(
        'value')

    tb32 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[4]/td[5]/input').get_attribute(
        'value')

    tb42 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[5]/td[5]/input').get_attribute(
        'value')
    tb52 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[6]/td[5]/input').get_attribute(
        'value')

    tb13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    tb23 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[3]/td[6]/input').get_attribute(
        'value')

    tb33 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[4]/td[6]/input').get_attribute(
        'value')

    tb43 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[5]/td[6]/input').get_attribute(
        'value')
    tb53 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[6]/td[6]/input').get_attribute(
        'value')

    # ХВС
    tn1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')

    tn2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[3]/td[3]/textarea').get_attribute(
        'value')

    tn3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[4]/td[3]/textarea').get_attribute(
        'value')

    tn4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[5]/td[3]/textarea').get_attribute(
        'value')
    tn5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[6]/td[3]/textarea').get_attribute(
        'value')

    tn11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')

    tn21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[3]/td[4]/input').get_attribute(
        'value')

    tn31 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[4]/td[4]/input').get_attribute(
        'value')

    tn41 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[5]/td[4]/input').get_attribute(
        'value')
    tn51 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[6]/td[4]/input').get_attribute(
        'value')

    tn12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')

    tn22 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[3]/td[5]/input').get_attribute(
        'value')

    tn32 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[4]/td[5]/input').get_attribute(
        'value')

    tn42 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[5]/td[5]/input').get_attribute(
        'value')
    tn52 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[6]/td[5]/input').get_attribute(
        'value')

    tn13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    tn23 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[3]/td[6]/input').get_attribute(
        'value')

    tn33 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[4]/td[6]/input').get_attribute(
        'value')

    tn43 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[5]/td[6]/input').get_attribute(
        'value')
    tn53 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[6]/td[6]/input').get_attribute(
        'value')

    # Канализация
    tm1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')

    tm2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[3]/td[3]/textarea').get_attribute(
        'value')

    tm3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[4]/td[3]/textarea').get_attribute(
        'value')

    tm11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')

    tm21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[3]/td[4]/input').get_attribute(
        'value')

    tm31 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[4]/td[4]/input').get_attribute(
        'value')

    tm12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')

    tm22 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[3]/td[5]/input').get_attribute(
        'value')

    tm32 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[4]/td[5]/input').get_attribute(
        'value')
    tm13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    tm23 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[3]/td[6]/input').get_attribute(
        'value')

    tm33 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[4]/td[6]/input').get_attribute(
        'value')

    # Мусоропроводы
    y1 = driver.find_element(By.XPATH,
                             '/html/body/form[1]/div/fieldset[3]/div[42]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    y11 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[42]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    y12 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[42]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    y13 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[42]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Система промывки и прочистки стволов мусоропроводов
    yu1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[44]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yu11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[44]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yu12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[44]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yu13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[44]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Вентиляц.
    yi1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[46]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yi11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[46]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yi12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[46]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yi13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[46]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Газоходы
    yo1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[48]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yo11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[48]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yo12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[48]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yo13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[48]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Лифты
    yp1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[50]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yp11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[50]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yp12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[50]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yp13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[50]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Подъёмное устройство для маломобильной группы населения
    ya1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[52]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    ya11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[52]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    ya12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[52]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    ya13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[52]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Устройство для автоматического опускания лифта
    ys1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[54]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    ys11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[54]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    ys12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[54]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    ys13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[54]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Система ЭС (ВРУ)
    yd1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[56]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yd11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[56]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yd12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[56]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yd13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[56]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # ВКВ (второй кабельный ввод)
    yf1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[58]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yf11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[58]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yf12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[58]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yf13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[58]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # АВР (автоматическое включение резервного питания)
    yg1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[60]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yg11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[60]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yg12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[60]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yg13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[60]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # ППАиДУ
    yh1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[62]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yh11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[62]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yh12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[62]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yh13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[62]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Система оповещения о пожаре
    yj1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[64]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yj11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[64]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yj12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[64]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yj13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[64]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # ГС
    yk1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[66]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yk11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[66]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yk12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[66]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yk13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[66]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Связь с ОДС
    yl1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[68]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yl11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[68]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yl12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[68]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yl13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[68]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # Система видеонаблюдения
    yz1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[70]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yz11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[70]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yz12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[70]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yz13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[70]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # ОЗДС(охранно-защитная дератизационная система)
    yx1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[3]/div[72]/div[2]/table/tbody/tr[2]/td[3]/textarea').get_attribute(
        'value')
    yx11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[72]/div[2]/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')
    yx12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[72]/div[2]/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')
    yx13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[3]/div[72]/div[2]/table/tbody/tr[2]/td[6]/input').get_attribute(
        'value')

    # ROOF

    # 2
    roof2 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[2]/td['
                                '3]/textarea').get_attribute(
        'value')
    roof21 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[2]/td['
                                 '5]/input').get_attribute(
        'value')
    # CheboxRoof = driver.find_element(By.XPATH, '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[
    # 3]/div/div/table/tbody/tr[2]/td[6]/span/table/tbody/tr/td/div[2]/ul/li[15]').get_attribute('value')

    # 3
    roof3 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[3]/td['
                                '3]/textarea').get_attribute(
        'value')
    roof31 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[3]/td['
                                 '5]/input').get_attribute(
        'value')
    # cheboxOverhangs = driver.find_element(By.XPATH,
    #                                  '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[2]/td[6]/span/table/tbody/tr/td/div[2]/ul/li[15]').get_attribute(
    #     'value')

    # 4
    roof4 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[4]/td['
                                '3]/textarea').get_attribute(
        'value')
    roof41 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[4]/td['
                                 '5]/input').get_attribute(
        'value')

    # 5
    roof5 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[5]/td['
                                '3]/textarea').get_attribute(
        'value')
    roof51 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[5]/td['
                                 '5]/input').get_attribute(
        'value')

    # 6
    roof6 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[6]/td['
                                '3]/textarea').get_attribute(
        'value')
    roof61 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[6]/td['
                                 '5]/input').get_attribute(
        'value')

    # 7
    roof7 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[7]/td['
                                '3]/textarea').get_attribute(
        'value')
    roof71 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[7]/td['
                                 '5]/input').get_attribute(
        'value')

    # DRAINAGE
    # 2
    drainage2 = driver.find_element(By.XPATH,
                                    '/html/body/form[1]/div/fieldset[4]/fieldset[2]/div[3]/div/div/table/tbody/tr['
                                    '2]/td[3]/textarea').get_attribute(
        'value')
    drainage21 = driver.find_element(By.XPATH,
                                     '/html/body/form[1]/div/fieldset[4]/fieldset[2]/div[3]/div/div/table/tbody/tr['
                                     '2]/td[5]/input').get_attribute(
        'value')

    # Inter-panel joints
    # 2
    interPanel2 = driver.find_element(By.XPATH,
                                      '/html/body/form[1]/div/fieldset[4]/fieldset[3]/div[3]/div/div/table/tbody/tr['
                                      '2]/td[3]/textarea').get_attribute(
        'value')
    interPanel21 = driver.find_element(By.XPATH,
                                       '/html/body/form[1]/div/fieldset[4]/fieldset[3]/div[3]/div/div/table/tbody/tr['
                                       '2]/td[5]/input').get_attribute(
        'value')

    # Front
    # 2
    front2 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[4]/div[3]/div/div/table/tbody/tr[2]/td['
                                 '3]/textarea').get_attribute(
        'value')
    front21 = driver.find_element(By.XPATH,
                                  '/html/body/form[1]/div/fieldset[4]/fieldset[4]/div[3]/div/div/table/tbody/tr['
                                  '2]/td[5]/input').get_attribute(
        'value')

    # Balconies
    # 2
    balc2 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr[2]/td['
                                '3]/textarea').get_attribute(
        'value')
    balc21 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr[2]/td['
                                 '5]/input').get_attribute(
        'value')
    # 3
    balc3 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr[3]/td['
                                '3]/textarea').get_attribute(
        'value')
    balc31 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr[3]/td['
                                 '5]/input').get_attribute(
        'value')
    # 4
    balc4 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr[4]/td['
                                '3]/textarea').get_attribute(
        'value')
    balc41 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr[4]/td['
                                 '5]/input').get_attribute(
        'value')

    # 5
    balc5 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr[5]/td['
                                '3]/textarea').get_attribute(
        'value')
    balc51 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr[5]/td['
                                 '5]/input').get_attribute(
        'value')

    # 6
    balc6 = driver.find_element(By.XPATH,
                                '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr[6]/td['
                                '3]/textarea').get_attribute(
        'value')
    balc61 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[6]/td['
                                 '5]/input').get_attribute(
        'value')

    # Walls

    # 2
    walls2 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[6]/div[3]/div/div/table/tbody/tr[2]/td['
                                 '3]/textarea').get_attribute(
        'value')
    walls21 = driver.find_element(By.XPATH,
                                  '/html/body/form[1]/div/fieldset[4]/fieldset[6]/div[3]/div/div/table/tbody/tr['
                                  '2]/td[5]/input').get_attribute(
        'value')

    # Basement
    # 2
    basement2 = driver.find_element(By.XPATH,
                                    '/html/body/form[1]/div/fieldset[4]/fieldset[7]/div[3]/div/div/table/tbody/tr['
                                    '2]/td[3]/textarea').get_attribute(
        'value')
    basement21 = driver.find_element(By.XPATH,
                                     '/html/body/form[1]/div/fieldset[4]/fieldset[7]/div[3]/div/div/table/tbody/tr['
                                     '2]/td[5]/input').get_attribute(
        'value')

    # Technical field

    # 2
    techField2 = driver.find_element(By.XPATH,
                                     '/html/body/form[1]/div/fieldset[4]/fieldset[8]/div[3]/div/div/table/'
                                     'tbody/tr['
                                     '2]/td[3]/textarea').get_attribute(
        'value')
    techField21 = driver.find_element(By.XPATH,
                                      '/html/body/form[1]/div/fieldset[4]/fieldset[9]/div[3]/div/div/table/'
                                      'tbody/tr['
                                      '2]/td[5]/input').get_attribute(
        'value')

    # Tech.floor

    # 2
    techFloor2 = driver.find_element(By.XPATH,
                                     '/html/body/form[1]/div/fieldset[4]/fieldset[9]/div[3]'
                                     '/div/div/table/'
                                     'tbody/tr['
                                     '2]/td[3]/textarea').get_attribute(
        'value')
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[9]/'
                        'div[3]/div/div/table/'
                        'tbody/tr['
                        '2]/td[5]/input').get_attribute(
        'value')

    # Parking garage

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[10]/div[3]/div/div/table/'
                        'tbody/'
                        'tr[2]/td[3]/textarea').get_attribute(
        'value')
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[10]/div[3]/div/div/table/'
                        'tbody/'
                        'tr[2]/td[5]/input').get_attribute(
        'value')

    # Common areas

    # 2
    areas2 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                 '/div[3]/div/div/table/tbody/tr[2]/td['
                                 '3]/textarea').get_attribute(
        'value')
    areas21 = driver.find_element(By.XPATH,
                                  '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                  '/div[3]/div/div/table/tbody/tr[2]/td['
                                  '5]/input').get_attribute(
        'value')

    # 3
    areas3 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                 '/div[3]/div/div/table/tbody/tr[3]/td['
                                 '3]/textarea').get_attribute(
        'value')
    areas31 = driver.find_element(By.XPATH,
                                  '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                  '/div[3]/div/div/table/tbody/tr[3]/td['
                                  '5]/input').get_attribute(
        'value')

    # 4
    areas4 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                 '/div[3]/div/div/table/tbody/tr[4]/td['
                                 '3]/textarea').get_attribute(
        'value')
    areas41 = driver.find_element(By.XPATH,
                                  '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                  '/div[3]/div/div/table/tbody/tr[4]/td['
                                  '5]/input').get_attribute(
        'value')

    # 5
    areas5 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                 '/div[3]/div/div/table/tbody/tr[5]/td['
                                 '3]/textarea').get_attribute(
        'value')
    areas51 = driver.find_element(By.XPATH,
                                  '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                  '/div[3]/div/div/table/tbody/tr[5]/td['
                                  '5]/input').get_attribute(
        'value')

    # 6
    areas6 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                 '/div[3]/div/div/table/tbody/tr[6]/td['
                                 '3]/textarea').get_attribute(
        'value')
    areas61 = driver.find_element(By.XPATH,
                                  '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                  '/div[3]/div/div/table/tbody/tr[6]/td['
                                  '5]/input').get_attribute(
        'value')

    # 7
    areas7 = driver.find_element(By.XPATH,
                                 '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                 '/div[3]/div/div/table/tbody/tr[7]/td['
                                 '3]/textarea').get_attribute(
        'value')
    areas71 = driver.find_element(By.XPATH,
                                  '/html/body/form[1]/div/fieldset[4]/fieldset[11]'
                                  '/div[3]/div/div/table/tbody/tr[7]/td['
                                  '5]/input').get_attribute(
        'value')

    # Stairs

    # 2
    stairs2 = driver.find_element(By.XPATH,
                                  '/html/body/form[1]/div/fieldset[4]/fieldset[12]'
                                  '/div[3]/div/div/table/tbody/tr[2]/td['
                                  '3]/textarea').get_attribute(
        'value')

    stairs21 = driver.find_element(By.XPATH,
                                   '/html/body/form[1]/div/fieldset[4]/fieldset[12]'
                                   '/div[3]/div/div/table/tbody/tr[2]/td['
                                   '5]/input').get_attribute(
        'value')

    # Overlaps

    # 2
    overlaps2 = driver.find_element(By.XPATH,
                                    '/html/body/form[1]/div/fieldset[4]/fieldset[13]'
                                    '/div[3]/div/div/table/tbody/tr[2]/td['
                                    '3]/textarea').get_attribute(
        'value')

    overlaps21 = driver.find_element(By.XPATH,
                                     '/html/body/form[1]/div/fieldset[4]/fieldset[13]'
                                     '/div[3]/div/div/table/tbody/tr[2]/td['
                                     '5]/input').get_attribute(
        'value')

    # Heating system

    # 2
    hs2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                              '/div[3]/div/div/table/tbody/tr[2]/td['
                              '3]/textarea').get_attribute(
        'value')
    hs21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                               '/div[3]/div/div/table/tbody/tr[2]/td['
                               '5]/input').get_attribute(
        'value')

    # 3
    hs3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                              '/div[3]/div/div/table/tbody/tr[3]/td['
                              '3]/textarea').get_attribute(
        'value')
    hs31 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                               '/div[3]/div/div/table/tbody/tr[3]/td['
                               '5]/input').get_attribute(
        'value')

    # 4
    hs4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                              '/div[3]/div/div/table/tbody/tr[4]/td['
                              '3]/textarea').get_attribute(
        'value')
    hs41 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                               '/div[3]/div/div/table/tbody/tr[4]/td['
                               '5]/input').get_attribute(
        'value')

    # 5
    hs5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                              '/div[3]/div/div/table/tbody/tr[5]/td['
                              '3]/textarea').get_attribute(
        'value')
    hs51 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                               '/div[3]/div/div/table/tbody/tr[5]/td['
                               '5]/input').get_attribute(
        'value')

    # 6
    hs6 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                              '/div[3]/div/div/table/tbody/tr[6]/td['
                              '3]/textarea').get_attribute(
        'value')
    hs61 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[14]'
                               '/div[3]/div/div/table/tbody/tr[6]/td['
                               '5]/input').get_attribute(
        'value')

    # Hot water supply

    # 2
    hw2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                              '/div[3]/div/div/table/tbody/tr[2]/td['
                              '3]/textarea').get_attribute(
        'value')
    hw21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                               '/div[3]/div/div/table/tbody/tr[2]/td['
                               '5]/input').get_attribute(
        'value')

    # 3
    hw3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                              '/div[3]/div/div/table/tbody/tr[3]/td['
                              '3]/textarea').get_attribute(
        'value')
    hw31 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                               '/div[3]/div/div/table/tbody/tr[3]/td['
                               '5]/input').get_attribute(
        'value')

    # 4
    hw4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                              '/div[3]/div/div/table/tbody/tr[4]/td['
                              '3]/textarea').get_attribute(
        'value')
    hw41 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                               '/div[3]/div/div/table/tbody/tr[4]/td['
                               '5]/input').get_attribute(
        'value')

    # 5
    hw5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                              '/div[3]/div/div/table/tbody/tr[5]/td['
                              '3]/textarea').get_attribute(
        'value')
    hw51 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                               '/div[3]/div/div/table/tbody/tr[5]/td['
                               '5]/input').get_attribute(
        'value')

    # 6
    hw6 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                              '/div[3]/div/div/table/tbody/tr[6]/td['
                              '3]/textarea').get_attribute(
        'value')
    hw61 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[15]'
                               '/div[3]/div/div/table/tbody/tr[6]/td['
                               '5]/input').get_attribute(
        'value')

    # Cold water supply

    # 2
    cw2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                              '/div[3]/div/div/table/tbody/tr[2]/td['
                              '3]/textarea').get_attribute(
        'value')
    cw21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[5]/input').get_attribute(
        'value')

    # 3
    cw3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                              '/div[3]/div/div/table/tbody/tr[3]/td['
                              '3]/textarea').get_attribute(
        'value')
    cw31 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                               '/div[3]/div/div/table/tbody/tr[3]/td['
                               '5]/input').get_attribute(
        'value')

    # 4
    cw4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                              '/div[3]/div/div/table/tbody/tr[4]/td['
                              '3]/textarea').get_attribute(
        'value')
    cw41 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                               '/div[3]/div/div/table/tbody/tr[4]/td['
                               '5]/input').get_attribute(
        'value')

    # 5
    cw5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                              '/div[3]/div/div/table/tbody/tr[5]/td['
                              '3]/textarea').get_attribute(
        'value')
    cw51 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                               '/div[3]/div/div/table/tbody/tr[5]/td['
                               '5]/input').get_attribute(
        'value')

    # 6
    cw6 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                              '/div[3]/div/div/table/tbody/tr[6]/td['
                              '3]/textarea').get_attribute(
        'value')
    cw61 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[16]'
                               '/div[3]/div/div/table/tbody/tr[6]/td['
                               '5]/input').get_attribute(
        'value')

    # Sewage system

    # 2
    ss2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[17]'
                              '/div[3]/div/div/table/tbody/tr[2]/td['
                              '3]/textarea').get_attribute(
        'value')
    ss21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[17]'
                               '/div[3]/div/div/table/tbody/tr[2]/td['
                               '5]/input').get_attribute(
        'value')

    # 3
    ss3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[17]'
                              '/div[3]/div/div/table/tbody/tr[3]/td['
                              '3]/textarea').get_attribute(
        'value')
    ss31 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[17]'
                               '/div[3]/div/div/table/tbody/tr[3]/td['
                               '5]/input').get_attribute(
        'value')

    # 4
    ss4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[17]'
                              '/div[3]/div/div/table/tbody/tr[4]/td['
                              '3]/textarea').get_attribute(
        'value')
    ss41 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[17]'
                               '/div[3]/div/div/table/tbody/tr[4]/td['
                               '5]/input').get_attribute(
        'value')

    # Waste chutes

    # 2
    wc2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[18]'
                              '/div[3]/div/div/table/tbody/tr[2]/td['
                              '3]/textarea').get_attribute(
        'value')
    wc21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[18]'
                               '/div[3]/div/div/table/tbody/tr[2]/td['
                               '5]/input').get_attribute(
        'value')

    np1 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[19]/'
                              'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np2 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[19]/'
                              'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np3 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[20]'
                              '/div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np4 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[20]'
                              '/div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np5 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[21]/'
                              'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np6 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[21]/'
                              'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np7 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[22]'
                              '/div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np8 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[22]'
                              '/div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np9 = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/fieldset[4]/fieldset[23]/'
                              'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np10 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[23]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np11 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[24]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np12 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[24]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np13 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[25]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np14 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[25]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np15 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[26]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np16 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[26]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np17 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[27]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np18 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[27]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np19 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[28]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np20 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[28]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np21 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[29]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np22 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[29]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np23 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[30]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np24 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[30]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np25 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[31]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np26 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[31]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np27 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[32]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np28 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[32]'
                               '/div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    np29 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[33]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').get_attribute(
        'value')

    np30 = driver.find_element(By.XPATH,
                               '/html/body/form[1]/div/fieldset[4]/fieldset[33]/'
                               'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').get_attribute(
        'value')

    dd = driver.find_element(By.XPATH,
                             '/html/body/form[1]/div/fieldset[4]/div[35]'
                             '/table/tbody/tr[1]/td[2]/div/div[2]/textarea').get_attribute(
        'value')

    re = driver.find_element(By.XPATH,
                             '/html/body/form[1]/div/fieldset[5]/fieldset/div[2]'
                             '/table/tbody/tr/td/div/div[2]/textarea').get_attribute(
        'value')

    di = driver.find_element(By.XPATH,
                             '/html/body/form[1]/div/div[12]/div[2]'
                             '/table/tbody/tr[2]/td[4]/input').get_attribute(
        'value')

    rur = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/div[12]/div[2]'
                              '/table/tbody/tr[3]/td[4]/input').get_attribute(
        'value')

    isr = driver.find_element(By.XPATH,
                              '/html/body/form[1]/div/div[12]/div[2]'
                              '/table/tbody/tr[4]/td[4]/input').get_attribute(
        'value')


    time.sleep(5)
    # driver.get(output_link)
    driver.get(
        newUrl)
    frame_0 = driver.find_element(By.NAME, 'formCanvas')
    driver.switch_to.frame(frame_0)
    time.sleep(5)

    # OUTPUT

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        ti1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[3]/td[3]/textarea').send_keys(
        ti2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[4]/td[3]/textarea').send_keys(
        ti3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[5]/td[3]/textarea').send_keys(
        ti4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[6]/td[3]/textarea').send_keys(
        ti5)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]/textarea').send_keys(
        ti6)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        ti11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[3]/td[4]/input').send_keys(
        ti21)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[4]/td[4]/input').send_keys(
        ti31)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[5]/td[4]/input').send_keys(
        ti41)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[6]/td[4]/input').send_keys(
        ti51)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[7]/td[4]/input').send_keys(
        ti61)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        ti12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[3]/td[5]/input').send_keys(
        ti22)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[4]/td[5]/input').send_keys(
        ti32)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[5]/td[5]/input').send_keys(
        ti42)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[6]/td[5]/input').send_keys(
        ti52)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[7]/td[5]/input').send_keys(
        ti62)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        ti13)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[3]/td[6]/input').send_keys(
        ti23)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[4]/td[6]/input').send_keys(
        ti33)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[5]/td[6]/input').send_keys(
        ti43)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[6]/td[6]/input').send_keys(
        ti53)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[2]/div[2]/table/tbody/tr[7]/td[6]/input').send_keys(
        ti63)

    # driver.find_element(By.XPATH,
    #                     '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
    #     to1)
    # driver.find_element(By.XPATH,
    #                     '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
    #     to11)
    # driver.find_element(By.XPATH,
    #                     '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
    #     to12)
    # driver.find_element(By.XPATH,
    #                     '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
    #     to13)

    # # водоотвод
    #

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tp1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tp11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tp12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[4]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tp13)

    # Герметизация

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[6]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        ta1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[6]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        ta11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[6]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        ta12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[6]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        ta13)

    # Фасад

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[8]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        td1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[8]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        td11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[8]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        td12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[8]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        td13)

    # #Балконы

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tf1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[3]/td[3]/textarea').send_keys(
        tf2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[4]/td[3]/textarea').send_keys(
        tf3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[5]/td[3]/textarea').send_keys(
        tf4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[6]/td[3]/textarea').send_keys(
        tf5)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tf11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[3]/td[4]/input').send_keys(
        tf21)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[4]/td[4]/input').send_keys(
        tf31)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[5]/td[4]/input').send_keys(
        tf41)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[6]/td[4]/input').send_keys(
        tf51)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tf12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[3]/td[5]/input').send_keys(
        tf22)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[4]/td[5]/input').send_keys(
        tf32)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[5]/td[5]/input').send_keys(
        tf42)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[6]/td[5]/input').send_keys(
        tf52)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tf13)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[3]/td[6]/input').send_keys(
        tf23)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[4]/td[6]/input').send_keys(
        tf33)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[5]/td[6]/input').send_keys(
        tf43)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[6]/td[6]/input').send_keys(
        tf53)

    # driver.find_element(By.XPATH,
    #                     '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
    #     tf13)
    # driver.find_element(By.XPATH,
    #                     '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[3]/td[6]/input').send_keys(
    #     tf23)
    #
    # driver.find_element(By.XPATH,
    #                     '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[4]/td[6]/input').send_keys(
    #     tf33)
    # driver.find_element(By.XPATH,
    #                     '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[5]/td[6]/input').send_keys(
    #     tf43)
    # driver.find_element(By.XPATH,
    #                     '/html/body/form[1]/div/fieldset[3]/div[12]/div[2]/table/tbody/tr[6]/td[6]/input').send_keys(
    #     tf53)

    # Стены

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[16]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tg1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[16]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tg11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[16]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tg12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[16]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tg13)

    # Подвал

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[20]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        th1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[20]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        th11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[20]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        th12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[20]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        th13)

    #   # Тех.подполье

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[22]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tj1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[22]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tj11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[22]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tj12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[22]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tj13)

    # Тех.этаж
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[24]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tk1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[24]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tk11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[24]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tk12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[24]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tk13)

    # Гараж стоянка (подземный)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[26]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tl1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[26]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tl11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[26]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tl12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[26]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tl13)

    # Места
    # общего
    # пользования

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tz1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[3]/td[3]/textarea').send_keys(
        tz2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[4]/td[3]/textarea').send_keys(
        tz3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[5]/td[3]/textarea').send_keys(
        tz4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[6]/td[3]/textarea').send_keys(
        tz5)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[7]/td[3]/textarea').send_keys(
        tz6)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[8]/td[3]/textarea').send_keys(
        tz7)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[9]/td[3]/textarea').send_keys(
        tz8)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tz101)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[3]/td[4]/input').send_keys(
        tz211)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[4]/td[4]/input').send_keys(
        tz311)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[5]/td[4]/input').send_keys(
        tz411)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[6]/td[4]/input').send_keys(
        tz511)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[7]/td[4]/input').send_keys(
        tz611)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[8]/td[4]/input').send_keys(
        tz711)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[9]/td[4]/input').send_keys(
        tz811)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tz12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[3]/td[5]/input').send_keys(
        tz22)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[4]/td[5]/input').send_keys(
        tz32)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[5]/td[5]/input').send_keys(
        tz42)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[6]/td[5]/input').send_keys(
        tz52)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[7]/td[5]/input').send_keys(
        tz62)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[8]/td[5]/input').send_keys(
        tz72)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[9]/td[5]/input').send_keys(
        tz82)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tz13)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[3]/td[6]/input').send_keys(
        tz23)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[4]/td[6]/input').send_keys(
        tz33)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[5]/td[6]/input').send_keys(
        tz43)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[6]/td[6]/input').send_keys(
        tz53)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[7]/td[6]/input').send_keys(
        tz63)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[8]/td[6]/input').send_keys(
        tz73)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[28]/div[2]/table/tbody/tr[9]/td[6]/input').send_keys(
        tz83)

    # Лестницы

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[30]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tx1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[30]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tx11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[30]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tx12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[30]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tx13)

    # Перекрытия
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[32]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tc1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[32]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tc11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[32]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tc12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[32]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tc13)

    # Система отопления

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tv1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[3]/td[3]/textarea').send_keys(
        tv2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[4]/td[3]/textarea').send_keys(
        tv3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[5]/td[3]/textarea').send_keys(
        tv4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[6]/td[3]/textarea').send_keys(
        tv5)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tv12)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[3]/td[4]/input').send_keys(
        tv22)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[4]/td[4]/input').send_keys(
        tv32)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[5]/td[4]/input').send_keys(
        tv42)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[6]/td[4]/input').send_keys(
        tv52)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tv121)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[3]/td[5]/input').send_keys(
        tv221)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[4]/td[5]/input').send_keys(
        tv321)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[5]/td[5]/input').send_keys(
        tv421)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[6]/td[5]/input').send_keys(
        tv521)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tv13)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[3]/td[6]/input').send_keys(
        tv23)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[4]/td[6]/input').send_keys(
        tv33)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[5]/td[6]/input').send_keys(
        tv43)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[34]/div[2]/table/tbody/tr[6]/td[6]/input').send_keys(
        tv53)

    # ГВС
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tb1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[3]/td[3]/textarea').send_keys(
        tb2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[4]/td[3]/textarea').send_keys(
        tb3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[5]/td[3]/textarea').send_keys(
        tb4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[6]/td[3]/textarea').send_keys(
        tb5)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tb11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[3]/td[4]/input').send_keys(
        tb21)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[4]/td[4]/input').send_keys(
        tb31)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[5]/td[4]/input').send_keys(
        tb41)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[6]/td[4]/input').send_keys(
        tb51)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tb12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[3]/td[5]/input').send_keys(
        tb22)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[4]/td[5]/input').send_keys(
        tb32)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[5]/td[5]/input').send_keys(
        tb42)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[6]/td[5]/input').send_keys(
        tb52)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tb13)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[3]/td[6]/input').send_keys(
        tb23)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[4]/td[6]/input').send_keys(
        tb33)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[5]/td[6]/input').send_keys(
        tb43)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[36]/div[2]/table/tbody/tr[6]/td[6]/input').send_keys(
        tb53)

    # ХВС
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tn1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[3]/td[3]/textarea').send_keys(
        tn2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[4]/td[3]/textarea').send_keys(
        tn3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[5]/td[3]/textarea').send_keys(
        tn4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[6]/td[3]/textarea').send_keys(
        tn5)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tn11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[3]/td[4]/input').send_keys(
        tn21)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[4]/td[4]/input').send_keys(
        tn31)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[5]/td[4]/input').send_keys(
        tn41)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[6]/td[4]/input').send_keys(
        tn51)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tn12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[3]/td[5]/input').send_keys(
        tn22)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[4]/td[5]/input').send_keys(
        tn32)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[5]/td[5]/input').send_keys(
        tn42)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[6]/td[5]/input').send_keys(
        tn52)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tn13)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[3]/td[6]/input').send_keys(
        tn23)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[4]/td[6]/input').send_keys(
        tn33)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[5]/td[6]/input').send_keys(
        tn43)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[38]/div[2]/table/tbody/tr[6]/td[6]/input').send_keys(
        tn53)

    # Канализация

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        tm1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[3]/td[3]/textarea').send_keys(
        tm2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[4]/td[3]/textarea').send_keys(
        tm3)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        tm11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[3]/td[4]/input').send_keys(
        tm21)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[4]/td[4]/input').send_keys(
        tm31)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        tm12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[3]/td[5]/input').send_keys(
        tm22)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[4]/td[5]/input').send_keys(
        tm32)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        tm13)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[3]/td[6]/input').send_keys(
        tm23)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[40]/div[2]/table/tbody/tr[4]/td[6]/input').send_keys(
        tm33)

    # Мусоропроводы

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[42]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        y1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[42]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        y11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[42]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        y12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[42]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        y13)

    # Система промывки и прочистки стволов мусоропроводов

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[44]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yu1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[44]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yu11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[44]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yu12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[44]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yu13)

    # Вентиляц.

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[46]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yi1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[46]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yi11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[46]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yi12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[46]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yi13)

    #     #Газоходы
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[48]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yo1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[48]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yo11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[48]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yo12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[48]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yo13)

    # Лифты
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[50]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yp1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[50]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yp11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[50]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yp12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[50]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yp13)

    # Подъёмное устройство для маломобильной группы населения

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[52]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        ya1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[52]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        ya11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[52]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        ya12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[52]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        ya13)

    # Устройство для автоматического опускания лифта
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[54]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        ys1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[54]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        ys11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[54]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        ys12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[54]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        ys13)

    # Система ЭС (ВРУ)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[56]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yd1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[56]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yd11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[56]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yd12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[56]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yd13)

    # ВКВ (второй кабельный ввод)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[58]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yf1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[58]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yf11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[58]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yf12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[58]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yf13)

    # АВР (автоматическое включение резервного питания)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[60]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yg1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[60]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yg11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[60]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yg12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[60]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yg13)

    # ППАиДУ
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[62]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yh1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[62]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yh11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[62]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yh12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[62]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yh13)

    # Система оповещения о пожаре
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[64]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yj1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[64]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yj11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[64]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yj12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[64]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yj13)

    # ГС
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[66]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yk1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[66]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yk11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[66]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yk12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[66]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yk13)

    # Связь с ОДС
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[68]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yl1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[68]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yl11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[68]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yl12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[68]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yl13)

    # Система видеонаблюдения
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[70]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yz1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[70]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yz11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[70]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yz12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[70]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yz13)

    # ОЗДС(охранно-защитная дератизационная система)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[72]/div[2]/table/tbody/tr[2]/td[3]/textarea').send_keys(
        yx1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[72]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys(
        yx11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[72]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys(
        yx12)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[3]/div[72]/div[2]/table/tbody/tr[2]/td[6]/input').send_keys(
        yx13)

    # ROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOFROOF

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        roof2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/'
                        'tr[2]/td[5]/input').send_keys(
        roof21)
    # RoofClickClick = driver.find_element(By.XPATH, '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[
    # 3]/div/div/table/tbody/tr[2]/td[6]/span/table/tbody/tr/td/div[1]/a').click() RoofClick = driver.find_element(
    # By.XPATH, '/html/body/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/a').click() CheboxRoofOut =
    # driver.find_element(By.XPATH, '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/tr[
    # 2]/td[6]/span/table/tbody/tr/td/div[2]/ul/li[15]').click()

    # 3
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div['
                        '3]/div/div/table/tbody/tr[3]/td[3]/textarea').send_keys(
        roof3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div['
                        '3]/div/div/table/tbody/tr[3]/td[5]/input').send_keys(
        roof31)

    # 4
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[3]/textarea').send_keys(
        roof4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[5]/input').send_keys(
        roof41)

    # 5
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/div/div/table/tbody/'
                        'tr[5]/td[3]/textarea').send_keys(
        roof5)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]/'
                        'div/div/table/tbody/'
                        'tr[5]/td[5]/input').send_keys(
        roof51)

    # 6
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div[3]'
                        '/div/div/table/tbody/tr[6]/td[3]/textarea').send_keys(
        roof6)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div['
                        '3]/div/div/table/tbody/tr[6]/td[5]/input').send_keys(
        roof61)

    # 7
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/'
                        'div[3]/div/div/table/tbody/tr[7]/td[3]/textarea').send_keys(
        roof7)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[1]/div['
                        '3]/div/div/table/tbody/tr[7]/td[5]/input').send_keys(
        roof71)

    # OUT DRAINAGE

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[2]/div[3]'
                        '/div/div/table/tbody/tr[2]/td[3]/textarea').send_keys(
        drainage2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[2]/div['
                        '3]/div/div/table/tbody/tr[2]/td[5]/input').send_keys(
        drainage21)

    # Inter-panel joints

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[3]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        interPanel2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[3]/div['
                        '3]/div/div/table/tbody/tr[2]/td[5]/input').send_keys(
        interPanel21)

    # Front

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[4]/div[3]/'
                        'div/div/table/tbody/tr[2]/td[3]/textarea').send_keys(
        front2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[4]/div[3]/'
                        'div/div/table/tbody/tr[2]/td[5]/input').send_keys(
        front21)

    # Balconies out

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/'
                        'div/div/table/tbody/tr[2]/td[3]/textarea').send_keys(
        balc2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/'
                        'div/div/table/tbody/tr[2]/td[5]/input').send_keys(
        balc21)

    # 3
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/'
                        'div/div/table/tbody/tr[3]/td[3]/textarea').send_keys(
        balc3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div['
                        '3]/div/div/table/tbody/tr[3]/td[5]/input').send_keys(
        balc31)

    # 4
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/div/div/table/tbody/tr['
                        '4]/td[3]/textarea').send_keys(
        balc4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div['
                        '3]/div/div/table/tbody/tr[4]/td[5]/input').send_keys(
        balc41)

    # 5
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/'
                        'div/div/table/tbody/tr[5]/td[3]/textarea').send_keys(
        balc5)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div['
                        '3]/div/div/table/tbody/tr[5]/td[5]/input').send_keys(
        balc51)

    # 6
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div[3]/'
                        'div/div/table/tbody/tr[6]/td[3]/textarea').send_keys(
        balc6)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[5]/div['
                        '3]/div/div/table/tbody/tr[6]/td[5]/input').send_keys(
        balc61)

    # Walls

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[6]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        walls2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[6]/div['
                        '3]/div/div/table/tbody/tr[2]/td[5]/input').send_keys(
        walls21)

    # Basement

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[7]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        basement2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[7]/div['
                        '3]/div/div/table/tbody/tr[2]/td[5]/input').send_keys(
        basement21)

    # Technical field

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[8]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        techField2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[8]/div[3]/'
                        'div/div/table/tbody/tr[2]/td[5]/input').send_keys(
        techField21)

    # Tech.floor

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[9]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        techFloor2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[9]/div['
                        '3]/div/div/table/tbody/tr[2]/td[5]/input').send_keys(
        techFloor2)

    # Parking garage

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[10]/div['
                        '3]/div/div/table/tbody/tr[2]/td[3]/textarea').send_keys(
        techFloor2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[10]/div['
                        '3]/div/div/table/tbody/tr[2]/td[5]/input').send_keys(
        techFloor2)

    # Common areas

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        areas2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div[3]/div/div/table/tbody/'
                        'tr[2]/td[5]/input').send_keys(
        areas21)

    # 3
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div['
                        '3]/div/div/table/tbody/tr[3]/td[3]/textarea').send_keys(
        areas3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div['
                        '3]/div/div/table/tbody/tr[3]/td[5]/input').send_keys(
        areas31)

    # 4
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[3]/textarea').send_keys(
        areas4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[5]/input').send_keys(
        areas41)

    # 5
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div[3]/div/div/table/tbody/'
                        'tr[5]/td[3]/textarea').send_keys(
        areas5)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div[3]/'
                        'div/div/table/tbody/'
                        'tr[5]/td[5]/input').send_keys(
        areas51)

    # 6
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div[3]'
                        '/div/div/table/tbody/tr[6]/td[3]/textarea').send_keys(
        areas6)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div['
                        '3]/div/div/table/tbody/tr[6]/td[5]/input').send_keys(
        areas61)

    # 7
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/'
                        'div[3]/div/div/table/tbody/tr[7]/td[3]/textarea').send_keys(
        areas7)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[11]/div['
                        '3]/div/div/table/tbody/tr[7]/td[5]/input').send_keys(
        areas71)

    # Stairs
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[12]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        stairs2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[12]/div[3]/div/div/table/tbody/'
                        'tr[2]/td[5]/input').send_keys(
        stairs21)

    # Overlaps
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[13]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        overlaps2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[13]/div[3]/div/div/table/tbody/'
                        'tr[2]/td[5]/input').send_keys(
        overlaps21)

    # Heating system 6

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        hs2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div[3]/div/div/table/tbody/'
                        'tr[2]/td[5]/input').send_keys(
        hs21)

    # 3
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div['
                        '3]/div/div/table/tbody/tr[3]/td[3]/textarea').send_keys(
        hs3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div['
                        '3]/div/div/table/tbody/tr[3]/td[5]/input').send_keys(
        hs31)

    # 4
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[3]/textarea').send_keys(
        hs4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[5]/input').send_keys(
        hs41)

    # 5
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div[3]/div/div/table/tbody/'
                        'tr[5]/td[3]/textarea').send_keys(
        hs5)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div[3]/'
                        'div/div/table/tbody/'
                        'tr[5]/td[5]/input').send_keys(
        hs51)

    # 6
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div[3]'
                        '/div/div/table/tbody/tr[6]/td[3]/textarea').send_keys(
        hs6)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[14]/div['
                        '3]/div/div/table/tbody/tr[6]/td[5]/input').send_keys(
        hs61)

    # Hot water supply

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        hw2)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div[3]/div/div/table/tbody/'
                        'tr[2]/td[5]/input').send_keys(
        hw21)

    # 3
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div['
                        '3]/div/div/table/tbody/tr[3]/td[3]/textarea').send_keys(
        hw3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div['
                        '3]/div/div/table/tbody/tr[3]/td[5]/input').send_keys(
        hw31)

    # 4
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[3]/textarea').send_keys(
        hw4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[5]/input').send_keys(
        hw41)

    # 5
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div[3]/div/div/table/tbody/'
                        'tr[5]/td[3]/textarea').send_keys(
        hw5)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div[3]/'
                        'div/div/table/tbody/'
                        'tr[5]/td[5]/input').send_keys(
        hw51)

    # 6
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div[3]'
                        '/div/div/table/tbody/tr[6]/td[3]/textarea').send_keys(
        hw6)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[15]/div['
                        '3]/div/div/table/tbody/tr[6]/td[5]/input').send_keys(
        hw61)

    # Cold water supply 6

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        cw2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div[3]/div/div/table/tbody/'
                        'tr[2]/td[5]/input').send_keys(
        cw21)

    # 3
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div['
                        '3]/div/div/table/tbody/tr[3]/td[3]/textarea').send_keys(
        cw3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div['
                        '3]/div/div/table/tbody/tr[3]/td[5]/input').send_keys(
        cw31)

    # 4
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[3]/textarea').send_keys(
        cw4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[5]/input').send_keys(
        cw41)

    # 5
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div[3]/div/div/table/tbody/'
                        'tr[5]/td[3]/textarea').send_keys(
        cw5)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div[3]/'
                        'div/div/table/tbody/'
                        'tr[5]/td[5]/input').send_keys(
        cw51)

    # 6
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div[3]'
                        '/div/div/table/tbody/tr[6]/td[3]/textarea').send_keys(
        cw6)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[16]/div['
                        '3]/div/div/table/tbody/tr[6]/td[5]/input').send_keys(
        cw61)

    # Sewage system

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[17]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        ss2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[17]/div[3]/div/div/table/tbody/'
                        'tr[2]/td[5]/input').send_keys(
        ss21)

    # 3
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[17]/div['
                        '3]/div/div/table/tbody/tr[3]/td[3]/textarea').send_keys(
        ss3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[17]/div['
                        '3]/div/div/table/tbody/tr[3]/td[5]/input').send_keys(
        ss31)

    # 4
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[17]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[3]/textarea').send_keys(
        ss4)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[17]/div[3]/div/div/table/tbody/'
                        'tr[4]/td[5]/input').send_keys(
        ss41)

    # Waste chutes 2

    # 2
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[18]/div[3]/div/div/table/tbody/tr['
                        '2]/td[3]/textarea').send_keys(
        wc2)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[18]/div[3]/div/div/table/tbody/'
                        'tr[2]/td[5]/input').send_keys(
        wc21)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[19]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np1)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[19]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np2)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[20]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np3)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[20]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np4)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[21]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np5)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[21]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np6)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[22]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np7)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[22]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np8)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[23]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np9)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[23]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np10)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[24]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np11)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[24]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np12)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[25]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np13)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[25]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np14)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[26]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np15)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[26]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np16)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[27]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np17)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[27]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np18)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[28]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np19)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[28]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np20)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[29]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np21)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[29]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np22)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[30]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np23)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[30]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np24)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[31]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np25)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[31]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np26)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[32]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np27)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[32]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np28)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[33]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[4]/textarea').send_keys(
        np29)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/fieldset[33]/'
                        'div[3]/div/div/table/tbody/tr[2]/td[5]/textarea').send_keys(
        np30)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[4]/div[35]'
                        '/table/tbody/tr[1]/td[2]/div/div[2]/textarea').send_keys(
        dd)
    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/fieldset[5]/fieldset/div[2]'
                        '/table/tbody/tr/td/div/div[2]/textarea').send_keys(
        re)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/div[12]/div[2]'
                        '/table/tbody/tr[2]/td[4]/input').send_keys(
        di)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/div[12]/div[2]'
                        '/table/tbody/tr[3]/td[4]/input').send_keys(
        rur)

    driver.find_element(By.XPATH,
                        '/html/body/form[1]/div/div[12]/div[2]'
                        '/table/tbody/tr[4]/td[4]/input').send_keys(
        isr)

    time.sleep(2000000)


if __name__ == "__main__":
    main()
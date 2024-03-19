from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def overview_data(skaterID):

    # Returns a dictionary in the format of: {stat: [player's stat, league avg, percentile]}

    driver = webdriver.Chrome()
    url = f'https://edge.nhl.com/en/skater/20232024-regular-{skaterID}'
    driver.get(url)
    XPATH = '//*[@id="overview-section-content"]/div[1]/div/table/tbody'
    wait = WebDriverWait(driver, 45)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
    elements = element.text.split()
    driver.quit()

    counter = 0

    overview_dict = {'Top Skating Speed (mph)': [],
                     'Speed Bursts Over 20 mph': [],
                     'Skating Distance (mi)': [],
                     'Top Shot Speed (mph)': [],
                     'Shots on Goal': [],
                     'Shooting %': [],
                     'Goals': [],
                     'Off. Zone Time (ES)': []
                     }

    for key in overview_dict:
        counter += len(key.split())
        overview_dict[key].append(elements[counter])
        overview_dict[key].append(elements[counter + 1])
        if elements[counter + 2] == 'Below':
            new_string = 'Below' + ' ' + elements[counter + 3]
            overview_dict[key].append(new_string)
            counter += 1
        else:
            overview_dict[key].append(elements[counter + 2])
        counter += 3

    return overview_dict


def skating_speed_data(skaterID):

    # Returns a dictionary in the format of: {stat: [player's stat, league avg, percentile]}

    driver = webdriver.Chrome()
    url = f'https://edge.nhl.com/en/skater/20232024-regular-{skaterID}'
    driver.get(url)
    XPATH = '//*[@id="skatingspeed-section-content"]/div[1]/div/table/tbody'
    wait = WebDriverWait(driver, 45)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
    elements = element.text.split()
    driver.quit()

    counter = 0

    skating_speed_dict = {'Top Speed (mph)': [],
                     '22+ mph bursts': [],
                     '20-22 mph bursts': [],
                     '18-20 mph bursts': [],
                     }

    for key in skating_speed_dict:
        counter += len(key.split())
        skating_speed_dict[key].append(elements[counter])
        skating_speed_dict[key].append(elements[counter + 1])
        if elements[counter + 2] == 'Below':
            new_string = 'Below' + ' ' + elements[counter + 3]
            skating_speed_dict[key].append(new_string)
            counter += 1
        else:
            skating_speed_dict[key].append(elements[counter + 2])
        counter += 3

    return skating_speed_dict

def skating_distance_data(skaterID):

    # Returns a dictionary in the format of: {stat: [player's stat, league avg, percentile]}

    driver = webdriver.Chrome()
    url = f'https://edge.nhl.com/en/skater/20232024-regular-{skaterID}'
    driver.get(url)
    XPATH = '//*[@id="skatingdistance-section-content"]/div[1]/div/table/tbody'
    wait = WebDriverWait(driver, 45)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
    elements = element.text.split()
    driver.quit()

    counter = 0

    skating_distance_dict = {'Total (mi)': [],
                     'Average Per 60 (mi)': [],
                     'Top Game (mi)': [],
                     'Top Period (mi)': [],
                     }

    for key in skating_distance_dict:
        counter += len(key.split())
        skating_distance_dict[key].append(elements[counter])
        skating_distance_dict[key].append(elements[counter + 1])
        if elements[counter + 2] == 'Below':
            new_string = 'Below' + ' ' + elements[counter + 3]
            skating_distance_dict[key].append(new_string)
            counter += 1
        else:
            skating_distance_dict[key].append(elements[counter + 2])
        counter += 3

    return skating_distance_dict

def shot_speed_data(skaterID):

    # Returns a dictionary in the format of: {stat: [player's stat, league avg, percentile]}

    driver = webdriver.Chrome()
    url = f'https://edge.nhl.com/en/skater/20232024-regular-{skaterID}'
    driver.get(url)
    XPATH = '//*[@id="shotspeed-section-content"]/div[1]/div/table/tbody'
    wait = WebDriverWait(driver, 45)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
    elements = element.text.split()
    driver.quit()

    counter = 0

    shot_speed_dict = {'Top Speed (mph)': [],
                     'Average Speed (mph)': [],
                     '100+ mph shots': [],
                     '90-100 mph shots': [],
                     '80-90 mph shots': [],
                     '70-80 mph shots': []
                       }

    for key in shot_speed_dict:
        counter += len(key.split())
        shot_speed_dict[key].append(elements[counter])
        shot_speed_dict[key].append(elements[counter + 1])
        if elements[counter + 2] == 'Below':
            new_string = 'Below' + ' ' + elements[counter + 3]
            shot_speed_dict[key].append(new_string)
            counter += 1
        else:
            shot_speed_dict[key].append(elements[counter + 2])
        counter += 3

    return shot_speed_dict

def zone_time_data(skaterID):

    # Returns a dictionary in the format of: {stat: [player's stat, league avg, percentile]}

    driver = webdriver.Chrome()
    url = f'https://edge.nhl.com/en/skater/20232024-regular-{skaterID}'
    driver.get(url)
    XPATH = '//*[@id="zonetime-section-content"]/div[1]/div/table/tbody'
    wait = WebDriverWait(driver, 45)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
    elements = element.text.split()
    driver.quit()

    counter = 0

    zone_time_dict = {'Offensive Zone': [],
                     'Neutral Zone': [],
                     'Defensive Zone': [],
                    }

    for key in zone_time_dict:
        counter += len(key.split())
        zone_time_dict[key].append(elements[counter])
        zone_time_dict[key].append(elements[counter + 1])
        if elements[counter + 2] == 'Below':
            new_string = 'Below' + ' ' + elements[counter + 3]
            zone_time_dict[key].append(new_string)
            counter += 1
        else:
            zone_time_dict[key].append(elements[counter + 2])
        counter += 3

    return zone_time_dict

# Auston Matthews ID - 8479318

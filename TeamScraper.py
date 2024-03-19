from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import matplotlib.pyplot as plt
import numpy as np

team_to_abbreviation = {'Anaheim': 'ANA', 'Arizona': 'ARI', 'Boston': 'BOS', 'Buffalo': 'BUF', 'Calgary': 'CGY',
                          'Carolina': 'CAR', 'Chicago': 'CHI', 'Colorado': 'COL', 'Columbus': 'CBJ', 'Dallas': 'DAL',
                            'Detroit': 'DET', 'Edmonton': 'EDM', 'Florida': 'FLA', 'Los Angeles': 'LAK', 'Minnesota': 'MIN',
                            'Montreal': 'MTL', 'Nashville': 'NSH', 'New Jersey': 'NJD', 'N.Y. Islanders': 'NYI',
                            'N.Y. Rangers': 'NYR', 'Ottawa': 'OTT', 'Philadelphia': 'PHI', 'Pittsburgh': 'PIT',
                            'Seattle': 'SEA', 'San Jose': 'SJS', 'St. Louis': 'STL', 'Tampa Bay': 'TBL', 'Toronto': 'TOR',
                            'Vancouver': 'VAN', 'Vegas': 'VGK', 'Washington': 'WSH', 'Winnipeg': 'WPG'}

abbreviation_to_team = {'ANA': 'Anaheim', 'ARI': 'Arizona', 'BOS': 'Boston', 'BUF': 'Buffalo', 'CGY': 'Calgary',
                            'CAR': 'Carolina', 'CHI': 'Chicago', 'COL': 'Colorado', 'CBJ': 'Columbus', 'DAL': 'Dallas',
                            'DET': 'Detroit', 'EDM': 'Edmonton', 'FLA': 'Florida', 'LAK': 'Los Angeles', 'MIN': 'Minnesota',
                            'MTL': 'Montreal', 'NSH': 'Nashville', 'NJD': 'New Jersey', 'NYI': 'N.Y. Islanders',
                            'NYR': 'N.Y. Rangers', 'OTT': 'Ottawa', 'PHI': 'Philadelphia', 'PIT': 'Pittsburgh',
                            'SEA': 'Seattle', 'SJS': 'San Jose', 'STL': 'St. Louis', 'TBL': 'Tampa Bay', 'TOR': 'Toronto',
                            'VAN': 'Vancouver', 'VGK': 'Vegas', 'WSH': 'Washington', 'WPG': 'Winnipeg'}

teams_data = {
    'Anaheim': [68, 336],
    'Florida': [68, 300],
    'Arizona': [68, 269],
    'Minnesota': [68, 262],
    'Tampa Bay': [67, 232],
    'Philadelphia': [68, 252],
    'Ottawa': [66, 241],
    'Montreal': [67, 264],
    'Boston': [69, 269],
    'Nashville': [68, 225],
    'Colorado': [68, 249],
    'Vancouver': [68, 233],
    'San Jose': [67, 242],
    'Calgary': [68, 243],
    'Buffalo': [69, 240],
    'Edmonton': [65, 242],
    'Detroit': [68, 261],
    'Toronto': [66, 221],
    'N.Y. Rangers': [68, 224],
    'Chicago': [68, 216],
    'Carolina': [68, 248],
    'Columbus': [68, 228],
    'Washington': [67, 228],
    'Winnipeg': [67, 208],
    'Los Angeles': [67, 241],
    'New Jersey': [68, 230],
    'Seattle': [67, 211],
    'Pittsburgh': [67, 223],
    'Vegas': [67, 193],
    'N.Y. Islanders': [67, 216],
    'St. Louis': [68, 199],
    'Dallas': [69, 217]
}


# with open('TeamStats.csv', 'r', newline='') as file:
#     reader = csv.reader(file)
#     data = list(reader)
#
#     data[0] = 'Team', 'Off. Zone Time', 'GP', 'Minor Penalties'
#
#     for row in data[1:]:
#         row.append(teams_data[abbreviation_to_team[row[0]]][0])
#         row.append(teams_data[abbreviation_to_team[row[0]]][1])
#
# with open('TeamStats.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)


min_per_game = []
ozone_time = []

with open('TeamStats.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)
    for row in data[1:]:
        min_per_game.append(float(row[-1])/float(row[-2]))
        ozone_time.append(float(row[-3][:-1]))

plt.scatter(min_per_game, ozone_time)
plt.xlabel('Minor Penalties per Game')
plt.ylabel('Offensive Zone Time')
plt.title('Minor Penalties per Game vs. Offensive Zone Time')

# Line of best fit
coefficients = np.polyfit(min_per_game, ozone_time, 1)  # Fit a first-degree polynomial (linear fit)
poly = np.poly1d(coefficients)
plt.plot(min_per_game, poly(min_per_game), color='red')

plt.show()



# nhl_teams = ['ANA', 'ARI', 'BOS', 'BUF', 'CGY', 'CAR', 'CHI', 'COL', 'CBJ', 'DAL', 'DET', 'EDM', 'FLA', 'LAK', 'MIN',
#              'MTL', 'NSH', 'NJD', 'NYI', 'NYR', 'OTT', 'PHI', 'PIT', 'SEA', 'SJS', 'STL', 'TBL', 'TOR', 'VAN', 'VGK',
#              'WSH', 'WPG']
#
# with open('TeamStats.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Team', 'Off. Zone Time'])
#
# for team in nhl_teams:
#     driver = webdriver.Chrome()
#     url = f'https://edge.nhl.com/en/team/20232024-regular-{team}'
#     driver.get(url)
#     XPATH = '//*[@id="zonetime-section-content"]/div[1]/div/table/tbody/tr[1]/th[1]'
#     wait = WebDriverWait(driver, 45)
#     element = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
#
#     with open('TeamStats.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([team, element.text])
#
#     driver.quit()


# Path: NHLEdge/NHLEdge-Scraper/TeamScraper.py
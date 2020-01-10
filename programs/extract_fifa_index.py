import requests
from bs4 import BeautifulSoup

# Take statistics by months from FIFA
def get_stats(url, filename, month):
    """
    Requests for the statistics of Attack, Mid, Defense, Overal in the date required
    :param url: fifa webpage filter Liga Santander and Date selected
    :param filename: output file name
    :param month: the month (i take the last day possible for each month
    :return: the filename created and writed
    """
    resp = requests.get(url)

    if resp.status_code == 200:
        print('{}  ---> OPENED!'.format(url))
        soup = BeautifulSoup(resp.text, 'html.parser')
        columns = (soup.find('tbody')).findAll('tr')

        with open(filename + ".csv", "a") as f:
            for c in columns:
                rows = c.findAll('td')
                for r in rows:
                    if r.get('data-title') == 'Name':
                        f.write('{},'.format(r.text))
                        f.write(month+',')
                    if r.get('data-title') == 'ATT':
                        f.write('{},'.format(r.text))
                    if r.get('data-title') == 'MID':
                        f.write('{},'.format(r.text))
                    if r.get('data-title') == 'DEF':
                        f.write('{},'.format(r.text))
                    if r.get('data-title') == 'OVR':
                        f.write('{}\n'.format(r.text))


# # COJO SIEMPRE EL ULTIMO DIA DEL MES POSIBLE REGISTRADO EN LA WEB DE LA FIFA

filename = 'fifaindex_1516'
with open(filename + ".csv", "a") as f:
    f.write('Team,Date,ATT,MID,DEF,OVR\n')

# 25 setiembre, 30 octubre, 26 noviembre, 30 diciembre, 28 enero, 25 febrero, 31 marzo, 28 abril, 26 mayo
dias = ['20', '25', '29', '34', '38', '44', '49', '53', '57']
months = ['9', '10', '11', '12', '1', '2', '3', '4', '5']
for i in range(len(dias)):
    url = 'https://www.fifaindex.com/teams/fifa16_' + dias[i] + '/?league=53'
    get_stats(url, filename, months[i])

# filename = 'fifaindex_1617'
# with open(filename + ".csv", "a") as f:
#     f.write('Team,Date,ATT,MID,DEF,OVR\n')
#
# # 25 agosto, 29 setiembre, 31 octubre, 28 noviembre, 27 diciembre, 30 enero, 27 febrero, 30 marzo, 27 abril, 29 mayo
# dias = ['74', '76', '81', '89', '97', '107', '115', '124', '132', '141']
# months = ['8', '9', '10', '11', '12', '1', '2', '3', '4', '5']
# for i in range(len(dias)):
#     url = 'https://www.fifaindex.com/teams/fifa17_' + dias[i] + '/?league=53'
#     get_stats(url, filename, months[i])

# filename = 'fifaindex_1718'
# with open(filename + ".csv", "a") as f:
#     f.write('Team,Date,ATT,MID,DEF,OVR\n')
#
# # 22 agosto, 28 setiembre, 30 octubre, 30 noviembre, 28 diciembre, 29 enero, 26 febrero, 29 marzo, 30 abril, 31 mayo
# dias = ['174', '176', '185', '193', '200', '209', '217', '225', '234', '243']
# months = ['8', '9', '10', '11', '12', '1', '2', '3', '4', '5']
# for i in range(len(dias)):
#     url = 'https://www.fifaindex.com/teams/fifa18_' + dias[i] + '/?league=53'
#     get_stats(url, filename, months[i])

# filename = 'fifaindex_1819'
# with open(filename + ".csv", "a") as f:
#     f.write('Team,Date,ATT,MID,DEF,OVR\n')
#
# # 21 agosto, 27 setiembre, 31 octubre, 26 noviembre, 27 diciembre, 31 enero, 28 febrero, 28 marzo, 29 abril, 30 mayo
# dias = ['279', '282', '293', '297', '302', '311', '318', '325', '335', '341']
# months = ['8', '9', '10', '11', '12', '1', '2', '3', '4', '5']
# for i in range(10):
#     url = 'https://www.fifaindex.com/teams/fifa19_' + dias[i] + '/?league=53'
#     get_stats(url, filename, months[i])


# filename = 'fifaindex_1920'
# with open(filename + ".csv", "a") as f:
#     f.write('Team,Date,ATT,MID,DEF,OVR\n')
#
# # 2 agosto, 22 agosto, 30 setiembre
# dias = ['354', '357', '359']
# months = ['8', '9', '10']
# for i in range(3):
#     url = 'https://www.fifaindex.com/teams/fifa20_' + dias[i] + '/?league=53'
#     get_stats(url, filename, months[i])

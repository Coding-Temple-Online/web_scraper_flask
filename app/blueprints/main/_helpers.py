from selenium import webdriver
from time import sleep
from app.blueprints.main.models import Player
from app import db


def get_player_data(player_info):
    # Create web driver
    driver = webdriver.Chrome('./chromedriver')

    # Connect to the website
    driver.get('https://www.nbastuffer.com')

    # Find and click on the NBA Player Stats button
    link_to_click = driver.find_elements_by_class_name('x-recent-post6')[3]
    link_to_click.click()

    # Type a name into the search input field
    search_field = driver.find_element_by_tag_name('input')
    search_field.send_keys(player_info)

    sleep(5)

    # Get the searched person's info from the search results
    data = driver.find_element_by_css_selector('.row-hover tr:first-of-type')

    # Put the player's data into a list
    columns = data.find_elements_by_css_selector('td')
    pd = [i.text for i in columns]
    new_player = Player(
        name=pd[1],
        team=pd[2],
        position=pd[3],
        age=pd[4],
        gp=pd[5],
        mpg=pd[6],
        fta=pd[10],
        ftp=pd[11],
        tpa=pd[12],
        tpp=pd[13],
        thpa=pd[14],
        thpp=pd[15],
        ppg=pd[18],
        rpg=pd[19],
        apg=pd[21],
        spg=pd[23],
        bpg=pd[24],
        topg=pd[25]
    )
    db.session.add(new_player)
    db.session.commit()
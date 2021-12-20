from time import sleep
from .import bp as main
from flask import jsonify, render_template, redirect, url_for, request, flash
from ._helpers import get_player_data
from .models import Player

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        player_name = request.form.get('player_search')
        get_player_data(player_name)
        # print('It worked!')
        flash(f"{player_name.title()}'s information has been added to your database.")
        
        redirect(url_for(request.referrer))
    context = {
        'players': Player.query.all()
    }
    return render_template('index.html', **context)

@main.route('/cronjob', methods=['POST'])
def cronjob():
    player_name = request.form.get('player_search')
    get_player_data('DeMar DeRozan')
    # print('It worked!')
    # flash(f"{player_name.title()}'s information has been added to your database.")
    sleep(10)
    redirect(url_for(main.cronjob))
    return redirect(url_for(request.referrer))
from flask import Flask

from SpecChoise.views.views import home, specialties, useful_articles, rendering_of_pr_list, rendering_of_pr_article, \
    what_profession_to_choose, prof_for_those_who_do_quickly_bored, parental_influence, test1_zno, test2_prof_orient_start, \
    _spec_gener, demand_for_prof, test2_prof_orient, _prof_calc

app = Flask(__name__)

# головна
app.add_url_rule('/', view_func=home, methods=['GET'])

# тести
app.add_url_rule('/zno-test', view_func=test1_zno, methods=['GET'])
app.add_url_rule('/prof-orient-test-start', view_func=test2_prof_orient_start, methods=['GET'])
app.add_url_rule('/prof-orient-test', view_func=test2_prof_orient, methods=['GET', 'POST'])

# довідник спеціальностей
app.add_url_rule('/specialties', view_func=specialties, methods=['GET'])
app.add_url_rule('/specialties/<name>', view_func=rendering_of_pr_list, methods=['GET'])
app.add_url_rule('/specialties/<name>/<profession>', view_func=rendering_of_pr_article, methods=['GET'])

# корисні статті
app.add_url_rule('/useful-articles', view_func=useful_articles, methods=['GET'])
app.add_url_rule('/useful-articles/what_profession-to-choose', view_func=what_profession_to_choose, methods=['GET'])
app.add_url_rule('/useful-articles/prof-for-those-who-do-quickly-bored', view_func=prof_for_those_who_do_quickly_bored,
                 methods=['GET'])
app.add_url_rule('/useful-articles/demand_for_prof', view_func=demand_for_prof, methods=['GET'])
app.add_url_rule('/useful-articles/parental-influence', view_func=parental_influence, methods=['GET'])

# ajax посилання
app.add_url_rule('/_spec_gener', view_func=_spec_gener, methods=['GET', 'POST'])  # для ЗНО тесту
app.add_url_rule('/_prof_calc', view_func=_prof_calc, methods=['GET', 'POST'])  # для проф-орієнт. тесту

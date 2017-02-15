from flask import render_template, jsonify, request
from SpecChoise.db.db import base_entries, prof_entries, test_entries, test_zno


def home():
    return render_template('home.html')


def test1_zno():
    return render_template('test1(zno).html')


def test2_prof_orient_start():
    return render_template('test2(prof-oriet)_start.html')


def test2_prof_orient():
    return render_template("test2(prof-oriet).html")


def specialties():
    return render_template('specialties.html')


def rendering_of_pr_list(name):
    entries = base_entries(name)
    return render_template('pr_group.html', name=name, entries=entries)


def rendering_of_pr_article(profession, name):
    entries = prof_entries(profession)
    right_list = base_entries(name)
    return render_template('article.html', entries=entries, profession=profession, name=name, right_list=right_list)


def useful_articles():
    return render_template('useful_articles.html')


def what_profession_to_choose():
    return render_template('what_profession_to_choose.html')


def demand_for_prof():
    return render_template("demand_for_prof.html")


def prof_for_those_who_do_quickly_bored():
    return render_template('prof_for_those_who_do_quickly_bored.html')


def parental_influence():
    return render_template('parental_influence.html')


def _spec_gener():
    entries = test_zno()
    subjects = []
    if request.args.get('math') == "true":
        subjects.append("Математика")
    if request.args.get('physics') == "true":
        subjects.append("Фізика")
    if request.args.get('ukrainian_history') == "true":
        subjects.append("Історія України")
    if request.args.get('foreign_lang') == "true":
        subjects.append("Англійська мова")
    if request.args.get('geography') == "true":
        subjects.append("Географія")
    if request.args.get('chemistry') == "true":
        subjects.append("Хімія")
    if request.args.get('biology') == "true":
        subjects.append("Біологія")
    result = dict()
    for spec_name, neaded_sub in entries.items():
        k = 0
        for sub in subjects:
            if sub in neaded_sub:
                k += 1
        if len(neaded_sub) == 1 and k == 1:
            result.update({spec_name: neaded_sub})
        if k >= 2:
            result.update({spec_name: neaded_sub})
    rspeciality = []
    rsubjects = []
    for speciality, subjects in result.items():
        rspeciality.append(speciality)
        rsubjects.append(subjects)
    return jsonify(speciality=rspeciality, subjects=rsubjects)


def _prof_calc():
    entries = test_entries()
    return jsonify(entries=entries)

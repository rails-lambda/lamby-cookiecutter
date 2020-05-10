# -*- coding: utf-8 -*-

"""
    inflection (trimmed)
    ~~~~~~~~~~~~
    A port of Ruby on Rails' inflector to Python.
    :copyright: (c) 2012-2015 by Janne Vanhala
    :license: MIT, see LICENSE for more details.
    https://github.com/jpvanhal/inflection
"""
import re
import unicodedata

__version__ = '0.3.1'

PLURALS = [
    (r"(?i)(quiz)$", r'\1zes'),
    (r"(?i)^(oxen)$", r'\1'),
    (r"(?i)^(ox)$", r'\1en'),
    (r"(?i)(m|l)ice$", r'\1ice'),
    (r"(?i)(m|l)ouse$", r'\1ice'),
    (r"(?i)(matr|vert|ind)(?:ix|ex)$", r'\1ices'),
    (r"(?i)(x|ch|ss|sh)$", r'\1es'),
    (r"(?i)([^aeiouy]|qu)y$", r'\1ies'),
    (r"(?i)(hive)$", r'\1s'),
    (r"(?i)([lr])f$", r'\1ves'),
    (r"(?i)([^f])fe$", r'\1ves'),
    (r"(?i)sis$", 'ses'),
    (r"(?i)([ti])a$", r'\1a'),
    (r"(?i)([ti])um$", r'\1a'),
    (r"(?i)(buffal|potat|tomat)o$", r'\1oes'),
    (r"(?i)(bu)s$", r'\1ses'),
    (r"(?i)(alias|status)$", r'\1es'),
    (r"(?i)(octop|vir)i$", r'\1i'),
    (r"(?i)(octop|vir)us$", r'\1i'),
    (r"(?i)^(ax|test)is$", r'\1es'),
    (r"(?i)s$", 's'),
    (r"$", 's'),
]

SINGULARS = [
    (r"(?i)(database)s$", r'\1'),
    (r"(?i)(quiz)zes$", r'\1'),
    (r"(?i)(matr)ices$", r'\1ix'),
    (r"(?i)(vert|ind)ices$", r'\1ex'),
    (r"(?i)^(ox)en", r'\1'),
    (r"(?i)(alias|status)(es)?$", r'\1'),
    (r"(?i)(octop|vir)(us|i)$", r'\1us'),
    (r"(?i)^(a)x[ie]s$", r'\1xis'),
    (r"(?i)(cris|test)(is|es)$", r'\1is'),
    (r"(?i)(shoe)s$", r'\1'),
    (r"(?i)(o)es$", r'\1'),
    (r"(?i)(bus)(es)?$", r'\1'),
    (r"(?i)(m|l)ice$", r'\1ouse'),
    (r"(?i)(x|ch|ss|sh)es$", r'\1'),
    (r"(?i)(m)ovies$", r'\1ovie'),
    (r"(?i)(s)eries$", r'\1eries'),
    (r"(?i)([^aeiouy]|qu)ies$", r'\1y'),
    (r"(?i)([lr])ves$", r'\1f'),
    (r"(?i)(tive)s$", r'\1'),
    (r"(?i)(hive)s$", r'\1'),
    (r"(?i)([^f])ves$", r'\1fe'),
    (r"(?i)(t)he(sis|ses)$", r"\1hesis"),
    (r"(?i)(s)ynop(sis|ses)$", r"\1ynopsis"),
    (r"(?i)(p)rogno(sis|ses)$", r"\1rognosis"),
    (r"(?i)(p)arenthe(sis|ses)$", r"\1arenthesis"),
    (r"(?i)(d)iagno(sis|ses)$", r"\1iagnosis"),
    (r"(?i)(b)a(sis|ses)$", r"\1asis"),
    (r"(?i)(a)naly(sis|ses)$", r"\1nalysis"),
    (r"(?i)([ti])a$", r'\1um'),
    (r"(?i)(n)ews$", r'\1ews'),
    (r"(?i)(ss)$", r'\1'),
    (r"(?i)s$", ''),
]

UNCOUNTABLES = {
    'equipment',
    'fish',
    'information',
    'jeans',
    'money',
    'rice',
    'series',
    'sheep',
    'species'}


def camelize(string, uppercase_first_letter=True):
    """
    Convert strings to CamelCase.
    Examples::
        >>> camelize("device_type")
        "DeviceType"
        >>> camelize("device_type", False)
        "deviceType"
    :func:`camelize` can be thought of as a inverse of :func:`underscore`,
    although there are some cases where that does not hold::
        >>> camelize(underscore("IOError"))
        "IoError"
    :param uppercase_first_letter: if set to `True` :func:`camelize` converts
        strings to UpperCamelCase. If set to `False` :func:`camelize` produces
        lowerCamelCase. Defaults to `True`.
    """
    if uppercase_first_letter:
        return re.sub(r"(?:^|_)(.)", lambda m: m.group(1).upper(), string)
    else:
        return string[0].lower() + camelize(string)[1:]


def dasherize(word):
    """Replace underscores with dashes in the string.
    Example::
        >>> dasherize("puni_puni")
        "puni-puni"
    """
    return word.replace('_', '-')


def humanize(word):
    """
    Capitalize the first word and turn underscores into spaces and strip a
    trailing ``"_id"``, if any. Like :func:`titleize`, this is meant for
    creating pretty output.
    Examples::
        >>> humanize("employee_salary")
        "Employee salary"
        >>> humanize("author_id")
        "Author"
    """
    word = re.sub(r"_id$", "", word)
    word = word.replace('_', ' ')
    word = re.sub(r"(?i)([a-z\d]*)", lambda m: m.group(1).lower(), word)
    word = re.sub(r"^\w", lambda m: m.group(0).upper(), word)
    return word


def pluralize(word):
    """
    Return the plural form of a word.
    Examples::
        >>> pluralize("post")
        "posts"
        >>> pluralize("octopus")
        "octopi"
        >>> pluralize("sheep")
        "sheep"
        >>> pluralize("CamelOctopus")
        "CamelOctopi"
    """
    if not word or word.lower() in UNCOUNTABLES:
        return word
    else:
        for rule, replacement in PLURALS:
            if re.search(rule, word):
                return re.sub(rule, replacement, word)
        return word


def singularize(word):
    """
    Return the singular form of a word, the reverse of :func:`pluralize`.
    Examples::
        >>> singularize("posts")
        "post"
        >>> singularize("octopi")
        "octopus"
        >>> singularize("sheep")
        "sheep"
        >>> singularize("word")
        "word"
        >>> singularize("CamelOctopi")
        "CamelOctopus"
    """
    for inflection in UNCOUNTABLES:
        if re.search(r'(?i)\b(%s)\Z' % inflection, word):
            return word

    for rule, replacement in SINGULARS:
        if re.search(rule, word):
            return re.sub(rule, replacement, word)
    return word


def tableize(word):
    """
    Create the name of a table like Rails does for models to table names. This
    method uses the :func:`pluralize` method on the last word in the string.
    Examples::
        >>> tableize('RawScaledScorer')
        "raw_scaled_scorers"
        >>> tableize('egg_and_ham')
        "egg_and_hams"
        >>> tableize('fancyCategory')
        "fancy_categories"
    """
    return pluralize(underscore(word))


def titleize(word):
    """
    Capitalize all the words and replace some characters in the string to
    create a nicer looking title. :func:`titleize` is meant for creating pretty
    output.
    Examples::
      >>> titleize("man from the boondocks")
      "Man From The Boondocks"
      >>> titleize("x-men: the last stand")
      "X Men: The Last Stand"
      >>> titleize("TheManWithoutAPast")
      "The Man Without A Past"
      >>> titleize("raiders_of_the_lost_ark")
      "Raiders Of The Lost Ark"
    """
    return re.sub(
        r"\b('?[a-z])",
        lambda match: match.group(1).capitalize(),
        humanize(underscore(word))
    )


def underscore(word):
    """
    Make an underscored, lowercase form from the expression in the string.
    Example::
        >>> underscore("DeviceType")
        "device_type"
    As a rule of thumb you can think of :func:`underscore` as the inverse of
    :func:`camelize`, though there are cases where that does not hold::
        >>> camelize(underscore("IOError"))
        "IoError"
    """
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
    word = word.replace("-", "_")
    return word.lower()





"""
    Super Hacky Derived Project Variables (setup)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    https://github.com/cookiecutter/cookiecutter/issues/1101
    https://github.com/cookiecutter/cookiecutter/pull/944
"""

import os
import pathlib
import json
from os.path import expanduser

project_name  = '{{cookiecutter.project_name}}'
cc_template   = '{{cookiecutter._template}}'
template_name = cc_template.split("/")[-1]

file_name  = singularize(tableize(project_name))
class_name = singularize(camelize(tableize(project_name)))
dash_name  = singularize(dasherize(project_name))
all_names  = {
  'file_name': file_name,
  'class_name': class_name,
  'dash_name': dash_name
}

home_dir = expanduser("~")
template_dir = os.path.join(home_dir, '.cookiecutters', template_name)
temp_dir = os.path.join(template_dir, '{{'{{'}}cookiecutter.project_name{{'}}'}}', '_cctmp')
pathlib.Path(temp_dir).mkdir(parents=True, exist_ok=True)

with open(os.path.join(temp_dir, 'vars.json'), 'w') as f:
  json.dump(all_names, f)

for name in all_names.keys():
  file_path = os.path.join(temp_dir, name + '.txt')
  with open(file_path, 'w') as f:
    f.write(all_names[name])


"""
    Super Hacky Derived Project Variables (teardown)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    https://github.com/cookiecutter/cookiecutter/issues/1101
    https://github.com/cookiecutter/cookiecutter/pull/944
"""

import os
import shutil
import json
from os.path import expanduser

cc_template   = '{{cookiecutter._template}}'
template_name = cc_template.split("/")[-1]

home_dir = expanduser("~")
template_dir = os.path.join(home_dir, '.cookiecutters', template_name)
temp_dir = os.path.join(template_dir, '{{'{{'}}cookiecutter.project_name{{'}}'}}', '_cctmp')

all_names = {}
with open(os.path.join(temp_dir, 'vars.json')) as f:
  all_names = json.load(f)

shutil.rmtree(temp_dir)
shutil.rmtree('_cctmp')

# -*- coding: utf-8 -*-

import sys
import os

# Prefer to use the version of the theme in this repo
# and not the installed version of the theme.
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('./demo/'))

from sphinx_rtd_theme import __version__ as theme_version
from sphinx_rtd_theme import __version_full__ as theme_version_full
from sphinx.locale import _


project = 'HipertansiyondaNorogoruntuleme'
copyright = '2023, Ali Bayram'
author = 'Ali Bayram'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
	'sphinx.ext.duration',
	'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'tr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = ["_themes", ]

html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
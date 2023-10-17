# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sigasi'
copyright = '2023, Dirk Seynhaeve'
author = 'Dirk Seynhaeve'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_rtd_theme",
]
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    # "amsmath",
    # "attrs_inline",
    # "colon_fence",
    # "deflist",
    # "dollarmath",
    # "fieldlist",
    # "html_admonition",
    # "html_image",
    # "linkify",
    # "replacements",
    # "smartquotes",
    # "strikethrough",
    # "substitution",
    # "tasklist",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_title = "Sigasi Studio Documentation"
html_logo = "_static/sigasi_logo_white.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    # List of themes           : 
    #   https://sphinx-themes.org/
    # ReadTheDocs documentation:
    #   https://readthedocs.org/projects/icona/downloads/pdf/stable/
    # ReadTheDocs sample       :
    #   https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/
    # ReadTheDocs configuration:
    #   https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": False,
    "navigation_depth": -1,
    "includehidden": True,
    "titles_only": False,
    # Analytical options
    # "analytics_id": "G-XXXXXXXXXX",  #  Provided by Google in your dashboard
    # "analytics_anonymize_ip": False,
    # Miscellaneous options
    "display_version": True,
    "logo_only": True,
    "prev_next_buttons_location": "both",
    "style_external_links": False,
    # Sigasi Orange:  #EC6508 
    # Sigasi Purple:  #360E61
    # Sigasi WHite :  #F8F8F8  
    "style_nav_header_background": "#360E61",
    # GitHub options

    "vcs_pageview_mode": "blob",
}
html_context = {
    "display_github": True,
    # "github_user": "",
    "github_repo": "dseynhae/SphinxDemo/",
    "github_version": "main/",
     "conf_py_path": "/source/",
}


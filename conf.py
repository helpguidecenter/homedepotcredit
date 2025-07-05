# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Home Depot MyCard Login Guide'
copyright = '2025, Home Depot'
author = 'Home Depot Credit Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# SEO Title for browser tab and HTML pages
html_title = "Manage Your Home Depot Credit Card at homedepot.com/mycard"


# Optional short title for nav bar
html_short_title = "Home Depot MyCard"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Uncomment to set a theme
# html_theme = 'sphinx_rtd_theme'

# Hide the "View page source" link
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if needed

# Files to exclude
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

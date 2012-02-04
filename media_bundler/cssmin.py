# media_bundler/cssmin.py

# Original source code:
# http://stackoverflow.com/questions/222581/python-script-for-minifying-css

# This is obviously a hacky script, and it probably has bugs.

import re

def minify_css(css):
    # remove comments - this will break a lot of hacks :-P
    css = re.sub(r'\s*/\*\s*\*/', "$$HACK1$$", css)
    css = re.sub(r'/\*[\s\S]*?\*/', "", css)
    css = css.replace("$$HACK1$$", '/**/') # preserve IE<6 comment hack
    # url() don't need quotes
    css = re.sub(r'url\((["\'])([^)]*)\1\)', "url(\\2)", css)
    # spaces may be safely collapsed as generated content will collapse them anyway
    css = re.sub(r'\s+', " ", css)
    return css

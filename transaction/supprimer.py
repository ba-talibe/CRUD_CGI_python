#! /usr/bin/python3 
# -*-coding : utf-8 -*- 

import cgi, cgitb
import operation
from format import *

entete = "Content-type: text/html\n\n"
html = """
    <html>
        <body>
        {nav}
        <script> alert('{message}'); </script>
        </body>
    </html>
"""


print(entete)

cgitb.enable()
form = cgi.FieldStorage()

try:

    id = form.getvalue("id")
    message = operation.suppression(int(id))
    html = html.format(nav=navigation, message=message)
    print(html)

except Exception as e:
    html = html.format(nav=navigation, message=e.args)
    print(html)



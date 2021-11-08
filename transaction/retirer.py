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
    numcompte = form.getvalue("numcompte")
    code = form.getvalue("code")
    montant = form.getvalue("montant")
    message = operation.retrait(numcompte, montant, code)
    html = html.format(nav=navigation, message=message)
    print(html)
    

except Exception as e:
    print(e.args)
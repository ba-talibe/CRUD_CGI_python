#! /usr/bin/python3 
# -*-coding : utf-8 -*- 

import cgi, cgitb
import operation
from format import *

entete = "Content-type: text/html\n\n"
html = """
    <html>
        <body>
        <script> alert('ajout effectue'); </script>
        {nav}
        </body>
    </html>
"""

html = html.format(nav=navigation)
print(entete)

cgitb.enable()
form = cgi.FieldStorage()

try:
    prenom = form.getvalue("prenom")
    nom = form.getvalue("nom")
    numcompte = form.getvalue("numcompte")
    code = form.getvalue("code")
    solde = form.getvalue("solde")

    print(html)
    operation.create(prenom, nom, code, numcompte, solde)

except Exception as e:
    print(e.args)


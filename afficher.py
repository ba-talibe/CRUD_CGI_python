#! /usr/bin/python3 
# -*-coding : utf-8 -*- 


from transaction import operation
from transaction.format import *


ligne = """<tr>
                <td>{id}</td><td>{prenom}</td> <td>{nom}</td><td>{numcompte}</td><td>{solde}</td>
        </tr>"""

body = """
		<table border='1px'>
        <th colspan=5> table des clients </th>
        {lignes}
        </table>.
			"""

html = """
<html>
	<body>
    {nav}\n
    {body}
    </body>
</html>
"""
lignes = ""
for client in operation.readAll():
    lignes += ligne.format(id=client[0],
                            prenom=client[1],
                            nom=client[2],
                            numcompte=client[4],
                            solde=client[5]) + "\n"

body = body.format(lignes=lignes)
html = html.format(nav=navigation, body=body)

print(entete)
print(html)
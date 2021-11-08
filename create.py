#! /usr/bin/python3 
# -*-coding : utf-8 -*- 

from transaction.format import *

html = """

<html>
	<body>
    {nav}
		<form method='POST' action='/cgi-bin/banque/transaction/ajouter.py' >
        <table>
			<tr><td>Prenom           :</td><td><input type='text' name='prenom' required></td></tr>
			<tr><td>Nom              :</td><td><input type='text' name='nom' required></td></tr>
			<tr><td>Numero de compte :</td><td><input type='text' name='numcompte' required></td></tr>
			<tr><td>Code             :</td><td><input type='text' name='code' required></td></tr>
			<tr><td>Solde            :</td><td><input type='text' name='solde' required></td></tr>
            <tr><td>                  </td><td><input type='submit' value='valider' ></td>
        </table>
			

		</form>
	</body>
</html>
"""


print(entete)
print(html.format(nav=navigation))
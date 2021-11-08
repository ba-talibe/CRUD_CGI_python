#! /usr/bin/python3 
# -*-coding : utf-8 -*- 

import cgi, cgitb
from transaction.format import *




html = """

<html>
	<body>
    {nav}
		<form method='POST' action='/cgi-bin/banque/transaction/verser.py' >
        <table>
			<tr><td>Numero de compte :</td><td><input type='text' name='numcompte' required></td></tr>
			<tr><td>Montant          :</td><td><input type='text' name='montant' required></td></tr>
            <tr><td>                  </td><td><input type='submit' value='valider' ></td>
        </table>
		</form>
	</body>
</html>
"""


print(entete)
print(html.format(nav=navigation))
#! /usr/bin/python3 
# -*-coding : utf-8 -*- 

from transaction.format import *




html = """

<html>
	<body>
    {nav}
		<form method='POST' action='/cgi-bin/banque/transaction/supprimer.py' >
        <table>
			<tr><td>Id :</td><td><input type='text' name='id' required></td></tr>
            <tr><td>                  </td><td><input type='submit' value='valider' ></td>
        </table>
		</form>
	</body>
</html>
"""


print(entete)
print(html.format(nav=navigation))
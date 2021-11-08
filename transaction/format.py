
#! /usr/bin/python3 
# -*-coding : utf-8 -*- 

entete = "Content-type: text/html\n\n"

navigation = """
<ul style="padding-left: 0px;background-color: #3D99CE;text-align: center;">
        <li style="display:inline;padding: 10px 20px;">
            <a 
            href="/cgi-bin/banque/afficher.py"
            style="color: white;
                text-decoration: none;" >afficher</a>
        </li>

        <li style="display:inline;padding: 10px 20px;">
            <a href="/cgi-bin/banque/create.py" style="color: white;text-decoration: none;" >ajouter</a>
        </li>

        <li style="display:inline;padding: 10px 20px;">
            <a href="/cgi-bin/banque/depot.py" style="color: white;text-decoration: none;">depot</a>
        </li>
        
        <li style="display:inline;padding: 10px 20px;">
            <a href="/cgi-bin/banque/retrait.py" style="color: white;text-decoration: none;">retrait</a>
        </li>

         <li style="display:inline;padding: 10px 20px;">
            <a href="/cgi-bin/banque/suppression.py" style="color: white;text-decoration: none;">Supprimer</a>
        </li>
</ul><br><br>
"""
chmod -r a+x *

cp * /usr/lib/cgi-bin
pip3 install -r requirements.txt
a2enmod cgi
systemclt restart apache2
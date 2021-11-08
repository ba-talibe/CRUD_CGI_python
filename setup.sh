chmod a+x *

cp * /usr/lib/cgi-bin
a2enmod cgi
systemclt restart apache2
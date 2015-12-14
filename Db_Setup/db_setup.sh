service postgresql initdb
service postgresql start
sudo -u postgres psql 
CREATE DATABASE "Tcount"";
ALTER USER postgres with encrypted password 'pass';
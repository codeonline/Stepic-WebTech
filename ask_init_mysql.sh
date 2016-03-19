sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE ask;"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION;"
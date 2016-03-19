sudo sed -i 's/skip-external-locking/skip-external-locking\ninnodb_use_native_aio = 0/' /etc/mysql/my.cnf
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE ask;"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION;"
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/test.conf
sudo rm /etc/gunicorn.d/test
sudo rm /etc/gunicorn.d/test_ask

sudo ln -s /home/box/web/etc/default /etc/nginx/sites-available/default
sudo ln -s /home/box/web/etc/nginx_ask.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/gunicorn_ask.conf   /etc/gunicorn.d/test_ask
sudo /etc/init.d/gunicorn restart

chmod 777 ask
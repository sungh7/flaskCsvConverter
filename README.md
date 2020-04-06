### README.md

conda env create -f conda_requirements.txt
pip3 install -r requirements.txt


# nginx setting

rm /etx/nginx/sites-available/default
re /etc/nignx/sites-enabled/default

vi /etc/nginx/sites-available/nginx-test

server{	
	listen 80;
	server_name ;
	root /mnt/c/project/flask_csv_convert;

	location / {
		proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
       	            proxy_set_header Host $http_host;
          	            proxy_redirect off;
           	            if (!-f $request_filename) {
                        	proxy_pass http://127.0.0.1:8000;
                        	break;
                }
        }
        location /static{
                alias /mnt/c/project/flask_csv_convert/static;
                proxy_pass http://127.0.0.1:8000;
        }

sudo ln -s /etc/nginx/sites-available/nginx-test /etc/nginx/sites-enabled/

sudo service nginx restart

gunicorn app:app -b localhost:8000# flaskCsvConverter

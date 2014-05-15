DB_SERVER = {
			"dev":{
			"engine":"django.db.backends.sqlite3",
			"user":"user",
			"password":"password",
			"name":"",
			"port":"port",
			"host":"host"
			},
			"prod":{
			"engine":"django.db.backends.mysql",
			"user":"user",
			"password":"",
			"name":"agenda",
			"port":"3306",
			"host":"host"
			},

			}

ENV = "dev"
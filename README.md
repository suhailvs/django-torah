Load database
=============

	./manage.py shell
	from torah import scripts
	helper = scripts.LoadData()
	helper.load_words()
	helper.link_words_and_lines()


Runserver
=========

postgres

	create database torah;
	./manage.py migrate
	./manage.py runserver
# my_project
 Week 4 Python Task: Pip, Virtual environments and intro to Django 



Create a new Django project named “songcrud” and create an app in the project called “musicapp”. Your project must contain a requirements.txt file housing all the pinned dependencies from your project. Push the project to GitHub and submit your public GitHub repository link.

Note: Always create a virtual environment anytime you're working on a new Django project. You can get your requirements.txt file from your virtual environment 

 

Mode of submission - Public GitHub repository link

 

Week 5 Python Task: Django CRUD



We would be building a simple song CRUD application. In our models.py file inside the “musicapp” application we created, you are expected to add the following Models and Attributes.

 

    Model: Artiste, Song, Lyric
    Attributes for “Artiste” : first_name, last_name, age

    Attributes for “Song” : title, date released, likes, artiste_id
    Attributes for “Lyric”: content, song_id

 

As you might have guessed, there is a relationship between all three Models. An Artiste can have multiple songs, and a song can have multiple lyrics.A song must only belong to one Artiste and a lyric must only belong to a song. You are to specify the foreignkey relationship yourself.

Also, the model field attributes should be specified by you. 

Push the task to GitHub when you finish and submit the GitHub repository link

 

Mode of submission - Public Github repository link


# pwd_generator

This app is a command line based application for generating and managing your credentials for different apps!
Built with python and PostgreSQL, the app is based on 2 tables  creating a one to many relationship
the first table contains the user of the app , an user can be created at the startup of the program, the table contains a name, a password which is hashed then stored and an auto-generatted id.
The second table contains all the credentials(password,username,email,the name for which the credentials are stored and the id which is foreign key which refferences the firs table)
Through the foreign key we can find which credentials belong to each account.
The hashing and the generated passwords are based on the sha256 algorithm

RESOURCES:


        https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04
        https://www.postgresqltutorial.com/postgresql-python/connect/
        https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/
        https://www.youtube.com/watch?v=OOSl2jeAA5U&list=WL&index=16&t=447s
        

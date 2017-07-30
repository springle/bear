# Set up your dev environment

1. Clone this repo.
2. Install [docker](https://docs.docker.com/engine/installation/) and
[docker-compose](https://docs.docker.com/compose/install/).
3. Run `docker-compose up` from the project directory.
4. Open [localhost:3000](http://localhost:3000) in your browser.
5. (Optional) If you plan to use the Berkeley APIs, you will need to add
the following two lines to your bash profile. Ask one of the admins to
give you the API_KEY and API_SECRET_KEY. Remember to restart your terminal
after updating your bash profile for the changes to take effect.

```bash
export CLASSES_APP_ID="<API_KEY>"
export CLASSES_APP_KEY="<API_SECRET_KEY>"
```

# Set up your database

1. Make sure your dev environment has been set up, and
`docker-compose up` has been run.
2. Run `docker ps` to view your running containers. Copy the container ID
of the `backend` container.
3. Run `docker exec -it <backend-container-id> bash` to open up a shell
session inside that container.
4. Run `python3 manage.py makemigrations` and `python3 manage.py migrate` to
set up your database.
5. (Optional) Run `python3 manage.py createsuperuser` to generate login
credentials for the Django admin.
6. (Optional) Open [localhost:8000/admin](http://localhost:8000/admin) and log
in using the credentials you just created.

# FAQ

Q: My containers didn't shut down properly after I hit `<CTRL-C>`. What should
I do?

A: Run `docker-compose kill` to shut down your containers. Run `docker ps` to
confirm that you no longer have any running containers. Now, if you run
`docker-compose up` again, everything should start up properly.

--

Q: Where can I find documentation on the API endpoints?

A: Run `docker-compose up`, then go to
[localhost:8000/search](http://localhost:8000/search) to view the api explorer.

--

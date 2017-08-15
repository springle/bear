# Set up your dev environment

1. Clone this repo.
2. Install [docker](https://docs.docker.com/engine/installation/) and
[docker-compose](https://docs.docker.com/compose/install/).
3. Add the following line to `/etc/hosts`: `<docker-ip> bear.dev`. Unless
you are using Docker Machine, your `<docker-ip>` is probably just `bear.dev`.
4. Run `docker-compose up` from the project directory.
5. Open [bear.dev:3000](http://bear.dev:3000) in your browser.
6. (Optional) If you plan to use the Berkeley APIs, you will need to add
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
2. Run `make migrations`.
3. (Optional) If you set up your bash profile with the API credentials
described in the previous section, then you can run `make get-classes` to
populate your database using the Berkeley API.
4. (Optional) Run `make superuser` to generate login credentials
for the Django admin.
6. (Optional) Open [bear.dev:8000/admin](http://bear.dev:8000/admin) and log
in using the credentials you just created.

# FAQ

Q: How can I add a new npm package?

A: Run `PACKAGE=<your-new-package> make add-npm-package`.

--

Q: The backend container failed because of a race condition with the database.
What should I do?

A: Run `docker-compose restart backend` :)

--

Q: My containers didn't shut down properly after I hit <CTRL-C>. What should
I do?

A: Run `docker-compose kill` to shut down your containers. Run `docker ps` to
confirm that you no longer have any running containers. Now, if you run
`docker-compose up` again, everything should start up properly.

--

Q: Where can I find documentation on the API endpoints?

A: Run `docker-compose up`, then go to
[bear.dev:8000/search](http://bear.dev:8000/search) to view the api explorer.

--

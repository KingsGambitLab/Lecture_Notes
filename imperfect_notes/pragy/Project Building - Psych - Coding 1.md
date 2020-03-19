Psych Coding 1
--------------

Base Setup
----------

1. Create free account on Heroku
1. Install Heroku CLI https://devcenter.heroku.com/articles/getting-started-with-java#set-up
1. Install PostgreSQL https://www.postgresql.org/download/
    ```bash
    brew install postgres
    sudo chown -R `whoami` /usr/local
    ```
1. Ensure postgres is started automatically on boot
    ```bash
    pg_ctl -D /usr/local/var/postgres start && brew services start postgresql
    postgres -V
    ```

3. Create new Idea Project
    1. Spring Initializer
    1.
        + SDK 11 or 13
        + com.psych.game
        + Scaler Backend Project - Psych
        + Java 11
        + Maven
    1.
        + Spring Boot Dev Tools
        + Lombok
        + Spring Web
        + Rest Repositories
        + Spring Web Services
        + Spring Data JPA
        + PostgreSQL Driver
    1. name: pragypsych
-- --

Hello World
-----------

1. Create File: devtest.HelloController
    ```java
    package com.psych.game.devtest;

    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    @RequestMapping("/dev-test")
    public class HelloController {
        @GetMapping("/")
        public String hello() {
            return "Hello, World!";
        }
    }
    ```
1. Try Build & Run
    - Build succeeds
    - Run fails: Because No DB
1. Run postgres
    ```bash
    psql postgres
    \du                  # display users
    \list                # list databases
    create database psych_local;
    \connect psych_local # connect to specific DB
    \dt                  # display tables in current DB
    # psql postgres -U pragyagarwal
    ```
1. Add psych_local DB to IntelliJ
1. Create application.properties
    ```java
    spring.datasource.url=jdbc:postgresql://localhost:5432/psych_local
    spring.jpa.hibernate.ddl-auto=update

    ```
1. Run again. Go to http://localhost:8080/dev-test/

-- --

Deploy on Heroku
----------------

1. Create new project.
    ```bash
    heroku create pragy-psych
    ```
1. goto https://pragy-psych.herokuapp.com/ to find nothing
1. add git
    ```bash
    git init
    git add .
    git commit -m "Init"
    ```
1. add heroku remote
    ```bash
    git remote add heroku https://git.heroku.com/pragy-psych.git
    ```
1. Deploy
    ```bash
    git push heroku master
    ```
1. Error: Push Rejected - invalid target release: 11
1. Create **system.properties**
    ```java
    java.runtime.version=11
    ```
1. Add, commit & deploy
1. Goto https://pragy-psych.herokuapp.com/dev-test/
1. Goto https://dashboard.heroku.com/apps/pragy-psych to see your stuff
1. Note: it auto adds postgres free account
1. See the logs
    ```bash
    heroku logs --tail
    ```
    
-- --

Make the models
---------------


-- --

Test
----

https://pragy-psych.herokuapp.com/dev-test/
https://pragy-psych.herokuapp.com/dev-test/questions
https://pragy-psych.herokuapp.com/dev-test/populate


-- --

Post Lecture
------------

Restore

[Google Docs – create and edit documents online, for free.](https://docs.google.com/document/d/1J1t-TFA-aw9ZS89LI4guAJ-muJeGTQ_BQB6Fan-zrk4/edit#)
[YouTube](https://www.youtube.com/watch?v=8cSYhtKzlhE)
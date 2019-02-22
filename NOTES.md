# Notes

## Handy resources

- [Django multiple settings](https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html)
- [Django calendar tutorial](https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html)
- [Git branches](https://confluence.atlassian.com/bitbucket/branching-a-repository-223217999.html)

## Summary

## UX Design

- Typography: 
    - Raleway & Roboto Slab
    - Open Sans & Open Sans condensed
    - Fjalla One & Noto Sans
- CSS Grid & Sass

## Database 

For both development and production will be using Postgress

- DB: Postgresql

## Components
A brief overview of the components. Explanation of what they should do.

### Users component
This project will have multiple types of users but I have yet to determine how to define their roles and to what degree. Atleast it will have an admin and client user. But the client itself is not the model that will be used as an "user" type, but instead as the base model. The admin is **Degree Synergy** itself.

### Events component

The events app is the component that will manage events inside the calendar of this project. The abilities are listed below:

- Show current projects.
- Add/retrieve/update/delete project
- Share selected event?

Adding events will be done by a form on the web app.

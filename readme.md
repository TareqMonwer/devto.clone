# How to run the project:
1. Clone/Download the project.
2. Go to the the project folder where manage.py is located.
3. create and activate virtual environment.
4. run this command in terminal: `pip install -r requirements.txt`
5. the above command will install all packages required to run the project.
6. run `python manage.py migrate`
7. run `python manage.py runserver`
8. go to `http://127.0.0.1:8000/`

## Features:
+ Login/Registration - Completed
+ User Profile - Completed
+ Publishing/Managing Articles - Partial
+ Articles Feed - Partial
+ Save article to read later
+ Filtering for (Weekly, Monthly, Latest) Articles.

### Addon Features: 
+ Social authentication
+ Password reset/change
+ Joining Email Sending
+ Commenting
+ Reaction on Articles
+ Popular Tags
+ Manage Badges for users


### URLS:
+ /login :login page
+ /registration :registration page
+ /users/username :user profile

+ / :Articles feed
+ /top/week :Top articles of the week
+ /top/month :Top articles of the month
+ /latest :Latest top articles
+ /some-article-slug :Article detail page



## Further Study Materials:
+ PEP-8
+ https://rsinger86.github.io/django-lifecycle/
+ https://github.com/wsvincent/awesome-django/
+ https://django-crispy-forms.readthedocs.io/
+ https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html
+ DJANGO ADMIN CUSTOMIZATION: https://books.agiliq.com/projects/django-admin-cookbook/en/latest/


# next:
show user profile in card | done
article detail page | done
update article publishing system
update tagging system
update user profile to manage articles

# next: <Date: 28th Sep 2021>
+ Social authentication
+ Password reset/change
+ Joining Email Sending

# next: <Date: 1st Oct 2021>
+ Commenting
+ Reaction on Articles
+ Popular Tags
+ Manage Badges for users
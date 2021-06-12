Hey, let's build a simple news board API.

We will start with a simple MVP. It will have a list of news with functionality to upvote and comment on them. Similar platform to [HackerNews](https://news.ycombinator.com/).

## **Functional Requirements**

- Create CRUD API to manage news posts. The post will have the next fields: title, link, creation date, amount of upvotes, author-name : done
- Posts should have CRUD API to manage comments on them. The comment will have the next fields: author-name, content, creation date : done 
- There should be an endpoint to upvote the post : done
- We should have a recurring job running once a day to reset post upvotes count : done

## **Technical Requirements**

- Code should be written with Python 3 : done
- REST API should be Django and Django REST Framework based : done
- API should be well documented with Postman collection. Make sure to use [Postman environments and variables](https://learning.postman.com/docs/postman/variables-and-environments/variables/#understanding-variables-and-environments), so you can switch between local API and deployed version. Add Postman collection link to the README
- API has to run as a Docker container. API + Postgres should be launched with docker-compose
- Code should be formatted with [Black](https://github.com/psf/black)
- Necessary to make sure that Flake8 linter passes. Would be great to have typing with [pyright](https://github.com/microsoft/pyright) as well
- The project should have clear README with steps to run it
- The code should be clean, passing linter checks and simple to understand. Code quality matters a lot
- Deploy API for testing to [Heroku](https://www.heroku.com/) or [DevSpace](https://devspace.cloud/). Add deployment link to the README

## **Conditions**

- Task usually takes **from 4 to 6 hours**. If you need more time, you're good to take it and it's appreciated, but results should be sent **no later than 48 hours after the start**
- Skills to write clean business logic and apply best practices are important
- The challenge code should be pushed to the **GitHub** repository. Please send us a link to the repository right after that. Thanks!

If you have any questions about challenge details, ask for more information, it's appreciated.

Have a good luck and looking forward to work with you!


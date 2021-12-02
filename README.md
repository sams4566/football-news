# Premier League News

The Premier League News site allows users to easily interact with up to date news regarding transfers, players and results within the English Premier League. The site enables users to post articles which can either be opinion posts or up to date news articles alongside sharing their thoughts on these articles through commenting and voting - similar to the social media site, Reddit, with upvoting and downvoting. The target audience are those who are interested in learning more about the English Premier League alongside what is currently trending. 

![Am I Responsive Mockup](https://github.com/sams4566/)

## User stories

### Epics

Below are three of the epics I had throughout the project:

#### Epic 1: Create articles
  - User Story 1: Create article 
    - Task 1: Create Article model in model.py
    - Task 2: Add function for add article
    - Task 3: Add html for add article page
  - User Story 2: View list of articles 
    - Task 1: Create a list of the articles and iterate them through on a html page
    - Task 2: Create create a 'Home' page that has the list of articles displayed
  - User Story 2 - Open individual article 
    - Task 1: Create function that selects an individual article and displays all the information stored in the data model
    - Task 2: Edit html to ensure the information is displayed in the correct place

#### Epic 2: Create Categories
  - User Story 1: Change category 
    - Task 1: Create category data model and link it to the article data model
    - Task 2: Create form to allow the user to submit a new category
  - User Story 2: Edit and delete categories 
    - Task 1: Create function for editing the category which prepopulates the existing data
    - Task 2: Create delete categories function

#### Epic 3: Create Comment
  - User Story 1: Comment on an article 
    - Task 1: Create comment data model that is linked to the article data model
    - Task 2: Create a form that allows users to comment on an individual article
  - User Story 2: Modify and display comments
    - Task 1: Add to the view article function an iteration that displays existing comments 
    - Task 2: Create function that allows users to delete their comments

### Story points
- Below is a diagram that shows the user stories for the projects timebox and breaks down the number of story points allocated to each:

![Story points](https://github.com/sams4566/)

- The user stories were also documented throughout the project using the 'Issues' tab in the github repository. Below is a screenshot of the table used:

![User Stories Table](https://github.com/sams4566/)

## Data Model
### Schema
  - The below database diagram shows the breakdown of my database which helped me to work out the layout of the site and how to structure my python functions.
  - The flow from category to article to comment meant that the functions I created had a logical flow alongside making it easier for those trying to decipher the code.
  - For the production database I used ‘postgres’ on Heroku and for the local database I used ‘sqlite3’.

![Schema](https://github.com/sams4566/)

### Site layout
- __Theme__

  - To work out the layout of the site I researched lots of different bootstraps themes and looked at many news and blog websites such as BBC News and Reddit.
  - I decided on the ‘Blog Home’ theme (image below) from Start Bootstraps as it had good proportions and limited the complexity of the site. 
  - I decided to have a contrast of black and white throughout the site as this highlights the colour in the images and buttons along with making the site easier to read.

![Theme](https://github.com/sams4566/)

- __Icons__
  - I used font awesome for some of the icons as they appear as text rather than an image which limits the icon from being altered at different screen sizes

- __Text field__
  - I used the summernote API to allow users to add in any content they like to their articles including pictures and videos. Summernote also gives users control of the spacing and layout compared with the original django provided text content box.

- __Images__
  - Images were stored on the Cloudinary API to allow the images to be saved and loaded quickly when required by the site.

## Features
- __Header__
  - Both the header and footer are styled to allow users to easily navigate the site and are stuck at the top and bottom of each page.
  - The header forms a dropdown menu at lower screen sizes to allow users to stop the options from being bunched up.
  - The header and footer are the same in all pages as they are part of the base.html file.

![Header](https://github.com/sams4566/)

- __Authentication__

  - Users will be able to sign-up, sign-in, and sign-out using the below screens. 
  - Users will have to sign in to add, edit, and delete categories and articles alongside adding and deleting comments.
  - I used the built in django.allauth package to retrieve the functionality to allow users to be created.

![Authentication](https://github.com/sams4566/)

- __List of articles pages__
  - Both the home page and the category articles page are both formatted in the same way with the only difference being the ordering of the articles. The home page is filtered with the most popular articles from all the categories at the top and the category articles page has the most recent articles for that category at the top.
  - Users can see the articles they have voted on due to the up and down buttons being highlighted green and red respectively.
  - The main image is present as a teaser to the article along with the headline and a short summary about the content. 
  - If more than six articles are on display the page is paginated that allows users to go back and forth between lists of articles.

![List of articles pages](https://github.com/sams4566/)

- __Categories__
  - If the user is logged in they have the option of adding, editing and deleting the categories they have created. 
  - If more than six categories are created a ‘More Categories’ button appears to allow the user to see the other categories.
  - They can go into each individual category to see a list of articles assigned to that category.

![Categories](https://github.com/sams4566/)

- __Article__
  - Each article has the main image in the center with the headline, date of publish and category badge at the top.
  - The user has the option of voting positively or negatively on the article and alongside leaving a comment.
  - The total number of comments and the net number of upvotes minus downvotes are indicated above the comments section to let user know the popularity of the article.
  - User’s can load more comments by clicking the ‘More comments’ button when there are more than four comments.
  - The user who created the article also has the option to edit and delete the article from within this page.

![Article](https://github.com/sams4566/)

- __Adding and editing Articles__
  - If a user is logged in they have the option of adding an article to a specific category. 
  - Through using the summernote API the user can add videos and photos to the body of their article. 
  - Once the article is submitted, a message will appear telling the user that their article is awaiting approval. This allows the content to be monitored by an administrator.
  - If an image is not selected a default image of the Premier League Lion is used.
  - The article is also not published until a unique headline is selected. An error message will display if the headline has been used.
  - If the user edits the page after it has been approved the page is prepopulated with the information they had entered previously making it easy for the user to make quick changes.

![Adding and editing Articles](https://github.com/sams4566/)

- __Approving articles and categories__
  - When a new article or category has been submitted an admin will have the ability to approve submissions through the built in django screen below.
  - They can also edit or delete the articles or categories if necessary at any point.

![Approving articles and categories](https://github.com/sams4566/)

### Future features
  - Add options for the list of article views so users can choose between the most popular articles and the most recent.
  - Add name tags to articles and comments so that users can click on other users profiles to see their articles.
  - Allow articles to be part of more than one category.
  - Add votes to comments and list the most popular comments at the top of the comment section.

## Technologies used

### Languages
  - **HTML** - I used html to create the content and main layout of each page
  - **CSS** - CSS was used to style the html elements and make the site more appealing to users. It was also used to allow the website to respond to different screen sizes.
  - **JavaScript** - I used JavaScript to enhance some of the front end functionality.
  - **Python** - I used python as the main back end language. It was used to write all of the different functions that occur when requested by the user.

### Extensions
  - **Django** - The site was built using the Django full-stack framework where I used many of the built in shortcuts and variables to create the websites backend. Out of the django extensions I used both AllAuth and Coverage. AllAuth was used to confirm authentication with users on the site and Coverage was used to find out how much of the back end code I had automatically tested.
  - **Summernote** - I used the summernote API to allow users to insert customised content,  including pictures and videos, to their articles. 
  - **Cloudinary** - Cloudinary was chosen to allow users to have their images saved once uploaded as the Heroku platform deletes photos around 24 hours after upload. The admin can also login to cloudinary and see a list of all of the photos uploaded.
  - **Bootstraps** - I used bootstraps to allow the site to be structured and built quickly. 
  - **jQuery** - jQuery was chosen to allow the javascript code to be implemented easily.
  - **Postgres** - I used Postgres as the database for the Heroku deployed website as it is well integrated with Heroku.

## Testing
 
### Bugs

#### Bug 1
  - Both my css and javascript were not appearing on Heroku when it was deployed and the below error message was appearing in the console:

`Refused to apply style from 'https://premier-league-news1.herokuapp.com/static/css/style.css' because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.`

  - The bug was resolved by setting Debug to False and for adding {% static %} tags to the css and javascript links in my html.

#### Bug 2
  - The footer wasn’t sticking to the bottom of the page which was impacting on the user experience. To fix this I created a new class for the footer and added `bottom: 0` and `position: absolute`.

#### Bug 3
  - Summernote was adding in all the html tags to my article content when I tried to edit the article. This was resolved by adding `| safe` to the javascript function.


### Automated Testing

The site was tested using the built-in django ‘TestCase’ library in the tests.py file. I ran 8 tests to test the sites basic functionality including testing:
  - Information was successfully entered in the data model 
  - Form data couldn’t be left empty
  - Categories could be added, edited and deleted

To run the tests you can type: `python3 manage.py test`

The coverage report for how much of the code I’ve covered with tests is below:

![Coverage](https://github.com/sams4566/)

### Manual Testing

I tested the site on several occasions throughout its development to make sure the urls were working correctly and that information was being submitted. I tested the site on several different browsers such as Google Chrome, Safari and Mozilla Firefox and between a width of 320px to 2000px the site is easily readable on all devices.

Below is a list of some of the key tests I completed before submitting the project: 
  - Check articles and categories could be both added, edited and deleted correctly and without errors. 
  - Ensure users that aren’t logged in cannot edit, add or delete any of the information - including accessing the administration page.
  - Make sure both the upvote and downvote buttons work on all pages. 
  - Check that pagination works correctly on all pages. 
  - Make sure comments are appearing correctly alongside a ‘More Comments’ button that allows users to see more comments.
  - Ensure admin users can approve Articles and Categories
  - Ensure users can easily login and logout without errors.
  - Check messages appear below the nav bar such as letting the user know their article is awaiting approval.

### User testing
For user testing I asked a friend to complete simple tasks such as adding and editing an article alongside going in and out of different pages of the site. This helped me realise that the layout of the ‘Add Article’ section had to be reshaped to make it more user friendly.

### Security

 - **Authentication** - I used Django’s AllAuth package to ensure users have to login to make edits to the site. I have also made sure that users can only edit their own articles and categories.

 - **Environment Variables** - I stored private information in the env.py file which was then added into the .gitignore file. This meant that any information in the env.py file was not committed to the repository.

 - **Debug** - When the site is in production on Heroku debug is set to `False` ensuring the user doesn’t get information about why certain urls aren’t working.

### Validators

  - HTML
    - No errors were returned when passing through the official W3C Validator
  - CSS
    - No errors were found when passing through the official (Jigsaw) Validator
  - JavaScript
    - No significant issues were found when passing through the JSHint JavaScript Validator
  - Python
    - No errors were returned when passing through PEP8 Online
  - Accessibility
    - The web page was tested through Lighthouse in Google Chrome’s developer tools and confirmed a high level of accessibility

![Accessibility](https://github.com/sams4566/)

## Deployment

### Cloning the repository

  - Navigate to the main page of this repository.
  - Click on the ‘Code’ dropdown menu to the left of the green ‘Gitpod’ button.
  - Copy the HTTPS url and then open your own workspace.
  - Go to the terminal of your new workspace and type `git clone` + 'copied url'. 
  - You will then need to create a env.py file and add a SECRET_KEY and your CLOUDINARY_URL in the below format.

    `import os`

    `os.environ["CLOUDINARY_URL"] = "Enter CLOUDINARY_URL”`

    `os.environ["SECRET_KEY"] = "Enter SECRET_KEY"`

  - You will also have to add the env.py file to a .gitignore file that will stop the information from being committed.
  - To install all of the required modules use `pip3 install -r requirements.txt` in the terminal. 
  - Finally, you will have to add `DEVELOPMENT = True` to your workspace variables. Alternatively you can remove `development` from settings.py and set `DEBUG = True` making sure the database is set to sqlite3.
  - Type `python3 manage.py runserver` to run the site.

### Deployment to Heroku

  - Create a Heroku app by firstly logging in through the terminal by using - `heroku login -i`
  - Create an app by using the command `heroku apps:create <appname> --region eu` in the terminal
  - Login to Heroku’s official site and go to the Resources section of your app and add 'Heroku Postgres' to the Add-ons section. 
  - Go to the Settings folder in Heroku’s website and add in the CLOUDINARY_URL, SECRET_KEY and HEROKU_HOSTNAME to the config vars. 
  - Add the DATABASE_URL and HEROKU_HOSTNAME config vars to your settings.py file (Check the setting.py file in this repository to find where they go).
  - Add the DATABASE_URL config var to your env.py file in the below format:

    `import os`

    `os.environ["DATABASE_URL"] = "Enter DATABASE_URL”`

  - Create a Procfile in the root directory and add `web: gunicorn <appname>.wsgi:application` to it. 
  - Add a requirements.txt file by typing `pip3 freeze --local > requirements.txt` in the terminal.
  - Go to your Heroku app on Heroku’s website and navigate to the ‘Deploy’ section. Click on ‘Github’ in the Deployment Section and add your github username and your repository name.
  - Click ‘Deploy Branch’ at the bottom of the deployment section. This will connect Heroku to your workspace.
  - Migrate the changes to the new Postgres database by typing `python3 manage.py migrate` in the terminal in your workspace and then commit all your changes.
  - Lastly, click ‘Deploy Branch’ at the bottom of the deployment section again on the Heroku website. You will now be able to visit your site.


## Credits

### Content/Tutorials
  - [The Django Documentation](https://docs.djangoproject.com/en/3.2/)
  - [PHP Documentation](https://www.php.net/manual/en/function.date.php) - How to change the date format
  - Bootstraps Themes - [Blog Home](https://startbootstrap.com/template/blog-home) and [Blog Post](https://startbootstrap.com/template/blog-post)
  - [Cloudinary Documentation](https://cloudinary.com/documentation/django_image_and_video_upload) - How to install Cloudinary
  - [Summernote Documentation](https://summernote.org/getting-started/#installation) - How to install Summernote

### Media
  - [Sky Sports](https://www.skysports.com/premier-league-news) - for article pictures and content
  - [Premier League Team Badges Background Photo](https://resources.evertonfc.com/photo-resources/2021/06/16/c7e13cc8-6c06-423c-af4b-560c751d2ad9/MSOC-0044-Fixture-Release-Graphics_16.9-FULL-SEASON-CRESTS-_neww.jpg?width=1600&height=900)
  - [Premier League Lion Image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.premierleague.com%2Fnews%2F942495&psig=AOvVaw11JUtw0rHz-7ZRYEqwLB1e&ust=1638476870804000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCOimzZG4w_QCFQAAAAAdAAAAABAD)


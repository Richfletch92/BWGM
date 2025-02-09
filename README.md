# Binge-Watchers

![Responsive Image](readme\images\responsive.png)

## Table of Contents
- [Overview](#overview)
- [UX Design Process](#ux-design-process)
  - [Link to User Stories in GitHub Projects](#link-to-user-stories-in-github-projects)
  - [Wireframes](#wireframes)
  - [Design Rationale](#design-rationale)
  - [Reasoning For Any Final Changes](#reasoning-for-any-final-changes)
- [Key Features](#key-features)
- [Deployment](#deployment)
- [AI Implementation and Orchestration](#ai-implementation-and-orchestration)
  - [Use Cases and Reflections](#use-cases-and-reflections)
- [Testing Summary](#testing-summary)
- [Future Enhancements](#future-enhancements)

## Overview
Binge-Watchers is your ultimate destination for movie and TV series reviews, ratings, and recommendations. The platform allows users to explore detailed information about movies and TV series, submit reviews, and apply filters to find content that matches their preferences.

## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [GitHub Projects Kanban Board](https://github.com/users/Richfletch92/projects/9)
  - I've also added my user stories to a separate [document](readme\userstories.md).
- **Wireframes:**
  - [Wireframes](readme\wireframes.md) - Here are my intial designs for the website. I had orignally planned to create another page for each individual season however due to time constrants I ran out of time so I've added that to my future plans. 
  - The design focuses on usability and accessibility for all users, including those using assistive technologies.
- **Design Rationale:**
  - Key design decisions include a clean layout, a consistent colour scheme, and typography that adheres to accessibility guidelines (e.g., WCAG).
  - Considerations for users with disabilities include screen reader support and keyboard navigation.
  **Design Changes**
  - Although I have followed my designs quite closely some changes have been made due to user feedback and techinical issues. I had to move away from having the login and registration pages on modals due to having issues getitng the forms to work. I plan to implement this in the future. 

## Key Features
- **Movie and TV Series Details:**
  - Fetches detailed information from the TMDb API, including images, release dates, runtime, and overviews.
  - Displays a brief overview of each movie and TV series to help users understand the premise.

- **User Reviews:**
  - Allows users to submit, edit, and delete reviews for movies and TV series.
  - Users can rate movies and TV series on a scale of 1 to 10.
  - Displays user reviews prominently on the movie and TV series pages.

- **Filtering Options:**
  - Users can filter content based on genre, release year, and rating.
  - Filtering options are available on both the movies and TV series pages.
  - Filters can be combined to narrow down results further.
  - Includes a "Clear Filters" button to reset all applied filters.

- **Search Functionality:**
  - Provides a search bar on the homepage and other relevant pages.
  - Users can search for movies and TV series by title or genre.
  - Each search result includes relevant details such as title, image, and brief description.

- **Responsive Design:**
  - The website layout is fully responsive and adapts to different screen sizes.
  - Ensures a consistent and user-friendly experience across desktop, tablet, and mobile devices.

- **Accessibility:**
  - Designed with accessibility in mind, adhering to WCAG guidelines.
  - Includes features such as screen reader support, keyboard navigation, and high contrast options.
  - Ensures that all interactive elements are accessible to users with disabilities.

- **Social Media Integration:**
  - Includes social media links in the footer for easy access to the project's social media pages.

- **User Authentication:**
  - Provides user registration and login functionality.
  - Supports social media login options for quick and easy access.
  - Ensures secure handling of user data with proper validation and error handling.
  - Users can reset their password via email. 

- **Admin Panel:**
  - Includes an admin panel for managing movies, TV series, and user reviews.
  - Allows administrators to approve or reject user reviews.
  - Provides tools for managing user accounts and site content.

- **Deployment and Hosting:**
  - Deployed on Heroku with environment variables for secure configuration.
  - Ensures that the deployed version matches the development version in functionality.
  - Includes steps for verifying and validating the deployed version.

- **Inclusivity Notes:**
  - Features are designed to address the needs of diverse users, including those with SEND.
  - Ensures that the platform is inclusive and accessible to all users.

## Deployment
- **Platform:** Heroku
- **High-Level Deployment Steps:** 
  1. Clone the repository and open in your IDE
  2. Create env.py and .env files
  3. Add the following variables to env.py
    - SECRET_KEY
    - DEBUG
    - ALLOWED_HOSTS (ensure you add your local address and .herokuapp.com)
    - DATABASE_URL
    - EMAIL_HOST_USER
    - EMAIL_HOST_PASSWORD
  4. Add the following variables to .env
    - TMDB_API_KEY
    - TMDB_BASE_URL
  5. Create a venv and run the following commands
    - pip install -r requirements.txt
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py fetch_data
    - python manage.py collectstatic
    - git add, commit and push
  6. Open Heroku and create a new app
  7. Connect your GitHub project to the app. 
  8. Click on settings and reveal config vars. Then enter all hidden variables from your env.py
  9. You can now deploy your project. 

- **Verification and Validation:**
  - Steps taken to verify the deployed version include functionality checks and accessibility tests.
  - Use of [Lighthouse](https://github.com/GoogleChrome/lighthouse) to check performance and accessibility. Accessibility is excellent scoring 100 on every page. Performance could have been better on mobile. Main issues with performance were due to the images gotten from TMDb API. [Results](readme\lighthouse.md)
  - [W3C HTML Validator](https://validator.w3.org/) used to validate HTML. All results passed apart from my registration page which unfortunately was out of my control due to AllAuth's forms having issues [Results](readme\html.md)
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) used to validate CSS [Results](readme\css.md)
  - [JSHint JavaScript Validator](https://jshint.com/) used to validate JS [Results](readme\js.md)
  - [CI Python Linter Validator](https://pep8ci.herokuapp.com/) used to validate Python [Results](readme\python.md)
- **Security Measures:**
  - Use of environment variables for sensitive data.
  - Ensured DEBUG mode is disabled in production.

## AI Implementation and Orchestration

### Use Cases and Reflections:

  - **Code Creation:** 
    - Reflection: I used Co-pilot through the majority of my project by using inline editing and chat. I had a lot of problems with Co-pilot consistently trying to override code that wasn't needed. I also had issues with the code being overly complex or not doing what I'd asked it to help create. I actually found ChatGPT to be more helpful in a lot of instances where Co-pilot was failing. I used a mix of question-and-answer prompts and multi-step prompts when getting AI to assist in my code creation. Sometimes Co-pilot would need further info as the original prompts wouldn't create what I'd asked it to do. 

    - Examples: When creating my fetch_data and utils I started using Co-pilot however I couldn't get Co-pilot to write the code effectively and get it to work. When asking ChatGPT to write the same functions the code worked straight away with little to no editing required had I used ChatGPT straight away I would have saved myself some considerable time.
    
  - **Debugging:** 
    - Reflection: Co-pilot was excellent for spotting smaller bugs and helped identify an issue causing overflow on the right-hand side of my screen. Whilst Co-pilot couldn't actually identify the issue itself it recommended adding a wildcard selector which added a border to each element. This allowed me to identify that my footer was overflowing. I did have a few issues with Co-pilot actually delaying me with some debugging. When I was trying to implement users being able to edit their reviews I was having an issue with the review form not prefilling. It was due to my JavaScript file not being correctly linked to the HTML file. There was a small typo in the file name set as script.js and not scripts.js. Co-pilot advised some real extensive and over-the-top fixes but didn't advise once about the potential typo. I wasted a good 2-3 hours trying with Co-pilot to fix the issue. My big takeaway from using AI is that I've been relying too heavily on using Co-pilot where manual testing can be a lot more time effective.

  - **Performance and UX Optimisation:** 
    - Reflection: Although I came up with the main design for the website, it was handy to get Co-pilot to create a lot of the forms using my original designs as templates to save time. I would prompt Co-pilot to use the design of my current form to use it as a template to design the other forms.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, AI not always detecting what is causing the underlying issues and some AI not always being effective as others. 
  - As I stated above, I think AI can be very effective however it's not always the most reliable and can have negative impacts if relied on too heavily. I found that manual testing can sometimes be more time effective than asking AI to fix your code. 

## Testing Summary
- **Manual Testing:**
  - **Overview:** Testing was continuously done during developement, AI was used to check through code consistently to spot any typos and missing closing elements. 
  - **Devices and Browsers Tested:** Tested on various devices Android and Apple devices. I had friends and family who tested on a variety of mobile devices and computers. Browsers used was Chrome, Edge and Safari. I also tested using dev tools to resize the screen to ensure my website was responsive.
  - **Features Tested:** CRUD operations, navigation, filtering, review submission, user registration and password resetting.
  - **Results:** All critical features worked as expected, including accessibility checks. 

## Future Enhancements
- Enhance the filtering options to include more criteria.
- Improve the design and layout based on user feedback.
- Add season pages and episode information (models have been added for this functionality already and is reflected in my ERDs)
- Give users the ability to add comments to reviews (models have been added for this functionality already and is reflected in my ERDs)
- Add further functionality to reviews by giving options to like/dislike reviews (models have been added for this functionality already and is reflected in my ERDs)
- Allow users to add movies/series and pull relevant information using API 
- Add ability to login using social media
- Move the registration and login/logout pages into a modal
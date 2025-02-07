# Binge-Watchers

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
  - [GitHub Projects Kanban Board](https://github.com/Richfletch92/BWGM/projects)
  - Userstories 
- **Wireframes:**
  - [Wireframes](https://github.com/Richfletch92/BWGM/wireframes) - Accessible wireframes with high colour contrast and alt text for visual elements.
  - The design focuses on usability and accessibility for all users, including those using assistive technologies.
- **Design Rationale:**
  - Key design decisions include a clean layout, a consistent colour scheme, and typography that adheres to accessibility guidelines (e.g., WCAG).
  - Considerations for users with disabilities include screen reader support and keyboard navigation.
- **Reasoning For Any Final Changes:**
  - Significant changes were made to enhance inclusivity and accessibility, such as improving contrast and ensuring all interactive elements are keyboard accessible.

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
  1. Set up the Heroku app and configure environment variables.
  2. Deploy the application using Git.
  3. Verify the deployed version matches the development version in functionality.
- **Verification and Validation:**
  - Steps taken to verify the deployed version include functionality checks and accessibility tests.
- **Security Measures:**
  - Use of environment variables for sensitive data.
  - Ensured DEBUG mode is disabled in production.

## AI Implementation and Orchestration

### Use Cases and Reflections:
(Highlight how prompts, such as reverse, question-and-answer or multi-step, were used to support learners with SEND or ALN where relevant.)

  - **Code Creation:** 
    - Reflection: Strategic use of AI allowed for rapid prototyping, with minor adjustments for alignment with project goals. 
    - Examples: Reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.
  - **Debugging:** 
    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.
  - **Performance and UX Optimization:** 
    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.
  - **Automated Unit Testing: (If undertaken)**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** Tested on various devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers and keyboard-only navigation.
  - **Features Tested:** CRUD operations, navigation, filtering, and review submission.
  - **Results:** All critical features worked as expected, including accessibility checks.
- **Automated Testing: (If undertaken)**
  - Tools Used: Django TestCase
  - Features Covered: Review submission, filtering functionality, and user authentication.
  - Adjustments Made: Manual corrections to AI-generated test cases, particularly for accessibility.

## Future Enhancements
- Enhance the filtering options to include more criteria.
- Improve the design and layout based on user feedback.
- Add season pages and episode information (models have been added for this functionality already and is reflected in my ERDs)
- Give users the ability to add comments to reviews (models have been added for this functionality already and is reflected in my ERDs)
- Add further functionality to reviews by giving options to like/dislike reviews (models have been added for this functionality already and is reflected in my ERDs)
- Allow users to add movies/series and pull relevenat information using API 
- Add ability to login using social media 
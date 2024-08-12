# Art Store
The Art Store is an online platform designed to sell high-quality, original paintings and provide mural services by talented artists. This document outlines the e-commerce business model for the Art Store, focusing on the B2C (Business-to-Consumer) segment. The application aims to connect individual art buyers and collectors with unique, hand-crafted art pieces and custom murals, enhancing both residential and commercial spaces.

[**Live Version**](https://art-store-bdbdae133a85.herokuapp.com/)

[**Repository GitHub Repo**](https://github.com/KaltrinaBM/art_store)


![home](/media/home.png)


## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Usage Instructions](#usage-instructions)
4. [User Stories](#user-stories)
5. [Technologies Used](#technologies-used)
6. [Design and Architecture](#design-and-architecture)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Overview

The Art Store Project is a Django-based web application where collectors and art lovers can purchase exquisite paintings and commission custom murals. It curates a selection of high-quality artwork and offer a streamlined service for mural installations, ensuring that our customers receive exceptional pieces and personalized service.

The application uses Bootstrap for styling and Django's built-in authentication system for user management.

## Features
- User authentication (sign up, sign in, sign out, recover password)
- CRUD (create, read, update, delete) operations for reviews on each painting, service
- Reading Blog posts posted by Site Owners
- Responsive design using Bootstrap
- Contact form for user inquiries

## Business Model

### Business Focus
- **Model:** B2C (Business-to-Consumer)
- **Purpose:** Provide a curated marketplace for purchasing expensive, original paintings and commissioning custom murals.

### Marketing Strategies
- **Digital Marketing:** Utilize social media platforms (Instagram, Pinterest, Facebook) for showcasing artwork and attracting customers. Implement SEO strategies for better visibility on search engines.
- **Email Marketing:** Develop a newsletter to inform customers about new arrivals, exclusive offers, and artist features.
- **Influencer Partnerships:** Collaborate with art influencers and bloggers to expand reach.
- **Content Marketing:** Publish blogs on art trends, artist interviews, and design tips to position the store as an industry leader.

### Features
- **Search and Filter:** Advanced search options to filter artworks by name and price.
- **User Reviews and Ratings:** Allow customers to leave feedback and ratings.
- **Secure Payment:** Integration with Stripe for safe transactions.
- **Personalized Recommendations:** AI-driven suggestions for relevant artworks.
- **Customer Support:** Multiple support channels for user assistance.

## Content Strategy

### Clarity and Understanding
- **Visual Appeal:** High-resolution images of artworks with zoom features.
- **Detailed Descriptions:** Information on the story behind each piece and artist.
- **User-Friendly Layout:** Clear navigation and design focusing on artwork presentation.

### Expertise, Authoritativeness, and Trustworthiness (E-A-T)
- **Artist Profiles:** Detailed backgrounds and achievements of artists.
- **Content Creation:** Regular blog posts on art-related topics to engage and inform.
- **Customer Testimonials:** Display reviews from satisfied customers.
- **Secure Transactions:** Emphasize security measures for protecting customer data.

## Enhancing User Experience

### Discoverability
- **AI Recommendations:** Implement algorithms to suggest artworks based on user behavior.
- **Related Products:** Show related items on product pages to encourage exploration.




![Contact Us](/static/images/contactform.PNG)

## Usage Instructions
To use the Art Store web application, follow these steps:

1. **Sign Up**: Create an account to add reviews, please orders, check order history, etc.
2. **Sign In**: Log in to access additional features like reading blog posts and leaving reviews.
5. **Place orders**: Place orders and secure payments. Registering is not required to place an order.
3. **Reviews for each painting**: Signed-in users can add reviews.
4. **Admin Panel**: Access the [admin panel](https://art-store-bdbdae133a85.herokuapp.com/admin/) with your superuser credentials to manage the site.
5. **Blog with articles posted by admins**: Use the contact form to send messages to the team. A valid email is required, but signing in is not.
6. **Contact Form**: Use the contact form to send messages to the team. A valid email is required, but signing in is not.

## User Stories
These user stories guided the development of this project:

 

- **Buy the product** - As a Registered User I can add the product to basked so I can make the order
- **Searched list** - As a Registered User I can easy view the list of searched items so I can easy find the product I was looking for
- **Personalized user profile** - As a Registered User I can view my order history and confirmation and save payment information
- **Easy Navigation** - As a Site User, I want to be able to easily navigate through the app, so that I can find the content.
- **Recover password** = As a Registered User I can recover the password in case I forgot it
- **Read Contact Us messages** - As a Site Owner I can read messages received
- **Contact Us** - As a Site User I can use the Contact Us form
- **Delete a review** - As a Regular User, I want to be able to delete a review
- **Update a review** - As a Regular User, I want to be able to update a review
- **Post a review** - As a Regular User, I want to be able to post a review
- **Blogn** - As a registered User, I want to be able to login
- **Sign In** - As a registered User, I want to be able to login
- **Register** - As a first time User, I want to open an account for more features


## Technologies Used

### Languages Used
- Python 3.7+
- HTML
- CSS
- JavaScript

### Frameworks and Libraries
- **[Django](https://www.djangoproject.com/)**: A high-level Python framework used to build robust web applications.
- **[Bootstrap 5](https://getbootstrap.com/)**: A front-end framework for creating responsive and mobile-friendly websites.
- **[Font Awesome](https://fontawesome.com/)**: A collection of icons and social logos for visual elements.
- **[Google Fonts](https://fonts.google.com/)**: A collection of free fonts for web projects.
- **[Crispy Forms](https://django-crispy-forms.readthedocs.io/)**: A Django library for simplifying form handling and styling.
- **[Cloudinary](https://cloudinary.com/)**: A cloud-based platform for storing and managing images.
- **[jQuery](https://jquery.com/)**: A JavaScript library for manipulating the DOM and creating interactive features.
- **[Git](https://git-scm.com/)**: A distributed version control system for tracking code changes and collaborating with others.
- **[PostgreSQL](https://www.postgresql.org//)**: A cloud-based PostgreSQL database service from Code Institute.
- **[GitHub](https://github.com/)**: A platform for hosting code repositories and collaborating with other developers.
- **[Chrome DevTools](https://developer.chrome.com/docs/devtools/)**: A set of debugging and analysis tools integrated into Google Chrome.
- **[W3C HTML Validator](https://validator.w3.org/)**: A tool for validating HTML to ensure compliance with web standards.
- **[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)**: A service for validating CSS code for correctness.
- **[JSHint](https://jshint.com/)**: A JavaScript linting tool for detecting errors.
- **[PEP 8](https://peps.python.org/pep-0008/)**: The official style guide for Python, providing best practices for coding in Python.


## Design and Architecture

### Flowcharts

The following flowchart was created to illustrate the application's structure and functionality.

![Flowchart](/media/flowchart.jpg)

### Wireframes

The following wireframe was created to display a visual guide of the website.

![Wireframe](/media/wireframe.jpg)

### Entity-Relationship Diagram (ERD)

The following tables represents the attributes of the models, including the database key and validation information:

## Review Model Attributes

| Attribute       | Type                     | Description                                          | Validation                         |
|-----------------|--------------------------|------------------------------------------------------|------------------------------------|
| `id`            | AutoField (Primary Key)   | Automatically generated unique identifier for each review. | Unique, auto-incremented.          |
| `painting`      | ForeignKey (to `Painting`) | The painting associated with this review.             | Must reference a valid `Painting`. |
| `user`          | ForeignKey (to `User`)    | The user who submitted the review.                   | Must reference a valid `User`.     |
| `rating`        | PositiveIntegerField      | Rating given by the user.                            | Must be between 1 and 5 (inclusive).|
| `content`       | TextField                | The content of the review.                           | No specific validation.            |
| `created_at`    | DateTimeField(auto_now_add=True) | Timestamp indicating when the review was created.   | Automatically generated.           |
| `updated_at`    | DateTimeField(auto_now=True) | Timestamp indicating when the review was last updated. | Automatically updated.            |


## BlogPost Model Attributes

| Attribute       | Type                     | Description                                          | Validation                         |
|-----------------|--------------------------|------------------------------------------------------|------------------------------------|
| `id`            | AutoField (Primary Key)   | Automatically generated unique identifier for each blog post. | Unique, auto-incremented.          |
| `title`         | CharField(max_length=200) | The title of the blog post.                          | Maximum 200 characters.            |
| `content`       | TextField                | The main content of the blog post.                   | No specific validation.            |
| `excerpt`       | TextField (Optional)      | A short summary or excerpt of the blog post.         | No specific validation.            |
| `image`         | ImageField (Optional)     | An optional image associated with the blog post.     | Must be a valid image file, can be null/blank. |
| `author`        | ForeignKey (to `User`)    | The author of the blog post.                         | Must reference a valid `User`.     |
| `category`      | ForeignKey (to `Category`) | The category associated with the blog post.          | Can be null/blank, references a `Category`. |
| `tags`          | ManyToManyField (to `Tag`) | Tags associated with the blog post.                  | Can be null/blank, references multiple `Tags`. |
| `created_at`    | DateTimeField(auto_now_add=True) | Timestamp indicating when the blog post was created. | Automatically generated.           |
| `updated_at`    | DateTimeField(auto_now=True) | Timestamp indicating when the blog post was last updated. | Automatically updated.            |

## ContactMessage Model Attributes

| Attribute       | Type                     | Description                                           | Validation                       |
|-----------------|--------------------------|-------------------------------------------------------|----------------------------------|
| `id`            | AutoField (Primary Key)   | Automatically generated unique identifier for each contact message. | Unique, auto-incremented.        |
| `name`          | CharField(max_length=255) | The name of the person sending the message.           | Maximum 255 characters.          |
| `email`         | EmailField                | The email address of the person sending the message.  | Must be a valid email format.    |
| `subject`       | CharField(max_length=255) | The subject of the message.                           | Maximum 255 characters.          |
| `message`       | TextField                 | The content of the message.                           | No specific validation.          |
| `created_at`    | DateTimeField(auto_now_add=True) | Timestamp indicating when the message was created.    | Automatically generated.         |



## Testing

### Manual Testing
In addition to automated testing, I manually validated each page of the web application using the W3C Markup Validation Service to check for proper HTML structure, CI Python Linter and Flake8 to ensure compliance with coding standards.

During the validation process, a few small warnings were detected, but they were promptly fixed to ensure compliance with web standards and code quality. These warnings were mostly minor issues that didn't affect functionality, but addressing them helps maintain a cleaner codebase and improves the user experience.

[W3C Markup Validation Service]()
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
      

- **W3C Markup Validation**: Each page was tested by entering its URL into the W3C Markup Validation Service. The validation service checks for syntax errors, structural issues, and other potential problems in the HTML markup.
- ***Results***: All pages passed the validation with no errors detected, indicating that the HTML structure conforms to the W3C standards. This validation step helps ensure cross-browser compatibility and contributes to a consistent user experience.


[CI Python Linter](https://pep8ci.herokuapp.com/) 

- **CI Python Linter**: Used to check the Python code for syntax errors and code style violations.
- ***Results***:
- No errors or style violations were found in the code.
- The code was checked and returned with no issues detected.

**Performance Testing with Lighthouse**

To ensure optimal performance, accessibility, and best practices, I tested the web application using [Lighthouse](https://developers.google.com/web/tools/lighthouse), a tool provided by Google Chrome. 

- ***Results***
Below are the results from the Lighthouse tests:

![Lighthouse Homepage Test](/static/images/lighthouse.PNG)

These screenshots demonstrate the outcomes of the performance and accessibility evaluations, showcasing the measures taken to ensure the web application's quality and compliance.

### Automated Testing

Django provides built-in support for automated testing, allowing for unit tests and integration tests. Automated testing helps maintain code quality and quickly identify issues.

While conducting integration tests, a bug was discovered in the 'Contact Us' form. The term 'Contact Us' was mentioned on the button leading to the form, but not within the actual form itself. This inconsistency could have caused confusion for users trying to understand the purpose of the form. The issue was identified during integration testing and was subsequently fixed by adding a clear title inside the form indicating that it was for 'Contact Us' inquiries.

To run the automated tests, use the following command:
```bash
python manage.py test
```

![Automated Testing](/static/images/testing.PNG)

### Further Testing
The Website was tested on Google Chrome and Internet Explorer.
The website was viewed on a variety of devices such as Desktop, Laptop, Andorid phones.
A large amount of testing was done to ensure that all functions are working as intended.
Family members were asked to review and play the game to point out any bugs and/or user experience issues.

### Known Bugs

#### Footer Position Issue
In certain situations, such as after submitting the contact form or when signing out, the footer may appear in the middle of the page instead of at the bottom.
The cause is likely related to CSS or layout issues, possibly due to flexbox configurations or page content dynamics.
This issue doesn't affect functionality but may disrupt the visual consistency of the page layout. Due to limited time, this issue will not be fixed. 

## Deployment

### Heroku Deployment
To deploy this Django project to Heroku from its [GitHub repository](https://github.com/KaltrinaBM/music-blog), the following steps were taken:

1. **Create a Heroku Account**: Log into your Heroku account or create a new one at [Heroku](https://www.heroku.com/).
2. **Create a New App**:
   - Click **New** in the top-right corner of the dashboard.
   - Select **Create new app** from the drop-down menu.
   - Enter a unique name for your app and choose your region.
   - Click **Create App**.
3. **Configure Settings**:
   - Go to the **Settings** tab.
   - Scroll down to **Config Vars** and click **Reveal Config Vars**.
   - Add a new variable with `PORT` as the key and `8000` as the value.
   - Click **Add**.
   - Scroll down to **Buildpacks** and click **Add buildpack**.
   - Select 'Python' and then 'Node.js'. **Ensure 'Python' is on top** of the buildpack list. If not, drag it to the top and save.
4. **Deploy from GitHub**:
   - Return to the **Deploy** tab and select 'GitHub' as the deployment method.
   - Connect your GitHub account and authorize Heroku to access your repositories.
   - Search for your repository by name and click **Connect**.
   - Choose a deployment method:  
     - Click **Enable Automatic Deploys** to automatically deploy when you push to GitHub.
     - Select the desired branch and click **Deploy Branch** for manual deployment.
5. **Deploy the App**:
   - After deploying, you should see a success message saying, "The app was successfully deployed."
   - Click **Open App** to view your deployed site.

## Credits

- Portions of this project were adapted from a Code Institute walkthrough project. Due to time constraints and personal challenges, these resources offered a valuable foundation. However, this adaptation does not include the custom model for the contact form, which was developed independently.

### AI Assistance
- **[ChatGPT](https://openai.com/blog/chatgpt/)**: Used for explanation and clarification of technical concepts, helping to understand Django structures and troubleshoot issues during project deployment.

### Other Resources
- **[Google](https://www.google.com/)**: An invaluable tool for researching solutions and finding documentation.
- **[W3Schools](https://www.w3schools.com/)**: A great resource for learning web technologies like HTML, CSS, and JavaScript.
- **[Stack Overflow](https://stackoverflow.com/)**: The community for resolving coding issues and getting answers to programming questions.

### Free Images
- A free-licensed image was obtained from Google, ensuring compliance with licensing terms.

### Acknowledgements
- Special thanks to Code Institute for their walkthrough project, which helped with certain parts of the project, excluding the custom contact form model.
- I also appreciate the support from my family and my mentor [Iuliia Konovalova](https://github.com/IuliiaKonovalova) who helped me through the project.

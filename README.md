# Art Store

The Art Store is an online platform designed to sell high-quality, original paintings and provide mural services by talented artists. This document outlines the e-commerce business model for the Art Store, focusing on the B2C (Business-to-Consumer) segment. The application aims to connect individual art buyers and collectors with unique, hand-crafted art pieces and custom murals, enhancing both residential and commercial spaces.

[**Live Version**](https://art-store-bdbdae133a85.herokuapp.com/)

[**Repository GitHub Repo**](https://github.com/KaltrinaBM/art_store)


![home](/media/home.png)


## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Business Model](#business-model)
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

- **User Authentication**: Secure sign-up, sign-in, sign-out, and password recovery functionalities.
- **User Profile Management**: Update profile details, view order history, and manage account settings.
- **Review Management**: Full CRUD (Create, Read, Update, Delete) operations for managing reviews on each painting.
- **Product Management**: Add, update, and delete products easily from the admin panel.
- **Blog Access**: View blog posts created and managed by site owners.
- **Responsive Design**: Adaptive layout and styling using Bootstrap for a seamless experience across all devices.
- **Contact Us Form**: Submit inquiries and messages via a user-friendly contact form.



![Product Reviews](/media/reviews.png)

![Contact Us](/media/blog.png)

![Contact Us](/media/contact-us.png)



## Business Model

Our e-commerce platform uses a direct-to-consumer model to offer a curated selection of artworks. We aim to provide a seamless shopping experience with secure transactions and an intuitive interface.

### Marketing Strategies

- **Digital Marketing:** Utilize social media platforms (Instagram, Pinterest, Facebook) for showcasing artwork and attracting customers.
- **Search Engine Optimization (SEO)**: Optimize product listings and content to enhance search engine visibility and attract organic traffic.
- **Email Marketing**: Use newsletters to keep subscribers informed about new arrivals, promotions, and updates.
- **Content Marketing**: Create and share blog posts and articles to engage visitors and establish our authority in the art industry.
- **Paid Advertising**: Implement targeted online ads to reach specific customer demographics and drive traffic to our site.
- **Influencer Partnerships:** Collaborate with art influencers and bloggers to expand reach.

These strategies are designed to boost our online presence, engage customers, and drive sales growth.

### Business Focus
- **Model:** B2C (Business-to-Consumer)
- **Purpose:** Provide a curated marketplace for purchasing expensive, original paintings and commissioning custom murals.

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

## SEO Enhancements: Sitemap, Meta Tags, Social Media Integration, and More
To improve the site's search engine optimization (SEO), I have integrated several important features, including a sitemap and robots.txt file to enhance search engine crawlability and indexing. Meta descriptions and keywords have been carefully crafted to optimize search visibility and relevance. A newsletter subscription option has been added to engage users and encourage return visits. Additionally, a genuine Instagram page has been linked to boost social media presence, though a Facebook page is currently represented by a mockup. These elements collectively support better search visibility, user engagement, and overall site performance.

![Facebook Mockup](/media/facebook-mockup.png)

![Newsletter](/media/newsletter.png)



## Usage Instructions

To use the Art Store web application, follow these steps:

1. **Sign Up**: Create an account to add reviews, place orders, and access order history.
2. **Sign In**: Log in to access features such as reading blog posts and leaving reviews.
3. **Manage Profile**: Update your profile details, recover your password, and view your order history.
4. **Place Orders**: Place orders and make secure payments. Note that registration is not required to complete a purchase.
5. **Reviews**: Registered users can add, update, and delete reviews for paintings. All site visitors can read reviews.
6. **Admin Panel**: Access the [admin panel](https://art-store-bdbdae133a85.herokuapp.com/admin/) with your superuser credentials to manage the site.
7. **Blog**: Read articles posted by admins.
8. **Contact Form**: Send messages to the team via the contact form. A valid email is required, but signing in is not.
9. **Newsletter**: Subscribe easily from the homepage.
10. **Manage Products**: Site owners can add, update, and delete products effortlessly.



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

***Review Model Attributes***

| Attribute       | Type                     | Description                                          | Validation                         |
|-----------------|--------------------------|------------------------------------------------------|------------------------------------|
| `id`            | AutoField (Primary Key)   | Automatically generated unique identifier for each review. | Unique, auto-incremented.          |
| `painting`      | ForeignKey (to `Painting`) | The painting associated with this review.             | Must reference a valid `Painting`. |
| `user`          | ForeignKey (to `User`)    | The user who submitted the review.                   | Must reference a valid `User`.     |
| `rating`        | PositiveIntegerField      | Rating given by the user.                            | Must be between 1 and 5 (inclusive).|
| `content`       | TextField                | The content of the review.                           | No specific validation.            |
| `created_at`    | DateTimeField(auto_now_add=True) | Timestamp indicating when the review was created.   | Automatically generated.           |
| `updated_at`    | DateTimeField(auto_now=True) | Timestamp indicating when the review was last updated. | Automatically updated.            |


***BlogPost Model Attributes***

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

***ContactMessage Model Attributes***

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

Manual testing was conducted throughout the development of the site to ensure that each feature worked as expected before being merged into the master branch. Usability testing involved user acceptance testing (UAT), where new users tested the site on various devices and browsers to catch any issues and provide feedback. The table below summarizes the tests performed, the expected results, and the outcomes.

### Sign Up

| **User Actions**                                  | **Expected Results**                                                   | **Y/N** | **Comments** |
|---------------------------------------------------|------------------------------------------------------------------------|---------|--------------|
| Click on "Sign Up" button                         | User is redirected to the Sign Up page                                 | Y       |              |
| Click on the "Login" link within the Sign Up form | User is redirected to the Login page                                   | Y       |              |
| Enter a valid email twice                         | The field only accepts valid email addresses                           | Y       |              |
| Enter mismatched passwords                        | The form shows an error message indicating passwords do not match      | Y       |              |
| Complete the form with valid data and submit      | User account is created, and the user has to verify via email address  | Y |              |

### Login

| **User Actions**                                  | **Expected Results**                                                   | **Y/N** | **Comments** |
|---------------------------------------------------|------------------------------------------------------------------------|---------|--------------|
| Enter a valid email and password                  | User is logged in and redirected to their profile or homepage           | Y       |              |
| Enter an invalid email or password                | An error message is displayed indicating invalid credentials            | Y       |              |
| Click on "Forgot Password?"                       | User is redirected to the password recovery page                        | Y       |              |
| Enter registered email in password recovery       | A password reset link is sent to the user's email                       | Y       |              |
| Submit the form with valid credentials            | User is logged in successfully and redirected to the Home page       | Y       |              |

### Place Order

| **User Actions**                                  | **Expected Results**                                                   | **Y/N** | **Comments** |
|---------------------------------------------------|------------------------------------------------------------------------|---------|--------------|
| Add items to the cart                             | Items are added to the cart, and the cart count is updated              | Y       |              |
| Click on "Checkout"                               | User is redirected to the checkout page                                 | Y       |              |
| Enter valid payment details                       | Payment is processed, and the user receives an order confirmation       | Y       |              |
| Enter invalid payment details                     | An error message is displayed indicating payment failure                | Y       |              |
| Submit order                                      | The order is processed, and the user is redirected to the order summary page with order details | Y |              |

### Contact Form

| **User Actions**                                  | **Expected Results**                                                   | **Y/N** | **Comments** |
|---------------------------------------------------|------------------------------------------------------------------------|---------|--------------|
| Navigate to the Contact page                      | User is able to view the contact form                                   | Y       |              |
| Fill out the form with valid data                 | The form is submitted successfully, and the user receives a confirmation message | Y |              |
| Submit the form with missing required fields      | The form shows an error message indicating required fields              | Y       |              |



### Reviews

| **User Actions**                                  | **Expected Results**                                                   | **Y/N** | **Comments** |
|---------------------------------------------------|------------------------------------------------------------------------|---------|--------------|
| Navigate to a product page                        | The product page displays with an option to view or add reviews         | Y       |              |
| Logged-in user clicks "Add Review"                | User is redirected to the review form page                              | Y       |              |                              | Y       |              |
| Logged-in user submits a review with valid data   | Review is submitted successfully and displayed on the product page      | Y       |              |
| Logged-in user submits an empty review form       | An error message is displayed indicating required fields are missing    | Y       |              |
| Logged-in user edits their review                 | Review is updated successfully and changes are reflected on the product page | Y  |              |
| Logged-in user deletes their review               | Review is removed from the product page                                 | Y       |              |
| Logged-in user edits their review                 | Review is updated in the product page                                   | Y |  |
| User views reviews on a product page              | All approved reviews are displayed, with the most recent reviews at the top | Y  |              |

### Blog

| **User Actions**                                   | **Expected Results**                                                   | **Y/N** | **Comments** |
|----------------------------------------------------|------------------------------------------------------------------------|---------|--------------|
| Navigate to the Blog page                          | The blog page loads with a list of published blog posts                 | Y       |              |
| Click on a blog post hyperlinked         title     | User is redirected to the full blog post page                           | Y       |              |
| View the blog post content                         | The blog post displays with the full content, images, author and date   | Y |  |
| Attempt to find a post using the search function   | Search results display relevant blog posts matching the query           | Y       |              |
| Admin creates a new blog post from the admin panel | The new post appears on the blog page and is accessible to all users    | Y       |              |
| User navigates through multiple pages of blog posts | Pagination works correctly, allowing users to browse older posts        | Y       |              |
| Admin updates a blog post                          | The updated post content is reflected immediately on the blog page      | Y       |              |
| Admin deletes a blog post                          | The post is removed from the blog page and is no longer accessible      | Y       |              |


Testing was performed on multiple devices and browsers to ensure that the review feature is fully functional and user-friendly. All identified issues were addressed and fixed during development.


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

- **W3C CSS Validation**: Each page's CSS was validated using the W3C CSS Validation Service to ensure adherence to CSS standards.
- ***Results***: All stylesheets passed the validation with no errors detected, confirming that the CSS code is compliant with W3C standards and helps maintain a consistent visual appearance across different browsers.   

- **W3C Markup Validation**: Each page was tested by entering its URL into the W3C Markup Validation Service. The validation service checks for syntax errors, structural issues, and other potential problems in the HTML markup.
- ***Results***: All pages passed the validation with no errors detected, indicating that the HTML structure conforms to the W3C standards. This validation step helps ensure cross-browser compatibility and contributes to a consistent user experience.

[CI Python Linter](https://pep8ci.herokuapp.com/) 

- **CI Python Linter**: Used to check the Python code for syntax errors and code style violations.
- ***Results***:
- No errors or style violations were found in the code.
- The code was reviewed and identified as having minor issues with unused imports. However, after addressing these issues, the website began experiencing new problems.

**Performance Testing with Lighthouse**

To ensure optimal performance, accessibility, and best practices, I tested the web application using [Lighthouse](https://developers.google.com/web/tools/lighthouse), a tool provided by Google Chrome. 

- ***Results***
Below are the results from the Lighthouse tests:

![Lighthouse Homepage Test](/media/lighthouse.png)

These screenshots demonstrate the outcomes of the performance and accessibility evaluations, showcasing the measures taken to ensure the web application's quality and compliance.

### Further Testing

#### Browser and Device Testing
The website was thoroughly tested across multiple web browsers, including Google Chrome and Microsoft Edge, to ensure full compatibility and functionality. Additionally, it was tested on various devices such as desktop computers, laptops, and Android smartphones, to verify responsiveness and performance across different screen sizes and resolutions.

#### Functionality Testing
Extensive testing was carried out on all major features of the website, with a focus on ensuring that the purchasing process—from product selection to order completion—works seamlessly. This includes testing the following:

User authentication: Registration, login, and password reset functions.
Shopping cart: Adding, updating, and removing items from the cart.
Checkout process: Verifying payment gateway integration (Stripe), shipping details, and order confirmation.
Order management: Ensuring orders are properly recorded in the database and can be viewed by both the customer and admin.
Cross-Device Usability Testing

To gain further insights into user experience and uncover potential issues, family members were invited to review the website and perform test purchases. Their feedback helped identify and resolve any usability challenges, as well as fine-tune the purchasing workflow. Specific attention was paid to:

User interface intuitiveness: Ensuring that the navigation and purchasing process are easy to follow for all users.
Bug identification: Family members were encouraged to report any bugs or issues encountered during their testing sessions.

### Bugs

#### Known Bugs: Forms, Buttons, and Image Size and Position
The appearance of forms, buttons, and images may vary across different devices. While this does not affect the functionality, it impacts the visual consistency and overall aesthetics of the page layout. Due to time constraints, I was unable to refine the CSS styling to enhance the visual presentation.

#### Bug Fixed: Email Notification Issue
The issue preventing confirmation emails from being sent to customers after placing an order has been resolved. Customers will now receive timely email notifications regarding their placed order.

#### Bug Fixed: Sensitive Information Exposure
The issue of sensitive information being exposed during commits has been fixed. Appropriate measures have been taken to ensure that sensitive data is no longer included, enhancing the security of the application.

### Features to be Implemented
Deleted Product Template: Create an HTML template that will display a message or a page when a product is removed from the website, ensuring a smooth user experience even when content is no longer available.
CSS Refinement: Enhance and perfect the CSS styling across the entire website to improve visual consistency, responsiveness, and overall aesthetic appeal.

## Deployment

During the development process, some sensitive information was accidentally committed to the repository. To resolve this, the project has been updated to ensure that all sensitive details are now securely managed using environment variables. Moving forward, all commits and deployments will follow best practices, keeping sensitive information stored in external files (e.g., env.py or environment variables) and ensuring it is not included in the repository.

### Heroku Deployment
To deploy this Django project to Heroku from its [GitHub repository](https://github.com/KaltrinaBM/art_store), the following steps were taken:

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

Some parts of this project were adapted from a Code Institute walkthrough. Given the time constraints and personal challenges, these resources provided a crucial foundation. However, the adapted version does not include the following features, which were developed independently:

Three custom models for managing product reviews: These models handle reviews for each painting submitted by registered users and include full CRUD (Create, Read, Update, Delete) functionality.
A blog with posts by site owners: This feature allows site owners to create and manage blog content from the Admin side.
A contact form: This form enables all site visitors to send contact messages.

### AI Assistance
- **[ChatGPT](https://openai.com/blog/chatgpt/)**: Used for explanation and clarification of technical concepts, helping to understand Django structures and troubleshoot issues during project deployment.

### Other Resources
- **[Google](https://www.google.com/)**: An invaluable tool for researching solutions and finding documentation.
- **[W3Schools](https://www.w3schools.com/)**: A great resource for learning web technologies like HTML, CSS, and JavaScript.
- **[Stack Overflow](https://stackoverflow.com/)**: The community for resolving coding issues and getting answers to programming questions.

### Free Images
- A free-licensed image was obtained from Google, ensuring compliance with licensing terms.

### Acknowledgements
- Special thanks to Code Institute for their comprehensive walkthrough project, which provided valuable guidance and insights for various aspects of this project.Although some aspects have been adapted to meet the unique needs of this project and custom models have been created independently, the foundational knowledge and structure provided by Code Institute have been crucial in progressing this work.

- I would also like to extend my gratitude to my family for their ongoing support, to my mentor, Iuliia Konovalova, for her invaluable guidance and assistance throughout the project, and to the tutors at Code Institute for their support. Their expertise and encouragement were greatly appreciated.
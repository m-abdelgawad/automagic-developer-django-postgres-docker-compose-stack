<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<a name="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="readme_files/logo.png" alt="Logo" width="80" height="80">

  <h3 align="center">AutoMagic Developer Docker Compose Stack</h3>

</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#preview-video">Preview Video</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol> 
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<img src="readme_files/cover.jpg" alt="Cover Image">

* Project Name: AutoMagic Developer Docker Compose Stack
* Version: v1.0.0
* Organization Department: Technology

### Description

This project is a Django web application, serving as a personal portfolio 
hosted on the domain "automagicdeveloper.com" 
The application is designed to showcase the developer's work and accomplishments. 

It consists of several distinct apps:

**Portfolio:** Showcases the developer's projects, skills, and professional 
achievements.

**Blog:** The blog app allows the developer to share their thoughts, experiences, 
and insights with the audience.

**App Gallery:** A gallery of developed applications with a beautiful slider.

**Insights Dashboard:** A dashboard that analyze the data of published project on the website.

**Contact:** A contact application with a contact form protected with reCAPTCHA.

**Admin Dashboard:** Features a comprehensive admin dashboard 
that provides valuable insights and information, including:
- Website traffic data retrieved from Google Analytics.
- Server utilization data from a separate System Monitor app running in a 
separate container.
- Cloud account billing information, specifically from DigitalOcean.

To ensure smooth functioning and scalability, the project is containerized 
using Docker. It consists of three containers:

**Django App Container:** This container houses the Django web application, 
responsible for handling user interactions and rendering the web pages.

**Postgres Database Container:** The Postgres database container stores 
application data securely.

**System Monitor Crontab Script Container:** This container runs a crontab 
script responsible for monitoring the server and gathering system 
utilization data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This project was developed using the following tech stacks:

* Python (Django Backend Framework)
* HTML
* CSS
* JavaScript
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Screenshots -->
## Screenshots

#### Admin Dashboard
<img src="readme_files/admin_dashboard.jpg">

#### Insights Dashboard
<img src="readme_files/insights_dashboard.jpg">

#### Homepage
<img src="readme_files/homepage.jpg">

#### App Gallery
<img src="readme_files/app_gallery.jpg">

#### Portfolio List
<img src="readme_files/portfolio_list.jpg">

#### Portfolio Project
<img src="readme_files/portfolio_project.jpg">

#### Blog List
<img src="readme_files/blog_list.jpg">

#### Blog Post
<img src="readme_files/blog_post.jpg">

#### Contact
<img src="readme_files/contact.jpg">

#### Login / Register
<img src="readme_files/login_register.jpg">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Preview Video -->
## Preview Video
[![Click Me](readme_files/video_cover.jpg)](https://youtu.be/39FHj4iAQSA)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Mohamed AbdelGawad Ibrahim - [@m-abdelgawad](https://www.linkedin.com/in/m-abdelgawad/) - <a href="tel:+201069052620">+201069052620</a> - muhammadabdelgawwad@gmail.com

GitHub Profile Link: [https://github.com/m-abdelgawad](https://github.com/m-abdelgawad)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/m-abdelgawad/

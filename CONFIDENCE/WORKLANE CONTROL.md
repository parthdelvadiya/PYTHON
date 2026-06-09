# Worklane Control

Worklane Control is a project management and employee tracking platform 
that also helps businesses create and share marketing content from one dashboard.

The idea behind the project was to connect development work and business marketing 
into a single system. Instead of using multiple tools, users can manage employees, 
projects, tasks, and marketing activities from one place.

## Technologies Used

* Backend: Django, Django REST Framework (DRF)
* Database: SQLite
* Authentication: JWT (JSON Web Tokens)
* Frontend: React, Vite, Tailwind CSS, Framer Motion

## Main Features

### 1. Project and Employee Management

Users can create and manage employees, projects, and tasks. The dashboard provides 
useful information such as:

* Total employees
* Active projects
* Project progress
* Upcoming deadlines
* Task status overview

### 2. GitHub Task Automation

The system can connect to GitHub repositories linked to projects.

It automatically checks recent commits and compares commit messages 
with task names. If a developer completes a task and mentions it in a 
commit message, the system can automatically mark that task as completed.

This reduces manual updates and helps keep project progress accurate.

### 3. AI Poster Generation

Users can generate marketing posters by simply entering a prompt and selecting options such as:

* Industry
* Style
* Tone

The system uses an AI image generation service to create posters automatically 
and provides a shareable image link.

### 4. Social Media Publishing

After generating a poster, users can publish it directly to Facebook and Instagram 
from the dashboard.

This removes the need to manually download and upload marketing content on different platforms.

### 5. Secure User Data

Each user's data is kept separate and secure. Users can only access their own 
employees, projects, tasks, posters, and social media settings.

---


## Why I Built This Project

I wanted to build something more than a simple task management application.

My goal was to create a complete workflow where:

* Developers can track project progress automatically through GitHub.
* Businesses can generate marketing content using AI.
* Marketing content can be published directly to social media.

This creates a single platform that supports both project management and business promotion.

---

## Common Interview Questions

### What problem does this project solve?

It combines project management, employee tracking, AI content generation, 
and social media publishing into one platform, reducing the need for multiple tools.

### How does the GitHub integration work?

The system regularly checks project repositories for recent commits. I
f a commit message matches a task, the task is automatically marked as completed.

### Why did you choose Django and React?

Django helped me quickly build secure APIs and backend functionality, 
while React allowed me to create a fast and interactive user interface.

### How does the AI poster feature work?

Users provide a prompt and select preferences like style and industry. 
The system sends this information to an AI image generation service, 
which creates a marketing poster.

### How does authentication work?

The application uses JWT authentication. Users receive access and refresh 
tokens when they log in, which helps maintain secure sessions.

### What was the most interesting part of the project?

The automation workflow. A task can move from GitHub development activity to project 
tracking and then into AI-generated marketing content, all within a single platform.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill, UserSkill

@login_required
def landing_page(request):
    return render(request, 'skill_exchange/landing_page.html')

@login_required
def my_skills(request):
    user_skills = UserSkill.objects.filter(user=request.user).select_related('skill')
    return render(request, 'skill_exchange/my_skills.html', {
        'user_skills': user_skills
    })

@login_required
def add_skill(request):
    if request.method == 'POST':
        skill_id = request.POST.get('skill')
        level = request.POST.get('level')

        if not skill_id or not level:
            messages.error(request, "Please select a skill and level.")
            return redirect('skill_exchange:add_skill')

        try:
            skill = Skill.objects.get(id=skill_id)
            UserSkill.objects.update_or_create(
                user=request.user,
                skill=skill,
                defaults={'level': level}
            )
            
            return redirect('skill_exchange:my_skills')

        except Skill.DoesNotExist:
            messages.error(request, "Skill not found.")
            return redirect('skill_exchange:add_skill')

    skills = Skill.objects.all().order_by('name')
    return render(request, 'skill_exchange/add_skill.html', {'skills': skills})

@login_required
def skill_guidance(request):
    guidance = {
        'Python': {
            'Beginner': "Start by understanding variables, data types, and basic operators. Practice writing small scripts to automate tasks. Explore loops and conditional statements with real examples. Try building simple programs like a calculator or a guessing game. Always test your code and read Python documentation for clarity.",
            'Intermediate': "Focus on functions, classes, and object-oriented programming. Work on modular code using modules and packages. Learn about error handling and debugging. Practice by creating small projects like a text-based game or a to-do list app. Explore Python libraries such as datetime, os, and random.",
            'Advanced': "Build complex projects integrating multiple modules and external APIs. Contribute to open-source projects to get real-world experience. Optimize your code for performance and readability. Explore advanced topics like decorators, generators, and concurrency. Focus on testing frameworks like pytest and code versioning with Git."
        },
        'Django': {
            'Beginner': "Learn the MVC structure, understand models, views, and templates. Build simple apps like a blog or a task manager. Practice setting up URLs, forms, and admin panel customization. Understand how to interact with the database through Django ORM. Experiment with static files and templates to make your pages dynamic.",
            'Intermediate': "Implement user authentication and authorization systems. Use Django forms effectively, including ModelForms and validation. Work on deployment basics using Heroku or Docker. Integrate third-party libraries like Django REST Framework. Focus on improving code organization and reusable components.",
            'Advanced': "Develop scalable applications with advanced features like APIs, caching, and signals. Optimize database queries for performance and security. Implement testing with Django’s testing framework. Work on real projects that require user management, analytics, and background tasks. Contribute to Django open-source projects to deepen your understanding."
        },
        'JavaScript': {
            'Beginner': "Understand variables, data types, operators, and loops. Learn DOM manipulation and basic event handling. Practice small scripts that interact with the page. Build mini-projects like a dynamic to-do list or a simple calculator. Learn how to debug using browser tools and console.log statements.",
            'Intermediate': "Explore ES6 features like let, const, arrow functions, and template literals. Learn asynchronous programming with promises and async/await. Practice creating modular code and using browser APIs. Build interactive applications using vanilla JS. Learn debugging and performance optimization techniques.",
            'Advanced': "Focus on frameworks like React, Vue, or Angular. Work with advanced patterns such as state management, hooks, and context API. Build full-scale web applications connecting front-end with backend APIs. Practice testing frameworks like Jest or Cypress. Optimize for performance and accessibility across devices."
        },
        'React': {
            'Beginner': "Understand components, props, and state. Learn JSX syntax and how to render elements dynamically. Practice building small projects like a counter or a task list. Learn about event handling and conditional rendering. Explore React DevTools to inspect components.",
            'Intermediate': "Learn hooks such as useState, useEffect, and custom hooks. Implement routing with React Router. Build projects that fetch data from APIs and display dynamic content. Learn context API for state management. Start optimizing performance with memoization techniques.",
            'Advanced': "Work with Redux or RTK for global state management. Build large projects with complex component trees. Implement authentication, protected routes, and API integrations. Optimize rendering with useMemo and React.lazy. Learn testing React components with libraries like React Testing Library."
        },
        'Vue.js': {
            'Beginner': "Understand templates, directives, and component structure. Build simple projects with data binding. Learn about event handling and basic reactivity. Explore Vue CLI to scaffold new projects. Practice using computed properties and methods effectively.",
            'Intermediate': "Work with Vue Router for navigation and Vuex for state management. Implement reusable components and slots. Practice lifecycle hooks and watch properties. Build projects that interact with APIs. Learn about component communication patterns.",
            'Advanced': "Develop large-scale applications using Composition API. Optimize performance and component reusability. Use advanced features like provide/inject, plugins, and directives. Implement testing strategies for Vue components. Focus on best practices for maintainable code."
        },
        'HTML': {
            'Beginner': "Learn basic tags including headings, paragraphs, and lists. Understand the structure of an HTML document. Practice creating forms and tables. Explore semantic HTML elements for better accessibility. Build simple static pages to practice layout.",
            'Intermediate': "Work on forms validation, input types, and semantic structure. Learn HTML5 APIs like canvas, video, and audio. Explore accessibility features like ARIA roles. Optimize your pages for SEO using meta tags. Practice creating responsive layouts with flexible containers.",
            'Advanced': "Master semantic HTML and best practices for SEO. Build complex, interactive pages with embedded media. Integrate HTML with CSS and JavaScript efficiently. Focus on accessibility, progressive enhancement, and performance optimization. Learn how to structure large-scale HTML projects."
        },
        'CSS': {
            'Beginner': "Learn selectors, colors, fonts, and spacing. Practice basic styling for text and boxes. Experiment with backgrounds, borders, and hover effects. Understand the box model and layout concepts. Build small projects to apply styles effectively.",
            'Intermediate': "Work with flexbox, grid, and responsive layouts. Implement animations and transitions. Learn advanced selectors and pseudo-classes. Practice creating reusable classes and CSS variables. Build multi-page responsive websites.",
            'Advanced': "Master responsive design principles, preprocessors like SASS/SCSS, and utility-first frameworks. Optimize CSS for performance and maintainability. Implement complex animations and transitions. Focus on accessibility and cross-browser compatibility. Create design systems for large projects."
        },
        'Tailwind CSS': {
            'Beginner': "Learn utility classes for spacing, typography, and colors. Apply simple layouts using Tailwind’s flex and grid utilities. Explore background, border, and shadow classes. Build small static pages to get comfortable with the syntax.",
            'Intermediate': "Practice responsive design with Tailwind’s breakpoints. Use components and plugins for reusable code. Build interactive layouts and forms. Customize Tailwind configuration for colors and fonts. Learn how to integrate Tailwind with JavaScript frameworks.",
            'Advanced': "Create complex UI patterns using Tailwind’s advanced features. Implement dark mode, themes, and design tokens. Optimize your projects for performance and maintainability. Build production-ready applications with reusable components. Follow best practices for accessible and responsive design."
        },
        'Node.js': {
            'Beginner': "Learn how Node.js works and basic JavaScript outside the browser. Understand modules, npm, and package.json. Build small scripts and simple server-side programs. Learn file system operations and basic server creation. Practice handling asynchronous code.",
            'Intermediate': "Work with Express.js to build REST APIs. Handle routing, middleware, and request-response cycles. Learn about asynchronous patterns and callbacks. Implement simple authentication and error handling. Connect to databases like MongoDB or PostgreSQL.",
            'Advanced': "Build scalable server applications with Express, REST APIs, and WebSockets. Optimize performance using clusters and caching. Implement robust authentication and authorization. Practice testing with Mocha, Jest, or Supertest. Deploy Node applications to cloud platforms like AWS or Heroku."
        },
        'Express.js': {
            'Beginner': "Learn routing basics, middleware, and server setup. Create simple routes and respond with JSON or HTML. Handle query parameters and request bodies. Explore Express documentation and examples. Practice building small APIs.",
            'Intermediate': "Implement REST API principles with proper HTTP methods. Use middleware for authentication, logging, and validation. Connect Express with a database and perform CRUD operations. Structure code for maintainability. Test your routes and error handling thoroughly.",
            'Advanced': "Build scalable and production-ready APIs with Express. Optimize routing, database queries, and middleware usage. Implement caching, rate limiting, and security measures. Integrate WebSockets for real-time applications. Apply testing frameworks and deploy applications in production."
        },
        'SQL': {
            'Beginner': "Learn basic commands: SELECT, INSERT, UPDATE, DELETE. Practice creating tables and inserting data. Understand primary keys and basic constraints. Execute queries using a sample database. Get comfortable with simple filtering and sorting operations.",
            'Intermediate': "Practice joins, indexes, transactions, and advanced filtering. Optimize queries for better performance. Learn subqueries, views, and stored procedures. Work with multiple related tables and ensure data integrity. Practice writing complex queries combining multiple operations.",
            'Advanced': "Focus on database design, normalization, and indexing strategies. Optimize queries for large datasets. Implement stored procedures, triggers, and advanced constraints. Analyze query performance and use explain plans. Design scalable relational databases for production systems."
        },
        'PostgreSQL': {
            'Beginner': "Learn creating tables, inserting data, and basic SELECT queries. Understand data types and constraints. Practice simple joins and aggregations. Explore PostgreSQL tools and CLI. Build simple databases to experiment with queries.",
            'Intermediate': "Work with functions, views, triggers, and sequences. Implement transactions and concurrency control. Optimize queries using indexing and proper schema design. Use advanced PostgreSQL data types and operators. Connect applications with PostgreSQL efficiently.",
            'Advanced': "Focus on performance tuning, replication, and partitioning. Design complex relational databases for scalability. Implement advanced security and access control. Use monitoring and logging tools to maintain high availability. Practice PostgreSQL in production-like environments."
        },
        'MongoDB': {
            'Beginner': "Understand documents, collections, and basic CRUD operations. Learn how to insert, update, delete, and find data. Explore MongoDB shell and Compass GUI. Practice designing simple document structures. Learn about ObjectIds and basic indexes.",
            'Intermediate': "Work with aggregation pipelines, indexing, and embedded documents. Implement schema design for efficient queries. Learn about relationships in MongoDB and referencing documents. Practice integrating MongoDB with Node.js or Python. Optimize queries for performance.",
            'Advanced': "Design scalable NoSQL databases for complex applications. Implement replication, sharding, and backup strategies. Optimize aggregation pipelines and indexing strategies. Use MongoDB in high-traffic production environments. Focus on security, authentication, and monitoring."
        },
        'Git': {
            'Beginner': "Learn git init, add, commit, and basic version control. Understand the staging area and repository structure. Practice creating local repositories and committing changes. Explore git status, log, and diff commands. Learn to revert changes safely.",
            'Intermediate': "Work with branches, merging, rebasing, and resolving conflicts. Use remote repositories and push/pull changes. Learn about tagging, stashing, and cherry-picking. Integrate Git with IDEs and CI/CD pipelines. Practice collaborative workflows.",
            'Advanced': "Master advanced Git workflows for large projects. Handle complex merges and rebases confidently. Implement Git hooks, submodules, and advanced branching strategies. Optimize collaboration with pull requests, code reviews, and continuous integration. Contribute to open-source projects."
        },
        'GitHub': {
            'Beginner': "Learn to create repositories, push and pull code. Understand issues, README files, and basic collaboration. Explore GitHub interface and basic project management features. Practice creating branches and merging them. Learn to clone repositories and submit pull requests.",
            'Intermediate': "Work with pull requests, code reviews, and collaborative workflows. Use GitHub Actions for automation. Manage issues, milestones, and project boards efficiently. Learn about forks, upstream, and contribution workflows. Integrate GitHub with local Git repositories.",
            'Advanced': "Manage large open-source projects and teams. Automate workflows with Actions and scripts. Implement CI/CD pipelines and code quality checks. Use GitHub packages and security features effectively. Mentor contributors and maintain project documentation."
        },
        'Docker': {
            'Beginner': "Learn containers, images, and basic Docker commands. Practice creating, starting, and stopping containers. Understand Dockerfile basics and building images. Explore volumes, networking, and container inspection. Run simple applications inside containers.",
            'Intermediate': "Use docker-compose to orchestrate multi-container applications. Optimize Dockerfiles for smaller images. Manage networks, volumes, and environment variables. Deploy simple applications with Docker in development environments. Learn best practices for containerization.",
            'Advanced': "Build complex containerized applications with multiple services. Implement CI/CD pipelines with Docker. Optimize performance and resource usage. Secure containers and manage secrets. Deploy Docker applications to production cloud platforms efficiently."
        },
        'AWS': {
            'Beginner': "Understand core AWS services like EC2, S3, and IAM. Learn to launch virtual servers and store data in S3. Explore AWS management console and CLI. Practice basic security and access controls. Deploy simple static websites to S3.",
            'Intermediate': "Work with Lambda, RDS, and DynamoDB. Implement serverless functions and automated workflows. Manage users and permissions with IAM policies. Integrate AWS services for small-scale applications. Monitor usage and cost management.",
            'Advanced': "Design scalable cloud infrastructure with multiple AWS services. Implement high availability, auto-scaling, and load balancing. Secure cloud resources and optimize costs. Deploy complex applications with CI/CD pipelines. Focus on best practices for cloud architecture."
        },
        'Firebase': {
            'Beginner': "Learn Authentication, Realtime Database, and Hosting. Build simple apps with login and data storage. Explore Firebase console and SDK. Implement basic CRUD operations in your app. Practice deploying a small project to Firebase Hosting.",
            'Intermediate': "Work with Firestore, Cloud Functions, and storage. Implement serverless backend logic. Manage users and authentication securely. Practice integrating Firebase with web and mobile apps. Explore analytics and performance monitoring.",
            'Advanced': "Build large-scale apps using Firebase services efficiently. Implement security rules, data indexing, and advanced queries. Use Cloud Functions for serverless operations. Optimize performance and scalability. Integrate Firebase with other cloud services and analytics tools."
        },
        'Machine Learning': {
            'Beginner': "Understand basic concepts like supervised and unsupervised learning. Learn libraries such as scikit-learn and TensorFlow basics. Practice with small datasets for regression and classification. Explore data preprocessing and feature engineering. Build simple models and evaluate performance.",
            'Intermediate': "Work on model training, evaluation, and hyperparameter tuning. Explore pipelines and cross-validation techniques. Learn about neural networks and basic deep learning. Practice building projects like image or text classifiers. Analyze model results and iterate improvements.",
            'Advanced': "Build and deploy complex ML systems with deep learning and NLP. Optimize model performance and scalability. Work with large datasets and cloud-based ML platforms. Implement production-ready ML pipelines and monitoring. Contribute to research or open-source ML projects."
        },
        'Data Science': {
            'Beginner': "Learn Python libraries such as pandas, numpy, and matplotlib. Practice data cleaning, transformation, and visualization. Explore datasets and basic statistics. Build small projects analyzing trends or summaries. Document your workflow clearly.",
            'Intermediate': "Practice advanced data analysis, statistical modeling, and visualization techniques. Work with multiple datasets, merging and cleaning them. Explore machine learning basics and predictive modeling. Create dashboards and reports for insights. Validate data quality and reproducibility.",
            'Advanced': "Develop end-to-end data science pipelines, including data ingestion, cleaning, analysis, and model deployment. Use advanced ML techniques and big data tools. Optimize workflows and collaborate in teams. Share insights through interactive dashboards and visualizations. Focus on reproducibility and scalability."
        },
    }

    user_skills = UserSkill.objects.filter(user=request.user).select_related('skill')
    skill_feedback = []
    for us in user_skills:
        name = us.skill.name
        level = us.level
        advice = guidance.get(name, {})
        feedback = advice.get(level, "Keep practicing and exploring!")
        skill_feedback.append({
            'name': name,
            'level': level,
            'advice': feedback
        })

    return render(request, 'skill_exchange/skill_guidance.html', {
        'skill_feedback': skill_feedback
    })
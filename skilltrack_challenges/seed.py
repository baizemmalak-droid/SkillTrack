from .models import Skill, Challenge, Badge

def seed_data():
    # ---------- SKILLS ----------
    skills_data = [
        {"name": "Python", "icon": "🐍"},
        {"name": "Django", "icon": "🌐"},
        {"name": "JavaScript", "icon": "🟨"},
        {"name": "React", "icon": "⚛️"},
        {"name": "Vue.js", "icon": "🖼️"},
        {"name": "HTML", "icon": "🌍"},
        {"name": "CSS", "icon": "🎨"},
        {"name": "Tailwind CSS", "icon": "💨"},
        {"name": "Node.js", "icon": "🟢"},
        {"name": "Express.js", "icon": "🚂"},
        {"name": "SQL", "icon": "🗄️"},
        {"name": "PostgreSQL", "icon": "🐘"},
        {"name": "MongoDB", "icon": "🍃"},
        {"name": "Git", "icon": "🔧"},
        {"name": "GitHub", "icon": "🐙"},
        {"name": "Docker", "icon": "🐳"},
        {"name": "AWS", "icon": "☁️"},
        {"name": "Firebase", "icon": "🔥"},
        {"name": "Machine Learning", "icon": "🤖"},
        {"name": "Data Science", "icon": "📊"},
    ]

    skills = {}
    for s in skills_data:
        skill_obj, _ = Skill.objects.get_or_create(name=s["name"], defaults={"icon": s["icon"]})
        skills[s["name"]] = skill_obj

    # ---------- CHALLENGES ----------
    challenges_data = [
        # Python
        {"title": "Variables & Loops", "desc": "Write a Python script that takes a list of numbers and prints only the even ones using loops and conditions.", "level": "easy", "points": 20, "skill": "Python"},
        {"title": "File Manager Script", "desc": "Build a script that reads a file, counts words, and saves the result into another file.", "level": "intermediate", "points": 50, "skill": "Python"},
        {"title": "API Data Processor", "desc": "Create a Python program that fetches data from a public API, cleans it, and stores it in a structured format.", "level": "advanced", "points": 100, "skill": "Python"},

        # Django
        {"title": "First Django View", "desc": "Create a Django app with one view and template that displays a welcome message.", "level": "easy", "points": 20, "skill": "Django"},
        {"title": "CRUD Blog App", "desc": "Build a blog system with create, read, update, and delete functionality using Django models and views.", "level": "intermediate", "points": 50, "skill": "Django"},
        {"title": "Authentication System", "desc": "Implement full authentication with signup, login, logout, profile page, and permissions.", "level": "advanced", "points": 100, "skill": "Django"},

        # JavaScript
        {"title": "DOM Click Counter", "desc": "Create a button that increments a counter when clicked using vanilla JS.", "level": "easy", "points": 20, "skill": "JavaScript"},
        {"title": "To-Do List App", "desc": "Build a to-do list with add, delete, and mark-as-done functionality.", "level": "intermediate", "points": 50, "skill": "JavaScript"},
        {"title": "Weather Dashboard", "desc": "Create a dashboard that fetches live weather data from an API and displays it dynamically.", "level": "advanced", "points": 100, "skill": "JavaScript"},

        # React
        {"title": "Counter Component", "desc": "Build a reusable React counter component using useState.", "level": "easy", "points": 20, "skill": "React"},
        {"title": "Movie Search App", "desc": "Create a React app that fetches and displays movies from an API with search functionality.", "level": "intermediate", "points": 50, "skill": "React"},
        {"title": "Authenticated Dashboard", "desc": "Build a full dashboard with protected routes, login system, and API integration.", "level": "advanced", "points": 100, "skill": "React"},

        # Vue.js
        {"title": "Vue Counter", "desc": "Create a simple counter using Vue data binding and methods.", "level": "easy", "points": 20, "skill": "Vue.js"},
        {"title": "Notes App", "desc": "Build a notes application with add, edit, and delete features using Vue components.", "level": "intermediate", "points": 50, "skill": "Vue.js"},
        {"title": "Real-Time Chat App", "desc": "Create a chat application using Vue with real-time updates and authentication.", "level": "advanced", "points": 100, "skill": "Vue.js"},

        # HTML
        {"title": "Personal Profile Page", "desc": "Build a simple personal profile page using semantic HTML tags.", "level": "easy", "points": 20, "skill": "HTML"},
        {"title": "Multi-Page Website", "desc": "Create a 3-page website with navigation and structured layout.", "level": "intermediate", "points": 50, "skill": "HTML"},
        {"title": "Accessible Website", "desc": "Build a fully accessible website following WCAG accessibility standards.", "level": "advanced", "points": 100, "skill": "HTML"},

        # CSS
        {"title": "Styled Card", "desc": "Design a card layout with borders, shadows, and hover effects.", "level": "easy", "points": 20, "skill": "CSS"},
        {"title": "Responsive Layout", "desc": "Build a responsive layout using Flexbox and Grid.", "level": "intermediate", "points": 50, "skill": "CSS"},
        {"title": "Animation Portfolio", "desc": "Create a portfolio website with advanced CSS animations and transitions.", "level": "advanced", "points": 100, "skill": "CSS"},

        # Tailwind CSS
        {"title": "Button Styling", "desc": "Style buttons using Tailwind utility classes.", "level": "easy", "points": 20, "skill": "Tailwind CSS"},
        {"title": "Responsive Card Grid", "desc": "Build a responsive card layout using Tailwind grid and spacing utilities.", "level": "intermediate", "points": 50, "skill": "Tailwind CSS"},
        {"title": "Full Landing Page", "desc": "Design a complete responsive landing page using only Tailwind CSS.", "level": "advanced", "points": 100, "skill": "Tailwind CSS"},

        # Node.js
        {"title": "Simple Server", "desc": "Create a basic Node.js server that responds with \"Hello World\".", "level": "easy", "points": 20, "skill": "Node.js"},
        {"title": "REST API", "desc": "Build a RESTful API with multiple endpoints using Express.", "level": "intermediate", "points": 50, "skill": "Node.js"},
        {"title": "Auth API System", "desc": "Create a secure API with JWT authentication and role-based access control.", "level": "advanced", "points": 100, "skill": "Node.js"},

        # Express.js
        {"title": "Express Routes", "desc": "Create basic routes using Express and return JSON responses.", "level": "easy", "points": 20, "skill": "Express.js"},
        {"title": "CRUD API", "desc": "Build a CRUD API connected to a database.", "level": "intermediate", "points": 50, "skill": "Express.js"},
        {"title": "Payment Integration", "desc": "Integrate a payment gateway into an Express backend securely.", "level": "advanced", "points": 100, "skill": "Express.js"},

        # SQL
        {"title": "Basic Queries", "desc": "Write SELECT, INSERT, UPDATE, and DELETE queries on a sample database.", "level": "easy", "points": 20, "skill": "SQL"},
        {"title": "Database Relations", "desc": "Design relational tables with foreign keys and perform JOIN queries.", "level": "intermediate", "points": 50, "skill": "SQL"},
        {"title": "Performance Optimization", "desc": "Optimize complex queries using indexes and query analysis tools.", "level": "advanced", "points": 100, "skill": "SQL"},

        # PostgreSQL
        {"title": "Database Setup", "desc": "Create a PostgreSQL database and insert sample data.", "level": "easy", "points": 20, "skill": "PostgreSQL"},
        {"title": "Stored Procedures", "desc": "Write stored functions and triggers.", "level": "intermediate", "points": 50, "skill": "PostgreSQL"},
        {"title": "Scalable Schema Design", "desc": "Design a scalable database schema for a large application.", "level": "advanced", "points": 100, "skill": "PostgreSQL"},

        # MongoDB
        {"title": "First Collection", "desc": "Create a collection and perform basic CRUD operations.", "level": "easy", "points": 20, "skill": "MongoDB"},
        {"title": "Aggregation Pipeline", "desc": "Use aggregation to generate reports from large datasets.", "level": "intermediate", "points": 50, "skill": "MongoDB"},
        {"title": "Distributed Database", "desc": "Design a scalable MongoDB cluster with replication and sharding.", "level": "advanced", "points": 100, "skill": "MongoDB"},

        # Git
        {"title": "First Commit", "desc": "Initialize a repo and make your first commit.", "level": "easy", "points": 20, "skill": "Git"},
        {"title": "Branching Workflow", "desc": "Create branches and merge them properly.", "level": "intermediate", "points": 50, "skill": "Git"},
        {"title": "Conflict Resolution", "desc": "Resolve complex merge conflicts in a team workflow.", "level": "advanced", "points": 100, "skill": "Git"},

        # GitHub
        {"title": "Push Your Project", "desc": "Push a local project to GitHub and manage commits.", "level": "easy", "points": 20, "skill": "GitHub"},
        {"title": "Pull Requests", "desc": "Create pull requests and review team code.", "level": "intermediate", "points": 50, "skill": "GitHub"},
        {"title": "CI/CD Pipeline", "desc": "Setup GitHub Actions to automate testing and deployment.", "level": "advanced", "points": 100, "skill": "GitHub"},

        # Docker
        {"title": "First Container", "desc": "Run a basic container and understand Docker commands.", "level": "easy", "points": 20, "skill": "Docker"},
        {"title": "Dockerized App", "desc": "Dockerize a full-stack application using Dockerfiles.", "level": "intermediate", "points": 50, "skill": "Docker"},
        {"title": "Multi-Container System", "desc": "Build a multi-service system using Docker Compose.", "level": "advanced", "points": 100, "skill": "Docker"},

        # AWS
        {"title": "EC2 Setup", "desc": "Launch and connect to a virtual server using AWS EC2.", "level": "easy", "points": 20, "skill": "AWS"},
        {"title": "S3 Storage App", "desc": "Store and retrieve files using AWS S3 buckets.", "level": "intermediate", "points": 50, "skill": "AWS"},
        {"title": "Scalable Cloud Architecture", "desc": "Design a scalable cloud infrastructure using AWS services.", "level": "advanced", "points": 100, "skill": "AWS"},

        # Firebase
        {"title": "Firebase Auth", "desc": "Setup email/password authentication using Firebase.", "level": "easy", "points": 20, "skill": "Firebase"},
        {"title": "Realtime Database App", "desc": "Build a realtime CRUD app using Firebase database.", "level": "intermediate", "points": 50, "skill": "Firebase"},
        {"title": "Serverless App", "desc": "Build a full serverless app using Firebase Functions and Hosting.", "level": "advanced", "points": 100, "skill": "Firebase"},

        # Machine Learning
        {"title": "First ML Model", "desc": "Train a simple linear regression model.", "level": "easy", "points": 20, "skill": "Machine Learning"},
        {"title": "Classification System", "desc": "Build a model that classifies emails as spam or not spam.", "level": "intermediate", "points": 50, "skill": "Machine Learning"},
        {"title": "Deep Learning Project", "desc": "Build and train a neural network for image recognition.", "level": "advanced", "points": 100, "skill": "Machine Learning"},

        # Data Science
        {"title": "Data Cleaning", "desc": "Clean and visualize a CSV dataset using Python.", "level": "easy", "points": 20, "skill": "Data Science"},
        {"title": "Data Analysis Report", "desc": "Analyze a dataset and generate insights using Pandas and Matplotlib.", "level": "intermediate", "points": 50, "skill": "Data Science"},
        {"title": "Predictive Analytics System", "desc": "Build a full predictive analytics pipeline from raw data to model deployment.", "level": "advanced", "points": 100, "skill": "Data Science"},
    ]

    for ch in challenges_data:
        skill_obj = skills[ch["skill"]]
        Challenge.objects.get_or_create(
            title=ch["title"],
            skill=skill_obj,
            defaults={
                "description": ch["desc"],
                "level": ch["level"],
                "points": ch["points"]
            }
        )

    # ---------- BADGES ----------
    badges_data = [
        {"name": "First Step", "description": "Complete your first challenge", "icon": "🥇"},
        {"name": "Python Beginner", "description": "Complete all easy Python challenges", "icon": "🐍"},
        {"name": "Django Starter", "description": "Complete your first Django challenge", "icon": "🌱"},
        {"name": "JS Rookie", "description": "Complete all easy JavaScript challenges", "icon": "🟨"},
        {"name": "React Starter", "description": "Complete your first React challenge", "icon": "⚛️"},
        {"name": "Vue Beginner", "description": "Complete all easy Vue.js challenges", "icon": "🖼️"},
        {"name": "HTML Novice", "description": "Complete all easy HTML challenges", "icon": "🌍"},
        {"name": "CSS Rookie", "description": "Complete all easy CSS challenges", "icon": "🎨"},
        {"name": "Tailwind Starter", "description": "Complete your first Tailwind CSS challenge", "icon": "💨"},
        {"name": "Node.js Beginner", "description": "Complete all easy Node.js challenges", "icon": "🟢"},
        {"name": "Express Starter", "description": "Complete your first Express.js challenge", "icon": "🚂"},
        {"name": "SQL Beginner", "description": "Complete all easy SQL challenges", "icon": "🗄️"},
        {"name": "PostgreSQL Starter", "description": "Complete your first PostgreSQL challenge", "icon": "🐘"},
        {"name": "MongoDB Beginner", "description": "Complete all easy MongoDB challenges", "icon": "🍃"},
        {"name": "Git Rookie", "description": "Complete your first Git challenge", "icon": "🔧"},
        {"name": "GitHub Starter", "description": "Complete your first GitHub challenge", "icon": "🐙"},
        {"name": "Docker Beginner", "description": "Complete all easy Docker challenges", "icon": "🐳"},
        {"name": "AWS Starter", "description": "Complete your first AWS challenge", "icon": "☁️"},
        {"name": "Firebase Starter", "description": "Complete your first Firebase challenge", "icon": "🔥"},
        {"name": "ML Beginner", "description": "Complete your first Machine Learning challenge", "icon": "🤖"},
    ]

    for b in badges_data:
        Badge.objects.get_or_create(
            name=b["name"],
            defaults={"description": b["description"], "icon": b["icon"]}
        )
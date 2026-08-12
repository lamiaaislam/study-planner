# study-planner
A full-stack, curriculum-aware study planning web application designed to help students organise their studies, track their progress and generate personalised study schedules.

## Project Overview

Study Planner is a university-level development of my original A-level Computer Science Study Planner project.

The original application was developed using Python, PyQt5 and SQLite. This project redesigns the application as a modern web application with a focus on scalability, usability, security and software engineering principles.

The application will allow students to:

- Create and manage an account
- Add their subjects and exam boards
- Select topics from their specific curriculum
- Track their confidence and progress across topics
- Create and manage study tasks
- Set their availability
- Record examination dates and deadlines
- View their study schedule through a calendar
- Generate personalised study plans
- Analyse their study progress

## Planned Features

- [ ] User registration and authentication
- [ ] Secure password hashing
- [ ] User profile management
- [ ] Subject management
- [ ] Curriculum and exam board selection
- [ ] Topic selection
- [ ] Topic confidence tracking
- [ ] Task management
- [ ] Study session management
- [ ] Availability management
- [ ] Calendar
- [ ] Automated study-plan generation
- [ ] Progress tracking and analytics
- [ ] Responsive web interface
- [ ] Testing
- [ ] Deployment

## Technology Stack

### Frontend

- React
- TypeScript
- Tailwind CSS

### Backend

- Python
- FastAPI

### Database

- PostgreSQL
- SQLAlchemy

### Testing

- pytest
- Vitest

### Development Tools

- Git
- GitHub
- VS Code

## Architecture

The application will use a client-server architecture:

```text
React + TypeScript
        │
        │ HTTP / REST API
        ▼
     FastAPI
        │
        ▼
   Application
     Services
        │
        ▼
   SQLAlchemy
        │
        ▼
   PostgreSQL

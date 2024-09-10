# Topics to be Covered


1. **Github Student Developer Pack**
2. **Dev Environment Setups**
3. **What is Backend ?**
4. **Introduction to Version Control System (VCS)**


## Github Student Developer Pack

Importance of Tools in Software Development
especially when working on large-scale projects, having access to the right tools is crucial. The tools provided through the GitHub Student Developer Pack are widely used in the industry and can significantly enhance your productivity and the quality of your work.

Key Tools Included in the Pack

**Integrated Development Environments (IDEs)**:

* **IntelliJ Ultimate**: A powerful IDE that supports multiple programming languages and frameworks. It’s especially useful for Java development, which is often used in backend systems. The Ultimate version, available through the pack, provides additional features that are critical for professional software development.
Cloud Services:

* **Azure Credits**: The pack includes $200 worth of credits for Microsoft Azure, allowing you to deploy and manage your applications in the cloud. Azure is a widely used cloud platform that supports various services like virtual machines, databases, and AI tools.
* **DigitalOcean Credits**: Similarly, the pack provides $200 in credits for DigitalOcean, another cloud service provider known for its simplicity and ease of use, particularly for deploying web applications.

**Domain Registration**:

**Free Domains**: The pack includes registration for two free domains, which you can use to host your websites or web applications. This is particularly useful for showcasing your projects to potential employers or clients.

**Benefits of the Github Student Developer Pack**:

The GitHub Student Developer Pack offers a full year of access to these premium tools at no cost, which is an incredible opportunity for students. This allows you to experiment with professional-grade tools and services without worrying about the financial burden, giving you a head start in your software development career.

## Dev Environment Setup

**Tools to Install**
Before the next class, ensure that you have the following tools installed and configured correctly:

* **Git**: Git is a version control system that will be essential for managing your code throughout the course. Make sure it’s installed and that you’re familiar with the basics of using it.
* **VS Code**: Visual Studio Code (VS Code) is a popular code editor that you’ll use for writing and editing your code. It’s lightweight, highly customizable, and supports a wide range of programming languages and extensions.
* **Java 17**: Install Java 17, as it is the version supported by Springboot and AWS (Amazon Web Services). Note that newer versions of Java are not yet supported by AWS, while older versions are not supported by Springboot, so it’s important to use this specific version.
* **IntelliJ Ultimate**: Use the GitHub Student Developer Pack to obtain a license for IntelliJ Ultimate, an IDE that you’ll use for more complex development tasks. Follow these steps:
    * Install the JetBrains Toolbox App.
    * Use the Toolbox to install IntelliJ Ultimate.

## Backend

**Why These Tools ?**
Each of these tools is chosen to ensure that you have a professional-grade development environment. This will not only make the learning process smoother but also prepare you for working in real-world software development environments.

* What is Backend and How Does the System Work?
* Frontend vs. Backend

In any web application, the system is divided into two main parts:

**Frontend (Client)**: The frontend, or client-side, is what the user interacts with directly. This includes everything from the design of a webpage to the buttons and forms that users interact with. It’s all about creating a user-friendly interface that is both visually appealing and functional.

**Backend (Server)**: The backend, or server-side, is where all the behind-the-scenes work happens. The backend handles the business logic, processes user requests, interacts with the database, and sends responses back to the frontend. It’s the backbone of any web application, making sure everything runs smoothly and efficiently.
Example: Google Search Suggestions

To understand how the frontend and backend work together, let’s consider the example of Google search suggestions:

When you start typing in the Google search bar, the frontend sends a request to the backend to fetch suggestions based on what you’ve typed so far.
The backend, which can be thought of as a large server or a network of servers, processes this request, quickly retrieves relevant suggestions from the database, and sends them back to the frontend.
The frontend then displays these suggestions in real-time as you continue typing.

**Key Components of a Web System**

**UI Layer (Frontend)**:

The UI layer is responsible for presenting data in a way that is easy for users to understand and interact with. However, it doesn’t hold or process any data itself. It simply sends requests to the backend and displays the responses it receives.
Backend Layer:

The backend layer is where all the critical processing happens. It includes the business logic, which determines how data should be processed, stored, and retrieved. The backend owns the data and manages the database, ensuring that everything the frontend needs is delivered accurately and efficiently.

**Request-Response Cycle**
Most web applications operate on a request-response cycle, which works as follows:

The frontend (client) sends a request to the backend (server) via the internet.
The backend receives the request, processes it (often by querying a database or executing business logic), and generates a response.
The frontend then receives this response and updates the user interface accordingly.
This cycle happens quickly, often in milliseconds, and is fundamental to how modern web applications function.

**The Importance of VCS in Team Collaboration** : In a typical software development team, multiple developers often work on the same codebase simultaneously. Without a Version Control System (VCS), this can lead to numerous issues, such as overwriting each other’s work or losing track of changes. VCS is essential for managing these challenges, ensuring that all changes are tracked and that developers can work together efficiently.

### Common Issues Without VCS
Consider a scenario where you and a teammate are both working on the same file:

**Conflict**: You might implement a new feature, while your teammate is fixing a bug in the same file. If you both try to save your changes without VCS, one of you might overwrite the other’s work, causing loss of progress and potential reintroduction of bugs.

**Lack of Tracking**: Without VCS, it’s difficult to know who made specific changes, when they were made, or why they were necessary. This lack of visibility can make debugging and collaboration much harder.

## How VCS Solves These Issues

* **Tracking Changes**:VCS tracks every change made to the codebase, recording who made the change, when it was made, and why. This creates a detailed history of the project’s development, which is invaluable for collaboration and debugging.
* **Merging Work**: VCS allows multiple developers to work on the same codebase simultaneously. When developers push their changes, VCS merges them into a single version, resolving conflicts and ensuring that no work is lost.
* **Reverting to Previous Versions** : If a recent change introduces a bug or causes issues, VCS allows you to revert to an earlier, stable version of the code. This ability to roll back changes is crucial for maintaining the integrity of the codebase.


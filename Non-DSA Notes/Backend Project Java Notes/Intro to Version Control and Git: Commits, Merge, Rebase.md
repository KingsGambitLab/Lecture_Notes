
## Topics to be covered

1. Types of Version Control Systems (VCS)
2. Understanding Commits in Git
3. Working with Branches in Git
4. Merge Operations in Git
5. Rebase in Git

### The Need for Version Control Systems
Version control systems (VCS) are essential tools in software development, providing a way to manage and track changes to code over time. They address several key needs:

- **Collaboration:** When multiple developers work on a project, VCS helps manage changes made by different people, ensuring that code can be merged and integrated smoothly.
- **Historical Reference:** VCS allows developers to go back to previous versions of the codebase. This is useful for debugging, understanding the evolution of the code, or reverting to a stable version after introducing new changes.
- **Version Tracking:** It enables developers to see who made changes, what changes were made, and why those changes were made, through detailed logs and history tracking.

### Types of Version Control Systems
There are two main types of version control systems: Centralized and Distributed.

#### Centralized Version Control System (CVCS)
- **Overview:**
  - In a centralized version control system, there is a single, central server that contains the entire codebase and its history. Developers must connect to this server to retrieve the latest version of the code and to push their changes.
  - This central server acts as a hub for all versioning activities.
  
- **Example:** 
  - **Google Docs** is an analogy for understanding CVCS. When working on a document in Google Docs, all changes are saved on Google’s servers. If the internet connection is lost, users cannot make further changes until the connection is restored.
  
- **Workflow:**
  - Developers must always be connected to the central server to perform any version control tasks, such as committing changes, viewing history, or updating to the latest version.

- **Issues with CVCS:**
  - **Internet Dependency:** If the server is inaccessible (e.g., due to network issues), no work can be done.
  - **Single Point of Failure (SPOF):** The central server is a single point of failure. If it crashes or becomes corrupted, the entire project may be at risk.

#### Distributed Version Control System (DVCS)
- **Overview:**
  - In a distributed version control system, each developer has a full copy of the codebase, including its complete history, on their local machine. This system eliminates the need to be constantly connected to a central server.
  
- **Workflow:**
  1. **Initial Setup:** The developer connects to the central server to clone the entire codebase onto their local machine.
  2. **Local Development:** They can work independently, making changes and committing them locally.
  3. **Synchronization:** When ready, the developer can push their changes back to the central server to share them with others.

- **Advantages of DVCS:**
  - **Offline Work:** Developers can work offline, without needing to be constantly connected to the central server.
  - **Resilience:** Since every developer has a complete copy of the codebase, there is no single point of failure. If the central server goes down, work can continue, and the server can be restored from any developer’s copy.

- **Disadvantages of DVCS:**
  - **Storage:** The need to clone the entire codebase, including its history, can be a burden, especially for large projects. This might require substantial disk space and can be time-consuming.

#### Git as a Distributed Version Control System
- **Git** is an example of a DVCS and is widely used in the software industry.
- **Origin:** Git was created by Linus Torvalds, the creator of Linux, to manage the development of the Linux kernel.
- **Popularity:** It is used by millions of developers worldwide and is known for its scalability, robustness, and flexibility.

---

## 2. Understanding Commits in Git

### Definition of a Commit
- A **commit** in Git represents a snapshot of your changes in the codebase at a particular point in time. When you make changes to files in your Git repository and then commit those changes, you are essentially taking a snapshot of your project that you can return to later if needed.

### How to Make a Git Commit
1. **Prepare Your Environment:**
   - First, create a new folder for your project and add some files that you want to version control.
   - Write code or make changes in these files.

2. **Initialize a Git Repository:**
   - Open a terminal and navigate to your project folder.
   - Run the command `git init`. This initializes a new Git repository in your project folder. A hidden `.git` directory is created, which Git uses to store all the information about the version control for your project.

3. **Stage Your Changes:**
   - Before you can commit your changes, you need to stage them. This means telling Git which changes you want to include in the next commit.
   - Use the command `git add filename` to stage specific files, or `git add .` to stage all changes in the project folder.

4. **Commit Your Changes:**
   - Once your changes are staged, you commit them with a descriptive message using the command:
     ```
     git commit -m "Your descriptive commit message"
     ```
   - The commit message should clearly describe the changes made. For example, if you fixed a bug, your message might be `"Fixed critical bug in user authentication"`.
   - This command creates a new commit object in the Git repository, which includes the staged changes, the author’s details, a timestamp, and the commit message.

5. **View Commit History:**
   - After making a few commits, you can view the history of your commits using:
     ```
     git log
     ```
   - This command shows a list of all commits made in the repository, along with their commit messages, authors, and timestamps.

### Properties of a Git Commit
- **Immutability:** 
  - Once a commit is made, it cannot be changed. This ensures the integrity of the version history.
  
- **Permanent History:**
  - Every commit is a permanent part of the project’s history. Even if you delete or undo changes, the commit itself remains in the history.

- **Reverting Changes:**
  - If you need to revert to a previous state of your project, you can create a new commit that undoes the changes from a previous commit. This does not delete the original commit but adds a new one that brings the project back to an earlier state.

- **Handling Sensitive Information:**
  - Be cautious not to commit sensitive information (like passwords or API keys), as it will become part of the permanent history and cannot be easily removed.

### How Git Stores Commits
- Git uses a **delta-based storage** approach to manage commits efficiently:
  - **Option 1: Full Snapshot:** In theory, Git could save a complete copy of the codebase with each commit. While this would make it easy to retrieve any version, it would result in an extremely large repository.
  - **Option 2: Delta Storage:** Instead, Git saves only the differences (or deltas) between each commit and its predecessor. This approach significantly reduces the amount of storage required.
  - **Linked List Structure:** Git organizes commits in a linked list-like structure, where each commit points to its parent. To reconstruct the state of the code at any point in history, Git starts from the desired commit and applies all previous changes in sequence.

---

## 3. Working with Git Branches

### What is a Git Branch?
- A **branch** in Git is essentially a pointer to a specific commit in the repository. Branches allow developers to work on different parts of a project simultaneously without interfering with each other’s work.

### Use Case for Branches
- Consider a scenario where two developers, P1 and P2, are working on different features of a project. P1 is tasked with adding a calculator to an app, while P2 is working on video streaming functionality for the website.
- These two tasks are independent of each other, and it would be inefficient and potentially problematic for both developers to work on the same branch.
- Instead, each developer should create a separate branch for their work. This allows them to work in isolation, with each branch containing only the changes relevant to its specific task.

### Steps to Work with Branches

1. **Create a New Branch:**
   - To create a new branch, use the command:
     ```
     git branch branch_name
     ```
   - For example, if P1 wants to create a branch for the calculator feature, they might use:
     ```
     git branch calculator-feature
     ```

2. **Switch to the New Branch:**
   - After creating the branch, you need to switch to it to start working on it. Use the command:
     ```
     git checkout branch_name
     ```
   - Continuing the example, P1 would use:
     ```
     git checkout calculator-feature
     ```

3. **Make Changes and Commit:**
   - Now that you are on the new branch, any changes you make and commit will be recorded in this branch, keeping them isolated from the main branch (often called `main` or `master`).

4. **View Branches:**
   - To see a list of all branches in

 the repository, use:
     ```
     git branch
     ```
   - The currently active branch will be highlighted with an asterisk (*).

5. **Create and Switch in One Step:**
   - You can also create a new branch and switch to it in one command:
     ```
     git checkout -b branch_name
     ```
   - For example, if P2 wants to create and switch to a branch for video streaming, they might use:
     ```
     git checkout -b video-streaming-feature
     ```

### Visualizing Branches
- Git branches can be visualized as a tree structure. The main branch is the trunk, and each new branch is like a limb growing from the trunk. When developers finish their work on a branch, they typically merge it back into the main branch, reintegrating the changes into the main project.

### Importance of Branches in Git Workflow
- **Isolation of Work:** Each branch allows a developer to work on a specific feature or bug fix in isolation, without affecting the main codebase.
- **Parallel Development:** Multiple developers can work on different features simultaneously, each on their own branch.
- **Safe Experimentation:** Developers can experiment with new ideas or code changes on a separate branch without risking the stability of the main branch.

### Ensuring Commit Integrity with Branches
- Git maintains the integrity of branches by using commit IDs, which are unique hashes generated based on the contents of the commit, its parent, the timestamp, and the author. If any part of the commit is altered, the commit ID changes, ensuring that all commits remain immutable and traceable.

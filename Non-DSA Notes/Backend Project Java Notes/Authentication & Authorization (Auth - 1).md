## Topics to be Covered
- **What is Authentication?**
- **What is Authorization?**
  - Introduction to **Role-Based Access Control (RBAC)**
- **How the Authentication Flow Works**:
  - Authentication within a single service
  - Password encoding using **Bcrypt**
  - Handling authentication as a separate service
  - Introduction to **JWT (JSON Web Token)** and **OAuth 2.0**
- **Start Implementing a User Service**

---

### What is Authentication and Authorization?

#### What is Authentication?

**Authentication** is the process of identifying who the user is. For example, when you visit a website, such as **Scaler**, you can browse general pages like event listings (e.g., `scaler.com/events`), but to access specific sections, the website needs to verify your identity.

##### Example: Scaler Website
- Anyone can visit Scaler's event page (e.g., `scaler.com/events/become-a-data-engineer`) without logging in or providing personal information.
- However, for more sensitive sections like live event links (e.g., `scaler.com/meetings/...`), Scaler must know **who** is trying to access the page.
- **[Question]**: Should Scaler allow anyone to access the meeting link without verifying who they are?
    - **Answer**: No. Only authenticated users (those who have logged in and verified their identity) can access this content.

##### Example: Hospital Analogy
- **General Access**: Anyone with a valid ID can enter the hospital.
- **Restricted Access**: However, only **authorized** individuals, such as medical personnel, can enter the operation theatre. Not everyone with an ID is permitted to access every part of the hospital.

Similarly, Scaler uses authentication to identify users. After authentication, different permissions are granted based on the user’s role or status, which leads us to **authorization**.

#### What is Authorization?

Once a user is **authenticated** (i.e., the system knows who they are), the next step is **authorization**. This is the process of determining whether the authenticated user has the necessary **permissions** or **roles** to access specific resources or perform certain actions.

##### Example: Admin Pages on Scaler
- A regular authenticated user might have access to general sections like events or courses.
- However, pages like `scaler.com/admin/...` are restricted to **administrators** only. Even though a user is authenticated, they must have the correct **role** (in this case, admin) to access this page.

#### Key Concepts:
1. **Authentication**: The process of confirming your identity (e.g., via a login system with an email and password).
2. **Authorization**: The process of determining if you have permission to access certain resources after your identity has been confirmed.  
   - **Authorization = Authentication + Role Checking**

##### Example: Movie Booking Website
![Movie Booking Website](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/669/original/1.png?1725530379)

In this example, logging into the movie website is the **authentication** step, while being able to book tickets or manage the admin dashboard depends on the user’s **authorization** or roles.

---

### Role-Based Access Control (RBAC)

#### What is Access Control?
Access control refers to **authorization**—deciding **who** can access **what** within a system. It is a critical security concept in any system that manages sensitive data or controls certain privileges.

#### What is Role-Based Access Control (RBAC)?

In an organization, users typically have different roles, and each role has a specific set of permissions associated with it. **RBAC** means that the system grants access to users based on the roles assigned to them. This is a more manageable and scalable way to handle access control compared to assigning permissions to individual users.

##### Example: Roles in Scaler
At Scaler, there are various roles such as:
- **Admin**: Full access to administrative features.
- **Mentee**: Access to course materials and classes.
- **Mentor**: Access to mentee progress and feedback tools.
- **Teaching Assistant (TA)**: Support role with access to student assignments.
- **Instructor**: Facilitates teaching with full course management permissions.

#### Characteristics of RBAC:
- A user can have multiple roles (e.g., a mentor might also be an admin).
- A single role can be assigned to multiple users (e.g., many users can have the "TA" role).
- This creates a **many-to-many (m:m) relationship** between users and roles.

![RBAC Diagram](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/670/original/2.png?1725530401)

#### Key Function of RBAC:
- If a user possesses the required role for a resource (e.g., Admin role for accessing the admin panel), access is granted. If not, the system denies access.

---

### How the Authentication Flow Works

#### Trusting User Identity:
For websites to operate securely, they must be able to **trust** the identity of the users accessing them. Simply knowing the email ID is not enough to verify someone’s identity, just as showing an ID card is not enough to bypass certain security protocols in real life.

##### Example: Security Guard and Identity Card
- Just as a security guard may inspect not only your ID card but also match it with your face or fingerprint, websites use additional methods to verify users (e.g., via passwords or OTPs).

#### Two Key Elements of Authentication:
1. **Unique Identifier**: For websites, this is usually an email or phone number.
2. **Validation Method**: This could be a password, OTP (One-Time Password), or a verification link sent to the user.

#### Signup Process
1. **Create an Account**: User provides details like name and email.
2. **Verification**: Website sends a verification email to ensure the provided email is valid.
3. **Password Setup**: Once verified, the user sets up a password, which will be used for future logins.

#### Login Process
- User inputs their email and password.
- The website checks its database to see if the email and password combination matches any existing record.
- If a match is found, the user is authenticated. Otherwise, the login attempt fails.

![Login Flow](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/671/original/3.png?1725530420)

#### Problems with Plain Password Storage:
- If the server's database is compromised (hacked), the attackers can steal all users' email-password combinations. This is especially risky if users reuse passwords across different sites.
  
- **Potential Solution**: Don't store passwords in plain text. Instead, store a **hashed** version of the password using encryption algorithms.

---

### Hashing and Salting: Securing Passwords

#### Password Hashing with Bcrypt

**Bcrypt** is a widely-used password-hashing function designed to store passwords securely. It is more secure than basic hashing functions like MD5 because it generates a unique hash each time, even if two users have the same password.

#### Bcrypt Methods:
1. **.encode()**: Encodes the password into an encrypted value.
2. **.verify()**: Compares the encrypted value to the password provided by the user during login.

##### Example: Password Encoding
- When a user creates a password, the server uses `bcrypt.encode(password)` to generate a unique, encrypted string (hash) and stores it in the database.

![Bcrypt Encoding Example](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/672/original/4.png?1725530439)

##### Verifying Passwords:
- **Question**: Can we re-encode the password at login and compare it to the stored hash?  
  **Answer**: No, because bcrypt generates a unique hash every time. Instead, bcrypt’s `.verify()` method checks whether the original password could have generated the stored hash.

![Bcrypt Verification](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/674/original/5.png?1725530464)

#### Salting:
- **Salting** adds extra information to the password before hashing it, such as the user’s email, server ID, or timezone. This makes it even harder for attackers to reverse-engineer the password, even if they have the hashed value.

---

### Tokens and JWT (JSON Web Token)

#### The Problem Without Tokens:
HTTP is a **stateless protocol**, meaning each request sent to the server is treated as independent. Without tokens, users would need to authenticate (e.g., by sending their email and password) every time they request a resource from the server. This would involve repeated database lookups and password validations, which can slow down the application.

#### Solution: Tokens

Tokens help solve this issue by allowing users to authenticate once and then use a **token** for subsequent requests, avoiding repeated email-password checks.

##### Analogy: Park Entry Band
- When you visit a park, you buy a ticket and are given a **wristband** that grants you access to all rides without having to buy separate tickets each time. The token functions similarly, granting you access to the website without repeatedly entering your credentials.

#### How Tokens Work:
1. After a successful login, the server generates a **token** and sends it back to the user. This token is stored on the user's device (typically in cookies or local storage).
2. The token is sent with every subsequent request to the server, which verifies it against its own records.
3. Tokens have an **expiry time**, just like how a park band is valid for a limited period. Once expired, the user must log in again.

#### Security Concerns:
- **Token Hijacking**: If someone steals your token (just like stealing your park band), they could impersonate you.
  - **Solution**: The server can check

 the IP address associated with the token to prevent unauthorized use from different locations.

---

### JSON Web Token (JWT)

JWT is a more advanced type of token that includes encoded user information (such as user ID, expiration time, and IP address) directly within the token itself. This reduces the need for the server to make additional database calls to verify the token, resulting in faster responses.

#### JWT Structure:
- JWT consists of three parts:
  1. **Header**: Specifies the token type and encryption algorithm.
  2. **Payload**: Contains the encoded data (e.g., user ID, roles).
  3. **Signature**: Ensures the token hasn’t been tampered with.

![JWT Structure](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/675/original/6.png?1725530481)

#### Benefits of JWT:
- The server can verify the token without querying the database, improving performance.
- JWTs are signed and secured to prevent tampering.

#### JWT Security:
- If someone tries to modify a JWT, the signature check will fail, and the token will be invalidated.
  

## Topics to be covered

*  Implementation of User Service

---

## Implementing Signup Functionality

### Overview of Signup

The **signup** functionality is a critical component of any user service, where new users can register by providing their details, such as email, password, and name. Here, we’ll implement the signup functionality by ensuring that the user's password is securely stored in the database. 

**Security** is the key concern in signup implementations, especially how passwords are handled. Instead of storing plain-text passwords, we use a **password hashing algorithm** called `bcrypt`, which transforms the plain password into an irreversible hash. This way, even if someone gains access to the database, they cannot retrieve the original passwords.


### Step-by-Step Implementation

1. **Implement `bcrypt` Password Encoder**: 
   - Use the `bcrypt` hashing algorithm to encode passwords before saving them to the database. This provides security by ensuring that even if the database is compromised, the passwords cannot be easily decoded.
   
   **Why `bcrypt`?** 
   - It is a widely used hashing function designed specifically for hashing passwords, offering features like a salt to defend against rainbow table attacks and a configurable work factor to adjust the computational cost.

2. **Allow All Requests Temporarily**: 
   - In the `SecurityConfiguration` class, temporarily allow all incoming HTTP requests. This step is necessary during development and testing to simplify access without authentication.

3. **Resolve CORS Issues**:
   - Ensure Cross-Origin Resource Sharing (CORS) policies are configured to allow requests from tools like Postman. CORS restrictions might prevent external clients from accessing resources, so removing these restrictions aids testing.

4. **Testing with Postman**:
   - Use Postman to make a `POST` request to the signup API endpoint. Postman allows us to send HTTP requests with a JSON body containing the user's email, password, and name, and observe the response.

5. **Use `bcrypt` with Different Key Values**:
   - Experiment with `bcrypt` by using different key values to explore how password encryption changes and observe the resulting hashed passwords.

### Code Implementation

The signup feature is implemented using two main components: a controller to handle incoming HTTP requests and a service that contains the business logic.

#### Controllers Code (Signup)
The controller manages the HTTP request for user signup and forwards it to the service layer for processing.
```java
@PostMapping("/signup")
public UserDto signUp(@RequestBody SignUpRequestDto request) {
    // Extract email, password, and name from the request object
    String email = request.getEmail();
    String password = request.getPassword();
    String name = request.getName();

    // Pass the extracted values to the signUp method in the service layer
    return UserDto.from(userService.signUp(name, email, password));
}
```

- **Explanation**:
   - The `@PostMapping("/signup")` annotation maps this method to a POST HTTP request for the `/signup` endpoint.
   - `@RequestBody` indicates that the request body contains JSON data (user's email, password, and name) that will be deserialized into a `SignUpRequestDto` object.
   - The signup request data is passed to the service layer for processing.
   - The response is converted into a `UserDto` object, which is then returned to the client.

#### Service Code (Signup)
The service handles the logic of storing the new user in the database after hashing their password.
```java
public User signUp(String fullName, String email, String password) {
    // Create a new User object and set its attributes
    User u = new User();
    u.setEmail(email);
    u.setName(fullName);
    
    // Hash the user's password using bcrypt before saving it to the database
    u.setHashedPassword(bCryptPasswordEncoder.encode(password));

    // Save the user object to the database and return the saved user
    User user = userRepository.save(u);
    return user;
}
```

- **Explanation**:
   - A new `User` object is created, and its `email`, `name`, and `hashedPassword` attributes are set.
   - The `password` is hashed using the `bCryptPasswordEncoder.encode()` method before being stored in the `hashedPassword` field.
   - The `userRepository.save(u)` method saves the new user to the database and returns the saved user object.

For more details on the structure of DTOs (Data Transfer Objects) and the complete project code, refer to the [GitHub repository](https://github.com/Naman-Bhalla/userservicemwfeve).

---

## Implementing Login Functionality

### Overview of Login

Login functionality allows users to authenticate themselves by providing their registered email and password. To ensure security, we verify the password against the stored hashed password using `bcrypt`. On successful authentication, the system generates a token that can be used to authenticate future requests.

### Key Steps for Login

1. **Find the User by Email**:
   - When a login request is made, the system first searches for the user in the database using the provided email address.
   
2. **Verify the Password**:
   - If the user is found, the next step is to compare the provided password with the stored hashed password using the `bcryptPasswordEncoder.matches()` method. This method returns `true` if the passwords match, ensuring that the user has provided the correct password.

3. **Generate a Token**:
   - Once the password is verified, a new token is generated. This token will be used to authenticate future requests made by the user. For now, we can generate a simple random string, but later we will replace this with a JWT token for better security and functionality.

### Code Implementation

#### Controllers Code (Login)
The controller handles the incoming login request and delegates it to the service.
```java
@PostMapping("/login")
public Token login(@RequestBody LoginRequestDto request) {
    // Pass email and password from the request to the login service method
    return userService.login(request.getEmail(), request.getPassword());
}
```

- **Explanation**:
   - Similar to the signup process, `@PostMapping("/login")` maps this method to handle POST requests at the `/login` endpoint.
   - The email and password are extracted from the `LoginRequestDto` object and passed to the service for validation.

#### Service Code (Login)
The service handles the login logic by checking the credentials and generating a token if the login is successful.
```java
public Token login(String email, String password) {
    // Find the user by email in the database
    Optional<User> userOptional = userRepository.findByEmail(email);

    // If user does not exist, return null or throw an exception
    if (userOptional.isEmpty()) {
        return null;
    }

    User user = userOptional.get();

    // Verify if the provided password matches the stored hashed password
    if (!bCryptPasswordEncoder.matches(password, user.getHashedPassword())) {
        return null;
    }

    // Generate a token for the user
    Token token = getToken(user);

    // TODO 1: Replace the random token with a JWT token in future
    Token savedToken = tokenRepository.save(token);

    return savedToken;
}
```

- **Explanation**:
   - The `userRepository.findByEmail(email)` method checks if a user with the provided email exists in the database. If not, the method returns null or throws an appropriate exception.
   - The `bcryptPasswordEncoder.matches(password, user.getHashedPassword())` method checks if the provided password matches the stored hashed password.
   - If the password matches, the `getToken()` method generates a new token for the user, which is then saved in the database.

#### `getToken` Method
This method generates a token with a 30-day expiration date.
```java
private static Token getToken(User user) {
    // Set the token expiration date to 30 days from the current date
    LocalDate today = LocalDate.now();
    LocalDate thirtyDaysLater = today.plus(30, ChronoUnit.DAYS);
    
    // Convert LocalDate to Date
    Date expiryDate = Date.from(thirtyDaysLater.atStartOfDay(ZoneId.systemDefault()).toInstant());

    // Create a new Token object
    Token token = new Token();
    token.setUser(user);
    token.setExpiryAt(expiryDate);

    // Generate a random alphanumeric token value
    token.setValue(RandomStringUtils.randomAlphanumeric(128));

    return token;
}
```

- **Explanation**:
   - The `getToken()` method generates a token object, associating it with the user and setting an expiration date 30 days from the current date.
   - The token value is a randomly generated alphanumeric string of 128 characters.

---

## Implementing Logout Functionality

### Overview of Logout

Logout functionality ensures that when a user logs out, their authentication token is invalidated. This can be done in two ways:
1. **Physically delete the token** from the database.
2. **Mark the token as "deleted"** using a `deleted` flag. This approach is preferred because it allows for easier debugging and analysis of past token data.

### Key Steps for Logout

1. **Invalidate the Token**:
   - Instead of deleting the token, we use a `deleted` flag to mark it as invalid. This way, the token data remains in the database but is no longer valid for future authentication.

### Code Implementation

#### Controllers Code (Logout)
```java
@PostMapping("/logout")
public ResponseEntity<Void> logout(@RequestBody LogoutRequestDto request) {
    // Call the logout method in the service layer to invalidate the token
    userService.logout(request.getToken());
    return new ResponseEntity<>(HttpStatus.OK);
}
```

- **Explanation**:
   - The `/logout` endpoint receives a `POST` request with the token to be invalidated. 
   - The token is passed to the service layer to be marked as invalid.

#### Service Code (Logout)
```java
public void logout(String token) {
    // Find the token in the database where it has not been deleted
    Optional<Token> token1 = tokenRepository.findByValueAndDeletedEquals(token, false);

    // If the token does not exist or is already deleted, do nothing or throw an exception
    if (token1.isEmpty()) {
        return;
    }

    // Mark the token as deleted
    Token tkn = token1.get();
    tkn.setDeleted(true);

    // Save the updated token back to the repository
    tokenRepository.save(tkn);
}
```

- **Explanation**:
   - The token is located in the database by its value, and only tokens that have not been marked as deleted are considered.
   - If the token is found, its `deleted` field is set to `true`, invalidating it.
   - The updated token is saved back to the database, effectively logging the user out.

---

## Implementing Token Validation

### Overview of Token Validation

Token validation is essential to ensure that only authenticated users can access protected resources. Before processing any request, the system checks the token to ensure it is valid. A token is considered valid if:
- It has **not been marked as deleted** (i.e., the `deleted` field is `false`).
- It has an **expiry date that is later than the current date**.

This method ensures that only valid, non-expired tokens can be used for authentication.

### Key Steps for Token Validation

1. **Check if the Token is Deleted**:
   - The `deleted` flag must be `false`, meaning the token has not been invalidated.
2. **Check Expiry Date**:
   - The token's expiry date must be in the future.
3. **Return User Details**:
   - If the token is valid, return the user details associated with the token.

### Code Implementation

#### Controllers Code (Validate Token)
```java
@PostMapping("/validate/{token}")
public UserDto validateToken(@PathVariable("token") @NonNull String token) {
    // Pass the token to the service layer for validation
    return UserDto.from(userService.validateToken(token));
}
```

- **Explanation**:
   - This method handles token validation requests, passing the token to the service for verification.

#### Service Code (Validate Token)
```java
public User validateToken(String token) {
    // Search for a valid token in the database
    Optional<Token> tkn = tokenRepository
            .findByValueAndDeletedEqualsAndExpiryAtGreaterThan(token, false, new Date());

    // If the token does not exist or is invalid, return null
    if (tkn.isEmpty()) {
        return null;
    }

    // TODO 2: In the future, replace this with JWT validation instead of DB validation
    return tkn.get().getUser();
}
```

- **Explanation**:
   - The service checks if the token exists, is not deleted, and is still within its valid time period (i.e., the expiry date is greater than the current date).
   - If the token is valid, it retrieves and returns the associated user details.

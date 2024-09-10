## Topics to be Covered

- **Implementing Authentication and Authorization with Spring Security**
- **Hands-on implementation using the **Spring Security framework** and **OAuth2** for token-based security**
## Token Validation in ProductService

### Token Validation Workflow in a Secured Service

1. **Token Generation**: Tokens are generated in the `UserService` during the authentication process. This token is essential for accessing protected resources across services.
   
2. **Token Usage in ProductService**: 
   - Whenever a user interacts with the `ProductService`, they must send the token (usually as a header in the HTTP request).
   - The `ProductService` will receive this token and proceed to validate it before processing the request.

3. **Token Verification Process**: 
   - The first step for `ProductService` is to validate the token. This ensures that the token is legitimate and has not expired.
   - If token verification **fails**, the system should deny access by returning an HTTP **403 Forbidden** status.
   - If token verification **succeeds**, the user is granted access to the requested resources.

4. **Role-Based Authorization**:
   - Beyond token verification, the service can also check the **role** associated with the user (e.g., admin, regular user).
   - This is essential for determining **access levels**. For instance:
     - **Admins** may be allowed to view and manage all products.
     - **Regular users** may have restricted access to certain details.
   - Based on the user's role, the system can enforce role-specific policies such as showing only relevant information or restricting certain actions.

#### Code Example: Token Validation in `AuthenticationCommons`

The code below shows how `AuthenticationCommons` handles token validation using an HTTP call to the user service.

```java
package com.scaler.productservicedecmwfeve.commons;

import com.scaler.productservicedecmwfeve.dtos.UserDto;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class AuthenticationCommons {
    private RestTemplate restTemplate;

    public AuthenticationCommons(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public UserDto validateToken(String token) {
        // Send an HTTP POST request to the UserService for token validation
        ResponseEntity<UserDto> userDtoResponse = restTemplate.postForEntity(
                "http://localhost:8181/users/validate/" + token,
                null, // No body needed for validation
                UserDto.class // Expecting a UserDto object as a response
        );

        // If no user is found, return null, which implies invalid token
        if (userDtoResponse.getBody() == null) {
            return null;
        }

        // If validation is successful, return the UserDto
        return userDtoResponse.getBody();
    }
}
```

- The `validateToken` method sends a request to the user service to validate the token. If the user service returns a valid user (`UserDto`), access is allowed; otherwise, it denies the request.

#### Code Example: Role-Based Authorization in `ProductController`

Here, we demonstrate how `ProductController` uses the validated token to enforce role-based access.

```java
public ResponseEntity<List<Product>> getAllProducts() {
    // Validate the token using AuthenticationCommons
    UserDto userDto = authenticationCommons.validateToken(token);

    // If the token is invalid, return 403 Forbidden
    if (userDto == null) {
        return new ResponseEntity<>(HttpStatus.FORBIDDEN);
    }

    // Check if the user is an admin
    boolean isAdmin = false;
    for (Role role : userDto.getRoles()) {
        if (role.getName().equals("ADMIN")) {
            isAdmin = true;
            break;
        }
    }

    // If the user is not an admin, return 401 Unauthorized
    if (!isAdmin) return new ResponseEntity<>(HttpStatus.UNAUTHORIZED);

    // Fetch all products
    List<Product> products = productService.getAllProducts();

    // Modify the product titles as per business logic (optional)
    List<Product> finalProducts = new ArrayList<>();
    for (Product p : products) {
        p.setTitle("Hello " + p.getTitle());  // Example modification
        finalProducts.add(p);
    }

    // Return the modified list of products
    return new ResponseEntity<>(finalProducts, HttpStatus.OK);
}
```

In this example:
- **Step 1**: Validate the token using `AuthenticationCommons`.
- **Step 2**: If validation fails, return `403 Forbidden`.
- **Step 3**: If validation succeeds, check if the user is an admin.
- **Step 4**: If the user is not an admin, return `401 Unauthorized`; otherwise, proceed with fetching and modifying the products.
- **Step 5**: Return the list of modified products with an `HTTP 200 OK` status.

---

## Implementing Authentication and Authorization Using Spring Security

### Why Use Spring Security?

- Implementing custom token validation, login, signup, and role management can lead to complex, repetitive code.
- **Spring Security** provides a standardized and robust way to handle all these functionalities with less effort.
- It comes with built-in support for common security concerns like token validation, role-based access, OAuth2, and more.

### Introduction to OAuth2

**OAuth2** is an industry-standard protocol for authorization. It enables applications to obtain limited access to user accounts on an HTTP service, such as Facebook or Google.

- **Key Components of OAuth2**:
  1. **User**: The person or system accessing the application.
  2. **Authorization Server**: The system responsible for authenticating the user and issuing access tokens.
  3. **Resource Server**: The server that contains the resources being accessed (e.g., ProductService).
  4. **Application**: The application (client) that the user interacts with, which requests authorization on their behalf.

#### Spring Security Authorization Server

- **Spring Security** provides built-in support for OAuth2, including an **Authorization Server** implementation.
- You can implement your own **Authorization Server** to handle user authentication and issue tokens.
- Refer to this [Github Repository](https://github.com/Naman-Bhalla/userservicemwfeve/tree/main) for a detailed implementation.

For a detailed setup guide, follow the [Spring Authorization Server Documentation](https://docs.spring.io/spring-authorization-server/reference/getting-started.html).

---

## Spring Security Configuration

To enable Spring Security in your project, you need to follow a few steps:

### Dependency Setup

First, include the relevant dependencies in your `pom.xml` file to add Spring Security and OAuth2 support.

### Application Configuration: `application.properties`

Add the following configuration properties in `application.properties`. These properties define the client credentials, authentication methods, and redirection URIs needed for OAuth2.

```properties
# OAuth2 Client Configuration
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=oidc-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods[0]=client_secret_basic
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types[0]=authorization_code
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types[1]=refresh_token
spring.security.oauth2.authorizationserver.client.oidc-client.registration.redirect-uris[0]=http://127.0.0.1:8080/login/oauth2/code/oidc-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.post-logout-redirect-uris[0]=http://127.0.0.1:8080/
spring.security.oauth2.authorizationserver.client.oidc-client.registration.scopes[0]=openid
spring.security.oauth2.authorizationserver.client.oidc-client.registration.scopes[1]=profile
spring.security.oauth2.authorizationserver.client.oidc-client.require-authorization-consent=true
```

This configuration includes:
- **Client ID and Secret**: Credentials for identifying the client application.
- **Grant Types**: Defines the authorization grant types supported (e.g., `authorization_code`, `refresh_token`).
- **Redirect URIs**: URIs where the user is redirected after login or logout.
- **Scopes**: Permissions granted to the client (e.g., `openid`, `profile`).

### Spring Security Configuration: `SecurityConfig.java`

Next, configure Spring Security in `SecurityConfig.java`. This file will handle security filters, user details management, and the OAuth2 server setup.

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean 
    @Order(1)
    public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http)
            throws Exception {
        // Apply default security settings for OAuth2 Authorization Server
        OAuth2AuthorizationServerConfiguration.applyDefaultSecurity(http);
        
        http.getConfigurer(OAuth2AuthorizationServerConfigurer.class)
            .oidc(Customizer.withDefaults());  // Enable OpenID Connect 1.0
        
        http
            .exceptionHandling((exceptions) -> exceptions
                .defaultAuthenticationEntryPointFor(
                    new LoginUrlAuthenticationEntryPoint("/login"),
                    new MediaTypeRequestMatcher(MediaType.TEXT_HTML)
               

 )
            )
            .oauth2ResourceServer((resourceServer) -> resourceServer
                .jwt(Customizer.withDefaults()));

        return http.build();
    }

    @Bean 
    @Order(2)
    public SecurityFilterChain defaultSecurityFilterChain(HttpSecurity http)
            throws Exception {
        http
            .authorizeHttpRequests((authorize) -> authorize
                .anyRequest().authenticated() // All requests require authentication
            )
            .formLogin(Customizer.withDefaults());  // Use form-based login

        return http.build();
    }

    @Bean 
    public UserDetailsService userDetailsService() {
        // In-memory user details for testing purposes
        UserDetails userDetails = User.withDefaultPasswordEncoder()
                .username("user")
                .password("password")
                .roles("USER")
                .build();

        return new InMemoryUserDetailsManager(userDetails);
    }

    @Bean 
    public RegisteredClientRepository registeredClientRepository() {
        RegisteredClient oidcClient = RegisteredClient.withId(UUID.randomUUID().toString())
                .clientId("oidc-client")
                .clientSecret("{noop}secret")
                .clientAuthenticationMethod(ClientAuthenticationMethod.CLIENT_SECRET_BASIC)
                .authorizationGrantType(AuthorizationGrantType.AUTHORIZATION_CODE)
                .authorizationGrantType(AuthorizationGrantType.REFRESH_TOKEN)
                .redirectUri("http://127.0.0.1:8080/login/oauth2/code/oidc-client")
                .postLogoutRedirectUri("http://127.0.0.1:8080/")
                .scope(OidcScopes.OPENID)
                .scope(OidcScopes.PROFILE)
                .clientSettings(ClientSettings.builder().requireAuthorizationConsent(true).build())
                .build();

        return new InMemoryRegisteredClientRepository(oidcClient);
    }

    @Bean 
    public JWKSource<SecurityContext> jwkSource() {
        // Generate RSA keys for JWT signing
        KeyPair keyPair = generateRsaKey();
        RSAPublicKey publicKey = (RSAPublicKey) keyPair.getPublic();
        RSAPrivateKey privateKey = (RSAPrivateKey) keyPair.getPrivate();
        RSAKey rsaKey = new RSAKey.Builder(publicKey)
                .privateKey(privateKey)
                .keyID(UUID.randomUUID().toString())
                .build();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return new ImmutableJWKSet<>(jwkSet);
    }

    private static KeyPair generateRsaKey() { 
        KeyPair keyPair;
        try {
            KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
            keyPairGenerator.initialize(2048);
            keyPair = keyPairGenerator.generateKeyPair();
        } catch (Exception ex) {
            throw new IllegalStateException(ex);
        }
        return keyPair;
    }

    @Bean 
    public JwtDecoder jwtDecoder(JWKSource<SecurityContext> jwkSource) {
        return OAuth2AuthorizationServerConfiguration.jwtDecoder(jwkSource);
    }

    @Bean 
    public AuthorizationServerSettings authorizationServerSettings() {
        // Create default authorization server settings
        return AuthorizationServerSettings.builder().build();
    }
}
```

This configuration does the following:
- **Security Filters**: Configures security filters for handling OAuth2 tokens and user login.
- **User Management**: Sets up a simple in-memory user service for authentication.
- **OAuth2 Server**: Sets up OAuth2 authorization, including client registration and RSA key management for JWT tokens.

### Running the Application

After completing the configuration:
1. Run the Spring Boot application.
2. Access the login page at `http://localhost:8181/login`.
3. You can log in using the credentials `user/password`.
4. By default, user details are stored in memory, so they will be lost when the application is restarted.

---

## Using OAuth2 in Postman

Postman supports OAuth2 out of the box, making it an excellent tool for testing OAuth2-based authentication systems.

### Steps to Use OAuth2 in Postman:
1. **Configure the OAuth2 details**:
   - **Auth URL**: The authorization URL from your OAuth2 setup.
   - **Token URL**: The URL where the token is issued.
   - **Client ID** and **Client Secret**: These values should match those configured in `SecurityConfig.java`.
   - **Redirect URI**: The URI to which users will be redirected after successful login.
   - **Scopes**: Specify the scopes for the OAuth2 token (e.g., `openid`, `profile`).
2. **Generate Token**: After filling in the details, Postman will generate an access token that you can use for further requests.
3. **Making Requests**: Once the token is generated, include it in the `Authorization` header for requests to your protected API.

---

## Persisting OAuth2 Details in a Database

By default, the OAuth2 authorization details (e.g., tokens, client credentials) are stored in memory. However, in a production application, these details should be persisted in a database.

### Implementing OAuth2 with JPA

Follow the steps outlined in the [Spring Authorization Server Documentation](https://docs.spring.io/spring-authorization-server/reference/guides/how-to-jpa.html) to configure Spring Authorization Server with JPA.

### Database Schema for OAuth2

Create tables in the database to store authorization details:

```sql
CREATE TABLE authorization (
    id VARCHAR(255) NOT NULL,
    registered_client_id VARCHAR(255) NULL,
    principal_name VARCHAR(255) NULL,
    authorization_grant_type VARCHAR(255) NULL,
    authorized_scopes TEXT NULL,
    attributes TEXT NULL,
    state TEXT NULL,
    authorization_code_value TEXT NULL,
    authorization_code_issued_at datetime NULL,
    authorization_code_expires_at datetime NULL,
    authorization_code_metadata VARCHAR(255) NULL,
    access_token_value TEXT NULL,
    access_token_issued_at datetime NULL,
    access_token_expires_at datetime NULL,
    access_token_metadata VARCHAR(255) NULL,
    access_token_type VARCHAR(255) NULL,
    access_token_scopes TEXT NULL,
    refresh_token_value TEXT NULL,
    refresh_token_issued_at datetime NULL,
    refresh_token_expires_at datetime NULL,
    refresh_token_metadata TEXT NULL,
    oidc_id_token_value TEXT NULL,
    oidc_id_token_issued_at datetime NULL,
    oidc_id_token_expires_at datetime NULL,
    oidc_id_token_metadata TEXT NULL,
    oidc_id_token_claims TEXT NULL,
    user_code_value TEXT NULL,
    user_code_issued_at datetime NULL,
    user_code_expires_at datetime NULL,
    user_code_metadata TEXT NULL,
    device_code_value TEXT NULL,
    device_code_issued_at datetime NULL,
    device_code_expires_at datetime NULL,
    device_code_metadata TEXT NULL,
    CONSTRAINT pk_authorization PRIMARY KEY (id)
);

CREATE TABLE authorization_consent (
    registered_client_id VARCHAR(255) NOT NULL,
    principal_name VARCHAR(255) NOT NULL,
    authorities VARCHAR(1000) NULL,
    CONSTRAINT pk_authorizationconsent PRIMARY KEY (registered_client_id, principal_name)
);

CREATE TABLE client (
    id VARCHAR(255) NOT NULL,
    client_id VARCHAR(255) NULL,
    client_id_issued_at datetime NULL,
    client_secret VARCHAR(255) NULL,
    client_secret_expires_at datetime NULL,
    client_name VARCHAR(255) NULL,
    client_authentication_methods VARCHAR(1000) NULL,
    authorization_grant_types VARCHAR(1000) NULL,
    redirect_uris VARCHAR(1000) NULL,
    post_logout_redirect_uris VARCHAR(1000) NULL,
    scopes VARCHAR(1000) NULL,
    client_settings VARCHAR(2000) NULL,
    token_settings VARCHAR(2000) NULL,
    CONSTRAINT pk_client PRIMARY KEY (id)
);
```

This schema provides a persistent store for OAuth2 tokens and client registrations.

### Implementing JPA Models and Repositories

Once the database schema is set up, create the corresponding JPA models and repositories to interact with the database. Use the Spring Authorization Server documentation as a reference for mapping these entities correctly.

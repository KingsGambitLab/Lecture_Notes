## Topics to be discussed

1. **Connecting Spring Authorization Server to a User Database**
2. **Adding Custom Claims to JWT** 
3. **Securing ProductService Endpoints**
---

## Connecting Spring Authorization Server to a User Database

In production environments, storing user information in a database is critical. We will replace the default in-memory user setup provided by Spring with a fully functional database-driven solution.

### Initial Setup: In-Memory User

By default, Spring provides a simple way to define user details in memory. The following example demonstrates how to create a user with hardcoded credentials.

```java
@Bean
public UserDetailsService userDetailsService() {
    UserDetails userDetails = User.builder()
        .username("user")
        .password("$2a$16$AcBmaZLe06Hx5QSL1PVmRev3W3Fuzy..A18THjaUM.AYEcEDoTORC")
        .roles("USER")
        .build();

    return new InMemoryUserDetailsManager(userDetails);
}
```

**Explanation:**
- In this example, a user is created with a username, password (hashed), and role.
- The `InMemoryUserDetailsManager` manages this user, but it doesn't communicate with a real database, making it unsuitable for a production environment.

We will now switch to using a custom user service that interacts with a database.

### Step-by-Step: Implementing a Custom UserDetailsService

1. **Create a `CustomUserDetailsService` Class:**
   - This class will implement the `UserDetailsService` interface provided by Spring Security. 
   - The `UserDetailsService` interface defines a single method, `loadUserByUsername`, which retrieves user details for authentication.

2. **Define Custom Granted Authorities:**
   - User roles and permissions in Spring Security are referred to as **granted authorities**. These define what actions a user can perform.
   - We will implement a `CustomGrantedAuthority` class to manage these roles.

#### CustomGrantedAuthority.java
```java
package com.scaler.userservicemwfeve.security.models;

public class CustomGrantedAuthority implements GrantedAuthority {
    private Role role;

    public CustomGrantedAuthority(Role role) {
        this.role = role;
    }

    @Override
    public String getAuthority() {
        return role.getName();  // This method returns the name of the role.
    }
}
```

**Explanation:**
- This class implements the `GrantedAuthority` interface.
- The `getAuthority` method returns the role name (e.g., "USER" or "ADMIN") assigned to the user.

3. **Load User Details from the Database:**
   - In the `CustomUserDetailsService` class, implement the `loadUserByUsername` method to fetch the user from the database based on their email (used as the username in this case).

#### CustomUserDetailsService.java
```java
@Override
public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
    Optional<User> userOptional = userRepository.findByEmail(username);

    if (userOptional.isEmpty()) {
        throw new UsernameNotFoundException("User by email: " + username + " doesn't exist.");
    }

    CustomUserDetails userDetails = new CustomUserDetails(userOptional.get());

    return userDetails;
}
```

**Explanation:**
- The `loadUserByUsername` method retrieves a `User` entity from the database using `userRepository.findByEmail`.
- If no user is found, a `UsernameNotFoundException` is thrown.
- If the user is found, it is converted into `CustomUserDetails`, which Spring Security will use for authentication.

---

## Handling Common Errors

While implementing the custom user service, you may encounter common issues, especially with how user roles are loaded and serialized.

### Eager Fetching of Roles

- By default, roles in the database might be **lazily** loaded, meaning they are only fetched when explicitly needed. However, during authentication, Spring Security expects the roles to be available immediately, causing potential errors.
- To fix this, set the fetching strategy of roles to **EAGER** in your `User` entity.

```java
@OneToMany(fetch = FetchType.EAGER)
```

**Explanation:**
- This ensures that roles are loaded immediately when the user is fetched from the database, preventing any lazy loading issues during authentication.

### JSON Serialization Issues

- You might encounter serialization errors when using custom user details or authorities, as these classes may not be properly serialized into JSON.
- To resolve this, add the `@JsonDeserialize` annotation to your custom classes (`CustomUserDetails` and `CustomGrantedAuthority`).

#### CustomUserDetails.java
```java
@JsonDeserialize
public class CustomUserDetails implements UserDetails {
    // Define properties like username, password, and roles
    // Implement methods such as getAuthorities(), getUsername(), etc.
}
```

#### CustomGrantedAuthority.java
```java
@JsonDeserialize
public class CustomGrantedAuthority implements GrantedAuthority {
    private String authority;

    public CustomGrantedAuthority(Role role) {
        this.authority = role.getName();  // Assign the role's name as the authority.
    }

    @Override
    public String getAuthority() {
        return authority;  // Return the role name.
    }
}
```

**Explanation:**
- Adding `@JsonDeserialize` ensures that these custom classes can be serialized and deserialized properly when transmitted as JSON, which is essential for handling requests and responses in a web service.

---

## Adding Custom Claims to JWT

JWT (JSON Web Token) is a popular format for securely transmitting information between parties. It contains **claims**, which are pieces of information about the user. By default, JWT includes standard claims like username and expiration time. However, you can also add custom claims to store additional user information.

### Custom Claims in JWT

1. **Customizing JWT Tokens:**
   - To add custom claims, such as user roles or user IDs, we need to modify the JWT encoding process in the security configuration.

#### SecurityConfig.java
```java
@Bean
public OAuth2TokenCustomizer<JwtEncodingContext> jwtTokenCustomizer() {
    return (context) -> {
        if (OAuth2TokenType.ACCESS_TOKEN.equals(context.getTokenType())) {
            context.getClaims().claims((claims) -> {
                Set<String> roles = AuthorityUtils.authorityListToSet(context.getPrincipal().getAuthorities())
                    .stream()
                    .map(c -> c.replaceFirst("^ROLE_", ""))
                    .collect(Collectors.toSet());
                claims.put("roles", roles);  // Add user roles to the JWT claims.
            });
        }
    };
}
```

**Explanation:**
- This configuration customizes the JWT encoding process, specifically for access tokens.
- It retrieves the user’s roles from their authorities and adds them to the JWT under the `roles` claim.

2. **Adding Custom User ID Claim:**
   - If you want to include the user's ID in the JWT, you can modify the code to add it as a custom claim.

```java
claims.put("userId", ((CustomUserDetails) context.getPrincipal().getPrincipal()).getUserId());
```

**Explanation:**
- This line adds the user's unique ID (`userId`) to the JWT, allowing it to be used in client-side applications or other services.

---

## Securing ProductService Endpoints

Once the Spring Authorization Server is set up and JWT tokens are issued, the next step is to secure the `productService` endpoints. This ensures that only authenticated users can access certain routes, and that users with specific roles have additional permissions.

### Step-by-Step: Securing ProductService

1. **Add OAuth2 Resource Server Dependency:**
   - To enable JWT-based authentication in the `productService`, you need to add the `spring-boot-starter-oauth2-resource-server` dependency.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
</dependency>
```

2. **Create a Security Configuration for ProductService:**

#### SpringSecurityConfig.java
```java
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
        .authorizeHttpRequests(authorize -> authorize
            .anyRequest().authenticated()  // All endpoints require authentication
        )
        .oauth2ResourceServer(oauth2 -> oauth2.jwt());  // Enable JWT-based security
    return http.build();
}
```

**Explanation:**
- This configuration ensures that all endpoints in `productService` require authentication using JWT tokens issued by the authorization server.

3. **Specify JWT Issuer:**
   - In the `application.properties` file, specify the JWT issuer to ensure the tokens are validated correctly.

```properties
spring.security.oauth2.resourceserver.jwt.issuer-uri=http://localhost:8181
```

4. **Restrict Access to Specific Endpoints:**
   - You can control which roles can access specific routes. For example, you can restrict access to `/products` for only admin users.

```java
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
        .authorizeHttpRequests(authorize

 -> authorize
            .requestMatchers("/products/{id}").authenticated()  // Requires authentication
            .requestMatchers("/products").hasAuthority("SCOPE_ADMIN")  // Only admin users can access
            .anyRequest().permitAll()  // Other routes are accessible by everyone
        )
        .oauth2ResourceServer(oauth2 -> oauth2.jwt());
    return http.build();
}
```

**Explanation:**
- This allows fine-grained control over which endpoints require authentication and which roles are allowed to access them.

---

## Extracting Authorities Manually

In some cases, you may need to manually extract and customize user authorities (roles) from the JWT token. Spring Security provides tools for this.

### Custom JWT Authority Extraction

1. **Implement a `JwtAuthenticationConverter`:**

```java
@Bean
public JwtAuthenticationConverter jwtAuthenticationConverter() {
    JwtGrantedAuthoritiesConverter grantedAuthoritiesConverter = new JwtGrantedAuthoritiesConverter();
    grantedAuthoritiesConverter.setAuthoritiesClaimName("roles");  // Specify the claim for roles

    JwtAuthenticationConverter jwtAuthenticationConverter = new JwtAuthenticationConverter();
    jwtAuthenticationConverter.setJwtGrantedAuthoritiesConverter(grantedAuthoritiesConverter);
    return jwtAuthenticationConverter;
}
```

**Explanation:**
- This configuration ensures that the roles stored in the `roles` claim of the JWT are extracted and recognized by Spring Security.
- You can use this converter in your security configuration to manually process the authorities for better control.


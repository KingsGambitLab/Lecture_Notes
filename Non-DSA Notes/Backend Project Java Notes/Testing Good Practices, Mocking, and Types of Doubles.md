## Topics to be covered

- **Unit Testing Good Practices**
- **What to Test**
- **Mocking**
- **Types of Test Doubles**
- **Code Implementation**

---

## What Test Cases Should We Have?

When developing software, selecting the right test cases is essential to ensure the code behaves correctly under a variety of conditions.

### Scenario: Problem Setter at Scaler
Let’s consider a practical scenario of a **problem setter at Scaler** who designs **DSA (Data Structures and Algorithms) problems**. They must also create test cases to verify the correctness of solutions. Each test case has two parts:
1. **Input**: The data provided to the problem, such as a set of numbers or a string.
2. **Expected Output**: The result you expect after processing the input, which determines whether the code is correct or not.

After designing the problem, the problem setter runs these test cases, which compare the actual output of the solution against the expected output to evaluate correctness.

### Key Test Cases to Consider

1. **Edge Cases**:  
   These are extreme or unusual inputs that might reveal hidden bugs in the code. For example, what happens when the input is empty, or when the input size is the maximum possible value? These scenarios are often overlooked but crucial for catching issues that occur in less common situations.

2. **Negative Scenarios**:  
   These test cases involve invalid or out-of-bound inputs. For instance, what happens if the input violates the expected constraints (e.g., providing a negative number when only positives are allowed)? Negative scenarios ensure the code can gracefully handle errors and invalid inputs.

3. **Happy Path Scenarios**:  
   These are the normal, expected cases where the input is within the allowed range, and everything works as intended. Developers often assume these "happy paths" are covered, but it's essential to verify even these common cases. Ignoring them can lead to bugs being missed in seemingly straightforward situations.

---

## Qualities of Unit Tests

Unit tests are the backbone of robust software development. They help ensure that individual components of your system work as expected. A well-written unit test should have certain essential qualities to be effective. Let’s break down what makes a unit test truly valuable.

### Characteristics of a Good Unit Test

1. **Fast Execution**:
   - Unit tests should run quickly to allow developers to run them frequently during development.
   - A popular method to write unit tests is following the **3 A's of Testing**:
     1. **Arrange**: Set up everything required for the test, such as initializing variables or creating necessary objects.
     2. **Act**: Perform the action or call the function being tested.
     3. **Assert**: Check whether the actual result matches the expected result. This comparison should be straightforward and **hard-coded** to avoid introducing potential errors in expected values due to miscalculations.

   ![3 A's of Unit Testing](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/689/original/1.png?1725541038)  
   **Note**: Always hard-code the expected result. If you calculate the expected value within the test, you risk making an error that will defeat the purpose of testing, as the test might pass incorrectly.

2. **Isolated**:
   - Unit tests should be independent of each other. One test should not influence the outcome of another.
   - **Why Isolation Matters**: Tests that are not isolated can result in **flaky tests**, which sometimes pass and sometimes fail unpredictably. These flakiness issues can stem from shared state between tests, causing false positives (indicating success when it shouldn’t) or false negatives (indicating failure when it shouldn’t).

3. **Repeatable**:
   - A good unit test should consistently produce the same result every time it is run, given the same inputs.
   - **Repeatability** is critical, especially in CI/CD pipelines where tests are run automatically on every code change. If a test sometimes fails and sometimes passes with the same code, it diminishes confidence in the test suite.

4. **Self-Checking**:
   - Tests should automatically verify success or failure without requiring human intervention. This makes them more efficient, especially in automated testing environments.
   - In modern development environments (e.g., **GitHub**), continuous integration tools automatically run tests on pull requests. If any test fails, the pull request is blocked from merging until the issue is resolved.

   **Instructor’s Tip**:  
   Show learners the [GitHub repo](https://github.com/Naman-Bhalla/sql-assignment-orders) to illustrate how automatic testing works in a real project. This repository automatically runs tests when a pull request is made and prevents merging if tests fail.

5. **Focus on Behavior, Not Implementation**:
   - Unit tests should test **what the code does** rather than **how the code does it**.
   - This principle means that as long as the code produces the correct output, the internal logic or approach doesn’t matter.
   
   **Key Insight**: Testing behavior allows the implementation to evolve without breaking the tests. You can refactor or optimize the internal workings of your code without needing to change your test cases, as long as the output remains the same.

   **Newsletter Reference**: Share the popular article [Testing on the Toilet: Test Behavior, Not Implementation](https://testing.googleblog.com/2013/08/testing-on-toilet-test-behavior-not.html) with students.

---

## Mocking

### Why Mocking is Important

In unit testing, we often need to isolate the unit of code under test. However, real-world systems involve multiple dependencies (e.g., databases, APIs, or third-party services). These dependencies introduce unpredictability and can slow down or cause failures in tests. This is where **mocking** comes in.

**Core Requirements of Unit Tests**:
1. **Repeatability**: Tests should always produce the same result for the same input.
2. **Isolation**: Tests should focus solely on the unit of code being tested without involving external systems.

**[Discussion with Students]**  
Consider testing a method `getDetailsOfProduct(id)` in a `ProductController` class. This method might call an external service, such as `productService`, which, in turn, communicates with a database. What issues could arise in testing this?

- **Network Unreliability**: If the service depends on network access, a lack of network during testing (e.g., in CI/CD environments) could cause the test to fail.
- **External Dependencies**: Dependencies on third-party services, APIs, or databases introduce additional complexity and instability, which can result in tests becoming **flaky** (passing sometimes, failing other times).

### Solution: Mocking

To eliminate this dependency on external factors, we **mock** external systems. Mocking means replacing real components (like services or repositories) with fake versions that return **pre-defined, hard-coded responses**. This allows you to focus on testing the core business logic without worrying about the behavior of external dependencies.

- **Example**: Instead of calling a real database through the `productRepo`, we mock the `productRepo` to return a specific object for a given input. This ensures the test runs predictably every time.

---

## Types of Test Doubles

When we mock objects, we create **test doubles**, which are stand-ins for real objects in the system. These doubles are used in place of the actual objects to simulate their behavior during testing. There are three common types of test doubles:

### 1. Mock

A **mock** is a simple stand-in for an object that returns hard-coded responses to function calls. The return values are predetermined, so the test doesn’t rely on any real logic or computation.

- **Example**: You want to test `getCountOfProducts()` in a product system. With a mock, you can simply return the value `5` when the method is called, regardless of how many products are actually in the system.

   ![Mock Example](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/690/original/2.png?1725541074)

   **Limitation**: Mocks are static and lack the ability to handle dynamic scenarios. For instance, if you want to test a system where the product count changes (e.g., after adding a new product), a mock won’t be able to simulate this dynamic behavior.

   **[Discussion with Students]**:  
   Can a mock handle dynamic scenarios like updating the count of products?  
   - **Answer**: No, mocks are static and cannot change their behavior based on state changes in the system. In such cases, you need to use a **stub**.

### 2. Stub

A **stub** is a more advanced stand-in for an object that can mimic certain behaviors of the real object. Unlike mocks, stubs can handle dynamic scenarios and simulate more complex behaviors.

- **Example**: A stub for a `productRepo` might simulate adding products and returning an updated product count. While it doesn’t have the full functionality of a real repository, it can mimic enough behavior for testing purposes.

   ![Stub Example](https://hackmd.io/_uploads

/SJmlrdJ30.png)

   **Key Concept**: A stub allows for some **dynamism**, meaning it can adjust its behavior based on changes in state (e.g., adding a new product and reflecting that in the product count).

   **Dependency Inversion**: This principle comes into play when injecting a stub into the test case. The test case doesn’t directly interact with the real object, but with the stub that mimics its behavior.

### 3. Fake

A **fake** is a more sophisticated version of a stub. It closely mimics the real object’s behavior but without involving real external systems. Fakes are often used when you need more realistic behavior for complex scenarios, such as simulating a database or an API.

- **Example**: You want to test saving a product and retrieving it via a search function. A fake might use in-memory storage (like a HashMap) to store and retrieve products, providing a realistic simulation of a real database without the overhead.

   ![Fake Example](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/691/original/3.png?1725541093)

   **Key Insight**:  
   - A **stub** provides basic, often hard-coded behavior.
   - A **fake** mimics the real object more closely, handling more complex scenarios like saving and searching for data.
   - Fakes are useful when you need to test more realistic behavior without using actual external systems.

### Summary of Test Doubles

- **Mock**: The simplest form, used for returning hard-coded values. Great for isolated, static tests.
- **Stub**: Adds dynamism, allowing some interaction based on state changes. Useful for more complex tests.
- **Fake**: The most sophisticated, simulating the real object’s behavior more closely. Ideal for testing realistic scenarios without involving real systems.

---

## Conclusion

Unit testing is an essential part of maintaining reliable and maintainable code. Following best practices ensures that your tests are effective, efficient, and robust. By focusing on behavior, isolating external dependencies through mocking, and understanding the different types of test doubles (Mocks, Stubs, Fakes), developers can write tests that ensure their code works as intended under a variety of conditions.

### Further Reading:
1. [Test Doubles: Fakes, Mocks, and Stubs](https://blog.pragmatists.com/test-doubles-fakes-mocks-and-stubs-1a7491dfa3da)
2. [Microsoft Unit Testing Best Practices](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices)

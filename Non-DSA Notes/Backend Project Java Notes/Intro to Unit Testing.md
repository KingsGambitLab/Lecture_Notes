## Topics to be covered

- **Importance of testing: Why testing is crucial in software development**.
- **Introduction to Test-Driven Development (TDD): A method where tests are written before code**.
- **Understanding flaky tests**.
- **Types of software testing:**
  - **Unit Testing**
  - **Integration Testing**
  - **Functional Testing**
- **What to test**
- **Best practices for writing and maintaining tests**.

---

## Why Do We Need Testing?

### The Importance of Testing in Software Development

In a complex software system, any change in one part of the code can unintentionally affect other parts of the application. Testing is necessary to catch these issues early and ensure that the software behaves as expected after changes.

example to illustrate this:

#### Example: The Multiplier Utility Function

Imagine you have a function in your codebase that multiplies a given number by 2. The function is written as follows:

```cpp
int multiplierUtility(int x) {
    return x * 2;
}
```

Now, let’s consider two separate parts of your application using this function:

1. **Counting lanes on a road**: A developer uses this function to calculate the total number of lanes on a two-lane road:
    ```cpp
    int numberOfLanes(int lanesOnOneSide) {
        return multiplierUtility(lanesOnOneSide);
    }
    ```

2. **Counting married people**: Another developer uses the same utility to count the number of people in a given number of married pairs:
    ```cpp
    int getTotalMarriedPeople(int uniquePairs) {
        return multiplierUtility(uniquePairs);
    }
    ```

Now, imagine that later, the road system changes, and each road now has 3 lanes instead of 2. To reflect this change, a developer modifies the `multiplierUtility` function:

```cpp
int multiplierUtility(int x) {
    return x * 3;
}
```

The developer updates the function for calculating lanes without realizing that it will now incorrectly affect the function for counting married people. As a result, the `getTotalMarriedPeople()` function will now produce incorrect results, implying that each married pair contains three people, which is obviously absurd.

This scenario highlights a key issue in software development: **a change in one part of the code can have unintended consequences in another part of the system**. As applications grow larger and more complex, such interdependencies become increasingly common.

### The Consequences of No Testing

When an application’s codebase becomes more complex, several challenges arise:

- **Increased interdependencies**: Different parts of the code rely on each other, meaning a change in one place can affect multiple other areas.
- **Higher cost of change**: As the codebase grows, the cost and risk associated with making changes increase because it becomes harder to predict how the changes will impact the entire system.
- **No complete knowledge of the codebase**: It’s unrealistic for any developer to fully understand the entire codebase in large projects. This limits the ability to predict the impact of changes.
- **Slower development pace**: Without automated testing, developers have to manually track down who might depend on their code and check if everything still works, which slows down the development process.
- **Accumulation of technical debt**: Over time, non-optimal decisions, shortcuts, and neglected code cleanup make the code harder to maintain and modify, a concept known as **technical debt**.

### The Solution: Automated Testing

To avoid these problems, developers need a way to ensure that any code changes are automatically checked for potential issues across the entire application. This is where **automated testing** comes into play.

Automated testing allows developers to:

- Make changes confidently, knowing that the tests will automatically catch any issues.
- Receive immediate feedback when something breaks, allowing for quick fixes or reversions.
  
### What Is Testing?

- Testing isn’t just about writing features; it’s about ensuring the features work as expected through automated test cases.
- **Test cases** are small programs that automatically verify whether the code is working correctly. They are written to test specific functionalities in the application.
- Before submitting a new feature, developers should run all test cases. If all tests pass, and assuming that the tests are comprehensive, the new feature is considered safe to deploy.
- **Comprehensive testing** means covering not only the expected use cases but also all possible edge cases.

### Why Do Some Developers Avoid Writing Tests?

Despite the clear benefits of automated testing, many developers skip this step due to several reasons:

- **Laziness**: Writing tests requires extra time and effort.
- **Lack of immediate reward**: Writing test cases can feel like a chore, and it’s not as exciting as building new features.
- **Underappreciated work**: Tests are often not recognized or praised, making it easy to deprioritize them.
  
Some companies handle this issue by requiring developers to follow different workflows:

1. **Feature First, Test Later**: Developers write the feature first, then create the test cases, and finally submit the feature.
2. **Test First, Feature Later**: Developers write the test cases first, then implement the feature, and finally submit it. This approach is called **Test-Driven Development (TDD)**.

---

## Test-Driven Development (TDD)

### What Is TDD?

In **Test-Driven Development (TDD)**, the process starts by writing test cases before the actual code. Here’s the typical workflow:

1. Write test cases for the feature (at this point, the tests will fail because the feature doesn’t exist yet).
2. Develop the feature and continuously run the tests until they all pass.
3. Once all tests pass, the feature is ready for submission.

### Why Do Developers Support TDD?

Despite the extra effort involved, many developers support TDD for the following reasons:

- **Better design**: Writing tests before the code forces developers to think about how the code will be used by others. This can lead to cleaner and more efficient code.
- **Confidence in changes**: Since tests are written before the feature, developers can be confident that their code works as expected once all tests pass.

### Downsides of TDD

- **Time-consuming**: Writing tests before coding can be a slow and tedious process.
- **Monotonous**: Some developers find it repetitive and less interesting compared to feature development.

In some companies, TDD is even part of the interview process, where candidates are required to write test cases before implementing the actual code.

---

## Flaky Tests

### What Are Flaky Tests?

A **flaky test** is a test that sometimes passes and sometimes fails without any changes to the code. Flaky tests are unreliable and can lead to confusion because they give inconsistent results.

### Why Do Flaky Tests Occur?

Flaky tests usually happen for two main reasons:

1. **Concurrency issues**: If the code involves multiple threads or relies on synchronization, tests might produce inconsistent results because of timing issues.
2. **Randomness**: If the code contains random elements, test results can vary based on different inputs or outcomes.

In both cases, developers should carefully review their test code and implementation to identify the source of the flakiness.

---

## Types of Testing

### Overview of Testing Dependencies

Consider a function `A()` that calls another function `B()` during its execution. If the test case for `A()` fails, the error could be caused by:

- A bug in the code of `A()`.
- A bug in the code of `B()`.

If both `A()` and `B()` have their own independent test cases, and the bug is in `B()`, both test cases for `A()` and `B()` will fail. However, if several other functions depend on `B()`, all their test cases will also fail, making it difficult to pinpoint the actual source of the problem.

### Isolated Testing with Mocking

To avoid such confusion, developers should isolate their tests using a technique called **mocking**. Mocking allows the developer to simulate dependencies and focus the test on a single piece of code.

- If `B()` contains a bug, only `B()`'s test cases should fail, while the test cases for `A()` and other functions should pass.

### Different Types of Testing

There are three primary types of testing that developers commonly use:

#### Unit Testing

- **Definition**: Unit testing involves testing individual methods or functions in isolation.
- **Characteristics**:
  - Unit tests are small and focus on testing a single "unit" of code.
  - They are fast to execute because they don’t rely on external dependencies.
  - Every individual method in the codebase should have at least one test case.

#### Test Coverage

- **Definition**: Test coverage refers to the percentage of the code that is covered by one or more test cases.
- A good unit test is often represented by input-output pairs, where specific inputs are tested to verify that the method produces the expected output.

#### Integration Testing

- **Definition**: Integration testing checks how different parts of the application work together as a whole.
- **Characteristics**:
  - In integration testing, the actual dependencies are called (e.g., database connections, services).
  - These tests are automated but are slower than unit tests due to the involvement of multiple components.
  - Integration tests are fewer

 in number but essential for verifying complex interactions between components.

#### Functional Testing

- **Definition**: Functional testing evaluates the entire application from an end-user’s perspective. It treats the system as a **black box**, focusing on whether the system behaves correctly from start to finish.
- **Characteristics**:
  - Functional tests simulate real-world scenarios by providing input data and expecting output that matches user requirements.
  - These tests are typically written for major features or workflows in the application.
  
### Testing Pyramid

To summarize, different types of testing follow a **testing pyramid** structure:

1. **Unit Testing**: The foundation of the pyramid, with the largest number of tests. These are small, fast, and focus on isolated units of code.
2. **Integration Testing**: These tests verify that components work together and are fewer in number compared to unit tests.
3. **Functional Testing**: At the top of the pyramid, functional tests validate end-to-end functionality from a user’s perspective. They are the fewest in number.

The visual below illustrates the proportional distribution of these test types:

![Testing Pyramid](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/688/original/1.png?1725540334)

## Topics to be covered

  - **Integrating Stripe API**
  - **LocalTunnel**
---

## Implementation of Payment Service

### **Repository and Codebase**

- **[Github Repo](https://github.com/Naman-Bhalla/paymentservicemar24mwfeve)**: This contains the complete implementation of the payment service, including all necessary packages and classes. Please refer to it for in-depth review and hands-on coding practice.

### APIs Implemented in `PaymentService`

The payment service exposes several critical API endpoints for interacting with payment gateways. These are:

- **createPaymentLink**: This API is responsible for generating a payment link for customers.
- **getPaymentStatus**: This API checks and returns the current status of a particular payment.
- **handleWebhookEvent**: This API processes webhook events triggered by the payment gateway, such as successful payments or payment failures.

---

### Step-by-Step Project Setup and Implementation

1. **Project Setup**:
   - Begin by creating a new Java project.
   - Inside the `src -> main -> java -> dev` directory, you’ll create packages to maintain a clean and modular structure.
   - The required packages are:
     - **controllers**: This will contain the classes responsible for handling HTTP requests.
     - **models**: This package will define the entities or models used in the application.
     - **dtos**: Data Transfer Objects (DTOs) are used to pass data between layers in the application.
     - **repositories**: This package manages the interaction with the database.
     - **services**: This package contains the business logic of the payment service.

2. **Controller Implementation**:
   - In the **controllers** package, create the `PaymentController` class, which will serve as the entry point for HTTP requests related to payments.
   - **Explanation**:
     - The `PaymentController` class defines endpoints for creating payment links and handling webhook events. It uses the **PaymentService** to handle business logic.
   - Here is the final code for `PaymentController`:

    ```java
    package dev.naman.paymentservicemar24mwfeve.controllers;

    import com.razorpay.RazorpayException;
    import dev.naman.paymentservicemar24mwfeve.dtos.CreatePaymentLinkRequestDto;
    import dev.naman.paymentservicemar24mwfeve.services.PaymentService;
    import org.springframework.web.bind.annotation.*;

    import java.util.Map;

    @RestController
    @RequestMapping("/payment")
    public class PaymentController {
        private PaymentService paymentService;

        public PaymentController(PaymentService paymentService) {
            this.paymentService = paymentService;
        }

        @PostMapping("/")
        public String createPaymentLink(@RequestBody CreatePaymentLinkRequestDto request) throws RazorpayException {
            // Call the service to generate a payment link
            String link = paymentService.createPaymentLink(request.getOrderId());
            return link;
        }

        @PostMapping("/webhook")
        public void handleWebhookEvent(@RequestBody Map<String, String> webhookEvent) {
            // Log webhook event data
            System.out.println(webhookEvent);
        }
    }
    ```

   **Key points**:
   - The `createPaymentLink` method takes a **CreatePaymentLinkRequestDto** object from the request body and calls the service to create a payment link. It returns the generated link as a response.
   - The `handleWebhookEvent` method is responsible for logging webhook events sent by Razorpay or Stripe (like payment success or failure).

3. **DTO (Data Transfer Object) Implementation**:
   - DTOs are used to encapsulate data sent in requests. In the **dtos** package, create the `CreatePaymentLinkRequestDto` class to capture the order ID from incoming requests:

    ```java
    package dev.naman.paymentservicemar24mwfeve.dtos;

    import lombok.Getter;
    import lombok.Setter;

    @Getter
    @Setter
    public class CreatePaymentLinkRequestDto {
        // DTO to receive order ID from client
        private String orderId;
    }
    ```

4. **Service Interface**:
   - Define the **PaymentService** interface inside the **services** package. This interface will outline the core methods related to payment operations. Both Stripe and Razorpay will implement this interface to provide specific behavior for each payment gateway.

    ```java
    package dev.naman.paymentservicemar24mwfeve.services;

    import com.razorpay.RazorpayException;

    public interface PaymentService {
        // Method to create a payment link
        String createPaymentLink(String orderId) throws RazorpayException;
        
        // Method to check payment status
        String getPaymentStatus(String paymentId);
    }
    ```

5. **Service Implementation**:
   - For Razorpay, we implement the `PaymentService` interface in the **RazorpayPaymentService** class. This class uses Razorpay's Java SDK to interact with the payment gateway.

    ```java
    package dev.naman.paymentservicemar24mwfeve.services;

    import com.razorpay.PaymentLink;
    import com.razorpay.RazorpayClient;
    import com.razorpay.RazorpayException;
    import org.json.JSONObject;
    import org.springframework.stereotype.Service;

    @Service
    public class RazorpayPaymentService implements PaymentService {
        private RazorpayClient razorpayClient;

        public RazorpayPaymentService(RazorpayClient razorpayClient) {
            this.razorpayClient = razorpayClient;
        }

        @Override
        public String createPaymentLink(String orderId) throws RazorpayException {
            try {
                // Create a new payment link request
                JSONObject paymentLinkRequest = new JSONObject();
                paymentLinkRequest.put("amount", 1000); // Amount in paise (INR)
                paymentLinkRequest.put("currency", "INR");
                paymentLinkRequest.put("accept_partial", false);
                paymentLinkRequest.put("expire_by", System.currentTimeMillis() + 15 * 60 * 1000); // Expires in 15 minutes
                paymentLinkRequest.put("reference_id", orderId);
                paymentLinkRequest.put("description", "Payment for order no " + orderId);

                // Customer information
                JSONObject customer = new JSONObject();
                customer.put("name", "+919996203771");
                customer.put("contact", "Naman Bhalla");
                customer.put("email", "naman@scaler.com");
                paymentLinkRequest.put("customer", customer);

                // Notifications
                JSONObject notify = new JSONObject();
                notify.put("sms", true);
                notify.put("email", true);
                paymentLinkRequest.put("reminder_enable", true);

                // Callback URL and method
                paymentLinkRequest.put("callback_url", "https://naman.dev/");
                paymentLinkRequest.put("callback_method", "get");

                // Create payment link via Razorpay API
                PaymentLink payment = razorpayClient.paymentLink.create(paymentLinkRequest);
                return payment.get("short_url");
            } catch (Exception e) {
                // Handle error and return an empty string or previous link
                return "";
            }
        }

        @Override
        public String getPaymentStatus(String paymentId) {
            // In production, this method will query the database or gateway for payment status
            return null;
        }
    }
    ```

   **Explanation of Key Concepts**:
   - **RazorpayClient**: This is initialized using API credentials and is responsible for communicating with Razorpay’s servers.
   - **paymentLinkRequest**: This is a JSON object used to construct the request to create a payment link. The key-value pairs represent different aspects of the payment, including the amount, currency, and customer details.
   - **Amount**: Razorpay requires the amount in the smallest currency unit (paise for INR). For example, ₹10.00 is sent as 1000 (paise).
   - **Callback URL**: After payment, Razorpay redirects to this URL, informing the system of the payment status.

---

### **Dependency Management** (`pom.xml`)

To integrate Stripe and Razorpay into your project, add the following dependencies to the `pom.xml` file:

```xml
<dependency>
    <groupId>com.stripe</groupId>
    <artifactId>stripe-java</artifactId>
    <version>24.18.0</version>
</dependency>
<dependency>
    <groupId>com.razorpay</groupId>
    <artifactId>razorpay-java</artifactId>
    <version>1.4.5</version>
</dependency>
```

These libraries provide the necessary functionality to interact with the payment gateways via their APIs.

---

### **Razorpay Configuration**

To use Razorpay’s API, you need an **API key** and **secret**. Follow these steps to generate them:

1. Visit the Razorpay website and log into your account.
2. Navigate to **Account & Settings** and select **API Keys**.
3. Generate a new test key or use

 an existing one.
4. In your `application.properties` file, store the keys securely:

```properties
razorpay.key_id=${RAZORPAY_KEY_ID}
razorpay.key_secret=${RAZORPAY_KEY_SECRET}
```

Ensure these keys are saved in environment variables to avoid hardcoding them in your application.

---

### **Razorpay Config Class**

Create a configuration class in the **configs** package that will provide the Razorpay client as a bean:

```java
package dev.naman.paymentservicemar24mwfeve.configs;

import com.razorpay.RazorpayClient;
import com.razorpay.RazorpayException;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RazorpayConfig {
    @Value("${razorpay.key_id}")
    private String razorpayKeyId;

    @Value("${razorpay.key_secret}")
    private String razorpaySecret;

    @Bean
    public RazorpayClient createRazorpayClient() throws RazorpayException {
        return new RazorpayClient(razorpayKeyId, razorpaySecret);
    }
}
```

This configuration allows your application to inject the Razorpay client wherever it’s needed.

---

### **Understanding `amount` in Razorpay**

Razorpay stores payment amounts as **integers** in the smallest unit of the currency, such as paise for INR. This means that:

- ₹10.01 is stored as `1001`.
- ₹99.99 is stored as `9999`.
- ₹999 is stored as `99900`.

**Why use integers instead of floats?**

Floats and doubles don’t store exact values, but rather approximations. For financial transactions, this could lead to inaccurate calculations. Integers, however, represent exact values, which is critical when handling money.

#### Example:
- The line `paymentLinkRequest.put("amount", 1000);` translates ₹10.00 into 1000 paise.
- Razorpay’s API allows up to 2 decimal places. Therefore, to charge ₹10.01, you need to send 1001.

---

## Handling Redirection Failures by the Server


* **Question :** What happens if a customer successfully makes a payment but due to poor internet connectivity, the frontend doesn’t load? In this case, the user might be anxious because the payment status may not update properly on the frontend, even though the payment is completed.
* **Solution :** To solve this issue, payment gateways like Razorpay offer **webhooks**. These are HTTP callbacks triggered automatically by the gateway when certain events occur, such as payment completion. Even if the frontend fails to load, the server will still receive payment status updates.

**Steps to set up a webhook in Razorpay**:
* Log in to the Razorpay dashboard.
* Navigate to the **Webhooks** section.
* Create a new webhook and specify the events you want to listen to, such as:
   - **payment_link_paid**
   - **payment_link_expired**
   - **payment_link_cancelled**
* Provide the server URL where the webhook data should be sent.

---

### **LocalTunnel for Webhook Testing**

Since your local machine is typically not accessible from the internet, use **LocalTunnel** to expose your local server to external services like Razorpay for webhook testing.

1. Install LocalTunnel via npm:
   ```bash
   npm install -g localtunnel
   ```
2. Run LocalTunnel on the port where your server is running (e.g., port 8080):
   ```bash
   lt --port 8080
   ```
3. This command generates a public URL that forwards requests to your local machine. Use this URL in Razorpay’s webhook configuration for testing purposes.

**Final Steps**:
- Add a webhook handler in your `PaymentController`.
- Test the complete payment flow with Razorpay, demonstrating how the server handles redirection and payment status updates.


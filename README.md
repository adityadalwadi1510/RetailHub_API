# ShopMange

>This project entails the development of a RESTful API designed to streamline the management of products and orders within a specific shop. Within this API, you'll find a comprehensive set of endpoints that facilitate the addition, modification, and removal of shop-related products and orders. Whether you need to create, update, or remove items, this API provides the necessary functionality to efficiently handle your shop's inventory and orders.

# Table of Contents
<ol type="1">
  <li>Introduction</li>
  <li>Design
    <ol type="i">
      <li>Structure</li>
      <li>Technology</li>
      <li>Database</li>
      <li>Authentication and Authorization</li>
    </ol>
  </li>
<!--   <li>Getting Started
    <ol type="i">
      <li>Setup</li>
    </ol>
  </li>
  <li>API Documentation
    <ol type="i">
      <li>Endpoints</li>
      <li>Usage</li>
      <li>Examples</li>
    </ol>
  </li>
  <li>Future Developments
    <ol type="i">
      <li>Future Scope</li>
    </ol>
  </li> -->
</ol>

## Introduction
Welcome to our REST API project, tailored for managing a specific shop's products and orders.

Within this API, we developed essential functionalities to create and update shop information, add multiple products, and efficiently retrieve product data with pagination to minimize network bandwidth usage. It also provides the ability to update product details and mark items as out of stock.

For order management, the API offers basic features, including adding orders, changing order statuses, and fetching orders based on specific dates. Explore the subsequent sections to understand the project's design, setup, and detailed documentation.

## Design
Designing our API before coding is like planning a blueprint for a building; it sets the foundation for a successful project. It defines the structure, endpoints, and functionality, ensuring that the code you write aligns with our goals, promotes scalability, and minimizes errors. In short, good design is the key to efficient and effective API development :)
### Structure
We've meticulously crafted the project's code structure to guarantee straightforward maintenance and adaptability as the project progresses. Our approach primarily revolves around utilizing the model and controller architecture for handling database code and computation-related logic efficiently.

Module-level Design: To enhance module-level testing and reusability, we've encapsulated major components like authentication and constant variables and functions within separate directories and files. This modular approach simplifies testing and makes it easier to reuse components throughout the project.

File-level Design: We've named each file according to its primary functionality. This naming convention makes it a breeze to locate and work on specific features within the relevant module, ensuring an efficient development process.

### Technology
We primarily chose the **Flask framework** for our API development because of its lightweight nature and exceptional scalability, allowing us to adapt to varying levels of API traffic. Furthermore, our decision was influenced by the fact that **Python**, the language of choice, aligns with our future development plans. These key reasons underpin our selection of the Flask framework.

### Database
In this application, we've harnessed the power of PostgreSQL as our database. PostgreSQL not only offers all the features provided by MySQL but also boasts a strong reputation for reliability, feature robustness, and outstanding performance. This choice ensures our data storage is secure, efficient, and well-equipped to meet our application's needs.

### Authentication and Authorization
Authentication and authorization in our system are managed through the use of JWT (JSON Web Tokens). JWT tokens serve as a secure and efficient way to confirm the identity of users and control their access to various resources within the application. By leveraging JWT, we can validate user credentials, grant access to specific endpoints, and maintain a high level of security. This approach not only enhances the user experience but also strengthens the protection of sensitive data and resources throughout the application.

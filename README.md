# blogging-app-with-graphql-django
Using GraphQL in your Python Django application

REST API has been the most popular architectural style for designing Application Programming Interfaces (APIs). It provided better efficiency, increased scalability & improved performance to its counterpart SOAP.

However, REST API encounters a few major drawbacks as the app complexity grows:

Inflexible Structure

In the REST API paradigm Server defines the structure of the data which leaves the Client completely inflexible to changes

Strong Coupling between Client-Server

The only way for the Client to access some data is if the server has an exposed endpoint for it.

Under-fetching/ Over-fetching

As the structure defined by the Server is fixed and inflexible, Client is faced with problems like over fetching or under fetching of data

Multiple API calls

Requesting correct and complete data in REST API structure frequently results in multiple roundtrip API calls which reduces performance over time

The solution for all the above problems is GraphQL! As per docs

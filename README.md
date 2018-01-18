Please create a web app that accepts a csv file with 1 column containing of multiple integers (max 1 - 999), for each number in this column it checks whether it is a prime number. If the provided number is not a prime number and > 20 it should be represented as a sum of 3 prime numbers in two different ways

e.g for a two digit number:

User input = 35, not prime

Option 1: 2 + 2 + 31
Option 2: 3 + 3 + 29

35 = 2 + 2 + 31 = 3 + 3 + 29

Additional requirements:

1. Web app should be created on Google App Engine
2. User should be able to upload a csv file via html form, which triggers the start of a function.
3. The representation of the sum should be done in a separate microservice. Main app should start several identical microservices concurrently.
4. User should receive an output csv file with 5 columns (number, prime TRUE / FALSE, Option 1 (string), Option 2 (string), processing time in ms).
5. The app should run completely within GAE free tier

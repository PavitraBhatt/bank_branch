📌 Project Overview
The Branch Service is a GraphQL-based Django application that allows querying bank branches along with their related bank details. The application uses raw SQL queries for optimized performance and flexibility when retrieving data from the PostgreSQL database.

🚀 Problem Statement
Initially, we faced the following challenges while implementing the allBranch query:

Dynamically Filtering Data

We needed to filter branches based on different input parameters (e.g., bank_id, ids), but Django ORM's filter method was too restrictive for this case.

The goal was to allow queries like:

graphql
Copy
Edit
query {
  allBranch(input: { bank_id: 1 }) {
    branch
    ifsc
    bank {
      name
    }
  }
}
The challenge was to dynamically construct an SQL query based on any user-provided filters.

Handling Nested Data (Branches & Banks)

Each branch is linked to a bank, and we needed to return nested JSON data for GraphQL responses.

Django ORM’s built-in methods didn't provide efficient ways to fetch and format this nested structure.

Performance Optimization

Since the dataset might grow significantly, we wanted to avoid unnecessary joins and improve query efficiency.

Django ORM queries resulted in extra database hits due to the way related objects are fetched.

🛠️ Solution Approach
✅ Using Raw SQL Queries
Instead of relying on Django ORM, we used raw SQL queries with django.db.connection.cursor().
This allowed us to:

Dynamically build SQL queries based on user input.

Fetch only the necessary fields, reducing database load.

Return structured JSON responses efficiently.

✅ Dynamic Query Construction
We looped through the input dictionary to automatically generate the WHERE clause based on provided filters.

This ensured that users could pass any combination of filters without modifying the resolver.

Example: If the user provides {bank_id: 1}, our query dynamically becomes:

sql
Copy
Edit
SELECT br.id AS branch_id, br.branch AS branch_name, br.ifsc AS branch_ifsc,
       b.id AS bank_id, b.name AS bank_name
FROM branch_branch AS br
JOIN banks_bank AS b ON br.bank_id = b.id
WHERE br.bank_id = 1;
If ids are provided:

sql
Copy
Edit
WHERE br.id IN (9, 15, 22);
This approach prevents hardcoding conditions in the SQL query.

✅ Returning Nested JSON Format
Since GraphQL expects a nested structure, we manually structured the query results into a JSON format before returning them.

Instead of using Django’s serializer, we built the response in Python using list comprehensions.


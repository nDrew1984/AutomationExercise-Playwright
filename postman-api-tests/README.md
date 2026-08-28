# AutomationExercise API Tests (Postman)

API tests for the public REST API of [automationexercise.com](https://automationexercise.com), built and organized in Postman.

## Structure

- **Products** – product listing, search (valid term, empty string, non-existing term, missing parameter)
- **Brands** – brand listing, including response schema and field type validation
- **Accounts** – full CRUD flow: create, read, update, delete a user account, with independent verification after each write operation
- **Auth** – login validation (valid/invalid credentials, non-existing email, missing parameters)

## How to run

1. Import `AutomationExercise-API.postman_collection.json` into Postman
2. Open the Collection Runner, select the collection, and run it

## Key findings

- Error handling is inconsistent across endpoints: some (e.g. `searchProduct`, `createAccount`) always return HTTP 200 and signal errors via the `responseCode` field in the body, while others (e.g. `verifyLogin`) correctly use HTTP status codes (404, 400).
- `verifyLogin` returns the same `"User not found!"` message for both a wrong password and a non-existing email — a deliberate security measure against user enumeration.
- The website's UI search and the public `/api/searchProduct` endpoint behave differently: an empty search on the UI returns all products, while the same empty parameter sent directly to the API returns an empty result list.

## Related project

UI automation for the same site (Playwright + pytest): see repository root.

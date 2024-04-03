# Web API Template

## Local development

At project root, perform the following.

1. Use python 3.12
    ```sh
    pyenv install 3.12
    pyenv local 3.12
    ```
2. Install poetry
    ```sh
    brew install poetry
    ```
3. Set up virtual environment
    ```sh
    poetry env use 3.12
    poetry install
    ```
4. Apply migrations and create a superuser for testing purposes
    ```sh
    make migrate
    # use 'admin' as the username and 'password' as the password
    poetry run python manage.py createsuperuser
    ```
5. Create a personal config file (replace `<API_KEY>` and `<URL>` with the appropriate values, this is to avoid having sensitive information in the codebase)
   ```sh
   touch web_api/config/personal.py
   echo "GOOGLE_REVERSE_GEOCODING_API_KEY = <API_KEY>" >> web_api/config/personal.py
   echo "PARTNER_API_URL = <URL>" >> web_api/config/personal.py
   ```
6. See the `core_partnerlocation` table with test data (if available)
7. Run the server
    ```sh
    make serve
    ```
   
## API

In a web browser, navigate to http://localhost:8000/api/v1/appointments/next-available/ to see the generated API documentation.

```http
GET /api/v1/appointments/next-available/?lat=123.456&lon=789.123 HTTP/1.1
Host: localhost:8000
Authorization: Basic admin:password
Accept: application/json
```

```json
{
    "location_id": "test_location_id",
    "appointment_time": 1712145600000
}
```

## What's next

1. Add unit tests to cover the codebase (views, services, client, data access)
2. Add integration tests to cover the API endpoints
3. Add a caching mechanism to cache reverse geocoding results
   - If zip code to location id mappings are mostly static, we can cache these as well
4. Consider a different api framework that has a better support for async operations
   - Django ORM doesn't fully support async yet
5. Calls for getting availabilities for multiple locations can be parallelized
6. http session should be reused for multiple requests to reduce overhead
7. Sorting for time is done using the standard library `sorted` which might not be the most efficient way

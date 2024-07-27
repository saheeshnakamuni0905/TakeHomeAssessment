# TakeHomeAssessment

This project is a web application that displays a list of companies and their details, including multiple possible locations. The application uses Flask or Django for the backend, React for the frontend, and Docker for containerization.

## Prerequisites

- Docker
- Docker Compose

## Setup and Run

1. **Clone the repository**:

    ```bash
    git clone https://github.com/saheeshnakamuni0905/TakeHomeAssessment.git
    cd TakeHomeAssessment
    ```

2. **Build and run the Docker containers**:

    ```bash
    docker-compose up --build
    ```

    This command will build and start the frontend and backend containers.

## Accessing the Application

- **Frontend**: Open your browser and navigate to [http://localhost:3000](http://localhost:3000)
- **Backend API**: The backend API is accessible at [http://localhost:8000/api](http://localhost:8000/api)
- **Swagger UI**: For API documentation, open [http://localhost:8000/api/swagger/](http://localhost:8000/api/swagger/)
## Additional Notes

- If you encounter any issues with the Docker containers, try rebuilding them using:

    ```bash
    docker-compose up --build
    ```

- To stop the Docker containers, press `Ctrl + C` in the terminal where `docker-compose up` is running.

- Ensure that you have the latest version of Docker and Docker Compose installed on your system.

## Project Structure

- **backend**: Contains the Django backend application.
- **frontend**: Contains the React frontend application.
- **docker-compose.yml**: Docker Compose configuration file to set up the multi-container application.

## API Endpoints

- **/api/companies/**: Endpoint to fetch all companies.
- **/api/companies/{id}/**: Endpoint to fetch details of a specific company.
- **/api/companies/{id}/locations/**: Endpoint to fetch locations of a specific company.

## Running Tests

To run the tests for both frontend and backend, use the following commands:

- **Frontend Tests**:

    ```bash
    docker-compose run frontend npm test
    ```

- **Backend Tests**:

    ```bash
    docker-compose run backend python manage.py test
    ```

## Contact

For any questions or inquiries, please feel free to reach out:

- LinkedIn: [Saheeshna Kamuni](https://www.linkedin.com/in/saheeshna-kamuni-30a09b62/)
- Email: kamuni.s@northeastern.edu
- Portfolio : https://main--saheeshnakamuni.netlify.app/


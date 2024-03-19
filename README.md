# Web Application API

This project encompasses a RESTful API designed to handle various web application requests with clear demarcations between successful and failing operations. Included are thorough examples of request types, database setup, and environment configuration for a seamless setup and testing experience.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- MySQL
- MySQL Workbench (suggested)
- Python 3
- pip

### Installing

1. **Clone the repository**

```bash
git clone https://github.com/tarekchaalan/CPSC-449-Assignment-1.git
```

2. **Set up the MySQL database**

- Open MySQL Workbench.
- Go to Server > Data Import.
- Select "Import from Self-Contained File" and choose the provided SQL file.
- Start the import.

3. **Configure Database Connection**

- In `config.py`, change `SQLALCHEMY_DATABASE_URI` to match your MySQL credentials and database name.

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://USERNAME:PASSWORD@localhost/DBNAME'
```

4. **Create a virtual environment**

Navigate to the project directory and run:

```bash
python -m venv env
```

Activate the virtual environment:

- On Windows:

```bash
.\env\Scripts\activate
```

- On Unix or MacOS:

```bash
source env/bin/activate
```

5. **Install the requirements**

With the virtual environment activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

6. **Running the server**

To start the server, run:

```bash
python run.py
```

## Postman Request Examples

Below are examples of various API requests and their outcomes, indicating successful operations and error handling.

### POST Requests

#### Successful POST Request
This screenshot shows a successful POST request, where a new item has been added to the inventory.
![Successful POST Request](https://github.com/tarekchaalan/CPSC-449-Assignment-1/blob/main/Postman%20Requests/POST%20-%20Should%20Succeed.png)

#### Failed POST Request
Here we see a failed POST request due to missing required fields, demonstrating the API's validation logic.
![Failed POST Request](https://github.com/tarekchaalan/CPSC-449-Assignment-1/blob/main/Postman%20Requests/POST%20-%20Should%20Fail.png)

### GET Requests

#### Successful GET Request
This image depicts a successful GET request, retrieving an item from the inventory.
![Successful GET Request](https://github.com/tarekchaalan/CPSC-449-Assignment-1/blob/main/Postman%20Requests/GET%20-%20Should%20Succeed.png)

#### Failed GET Request
This is an example of a failed GET request, where the requested item is not found in the inventory.
![Failed GET Request](https://github.com/tarekchaalan/CPSC-449-Assignment-1/blob/main/Postman%20Requests/GET%20-%20Should%20Fail.png)

### PUT Requests

#### Successful PUT Request
In this screenshot, we see a successful PUT request updating an item's details in the inventory.
![Successful PUT Request](https://github.com/tarekchaalan/CPSC-449-Assignment-1/blob/main/Postman%20Requests/PUT%20-%20Should%20Succeed.png)

#### Failed PUT Request
This image shows a failed PUT request where the update operation is unsuccessful due to invalid data.
![Failed PUT Request](https://github.com/tarekchaalan/CPSC-449-Assignment-1/blob/main/Postman%20Requests/PUT%20-%20Should%20Fail.png)

### DELETE Requests

#### Successful DELETE Request
This screenshot demonstrates a successful DELETE request, removing an item from the inventory.
![Successful DELETE Request](https://github.com/tarekchaalan/CPSC-449-Assignment-1/blob/main/Postman%20Requests/DELETE%20-%20Should%20Succeed.png)

#### Failed DELETE Request
Here is an example of a failed DELETE request, indicating the item to delete was not found.
![Failed DELETE Request](https://github.com/tarekchaalan/CPSC-449-Assignment-1/blob/main/Postman%20Requests/DELETE%20-%20Should%20Fail.png)

### Support

For support, contact <tchaalan23@csu.fullerton.edu>.

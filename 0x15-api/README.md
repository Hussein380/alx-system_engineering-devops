# API Data Gathering

This project involves using a REST API to gather and display information about an employee's TODO list progress. The script is written in Python and makes use of the `requests` library to interact with the API.

# Requirements

- Python 3.8.5
- `requests` library
- The script should be executable

## Usage

The script accepts an employee ID as a command-line argument and displays the employee's TODO list progress.

### Example

To run the script:

```sh
./0-gather_data_from_an_API.py <employee_id>
```

For example:

```sh
./0-gather_data_from_an_API.py 2

Output:


Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
```

## Project Structure

- `0-gather_data_from_an_API.py`: The main Python script that fetches and displays the data.
- `README.md`: This file containing the project description and instructions.

## Script Details

The script performs the following tasks:

1. Fetches user data for a given employee ID from the API endpoint `https://jsonplaceholder.typicode.com/users/<employee_id>`.
2. Fetches TODO list data for the same employee from the API endpoint `https://jsonplaceholder.typicode.com/todos?userId=<employee_id>`.
3. Calculates the number of completed tasks and the total number of tasks.
4. Displays the employee's TODO list progress in the specified format.

### Script Usage

1. Import Necessary Libraries:
    - `requests`: For making HTTP requests.
    - `sys`: For handling command-line arguments.

2. Fetch Data from the API**:
    - The `fetch_employee_data` function retrieves user data and TODO list data for the specified employee.

3. Display TODO List Progress:
    - The `display_employee_todo_progress` function formats and prints the employee's TODO list progress, including the titles of completed tasks.

4. Command-Line Interface:
    - The script accepts an employee ID as a command-line argument.
    - If the employee ID is not provided or is not an integer, the script exits with an error message.

# Notes

- Ensure the script is executable by running `chmod +x 0-gather_data_from_an_API.py`.
- The script adheres to PEP8 Python style guidelines.
- The libraries imported in the Python file are organized in alphabetical order.
- The script uses the `get` method to access dictionary values to avoid exceptions if the key doesn't exist.

# References

- [What is an API](https://www.programmableweb.com/api-university/what-are-apis-and-how-do-they-work)
- [What is a REST API](https://restfulapi.net/)
- [PEP8 Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Requests Library Documentation](https://docs.python-requests.org/en/master/)

## Author

This project was created by Hussein Garane

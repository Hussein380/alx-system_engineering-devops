# Reddit API Advanced

## Overview

This project involves interacting with the Reddit API to fetch and process data from various subreddits. The tasks in this project help you get familiar with making API calls, handling pagination, parsing JSON data, making recursive calls, and sorting data. Mastering these tasks is useful for technical interviews and practical applications.

## Learning Objectives

By the end of this project, you should be able to:
- Read API documentation to find the endpoints you need.
- Use an API with pagination.
- Parse JSON results from an API.
- Make recursive API calls.
- Sort a dictionary by value.

## Requirements

- *Editors*: vi, vim, emacs
- *Environment*: All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- *Style*: Code must adhere to PEP 8 style guidelines.
- *Executable*: All scripts must be executable.
- *Libraries*: Must use the `requests` library for making HTTP requests.

## Files and Modules

### 0. How many subs?
*File*: `0-subs.py`

Function that queries the Reddit API and returns the number of subscribers for a given subreddit.

### 1. Top Ten
*File*: `1-top_ten.py`

Function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

### 2. Recurse it!
*File*: `2-recurse.py`

Recursive function that queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.

### 3. Count it!
*File*: `100-count.py`

Recursive function that queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords.

## Usage

### 0. How many subs?

To find the number of subscribers for a subreddit:
```bash
$ ./0-main.py <subreddit>
```

### 1. Top Ten

To print the titles of the first 10 hot posts for a subreddit:
```bash
$ ./1-main.py <subreddit>
```

### 2. Recurse it!

To get a list of titles of all hot articles for a subreddit:
```bash
$ ./2-main.py <subreddit>
```

### 3. Count it!

To count and print the occurrences of keywords in the titles of hot articles for a subreddit:
```bash
$ ./100-main.py <subreddit> <'keyword1 keyword2 keyword3'>
```

## Examples

### 0. How many subs?
```bash
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```

### 1. Top Ten
```bash
$ python3 1-main.py programming
Post Title 1
Post Title 2
...
Post Title 10
$ python3 1-main.py this_is_a_fake_subreddit
None
```

### 2. Recurse it!
```bash
$ python3 2-main.py programming
932
$ python3 2-main.py this_is_a_fake_subreddit
None
```

### 3. Count it!
```bash
$ python3 100-main.py programming 'python java javascript'
java: 27
javascript: 20
python: 17
$ python3 100-main.py programming 'JavA java'
java: 54
$ python3 100-main.py not_a_valid_subreddit 'python java javascript'
```

## Project Structure

```
.
├── 0-main.py
├── 0-subs.py
├── 1-main.py
├── 1-top_ten.py
├── 2-main.py
├── 2-recurse.py
├── 100-main.py
├── 100-count.py
└── README.md
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This README provides an overview of the project, including its objectives, requirements, and usage examples for each task.

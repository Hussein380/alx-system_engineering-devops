Project Title: MySQL Setup and Backup Automation
# Overview
This project aims to set up a MySQL database infrastructure with primary-replica replication and implement an automated backup solution for data security and redundancy.

## Table of Contents
1. [Introduction](#introduction)
2. [Tasks](#tasks)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

# Introduction
MySQL is a widely used relational database management system known for its reliability, performance, and ease of use. In this project, we'll install MySQL, set up primary-replica replication, and implement a backup strategy to ensure data integrity and availability.

# Tasks
1. Install MySQL: Install MySQL 5.7.x on designated servers.
2. User Setup: Create MySQL users with appropriate permissions for replication and monitoring.
3. Database Preparation: Create a database with tables and data for replication testing.
4. Primary-Replica Setup: Configure MySQL replication between primary and replica servers.
5. Backup Automation: Develop a Bash script to generate MySQL backups and store them securely.

# Setup
To get started with this project, ensure you have access to the designated servers and necessary permissions to install software and configure MySQL. Make sure you have the required SSH keys configured for server access.

# Usage
1. Installation: Run the provided Bash script to install MySQL on the designated servers.
2. User Setup: Execute SQL commands to create MySQL users with appropriate permissions.
3. Database Preparation**: Create databases, tables, and data for testing replication.
4. Primary-Replica Setup: Configure MySQL replication by modifying MySQL configuration files.
5. Backup Automation: Utilize the provided Bash script to automate MySQL backups. Pass the MySQL root password as an argument to the script

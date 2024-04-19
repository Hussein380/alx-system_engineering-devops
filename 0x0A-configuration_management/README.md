
# Configuration Management with Puppet

This project is designed to familiarize you with basic configuration management tasks using Puppet. It covers various aspects such as file management, package installation, and executing commands.

# Project Overview

In this project, you will utilize Puppet to automate several tasks commonly encountered in system administration and DevOps environments. These tasks include:

1. Creating a file with specific permissions, owner, group, and content.
2. Installing a package (Flask) with a specific version using pip3.
3. Executing a command to terminate a specific process.

# Project Structure

The project is organized into directories, each containing Puppet manifest files (.pp) for individual tasks:

- `0x0A-configuration_management`
  - `0-create_a_file.pp`: Creates a file with specific permissions, owner, group, and content.
  - `1-install_a_package.pp`: Installs the Flask package with a specific version using pip3.
  - `2-execute_a_command.pp`: Executes a command to terminate a specific process.

# Prerequisites

Before running the Puppet manifests, ensure the following prerequisites are met:

- Ubuntu 20.04 LTS environment.
- Puppet 5.5 preinstalled.
- Puppet-lint version 2.1.1 installed.
  
# Getting Started

1. Clone the project repository:

   git clone https://github.com/your_username/alx-system_engineering-devops.git

2. Navigate to the appropriate directory for the task you want to perform.

3. Run the Puppet manifest using the following command:

   puppet apply <filename>.pp

4. Verify the task execution and any relevant output.

# Task Details

# 0. Create a file

Creates a file in `/tmp` with specific permissions, owner, group, and content.

# 1. Install a package

Installs the Flask package with version 2.1.0 using pip3.

# 2. Execute a command

Executes a command to terminate a specific process named "killmenow" using Puppet's `exec` resource.

# Author

This project was created by [Hussein]```

# Web Stack Debugging #2

# Overview
This project aims to delve into debugging web stack issues and implementing security best practices. It involves fixing configurations and permissions related to Nginx web server to ensure smooth and secure operation.

# Concepts
The primary concept explored in this project is *Web stack debugging*.

# Requirements
- /*Environment*/: All files are interpreted on Ubuntu 20.04 LTS.
- /*File Endings*/: All files should end with a new line.
- /*README*/: A README.md file at the root of the project folder is mandatory.
- /*Executable Scripts*/: All Bash script files must be executable.
- /*Shellcheck*/: Bash scripts must pass Shellcheck without any error.
- /*Error-free Execution*/: Bash scripts must run without error.
- /*Script Declaration*/: The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`.
- /*Commenting*/: The second line of all Bash scripts should be a comment explaining the script's purpose.

# Tasks
# Task 0: Run software as another user
Implement a Bash script that runs the `whoami` command under the user passed as an argument.

# Task 1: Run Nginx as Nginx
Configure the container so that Nginx runs as the `nginx` user, listening on all active IPs on port 8080. Ensure the process is not running as the `root` user.

# Task 2: 7 lines or less
Build upon Task 1, crafting a concise Bash script to achieve the same outcome within 7 lines.

# Repository Information
- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/USERNAME/alx-system_engineering-devops)
- **Directory**: 0x12-web_stack_debugging_2

#Files
- `0-iamsomeoneelse`: Bash script for Task 0.
- `1-run_nginx_as_nginx`: Bash script for Task 1.
- `100-fix_in_7_lines_or_less`: Bash script for Task 2.

# HTTPS SSL Project README

## Project Overview

This project aims to implement HTTPS SSL termination using HAProxy, configure subdomains, and enforce HTTPS traffic redirection. It involves setting up SSL termination on HAProxy, configuring domain zones, and ensuring secure web traffic.

## Project Structure

The project is organized into tasks, each focusing on specific aspects of HTTPS SSL implementation:

1. World wide web
    - Configure domain zone and create a script to display information about subdomains.
    
2. HAProxy SSL termination
    - Create a certificate using certbot and configure HAProxy to accept encrypted traffic for the subdomain www.

3. No loophole in your website traffic (Advanced)
    - Configure HAProxy to automatically redirect HTTP traffic to HTTPS.

## Task Details

### Task 0: World wide web

- Configure domain zone to point subdomains to respective IPs.
- Create a Bash script to display information about subdomains.
- Script should accept domain and optional subdomain as arguments.

### Task 1: HAProxy SSL termination

- Configure HAProxy to terminate SSL traffic for subdomain www.
- HAProxy should serve encrypted traffic returning the root of the web server.
- Provide HAProxy configuration file.

### Task 2: No loophole in your website traffic (Advanced)

- Configure HAProxy to automatically redirect HTTP traffic to HTTPS.
- HAProxy should transparently return a 301 redirect.
- Provide HAProxy configuration file.

## Repository Information

- GitHub Repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
- Directory: 0x10-https_ssl

## Execution Instructions

- Each task has its own script or configuration file.
- Scripts should be executed on Ubuntu 16.04 LTS.
- Ensure scripts are executable (`chmod +x script.sh`).
- HAProxy configurations should be placed in `/etc/haproxy/haproxy.cfg`.

## Additional Notes

- Follow task requirements strictly.
- Ensure scripts pass Shellcheck without errors.
- Provide necessary documentation and comments in scripts and configuration files.

--- 

This README provides an overview of the HTTPS SSL project, including task details, repository information, execution instructions, and additional notes. It serves as a guide for project execution and understanding.

## Web Server Configuration Project

# Overview
In this project, we'll be setting up and configuring a web server using Nginx on Ubuntu 16.04. The main goal is to automate the setup process and ensure the server meets specific requirements such as listening on port 80, handling redirects, setting up custom error pages, and more.

# Project Structure
- 0x0C-web_server: Main project directory.
  - 0-transfer_file: Bash script to transfer files to the server.
  - 1-install_nginx_web_server: Bash script to install Nginx and configure it to serve a "Hello World!" page.
  - 2-setup_a_domain_name: File containing the registered .tech domain name.
  - 3-redirection: Bash script to configure Nginx to handle redirects.
  - 4-not_found_page_404**: Bash script to configure a custom 404 error page.
  - 7-puppet_install_nginx_web_server.pp: Puppet manifest to install and configure Nginx with redirection.

# Tasks
1. Transfer a file to your server: This task involves creating a Bash script to transfer files from a client to the server using scp.
2. Install Nginx web server: Install Nginx on the server and configure it to serve a "Hello World!" page.
3. Setup a domain name: Register a .tech domain and configure DNS records to point to the server's IP address.
4. Redirection: Configure Nginx to handle a 301 redirect from a specific URL to another page.
5. Not found page 404: Configure Nginx to display a custom 404 error page.

# Usage
1. Clone the repository: `git clone https://github.com/username/alx-system_engineering-devops.git`
2. Navigate to the `0x0C-web_server` directory.
3. Execute the respective scripts or manifest for each task:
   - For Bash scripts: `./script_name`
   - For Puppet manifest: `sudo puppet apply 7-puppet_install_nginx_web_server.pp`

# Note
Ensure proper permissions are set for executing the Bash scripts: `chmod +x script_name`

# Contributors
- [Your Name](https://github.com/your_username)
- [Collaborator Name](https://github.com/collaborator_username)

# Resources
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Ubuntu Documentation](https://help.ubuntu.com/)
- [Bash Scripting Guide](https://www.gnu.org/software/bash/manual/bash.html)
- [Puppet Documentation](https://puppet.com/docs/)

## Load Balancer Project

### Introduction
This project aims to enhance the redundancy and reliability of our web infrastructure by implementing a load balancer and configuring additional web servers. Load balancing will distribute incoming traffic across multiple web servers, improving performance and ensuring high availability.

### Tasks Overview
1. Double the number of webservers
   - Configure web-02 to mirror the setup of web-01.
   - Add a custom HTTP response header (`X-Served-By`) to Nginx on both web servers to track server handling requests.

2. Install your load balancer
   - Install and configure HAProxy on lb-01 server.
   - Configure HAProxy to distribute traffic using a round-robin algorithm to web-01 and web-02.
   - Ensure HAProxy can be managed via an init script.

3. Add a custom HTTP header with Puppet (Advanced)**
   - Automate the task of creating a custom HTTP header using Puppet.

### Project Repository
- GitHub Repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
- Directory: 0x0F-load_balancer

### File Structure
- 0-custom_http_response_header: Bash script to configure Nginx with custom HTTP response headers on web servers.
- 1-install_load_balancer: Bash script to install and configure HAProxy on lb-01 server.
- 2-puppet_custom_http_response_header.pp: Puppet manifest to automate adding custom HTTP response headers.

### Requirements and Considerations
- All scripts are designed to configure brand new Ubuntu servers.
- Scripts are executable and pass Shellcheck without errors.
- Documentation follows a standardized format with clear explanations.
- Server hostnames must be correctly configured as [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.
- Initiatives taken to automate tasks where possible, promoting efficiency and consistency.

### Usage
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/username/alx-system_engineering-devops.git
   ```

2. Navigate to the appropriate directory:
   
   cd 0x0F-load_balancer
   

3. Execute the desired script or manifest to perform the specified task.

### Contributors
- [Your Name](https://github.com/yourusername)
- [Co-contributor's Name](https://github.com/cocontributor)

## Acknowledgments
- This project is a part of the ALX Software Engineering program.
- Special thanks to our mentors and instructors for their guidance and support.

### License
This project is licensed under the [MIT License](LICENSE).

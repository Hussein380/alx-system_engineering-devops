# Web Stack Debugging #3

## Overview
This project involves debugging a Wordpress website running on a LAMP (Linux, Apache, MySQL, and PHP) stack. The goal is to resolve an issue causing Apache to return a 500 Internal Server Error by using strace to trace system calls and then automate the fix using Puppet.

## Project Details
### Task
- **0. Strace is your friend**
  - Use strace to identify why Apache is returning a 500 error.
  - Fix the issue and automate it using Puppet.
  
### Requirements
- All files should be interpreted on Ubuntu 14.04 LTS.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without errors.
- Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

## How to Run
1. Clone the repository from GitHub: `git clone https://github.com/username/alx-system_engineering-devops.git`
2. Navigate to the directory `0x17-web_stack_debugging_3`.
3. Run Puppet lint to check for any syntax errors: `puppet-lint --version 2.1.1 *.pp`
4. Apply the Puppet manifest: `puppet apply 0-strace_is_your_friend.pp`
5. Test the fix by accessing the website or using curl.

# Additional Information
- Install puppet-lint by running:
  ```
  $ apt-get install -y ruby
  $ gem install puppet-lint -v 2.1.1
  ```
- Consider using tmux to run strace in one window and curl in another for efficient debugging.

# Contributors
- [Hussein Garane](https://github.com/Hussein380) - Developer

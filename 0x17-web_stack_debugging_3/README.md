## 0x17. Web Stack Debugging #3

### Description
This project focuses on debugging a WordPress website running on a LAMP (Linux, Apache, MySQL, PHP) stack. The task involves using `strace` to trace the Apache process to identify why it's returning a 500 error, fixing the issue, and then automating the fix using Puppet.

### Concepts
- Web Server
- Web Stack Debugging

### Background Context
When debugging web applications, logs might not always provide sufficient information. In such cases, it becomes necessary to delve deeper into the stack to identify and resolve issues. WordPress, being a widely used tool, often requires debugging, especially when hosted on a LAMP stack.

### Requirements
- All files are interpreted on Ubuntu 14.04 LTS.
- Files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Puppet manifests must run without error and contain a comment explaining their purpose as the first line.
- Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

### Tasks
#### 0. Strace is Your Friend
**Objective:** Using `strace`, identify why Apache is returning a 500 error. Fix the issue and automate it using Puppet.

**Hint:**
- `strace` can attach to a currently running process.
- Use `tmux` to run `strace` in one window and `curl` in another.

### Example
```bash
$ curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

$ puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds

$ curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

$ curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
<div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>
<h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
<p>Yet another bug by a Holberton student</p>
```

### Repository
- GitHub Repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
- Directory: 0x17-web_stack_debugging_3
- File: 0-strace_is_your_friend.py

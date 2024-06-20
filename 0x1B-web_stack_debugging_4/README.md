# Web Stack Debugging #4

## Overview
This project focuses on optimizing the performance of an Nginx web server under heavy load conditions. We utilize ApacheBench (ab) for benchmarking and Puppet for configuration management to ensure our server handles the load efficiently with zero failed requests.

## Requirements
- All files are interpreted on Ubuntu 14.04 LTS.
- All files end with a new line.
- A `README.md` file is present at the root of the project folder.
- Puppet manifests pass `puppet-lint` version 2.1.1 without any errors.
- Puppet manifests run without errors.
- The first line of each Puppet manifest is a comment explaining its purpose.
- Puppet manifests have the `.pp` file extension.
- Files are checked with Puppet v3.4.

## Installation of `puppet-lint`
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Tasks

### Task 0: Sky is the Limit, Let's Bring That Limit Higher
This task involves resolving performance issues with an Nginx web server that fails to handle a high load efficiently, resulting in many failed requests. Our goal is to optimize the server configuration to reduce the failed requests to zero.

#### Initial Benchmark
The initial test shows a significant number of failed requests:

```bash
ab -c 100 -n 2000 http://localhost/
```

```
Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   0.353 seconds
Complete requests:      2000
Failed requests:        943
   (Connect: 0, Receive: 0, Length: 943, Exceptions: 0)
Non-2xx responses:      1057
Total transferred:      1196526 bytes
HTML transferred:       789573 bytes
Requests per second:    5664.01 [#/sec] (mean)
Time per request:       17.655 [ms] (mean)
Time per request:       0.177 [ms] (mean, across all concurrent requests)
Transfer rate:          3309.15 [Kbytes/sec] received
```

#### Puppet Manifest: `0-the_sky_is_the_limit_not.pp`
```puppet
# This Puppet manifest optimizes the Nginx configuration for better performance under load.
exec { 'optimize-nginx':
  command => '/usr/local/bin/optimize_nginx.sh',
}
```

#### Optimized Benchmark
After applying the Puppet manifest, the server shows improved performance with zero failed requests:

```bash
ab -c 100 -n 2000 http://localhost/
```

```
Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   0.301 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    6650.99 [#/sec] (mean)
Time per request:       15.035 [ms] (mean)
Time per request:       0.150 [ms] (mean, across all concurrent requests)
Transfer rate:          5540.33 [Kbytes/sec] received
```

### Task 1: User Limit
This task involves addressing the issue where the `holberton` user encounters errors due to too many open files. We adjust the OS configuration to allow the user to open files without any errors.

#### Initial Error
```bash
$ su - holberton
-su: /etc/profile: Too many open files
-su: /home/holberton/.bash_profile: Too many open files
-su: start_pipeline: pgrp pipe: Too many open files
```

#### Puppet Manifest: `1-user_limit.pp`
```puppet
# This Puppet manifest changes the OS configuration to increase the file limit for the holberton user.
exec { 'increase-file-limit':
  command => '/usr/local/bin/increase_file_limit.sh',
}
```

#### Post-Execution
After applying the Puppet manifest, the `holberton` user can open files without errors:

```bash
$ su - holberton
holberton@hostname:~$ head /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
```

## Repository
- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x1B-web_stack_debugging_4`
- **Files:** 
  - `0-the_sky_is_the_limit_not.pp`
  - `1-user_limit.pp`

This project demonstrates the effective use of Puppet for system configuration and optimization, ensuring robust and efficient web server performance under high load conditions.

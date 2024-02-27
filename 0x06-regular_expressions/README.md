Regular Expression Project

This project involves the use of regular expressions in Ruby scripts, utilizing the Oniguruma library. Each Ruby script matches regular expressions based on an argument passed to it via the command line.

 Tasks

0. Simply matching Holberton
- File: [0-simply_match_holberton.rb](./0-simply_match_holberton.rb)
-Description: Matches the regular expression `School`.

1. Repetition Token 0
- File: [1-repetition_token_0.rb](./1-repetition_token_0.rb)
- Description: Matches the regular expression `hbn` with between 2-5 `t`'s in between `hb` and `n`.

2. Repetition Token 1
- File:[2-repetition_token_1.rb](./2-repetition_token_1.rb)
- Description: Matches the regular expression `hn` with 0 or 1 occurrences of `b` and 0 or 1 occurrences of `t` in between `h` and `n`.

 3. Repetition Token #2
- File: [3-repetition_token_2.rb](./3-repetition_token_2.rb)
- Description: Matches the regular expression `hbn` with 1 or more `t`'s in between `hb` and `n`.

 4. Repetition Token #3
- File: [4-repetition_token_3.rb](./4-repetition_token_3.rb)
- Description:Matches the regular expression `hbn` with 0 or more `t`'s in between `hb` and `n`.

 5. Not quite HBTN yet
- File: [5-beginning_and_end.rb](./5-beginning_and_end.rb)
- Description: Matches a regular expression starting with `h` and ending with `n` with any single character in between.

 6. Call me maybe
- File: [6-phone_number.rb](./6-phone_number.rb)
- Description: Matches a regular expression representing a 10-digit phone number.

 7. OMG WHY ARE YOU SHOUTING?
- File: [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./7-OMG_WHY_ARE_YOU_SHOUTING.rb)
- Description : Matches regular expressions of uppercase letters.

 8. Textme
- File: [100-textme.rb](./100-textme.rb)
- Description: Runs statistics on TextMe app text message transactions.
- Output: `[SENDER],[RECEIVER],[FLAGS]` where
  - [SENDER] is the sender phone number or name (including country code if present).
  - [RECEIVER] is the receiver phone number or name (including country code if present).
  - [FLAGS] are the flags that were used.

     Requirements
- Editors allowed: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- The first line of all Bash scripts should be exactly `#!/usr/bin/env ruby`
- All regular expressions must be built for the Oniguruma library


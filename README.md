# ip script
### *Remotely access ip address.*

- This is mostly all template/example code
- Set your own machine's paths in `run_sender.sh`
- Assume you cannot send mail from a non-gmail email account, but this has not yet been verified
- You may have to establish an app password in your [Google Account Security Settings](https://myaccount.google.com/security)


**config.py**
```
import os
FROM_EMAIL = os.environ.get('from_some_gmail@gmail.com') 
TO_EMAIL = os.environ.get('toAnyEmail@csumb.edu') 
PASSWORD = os.environ.get('your google app password')
```

__Add config.py to your .gitignore file if reusing code__
__or email me if there is a better way of hiding sensitive info__


----
ebleier4@gmail.com\
ebleier@csumb.edu
----


hours worked on: 1

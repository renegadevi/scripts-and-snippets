# Cronjob, I dislike sysadmin tasks, I need a quick cheat sheet.

View user crontabs: ```$ crontab -l```
View other contrabs: ```# crontab -u <username> -l```
Type to edit: ```contab -e```

| Minute | Hour | Day  | Month | Day of Week | Command to execute |
|--------|------|------|-------|-------------|--------------------|
| 0-59   | 0-23 | 1-31 | 1-12  | 0-6**        | rm -rf /tmp/*     |
** Sunday to Saturday (some systems is Sunday to Sunday)

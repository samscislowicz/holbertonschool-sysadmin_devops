## Issue Summary

On April 1st, 2017 at 3:10pm (PST) macandcheese.space website had an outage. The
outage until April 1st, 2017 at 5:00pm (PST). The impact was low,
the website was down for about 4 hours. Users were unable to reach the site
anytime during the outage. The root cause was an accidental removal of data
from our primary database server.


## Timeline

* 3:00pm (PST) - One of the engineers wiped the data directory for the primary thinking it was the secondary database directory. 
* 3:10pm (PST) - macandcheese.space starts experiencing an increase in database load.
* 3:15pm (PST) - Hoping they could restore the database the engineers involved went to look for the database backups.
* 4:00pm (PST) - Successfully found and backup on secondary database. Loaded the backup onto the primary server.
* 5:00pm (PST) - macandcheese.space was up and running again.

## Root Cause and Resolution

Macandcheese.space was down because the database directory of the primary database was removed by accident, instead of removing the database directory of the secondary. The issue was fixed by loading a backup from the other database onto the primary.


## Corrective and Preventative Actions

While we were lucky to have the backup on the other database, we need to continue to keep up to date backups and be sure not to delete such amounts of data. 

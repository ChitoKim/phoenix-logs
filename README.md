Tested with **Python 3.8+**

# Logs downloader

Tools to download phoenix replays from tenhou.net.

For example, these logs can be useful for machine learning.

This repo contains two main scripts:

- Download and store log IDs. 
It can both obtain game IDs from year archive (e.g., https://tenhou.net/sc/raw/scraw2009.zip) 
or from latest phoenix games page (https://tenhou.net/sc/raw/list.cgi).
- Download logs content for already collected log IDs.

# Installation

Just install requirements with command `pip install -r requirements.txt`

# Download log IDs

The first step is to add list of log IDs to the DB.

## Historical logs (per year)

For example, we want to download game IDs for the 2009 year (keep in mind that phoenix games started to appear only from the 2009 year).

Download https://tenhou.net/sc/raw/scraw2009.zip manually and put it to the `temp/scraw2009.zip`.

Input command:
```
python main.py -a id -y 2009 --from_archive
```

Output:
```
Preparing the list of games...
Found 80156 games
Temp folder was removed
Inserting new IDs to the database...
Done
```

## Latest log IDs
 
To download games from 1 January (current year) until (current day - 7 days) specify `-s` flag:

`python main.py -a id -s -p db/2021.db`

To download just log IDs from the latest 7 days:

`python main.py -a id -p db/2021.db`

You can add this command to the cron (for example to run each one hour) and it will add new log IDs to the DB.

## Download yakuman log IDs

You can download hanchans where yakuman was collected for specific year and month with this command:

`python download_yakuman_game_ids.py -y 2006 -m 10`

It will be saved to the `db/yakuman/2006/10.db` file.

After that you can download content for these IDs with this command: `python main.py -a content -p db/yakuman/2006/10.db -l 100000 -t 10 --strip`

# Download log content

To download log content for already downloaded IDs use this command:

`python main.py -a content -y 2009 -l 50 -t 3 --strip`

Where is `-l` is how many items to download and `-t` is the number of threads to use.

It will create N threads and parallel downloads. 

You can choose that `-l` and `-t` numbers to download logs that will take ~one minute and add this command to a cron job. 
I used `-l 180 -t 5` for my downloads.

# Validate that downloaded logs can be parsed

You can validate that all downloaded logs can be parsed with this command:

`python validate.py -y 2009`

It contains example of parsing log content on separate tags as well.


# Download games example

`python main.py -a id -p db/2024.db -y 2024 -s`

`python main.py -a content -p db/2024.db -l 100000 -t 1`

# Output raw mjlog(xml) game logs into text files

`python getxml.py -p {DB Path} -l {Limit} -o {Offset} -f {Format} -n {Output File Name}`

for example, if you have 2024.db in db folder

`python getxml.py -p db/2024.db -l 100 -o 0`

Then it outputs a single file containing 100 games, as db/2024.xml

# 🔍 ETHGlobal Explorer

Demo: https://x.com/mattwong_ca/status/1875358547569197460

<img width="1552" alt="ETHGlobalExplorer com" src="https://github.com/user-attachments/assets/a29d841a-40b0-4cdf-90a1-5b4cf35f973f" />

### Scripts

- `01_upload_prizes.py` - upload prizes to the database, using a prebuilt dict of prize logo urls <> prize names.
- `02_scrape_projects.py` - scrapes every project on the showcase page and saves the project data to a JSON file
- `03_upload_projects.py` - uploads the project data from the JSON file to the database

Next steps: make updating the db easier - ideally whenever there's a new hackathon, we can run a single script to update all tables. 

- Goal: add an event name like `bangkok`, and the script will check for any new sponsors + projects, and update the db accordingly. 

### Notes on Data Quality
- ETHGlobal's showcase page only has data from HackMoney (2020) and onwards (No ETHNYC either). Previous hackathons were likely hosted on platforms like Devpost (eg. [ETHWaterloo 2017](https://ethwaterloo.devpost.com/))
- Prize data (eg. prize logos on project cards) is only available from HackFS 2021 and onwards.
- Hackathon slugs with working links start at `/spacewarp` (also `/hackfs2022`), previous hackathons use a different URL or are broken
- On ethglobalexplorer.com, some sponsor logos have broken links / generic trophy logos - this means ETHGlobal represents them as generic trophy logos (I'll likely manually go through it and fix it in the future)

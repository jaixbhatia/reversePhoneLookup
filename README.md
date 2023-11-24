# reversePhoneLookup

1) goto consts.py and assign GPLACES_API_KEY and FUSION_API_KEY to their respective api keys
2) run main.py. there should be an interactive and it will output a list of results

example:
<img width="782" alt="Pasted Graphic" src="https://github.com/jaixbhatia/reversePhoneLookup/assets/66648216/dd4ad1d2-ec19-45a2-bce7-8102fc127327">


## Usage Instructions for sqlite db access

### Download the Database

1. Click the following link to download the database file: [cache.db](link will be added here soon)

### Accessing the Database

2. Install SQLite: If you don't have SQLite installed, you can download it from [SQLite Downloads](https://www.sqlite.org/download.html).

3. Open the Database:
   - On Windows:
     ```bash
     sqlite3 cache.db
     ```
   - On macOS and Linux:
     ```bash
     sqlite3 ./path/to/cache.db
     ```

### Sample Queries

Here are some sample SQL queries to get you started:

```sql
-- Retrieve all records from the 'cache' table
SELECT * FROM cache;

-- Retrieve names associated with a specific phone number
SELECT names FROM cache WHERE phone_number = '123-456-7890';

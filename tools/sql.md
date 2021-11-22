## Introduction

SQL is

## Summary

FYI

SQL Server (MS SQL)

https://www.microsoft.com/en-us/sql-server/sql-server-2022
https://www.youtube.com/watch?v=ncF-zFzBDAY
https://www.youtube.com/playlist?list=PL3EZ3A8mHh0xUC8xqFg7k1Qzp-f5HzbTB


## JSON Data

Storying JSON data in a table column:
- Usually json columns are defined with NVARCHAR(n), where n is size of the characters. NVARCHAR(MAX) for maximum size. 

- SQL server is found to have issues if NVARCHAR(MAX) is defined for a lot of columns. Based on the settings and situation, there may be slowdown of queries in certain circumstances.



### OPENJSON 

OPENDATA for Parsing JSON Columns

Example code to help build on examples are:
- A simple example code with inline json definition and parsing the data:
    - tools\sql\opendata_json_01.sql
- A simple json object parsed and insert into table
    - tools\sql\opendata_json_insert_into_table.sql
- A simple json object read from table and parsed. Contains, simple key parsing
    - tools\sql\opendata_json_read_from_table_to_relational_format.sql
- A json object read from table and parsed. Contains examples of simple key parsing, array, array values:
    - tools\sql\opendata_json_read_from_table_to_relational_format.sql

References:

[https://docs.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver15)

[https://www.sqlshack.com/how-to-parse-json-in-sql-server/](https://www.sqlshack.com/how-to-parse-json-in-sql-server/)

### References

Good reference cheatsheets

scripting language
https://github.com/zyxnowell/sql-cheatsheet

Finding data, data modification, reporting queries, join queries, view queries, altering table queries, creating table
https://github.com/enochtangg/quick-SQL-cheatsheet

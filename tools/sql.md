## Introduction

SQL is

## Summary

FYI

Use print statements to quickly check values, calculations etc.
<pre>
print 1.0 / (1.0 / 60.0)
print cast(1.0 as float) / (cast(1.0 as float) / cast(60.0 as float))
</pre>



SQL Server (MS SQL)

https://www.microsoft.com/en-us/sql-server/sql-server-2022
https://www.youtube.com/watch?v=ncF-zFzBDAY
https://www.youtube.com/playlist?list=PL3EZ3A8mHh0xUC8xqFg7k1Qzp-f5HzbTB


## Data Types


https://docs.microsoft.com/en-us/sql/t-sql/data-types/decimal-and-numeric-transact-sql?view=sql-server-ver15
https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2005/ms191530(v=sql.90)?redirectedfrom=MSDN#_decimal
https://stackoverflow.com/questions/1072806/sql-server-calculation-with-numeric-literals

### Float vs. Numeric




## JSON Data

Storying JSON data in a table column:
- Usually json columns are defined with NVARCHAR(n), where n is size of the characters. NVARCHAR(MAX) for maximum size. 

- SQL server is found to have issues if NVARCHAR(MAX) is defined for a lot of columns. Based on the settings and situation, there may be slowdown of queries in certain circumstances.



### OPENJSON 

OPENDATA for Parsing JSON Columns. OPENDATA is a new feature and is not very error tolerant and difficult to troubleshoot if used for 

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

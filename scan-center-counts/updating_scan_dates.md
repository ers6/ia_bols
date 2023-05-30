# Updating Scan Counts 

To update scan counts, I accessed internet archive's read API using the following request structure: 
https://archive.org/advancedsearch.php?q=%22scanningcenter%3A+{scan center name}%22&fl%5B%5D={metadata field(s) returned}&rows={number of results (cannot exceed 10000000)}&output=json&callback=callback&save=no

For the BoLs project, I am only concerned with outsourced scanning centers to which IA shipped books (Cebu, Shenzhen, and Hong Kong). The requests for these centers should be structured as follows:

**cebu**: 

https://archive.org/advancedsearch.php?q=%22scanningcenter%3A+cebu%22&fl%5B%5D=scandate&rows=5600000&output=json&callback=callback&save=no

**shenzhen**:

https://archive.org/advancedsearch.php?q=%22scanningcenter%3A+shenzhen%22&fl%5B%5D=scandate&rows=5600000&output=json&callback=callback&save=no

**hongkong**:

https://archive.org/advancedsearch.php?q=%22scanningcenter%3A+hongkong%22&fl%5B%5D=scandate&rows=5600000&output=json&callback=callback&save=no


## More detailed requests 

https://archive.org/advancedsearch.php?q=scanningcenter%3Ahongkong&fl%5B%5D=identifier&fl%5B%5D=scandate&rows=500000&output=csv&callback=callback&save=no 

- Saving output as a csv takes up less room than json and makes for faster downloading! 

## For more on IA's API 
- See advnaced search: https://archive.org/advancedsearch.php
- See IA developer's portal: https://archive.org/developers/ (this timed out given the number of requests, but would be necessary to use to make more complex queries) 

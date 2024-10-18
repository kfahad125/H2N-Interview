## H2N-DEV-interview


# XML Processing, JSON Conversion, and Data Handling in Python



## Instructions

### 1. Set Up the Environment
- Created a GitHub repository H2N-Interview


### 2. **Parsing XML to JSON:**
   XML_TO JSON_Code.txt conatins the Python script that:
     - Iterates through each XML file in the `/xml-files/` folder.
     - Extracts key fields (like `OrderID`, `Customer`, and `Products`).
     - Converts the extracted data to JSON format.
	 
### 3 Error handling
A) Try-Except Blocks: Each critical function (like extract_order_fields and parse_xml_file) is wrapped in 
a try-except block to catch and handle exceptions without crashing the script.
Eg: 
try:
    order_id = order.find('OrderID')
    ...
except Exception as e:
    logging.error(f'Error extracting fields in {os.path.basename(order)} - {str(e)}')

B)  Validation of Mandatory Fields
Field Checks: The extract_order_fields function checks for mandatory fields, such as <OrderID> and <Customer>. 
If these fields are missing, a warning is logged, and the function returns None. This prevents incomplete order data from being processed further

C)   Collecting Results Safely
Filtering Valid Orders: When compiling the list of orders, the script filters out None values returned from 
the extract_order_fields function. This ensures that only successfully parsed orders are included in the final output:

Eg: return [order for order in orders if order is not None]

D) Feedback on Completion
User Notification: After processing, the script provides feedback to the user, 
indicating that the processing is complete and where to check for errors

Eg: print("Processing complete. Check 'process.log' for any errors.")

E)  Structured Logging
Logging is configured at the beginning of the script, which allows for easy tracking of events
and errors throughout the execution process. This is crucial for debugging and understanding the script's flow.

Eg: logging.basicConfig(filename='process.log', level=logging.INFO, format='%(asctime)s - %(message)s')

### 4 Challenges Faced
Performance Considerations: Depending on the number of XML files and their sizes, processing can take time.
Although not explicitly handled in the script, it could be beneficial to implement progress tracking or multithreading
for larger datasets in a real-world application.

Data Integrity:
Ensuring the extracted data is complete and correctly formatted is crucial, especially when converting to JSON.
 The checks for mandatory fields help mitigate issues related to data integrity.


### 5 Online resources used
XML Parsing in Python:
Resource: Python Official Documentation and Stack Overflow

Handling Errors:
Resource: ChatGPT, Stack Overflow

JSON Handling:
Resource: Python Official Documentation







-


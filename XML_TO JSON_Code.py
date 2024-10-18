import os
import xml.etree.ElementTree as ET
import json
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='process.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Defining the directory containing the XML files
directory = 'Downloads/xml-files'

def extract_order_fields(order):
    """Extract fields from a single order element."""
    try:
        order_id = order.find('OrderID')
        customer = order.find('Customer')
        products = order.find('Products')

        # Checking for mandatory fields
        if order_id is None:
            logging.warning(f'Skipped {os.path.basename(order)} - Missing <OrderID> element.')
            return None
        
        if customer is None:
            logging.warning(f'Skipped {os.path.basename(order)} - Missing <Customer> element.')
            return None

        customer_id = customer.find('CustomerID').text if customer.find('CustomerID') is not None else None
        customer_name = customer.find('Name').text if customer.find('Name') is not None else None
        
        # Extract product details using list
        product_list = [
            {
                'ProductID': product.find('ProductID').text,
                'Name': product.find('Name').text,
                'Quantity': product.find('Quantity').text,
                'Price': product.find('Price').text
            }
            for product in products.findall('Product')
        ] if products is not None else []

        total_amount = order.find('TotalAmount').text if order.find('TotalAmount') is not None else None
        
        return {
            'OrderID': order_id.text,
            'Customer': {
                'CustomerID': customer_id,
                'Name': customer_name
            },
            'Products': product_list,
            'TotalAmount': total_amount
        }

    except Exception as e:
        logging.error(f'Error extracting fields in {os.path.basename(order)} - {str(e)}')
        return None

def parse_xml_file(xml_file):
    """Parse an XML file and extract order data."""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Process each order based on root element
        orders = []
        if root.tag == 'Orders':
            orders = [extract_order_fields(order) for order in root.findall('Order')]
        elif root.tag == 'Order':
            orders = [extract_order_fields(root)]

        return [order for order in orders if order is not None]

    except ET.ParseError as e:
        logging.error(f'Parsing error in {os.path.basename(xml_file)} - {str(e)}')
    except Exception as e:
        logging.error(f'Error processing {os.path.basename(xml_file)} - {str(e)}')
    
    return []

def main():
    all_orders = []

    # Iterate through each XML file in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            xml_file_path = os.path.join(directory, filename)
            all_orders.extend(parse_xml_file(xml_file_path))

    # Convert extracted orders to JSON format and save to a file
    with open('extracted_orders.json', 'w') as json_file:
        json.dump(all_orders, json_file, indent=4)

    print("Processing complete. Check 'process.log' for any errors.")

if __name__ == '__main__':
    main()

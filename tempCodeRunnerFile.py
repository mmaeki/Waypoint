hotel_names = []

# Extracting hotel names from the brands section
for brand in results.get('brands', []):
    hotel_names.append(brand['name'])
    for child_brand in brand.get('children', []):
        hotel_names.append(child_brand['name'])

# Extracting hotel names from the properties section
for property_data in results.get('properties', []):
    hotel_names.append(property_data['name'])
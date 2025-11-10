import pandas as pd
import tkinter as tk
import webbrowser as wb

# Get user input
Object_Name = str(input("Please input Object Name along with main keyword- (Plastic/Paper/Glass/Metal): "))
Object_recycled = str(input("Recycled-Y/N: "))
if (Object_Name == 'plastic soda bottle' in Object_Name.lower() \
   or Object_Name == 'plastic water bottle' in Object_Name.lower() \
   or Object_Name == 'plastic food packaging' in Object_Name.lower())\
   and Object_recycled.lower() == 'n':
    Plastic_Category = 'PETE'
elif (Object_Name == 'plastic soda bottle' in Object_Name.lower() \
     or Object_Name == 'plastic water bottle' in Object_Name.lower() \
     or Object_Name == 'plastic food packaging' in Object_Name.lower())\
   and Object_recycled.lower() == 'y':
    Plastic_Category = 'rPETE'
elif (Object_Name == 'plastic milk jug' in Object_Name.lower() \
     or Object_Name == 'plastic detergent bottle' in Object_Name.lower() \
     or Object_Name == 'plastic shampoo bottle' in Object_Name.lower())\
   and Object_recycled.lower() == 'n':
    Plastic_Category = 'HDPE'
elif (Object_Name == 'plastic milk jug' in Object_Name.lower() \
     or Object_Name == 'plastic detergent bottle' in Object_Name.lower() \
     or Object_Name == 'plastic shampoo bottle' in Object_Name.lower())\
   and Object_recycled.lower() == 'y':
    Plastic_Category = 'rHDPE'
elif (Object_Name == 'plastic yogurt cup' in Object_Name.lower() \
     or Object_Name == 'plastic margarine tub' in Object_Name.lower() \
     or Object_Name == 'plastic salad dressing bottle' in Object_Name.lower())\
   and Object_recycled.lower() == 'n':
    Plastic_Category = 'LDPE'
elif (Object_Name == 'plastic yogurt cup' in Object_Name.lower() \
     or Object_Name == 'plastic margarine tub' in Object_Name.lower() \
     or Object_Name == 'plastic salad dressing bottle' in Object_Name.lower())\
   and Object_recycled.lower() == 'y':
    Plastic_Category = 'rLDPE'
elif (Object_Name == 'plastic clamshell container' in Object_Name.lower() \
     or Object_Name == 'plastic cutlery' in Object_Name.lower() \
     or Object_Name == 'plastic straw' in Object_Name.lower())\
   and Object_recycled.lower() == 'n':
    Plastic_Category = 'PP'
elif (Object_Name == 'plastic clamshell container' in Object_Name.lower() \
     or Object_Name == 'plastic cutlery' in Object_Name.lower() \
     or Object_Name == 'plastic straw' in Object_Name.lower())\
   and Object_recycled.lower() == 'y':
    Plastic_Category = 'rPP'
elif (Object_Name == 'plastic wrap' in Object_Name.lower() \
     or Object_Name == 'plastic bag' in Object_Name.lower() \
     or Object_Name == 'plastic bubble wrap' in Object_Name.lower())\
   and Object_recycled.lower() == 'n':
    Plastic_Category = 'PVC'
elif (Object_Name == 'plastic wrap' in Object_Name.lower() \
     or Object_Name == 'plastic bag' in Object_Name.lower() \
     or Object_Name == 'plastic bubble wrap' in Object_Name.lower())\
   and Object_recycled.lower() == 'y':
    Plastic_Category = 'PVC'
elif (Object_Name == 'plastic cup' in Object_Name.lower() \
     or Object_Name == 'plastic plate' in Object_Name.lower() \
     or Object_Name == 'plastic utensil' in Object_Name.lower())\
   and Object_recycled.lower() == 'n':
    Plastic_Category = 'PS'
elif (Object_Name == 'plastic cup' in Object_Name.lower() \
     or Object_Name == 'plastic plate' in Object_Name.lower() \
     or Object_Name == 'plastic utensil' in Object_Name.lower())\
   and Object_recycled.lower() == 'y':
    Plastic_Category = 'rPS'    
elif 'plastic' in Object_Name.lower() or 'other plastic item' in Object_Name.lower():
    Plastic_Category = 'Other'
else:
    Plastic_Category = 'N/A'
if 'metal' in Object_Name.lower():
    metal_category = 'N/A'
    metal_category = str(input("Please input metal type (STEEL/STAINLESS STEEL/ALUMINUM/COPPER/ZINC/LEAD/NICKEL/IRON/GOLD/SILVER/METAL ORES/OTHER): "))    
else:       
    metal_category = 'N/A'  
size = str(input("Please input Size (small, medium, or large): "))
Quantity = str(input("Please input Quantity: "))
Weight = str(input("Please input Weight (in grams): "))

# Initialize carbon_footprint variable
carbon_footprint = "N/A"

# Determine the carbon footprint based on object and size as per US LCI database
if 'n/a' not in Plastic_Category.lower():
    if Plastic_Category.lower() == 'pete':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*2.37)+'kg CO2e'
    elif Plastic_Category.lower() == 'rpete':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.45)+'kg CO2e'
    elif Plastic_Category.lower() == 'hdpe':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*1.92)+'kg CO2e'
    elif Plastic_Category.lower() == 'rhdpe':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.28)+'kg CO2e'
    elif Plastic_Category.lower() == 'ldpe':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*2.79)+'kg CO2e'
    elif Plastic_Category.lower() == 'rldpe':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.2)+'kg CO2e'
    elif Plastic_Category.lower() == 'pp':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*1.91)+'kg CO2e'
    elif Plastic_Category.lower() == 'rpp':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.35)+'kg CO2e'
    elif Plastic_Category.lower() == 'pvc':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*7.83)+'kg CO2e'
    elif Plastic_Category.lower() == 'ps':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*3.11)+'kg CO2e'
    elif Plastic_Category.lower() == 'rps':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.59)+'kg CO2e'
    elif Plastic_Category.lower() == 'other':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*3)+'kg CO2e'
elif 'paper' in Object_Name.lower() and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*910)+'kg CO2e'
elif 'paper' in Object_Name.lower() and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*730)+'kg CO2e'
elif 'glass' in Object_Name.lower() and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*1.10)+'kg CO2e'
elif 'glass' in Object_Name.lower() and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.64)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'steel' and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*1.92)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'steel' and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.8)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'stainless steel' and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*6.15)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'stainless steel' and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*1.6)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'aluminum' and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*11)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'aluminum' and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*4)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'copper' and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*4.1)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'copper' and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*1.5)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'zinc' and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*3.89)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'zinc' and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*1.2)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'lead' and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*1.64)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'lead' and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.4)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'nickel' and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*11.53)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'nickel' and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*4.5)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'iron/gold/silver/metal ores' and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.42)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'iron/gold/silver/metal ores' and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*0.15)+'kg CO2e'
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'other' and Object_recycled.lower() == 'n':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*5)+'kg CO2e' 
elif 'metal' in Object_Name.lower() and metal_category.lower() == 'other' and Object_recycled.lower() == 'y':
        carbon_footprint = str(int(Weight)/1000*int(Quantity)*2)+'kg CO2e'   
# Create the data dictionary
data = {
    'Object': [Object_Name],
    'Recycled': [Object_recycled],
    'Size': [size],
    'Quantity': [Quantity],
    'Weight in Grams': [Weight],
    'Plastic Category': [Plastic_Category],
    'Metal Category': [metal_category],
    'Carbon Footprint': [carbon_footprint]
}

# Create a DataFrame
df = pd.DataFrame(data)




# # Color columns
# styled_df = df.style.set_properties(**{'background-color': 'lightblue'}, subset=['Object'])
# styled_df = styled_df.set_properties(**{'background-color': 'lightyellow'}, subset=['Size'])
# styled_df = styled_df.set_properties(**{'background-color': 'lightgreen'}, subset=['Carbon Footprint'])

 # Apply styles for borders
html_table_pandas = df.style.set_table_styles(
        [{'selector': 'table, th, td', 'props': [('border', '1px solid black'), ('border-collapse', 'separate')]}]
    ).to_html()

# Save to an HTML file
with open("foo.html", "w") as f:
        f.write(html_table_pandas)
print("HTML table saved to foo.html")
import pandas


sea_salt_crackers = []
griffins_snax = []
pizza_shapes = []
arnotts_cheds = []
rosemary_wheat = []
original_rice_crackers = []

product_frame = []

product_frame_headings = {
    "Name": product_frame_headings
}


product_data_dict = {
    "Sea Salt Crackers": sea_salt_crackers,
    "Griffins Snax": griffins_snax,
    "Pizza Shapes": pizza_shapes,
    "Arnotts Cheds": arnotts_cheds,
    "Rosemary Wheat": rosemary_wheat,
    "Original Rice Crackers": original_rice_crackers
}

product_weight_dict = {
    "Sea Salt Crackers": 0.185,
    "Griffins Snax": 0.25,
    "Pizza Shapes": 0.19,
    "Arnotts Cheds": 0.25,
    "Rosemary Wheat": 0.17,
    "Original Rice Crackers": 0.1
}

product_frame_headings = ["Product Name", "Product Weight"]

product_frame = pandas.DataFrame(product_data_dict)
product_frame = product_frame.set_index("Product Name")



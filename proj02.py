#11-15-20
#Unubold Batsuuri
#Numerical Assignment Activity 3 
#I'm not sure how to truncate. My numbers for plants for the circle gardent and total plants are more than the test amount by 1

import math

#get input for side length for the garden, spacing between plants, depth of flowerbed, depth of filled area
side_length = float(input("Enter side length (in feet):"))
space_between_plants = float(input("Enter recommended spacing between plants (in feet):"))
flowerbed_depth = float(input("Enter depth of the flowerbeds (in feet):"))
filled_depth = float(input("Enter depth of the filled areas (in feet):"))

#area of garden
garden_area = side_length**2    

# Area of circle A=3.14r**2
full_circle_radius = side_length/4
full_circle_area = (full_circle_radius**2)*math.pi

#area of semi circle
semi_circle_area = full_circle_area/2

#number of plants for full circle and semicircle
new_space_between_plants = space_between_plants**2
plants_full_circle = full_circle_area/new_space_between_plants
plants_semi_circle = semi_circle_area/new_space_between_plants

text = f"{plants_full_circle:.0f}"  #formatting to 0 decimal place
formatted_plants_full_circle = float(text)  

text = f"{plants_semi_circle:.0f}"  #formatting to 0 decimal place
formatted_plants_semi_circle = float(text)

#total number of plants
plants_total = (formatted_plants_semi_circle*4)+formatted_plants_full_circle

#convert to cubic yards for soil (area*depth)27 
full_circle_soil = (full_circle_area*flowerbed_depth)/27
semi_circle_soil = (semi_circle_area*flowerbed_depth)/27

text = f"{full_circle_soil:.1f}"    #formatting to 1 decimal place
formatted_full_circle_soil = float(text)

text = f"{semi_circle_soil:.1f}"    #formatting to 1 decimal place
formatted_semi_circle_soil = float(text)

#total number of soil
soil_total = (formatted_semi_circle_soil*4)+formatted_full_circle_soil
text = f"{soil_total:.1f}"  #formatting to 1 decimal place
formatted_soil_total = float(text)

#amount of fill
total_flower_area = (semi_circle_area*4)+full_circle_area
fill_area = garden_area-total_flower_area
total_fill = (fill_area*filled_depth)/27

text = f"{total_fill:.1f}"  #formatting to 1 decimal place
formatted_total_fill = float(text)

print("Plants for each semicircle garden:", formatted_plants_semi_circle)
print("Plants for the circle garden:", formatted_plants_full_circle)
print("Total plants for the garden:", plants_total)
print("Soil for each semicircle garden:", formatted_semi_circle_soil, "cubic yards")
print("Soil for the circle garden:", formatted_full_circle_soil, "cubic yards")
print("Total soil for the garden:", formatted_soil_total, "cubic yards")
print("Total fill for the garden:", formatted_total_fill, "cubic yards")
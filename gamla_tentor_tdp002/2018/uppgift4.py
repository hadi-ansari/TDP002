import json

with open("ident_numbers.json", "r") as f:
    content = json.load(f)

for i in range(len(content)):
    number_to_string = str(content[i])
    x = 2
    product_list = []
    sum_of_products = 0
    
    for j in number_to_string:
        s = int(j) * x
        if x == 2:
                x = 1
        else:
                x = 2
        if s > 9:
            product_list.append(str(s)[0])
            product_list.append(str(s)[1])
        else:
            product_list.append(s)
       
    for product in product_list:
        sum_of_products = sum_of_products + int(product)

    if (sum_of_products % 10) != 0:
        closest_number = sum_of_products // 10
        closest_number = (closest_number + 1) * 10
        result_number = closest_number - sum_of_products
    else:
        result_number = 0

    
    print("{}{}".format(content[i], result_number))
    
            
        

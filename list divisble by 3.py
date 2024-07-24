def divisble_by_3(list):
    output_list=[]
    for i in list:
        if(i%3==0):
            output_list.append(i)
    return output_list
list=[43,67,23,3,97,27,45,6,19]
output_list=divisble_by_3(list)
print(output_list)
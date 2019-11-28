def weights_list(plan_list):

    weight_list = []
    parameter = 0
    
    for row in plan_list:
        plan = row[0]

        if plan is 'A':
            parameter+=30

        elif plan is 'B':
            parameter+=3

        else:
            parameter+=1

        
    for row in plan_list:
        plan = row[0]

        if plan is 'A':
            weight_list.append(30/parameter)

        elif plan is 'B':
            weight_list.append(3/parameter)

        else:
            weight_list.append(1/parameter)

    return weight_list

categories = {item: {} for item in input().split(', ')}

n = int(input())

for _ in range(n):
    command = input()
    category = command.split(' - ')[0]
    sub_category = command.split(' - ')[1]
    quantity_name = command.split(' - ')[2].split(';')[0].split(':')[0]
    quantity = int(command.split(' - ')[2].split(';')[0].split(':')[1])
    quality_name = command.split(' - ')[2].split(';')[1].split(':')[0]
    quality = int(command.split(' - ')[2].split(';')[1].split(':')[1])

    if category not in categories:
        categories[category] = {}
        categories[category][sub_category] = {}
        categories[category][sub_category]['quantity'] = quantity
        categories[category][sub_category]['quality'] = quality
    elif sub_category not in categories[category]:
        categories[category][sub_category] = {}
        categories[category][sub_category]['quantity'] = quantity
        categories[category][sub_category]['quality'] = quality
    elif quantity_name not in categories[category][sub_category]:
        categories[category][sub_category]['quantity'] = quantity
        categories[category][sub_category]['quality'] = quality

print(f"Count of items: {sum([categories[category][sub_category]['quantity'] for category in categories for sub_category in categories[category]])}")
print(f'Average quality: {sum([categories[category][sub_category]["quality"] for category in categories for sub_category in categories[category]]) / len(categories.keys()):0.2f}')
[print(f"{category} -> {', '.join(categories[category].keys())}") for category in categories]
def make_car(manufacturer, model, **features):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in features.items():
        car[key] = value
    return car

new_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(new_car)

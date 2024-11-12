Cars = ["bmw", "mahindra", "suzuki", "rolls royce", "bentley", "aston martin", "tata", "audi", "mustang"]
Cars.append("jaguar")
Cars.append("fiat")
print(Cars)
#['bmw', 'mahindra', 'suzuki', 'rolls royce', 'bentley', 'aston martin', 'tata', 'audi', 'mustang', 'jaguar', 'fiat']

#OR

Cars.extend(["jaguar", "fiat"])
print(Cars)  
#['bmw', 'mahindra', 'suzuki', 'rolls royce', 'bentley', 'aston martin', 'tata', 'audi', 'mustang', 'jaguar', 'fiat']
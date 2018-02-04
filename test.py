class AirBNBProperty:

	number_of_airbnbs = 0
	all_airbnbs = []

	def __init__(self, host, price, location):
		self.host = host
		self.price = price
		self.location = location
		AirBNBProperty.number_of_airbnbs += 1
		AirBNBProperty.all_airbnbs.append(self)

	def __repr__(self):
		return self.host + "'s AirBNB located in " + self.location + "($" + str(self.price) +")"

	def get_all_airbnbs_over_price(price_threshold):
		properties_over_threshold = []
		for property in AirBNBProperty.all_airbnbs:
			if property.price > price_threshold:
				properties_over_threshold.append(property)
		return properties_over_threshold

	def most_expensive_airbnb():
		most_expensive = None
		for property in AirBNBProperty.all_airbnbs:
			if most_expensive == None:
				most_expensive = property
			else:
				if  property.price > most_expensive.price:
					most_expensive = property
		return most_expensive


KatyasProperty = AirBNBProperty("Katya", 1000000, "NYC")

print("Host", KatyasProperty.host)
print("Location", KatyasProperty.location)


PhilsProperty = AirBNBProperty("Phil", 2, "Urbana")
AirBNBProperty("Yury", 5, "NYZ")
print("Host", PhilsProperty.host)

print("most expensive host", AirBNBProperty.most_expensive_airbnb().host)

print("Number of Properties", AirBNBProperty.number_of_airbnbs)


print(AirBNBProperty.all_airbnbs)


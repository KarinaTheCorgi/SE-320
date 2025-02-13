"""
FileName: Solis_sensors.py
Author: Karina Solis
Date: 2/3/2025
Resources:
    - Wolf Paulus: Python OOP (creating classes and implementing methods)
"""

# Sensor Class Definition (Parent)
class Sensor(): 
    def __init__(self, name: str, link: str, polling_frequency: int)->None:
        """
            Sensor initializer

            Args:
                name (str): the name of the news source
                link (str): the url to get information from
                polling_frequency (int): how often the sensor polls information

            Yields:
                None. Used to create a Sensor object
        """
        print("A new Sensor was created.")
        self.name = name
        self.url = link
        self.polling_frequency = polling_frequency
                
    def __str__(self)->str:
        """ Used to print a readable Sensor object """
        return "Sensor Name: " + self.name + "\nURL: " + self.url + "\nPolling frequency (in secs): " + str(self.polling_frequency)
    
# SensorDictMixin Class Definition 
class SensorDictMixin():
    """ A mixin class to convert sensor information into a dictionary """
    def to_dict(self):
        """ function that returns the dictionary from the sensor's information """
        return {key: value for key, value in self.__dict__.items()}    
        
# StorySensor Class Definition (Subclass of Sensor and SensorDictMixin)        
class StorySensor(Sensor, SensorDictMixin):
    def __init__(self, name: str, url: str, polling_frequency: int, category: str)->None:
        """
            StorySensor initializer

            Args:
                name (str): the name of the news source
                link (str): the url to get information from
                polling_frequency (int): how often the sensor polls information
                category (str): category of stories to poll for

            Yields:
                None. Used to create a StorySensor object
        """
        print("A new StorySensor was created.")
        super().__init__(name, url, polling_frequency) 
        self.category = category
    
    def __str__(self)->str:
        """ Used to print a readable StorySensor object """
        return Sensor.__str__(self) + "\nCategory: " + self.category
   
# EventSensor Class Definition (Subclass of Sensor and SensorDictMixin)         
class EventSensor(Sensor, SensorDictMixin):
    def __init__(self, name: str, url: str, polling_frequency: int, event_type: str, location: str)->None:
        """
            EventSensor initializer

            Args:
                name (str): the name of the news source
                link (str): the url to get information from
                polling_frequency (int): how often the sensor polls information
                event_type (str): what kind of event to be looking for
                location (str): where the event would/could take place

            Yields:
                None. Used to create a EventSensor object
        """
        print("A new EventSensor was created.")
        super().__init__(name, url, polling_frequency) 
        self.event_type = event_type
        self.location = location
        
    def __str__(self)->str:
        """ Used to print a readable EventSensor object """
        return Sensor.__str__(self) + "\nEvent Type: " + self.event_type + "\nLocation: " + self.location
 
# DataSensor Class Definition (Subclass of Sensor and SensorDictMixin)     
class DataSensor(Sensor, SensorDictMixin): 
    def __init__(self, name: str, url: str, polling_frequency: int, data_type: str)->None:
        """
            DataSensor initializer

            Args:
                name (str): the name of the news source
                link (str): the url to get information from
                polling_frequency (int): how often the sensor polls information
                data_type (str): what kind of data being gathered

            Yields:
                None. Used to create a DataSensor object
        """
        print("A new DataSensor was created.")
        super().__init__(name, url, polling_frequency) 
        self.data_type = data_type
        
    def __str__(self)->str:
        """ Used to print a readable DataSensor object """
        return Sensor.__str__(self) + "\nData Type: " + self.data_type
    

    

#  Checking if instances are their respective classes and the object class     
print("Testing Instance/Subclass Instantiation\n\n")      
sensor = Sensor("Generic News", "www.news.com", 5800)
if isinstance(sensor, Sensor):
    print("The object is a Sensor.")
if isinstance(sensor, object):
    print("The object is an object.\n")

story_sensor = StorySensor("ABC News", "www.abcnews.go.com", 5800, "Politics")
if isinstance(story_sensor, StorySensor):
    print("The object is a StorySensor.")
if isinstance(story_sensor, object):
    print("The object is an object.\n")

event_sensor = EventSensor("LA Times", "www.latimes.com", 1800, "Climate", "Los Angeles")
if isinstance(event_sensor, EventSensor):
    print("The object is an EventSensor.")
if isinstance(event_sensor, object):
    print("The object is an object.\n")

data_sensor = DataSensor("KGUN 9", "www.kgun9.com", 86400, "Weather")
if isinstance(data_sensor, DataSensor):
    print("The object is a DataSensor.")
if isinstance(data_sensor, object):
    print("The object is an object.\n")

# Iterating over list of Sensors
print("Testing polymorphism: \n\n")    
list = [sensor, story_sensor, event_sensor, data_sensor]

for s in list:
    print(s)
    print("\n")

# Converting each sensor into a dictionary and printing the dictionary
print("Testing Mixin: \n\n")
print("Story Sensor as Dictionary:\n")
print(story_sensor.to_dict())

print("Event Sensor as Dictionary:\n")
print(event_sensor.to_dict())

print("Data Sensor as Dictionary:\n")
print(data_sensor.to_dict())
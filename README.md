# AirBnB clone - The console

<p align="center">
    <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221030%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221030T221552Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f39a99c3a93b5e61c560cf72b4d5122cb492dad9bdee916f406602b9ef73e14e">
</p>

## Description

This team project is part of the AlX Software Engineer program.
It's the first step towards building a first full web application: an AirBnB clone.
This first step consists of a custom command-line interface simulating data management, and the base classes for the storage of data.

## Console and Command Usage

The console is a Unix shell-like command line user interface provided by the python [CmdModule](https://docs.python.org/3.8/library/cmd.html)
It prints a prompt and waits for the user for input, for our project we used **(hbnb)**

Command | Example
------- | -------
Display commands help | ```(hbnb) help <command>```
Create object (prints its id)| ```(hbnb) create <class>```
Destroy object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Show "all" objects or instances class | ```(hbnb) all``` or ```(hbnb) all <class>```
Run console | ```./console.py```
Quit console | ```(hbnb) quit```


Help command example

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

## Class Models Used


File | Description | Attributes
---- | ----------- | ----------
[base_model.py](./models/base_model.py) | The BaseModel class is inherited by other classes | id, created_at, updated_at
[user.py](./models/user.py) | User class stores user-related info | email, password, first_name, last_name
[city.py](./models/city.py) | City class stores city-specific information | state_id, name
[state.py](./models/state.py) | State class stores state-specific information | name
[place.py](./models/place.py) | Place class stores full detailed outline of rental unit features | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
[review.py](./models/review.py) | Review class stores previous customer reviews and opinions | place_id, user_id, text
[amenity.py](./models/amenity.py) | Amenity class stores highlighted amenity information | name

## Tests

All the code is tested with the **unittest** module.
The test for the classes are in the [test_models](./tests/test_models/) folder.

## Authors

* **Oscar Tiego** - [Github profile](https://github.com/Tom-254)
* **Fredrick Onyango** - [Github profile](https://github.com/aTfure)
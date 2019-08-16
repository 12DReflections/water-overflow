# water-overflow
A water overflow code challenge

### Setup 
- Linux commands for python3 and virtual environments

``` bash
cd <installed directory>
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv venv 
source venv/bin/activate
```

### Run the software
- Run the unit tests

``` bash
python3 -m unittest discover tests/
```

- Run the program
``` bash
python3 main.py 3 5 10
python3 main.py 3 5 2
```

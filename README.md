# OMDbPlot
A project aiming to plot various movie statistics against year of release, because data is beautiful.

Built and tested using Python 3.5.1 on Ubuntu Linux.

Many thanks to [The Movie DB](http://themoviedb.org) for allowing me to use their API to collect data.

## Usage
1. download an archive of the repo and extract all, or clone the repo to a destination of your choosing.

2. create a file called `secret.py` in the same directory.

3. go to [The Movie DB API Docs](https://www.themoviedb.org/documentation/api), create an account, and apply for an API key. This is free, and should be immediately, automatically approved.

4. create a method inside `secret.py`:
  ```python
  def get_secret():
    return "my_api_key_goes_here"
  ```
  replacing my_api_key_goes_here with, well, your api key, and save your changes to `secret.py`.

5. simply run `main.py`:
  ```
  python /path/to/main.py
  ```

6. make a cup of tea and get some biscuits, data collection will take a while.

7. marvel at how consistent average movie statistics have been over the past 10 years.

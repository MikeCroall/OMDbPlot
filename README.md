# OMDbPlot
A project which plots various movie statistics against year of release, because data is beautiful.

Built and tested using Python 3.5.1 on Ubuntu Linux.

Many thanks to [The Movie DB](http://themoviedb.org) for allowing me to use their API to collect data.

## Usage
1. download an archive of the repo and extract all, or clone the repo to a destination of your choosing.

2. create a file called `secret.py` in the `src` directory.

3. go to [The Movie DB API Docs](https://www.themoviedb.org/documentation/api), create an account, and apply for an API key. This is free, and should be immediately, automatically approved.

4. create a method inside `secret.py`:
  ```python
  def get_secret():
    return "my_api_key_goes_here"
  ```
  replacing my_api_key_goes_here with, well, your api key, and save your changes to `secret.py`.

5. simply run `main.py`:
  ```
  python /path/to/src/main.py
  ```
  and choose your mode.
  
6. make a cup of tea and get some biscuits, data collection will take a while, though all data collected will be saved for lightning quick plotting next time!

7. marvel at how consistent average movie statistics have been over the past 10 years (average rating, at least).

##Package Dependencies

seaborn, matplotlib
: both for plotting the results, seaborn purely for styling purposes.
  
colorama
: for easy coloured terminal output without looking awful on windows when ANSI isn't enabled.
  
shutil
: for recursive deletion of the local data save directory.

os
: for directory and file checking.

requests
: for making web requests to retrieve JSON data.
  
time
: to pause the thread to avoid exceeding the API call rate limiter imposed upon us.
  

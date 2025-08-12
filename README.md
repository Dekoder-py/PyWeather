# PyWeather - Weather CLI

PyWeather will show you the current conditions of a given location.
Written in python and uses the tomorrow.io api.

## Install

1. Clone this repo:
    ```bash
    git clone https://github.com/dekoder-py/PyWeather
    ```
2. Install requirements:
    ```bash
    python3 -m pip install -r requirements.txt 
    ```

## Usage

Run the main file:

```bash
python3 main.py
```

You'll need to enter an API key from [Tomorrow.io](https://docs.tomorrow.io/reference/welcome) at runtime, or create a
.env file with the following:

```dotenv
TOMORROW_IO_API=*YOURKEYHERE*
```

### Getting a tomorrow.io API Key

1. Go to [the tomorrow.io api docs](https://docs.tomorrow.io/reference/welcome)
2. In the top right, click Log In
3. Sign Up for an account
4. Go to [the API keys section](https://app.tomorrow.io/development/keys) while signed in
5. Copy the API key!
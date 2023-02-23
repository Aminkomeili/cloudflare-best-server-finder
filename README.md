# Cloudflare Best Server Finder

This program helps you find the best Cloudflare server to use in load balancing.
Installation

1. Clone the code from this repository.
2. In the cloudflare.py file, replace your email and API key in the email and api_key variables.
3. Install the requests package using the command:

`pip install requests`

## Usage

1. Run the program using the command:

`python cloudflare.py`

The best Cloudflare server to use in load balancing is displayed.

## How it works

This program retrieves a list of servers available in a specific pool and monitor using the Cloudflare API, and then finds the best server based on their ping.
# Author

This program was written by Amin Komeili. If you have any questions, please email me at a.komeili@ymail.com

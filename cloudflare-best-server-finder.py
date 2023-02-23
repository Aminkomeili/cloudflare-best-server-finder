import requests
import json

class CloudflareServer:

    def __init__(self, location, server_id, ping):
        self.location = location
        self.server_id = server_id
        self.ping = ping

    def __repr__(self):
        return f"Cloudflare Server({self.location}, {self.server_id}, {self.ping})"

class Cloudflare:

    def __init__(self, email, api_key):
        self.email = email
        self.api_key = api_key
        self.base_url = "https://api.cloudflare.com/client/v4"

    def get_servers(self):
        headers = {
            "X-Auth-Email": self.email,
            "X-Auth-Key": self.api_key,
            "Content-Type": "application/json"
        }

        response = requests.get(f"{self.base_url}/user/load_balancers/pools/8c42af1366d7f0669bc68f84da8b84db/monitors/e644b48a3a0547dd8cbf03ccff1aa2e9/nodes", headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")

        servers = []
        for server in json.loads(response.text)["result"]:
            servers.append(CloudflareServer(server["location"], server["id"], server["ping"]))

        return servers

    def get_best_server(self):
        servers = self.get_servers()
        return min(servers, key=lambda x: x.ping)

if __name__ == "__main__":
    cf = Cloudflare("youremail@example.com", "your_api_key")
    best_server = cf.get_best_server()
    print(f"The best server is {best_server.server_id} with ping {best_server.ping} ms in {best_server.location}")

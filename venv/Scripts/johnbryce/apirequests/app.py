from api_factory import RestClient

restClient = RestClient("jsonplaceholder.typicode.com")
http_response = restClient.get("https://jsonplaceholder.typicode.com/posts/1")
http_response.status
print("asd")

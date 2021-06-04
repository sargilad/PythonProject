from app_requests import PostsRequests
HOST = "jsonplaceholder.typicode.com"

posts_requests = PostsRequests(HOST)
response = posts_requests.get_posts()
response = posts_requests.get_single_post(1)
print(response)


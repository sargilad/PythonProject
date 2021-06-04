from app_requests import PostsRequests

HOST = "https://jsonplaceholder.typicode.com"

posts_requests = PostsRequests()
# body = {'title': 'foo', 'body': 'bar', 'userId': '1'}
# response = posts_requests.create_post(body)
response = posts_requests.get_posts()
response = posts_requests.get_single_post(1)
print(response)

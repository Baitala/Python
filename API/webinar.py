import http.client
import mimetypes
conn = http.client.HTTPSConnection("postman-echo.com")
payload = ''
headers = {
  'api_key': '3213215',
  'Cookie': 'sails.sid=s%3A1DYn-2uN--vO9fBVBQFlBYToqntsSAle.JkX4ewI4ICPSiOky1zgiM9zXSTpr9bc%2FK1xRJbJlb%2FM'
}
conn.request("GET", "/get?name=Michael Scott&age=40", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


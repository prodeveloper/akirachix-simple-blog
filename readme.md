Running the app
```
docker run -p 8080:8080 -v /Users/jchencha/Google\ Drive/GDocuments/akirachix/assignments/simple_blog/app:/app akirachix/simple_blog
```

Building the app
```
 docker build -t akirachix/simple_blog .
```
Tinkering with the app
```
docker exec -it simple_blog /bin/bash
```

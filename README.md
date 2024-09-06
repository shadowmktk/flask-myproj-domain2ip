# flask-myproj-domain2ip
Flask Web项目，通过URL方式获取指定域名的IP地址


Install requirements.
```
pip3 install -r requirements.txt
```

Running demo.
```
python3 app.py

curl http://127.0.0.1:5000/?domain=域名
```


Example.
```
http://127.0.0.1:5000/?domain=域名
http://127.0.0.1:5000/?domain=域名&nameservers=223.5.5.5
http://127.0.0.1:5000/?domain=域名&nameservers=119.29.29.29
```

```
root@ubuntu:~# curl -s "http://127.0.0.1:5000/?domain=www.tencent.com" | jq .
{
  "域名": "www.tencent.com",
  "DNS": [
    null
  ],
  "IP地址": [
    "61.241.131.107",
    "211.91.65.122",
    "211.91.65.218"
  ]
}
root@ubuntu:~#
root@ubuntu:~# curl -s "http://127.0.0.1:5000/?domain=www.aliyun.com&nameservers=223.5.5.5" | jq .
{
  "域名": "www.aliyun.com",
  "DNS": [
    "223.5.5.5"
  ],
  "IP地址": [
    "121.31.230.219",
    "36.249.188.243",
    "119.39.74.106"
  ]
}
root@ubuntu:~#
```

Docker.
```
docker build -t flask-myproj-domain2ip:v1.0.0 .

docker run -d --name flask-myproj-domain2ip -p 5000:5000 flask-myproj-domain2ip:v1.0.0
```

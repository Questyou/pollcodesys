import  json


data0  = '{"id":54,"runDate":"2020-07-08","time":"18:30:00-19:00:00","serviceId":32,"taskName":"青海卫视转播","log":"执行成功","parentId":8,"resultList":{"630100":[{"serviceId":2,"serviceName":"湟中新闻综合","date":"2020-07-08"},{"serviceId":24,"serviceName":"湟源新闻综合","date":"2020-07-08"}],"632100":[{"serviceId":26,"serviceName":"民和新闻综合","date":"2020-07-08"}],"632200":[{"serviceId":7,"serviceName":"祁连新闻综合","date":"2020-07-08"}],"632300":[{"serviceId":28,"serviceName":"尖扎新闻综合","date":"2020-07-08"}],"632500":[{"serviceId":30,"serviceName":"共和新闻综合","date":"2020-07-08"},{"serviceId":31,"serviceName":"兴海新闻综合","date":"2020-07-08"},{"serviceId":5,"serviceName":"贵德新闻综合","date":"2020-07-08"}],"632600":[{"serviceId":15,"serviceName":"久治新闻综合","date":"2020-07-08"}],"632800":[{"serviceId":12,"serviceName":"天峻新闻综合","date":"2020-07-08"},{"serviceId":8,"serviceName":"德令哈新闻综合","date":"2020-07-08"},{"serviceId":10,"serviceName":"乌兰新闻综合","date":"2020-07-08"}]},"locationNum":7,"serviceNum":12}'

json_str = json.dumps(data0)
print(json_str)
data2 = json.loads(json_str)

data4 = data2["id"]
print(data4)
- Test Add
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":2, "argument2":1 }' http://localhost:5000/add
{
  "answer": 3
}
```

- Test Subtract
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":4, "argument2":3 }' http://localhost:5000/subtract
{
  "answer": 1
}
```

- Test Division
```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":12, "argument2":4 }' http://localhost:5000/division
{
  "answer": 3
}
```

- Test Random 
```bash
$ curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/random
- Test Random number 
```bash
$ curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/random/13

```

FASTAPI
===
FastAPI framework, high performance, easy to learn, fast to code, ready for production

### 
Documentation: https://fastapi.tiangolo.com
中文文档：https://fastapi.tiangolo.com/zh/
Source Code: https://github.com/tiangolo/fastapi

### 安装fastapi

```shell
pip install fastapi
```

```shell
pip install uvicorn
```


### 运行程序
下面这种非常规启动程序与java的war包丢在tomcat里面一样。本质上差不多。而且效果可能更好，可以自动热重启。
```shell
uvicorn main:app --reload
```
#### main方法运行

下面这种与上面没有本质区别。
```python
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
[FastAPI 开始安装(创建第一个例子）多种运行方式](https://blog.csdn.net/qq_40815295/article/details/106896707)
[官网提供这种运行方式](https://fastapi.tiangolo.com/zh/tutorial/debugging/)
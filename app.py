import os
import logging
from flask import Flask
from threading import Lock
from flask import request, redirect
import tool.queue as logF
from flask_socketio import SocketIO
from tool.queue import log

# 方法来渲染模板
# 将模板名和你想作为关键字的参数传入模板的变量
from flask import render_template, flash

from service.googleimagedownload import GoogleCrawler
from service.baiduimagedownload import BaiduCrawler
from service.bingimagedownload import BingCrawler
from service import bingimagedownload
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

thread = None
thread_lock = Lock()

# async_mode = None
# socketio = SocketIO(app)

# 打开调试模式：启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器
app.run(debug=True)


@app.route("/", methods=['GET', 'POST'])
@app.route('/search/')
def search_temple(name=None):
    return render_template('search.html', name=name)


@app.route("/download", methods=['GET', 'POST'])
def download():
    log("REQUEST_METHOD : {}".format(request.method))
    searchEngine = request.form.get('searchEngine')
    if searchEngine is None or searchEngine == '':
        searchEngine = "Google"
        log("searchEngine : {}".format(searchEngine))
    else:
        log("searchEngine : {}".format(searchEngine))
    keyword = request.form.get('keyword')
    keyword = keyword.strip()
    print("keyword::" + str(keyword))
    log("keyword::" + str(keyword))
    if keyword is None or keyword == '':
        print("keyword is none")
        flash('please input keyword')
        return redirect("/search")
    print("todo")
    try:
        if searchEngine == "Google":
            print("Google 执行中")
            craw = GoogleCrawler()
            craw.run(keyword)
        if searchEngine == "Baidu":
            print("Baidu 执行中")
            craw = BaiduCrawler()
            craw.run(keyword)
        if searchEngine == "Bing":
            print("Bing 执行中")
            craw = BingCrawler()
            craw.run(keyword)
        else:
            flash('engine error')
            return redirect("/search")
        flash('Download has finished!!!')
        return redirect("/search")
    except Exception as e:
        print('Error: ' + str(e))
        return redirect("/search")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'), 500


# Get data from queue and push to front
# def background_thread():
#     while True:
#         if logF.not_empty:
#             socketio.emit('server_response', logF.pop(), namespace='/log')


# @socketio.on('connect', namespace='/log')
# def log_socket():
#     global thread
#     with thread_lock:
#         if thread is None:
#             thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':
    app.run()

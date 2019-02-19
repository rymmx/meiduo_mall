# 自定义中间件
# 中间件的执行原理,请求是自上而下,响应是自下而上


def my_middleware(get_response):
    print('init 被调用')

    def middleware(request):
        print('before request 被调用')

        response = get_response(request)

        print('after response 被调用')

        return response

    return middleware


def my_middleware2(get_response):
    print('init2 被调用')

    def middleware2(request):
        print('before request2 被调用')

        response = get_response(request)

        print('after response2 被调用')

        return response

    return middleware2


#

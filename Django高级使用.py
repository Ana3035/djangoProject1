"""
静态文件:css js 图片 json文件 字体文件等
        首先在总目录下面创建static文件,里面放置的就是上面的那些静态文件,在这里面再创建对应项目的目录,因为还可能有其他对应的项目
DEBUG = True
        配置路径:添加上STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
            ]

中间件:
    概述:是一个轻量级,底层的插件,可以介入Django的请求和相应
    本质:是一个Python类
    方法:
        __init__:无需传参数,在服务器相应第一个请求的时候自动调用,用于确定是否启用此中间件
        process_request(self,request):在执行视图之前调用(分配url匹配视图之前,每个请求都会调用,返回none或者HTTPREsponse对象)
        process_view(self,request,view_func,view_args,view_kwargs):调用视图之前执行,每个请求都会调用,也是返回上面的对象
        process_template_response(self,request,response):在视图刚好执行完调用,也是每个请求都会调用,返回也是上面的返回结果
                                        但是使用render就可以返回视图了在views和template之间
        process_responce(self,request,responce):所有的相应返回浏览器之前,每个请求都会调用,但是不会返回none
        process_exception(self,request,exception):当视图抛出异常的时候调用
    相应的流程:url-views-url
    实例:首先创建一个中间件的目录middle,自定义一个中间件,要想使用这个中间件,需要配置settings文件,

上传图片:
    要想图片不会加载不出来,要将图片存在服务器里面,文件上传的时候,文件数据存储在request.FILES中
    首先在static里面创建一个upfile,和app平级,
    确定存储路径,在settings里面配置目录MEDIA_ROOT=os.path.join(BASE_DIR,'static/upfile')
    注意上传文件一定不能是get请求,是post请求

分页:
    Paginator对象:
        创建对象:格式:Paginator(列表,整数)
                返回值:返回一个分页对象,
        属性:count:对象总数
            num_pages:页面总数
            page_range:页码列表,例如1,2,3,4,5
        方法:page(num)表示的是获得一个page对象,如果提供的页码不存在,会抛出异常,invalidpage
        异常:invalidpage表示的是page对象的函数传递是无效的页码
            pagenotaninteger向page传递的不是一个整数的时候,
            empty表示传递一个有效值但是页面上没有数据

    Page对象:
        创建对象:无需手动创建,可以根据上面的对象再获得对象
        属性:object_list:当前页面上所有数据列表
            number表示当前页面的页码值
            Paginator当前page关联的Paginator对象
        方法:has_next()判断是否有下一页,如果有返回true
            has_previous判断是否有上一页
            has_other_pages表示的是判断是否有上一页或者下一页
            next_page_number表示的是返回下一页的页码
            previous_page_number返回上一页的页码
            len表示的是返回当前页面数据对象的个数
        上述两个对象的关系:根据students.object.all生成的列表创建一个对象,且进行分页,,再调用page对象,page对象里面寸的是第几页的数据

    ajax:网页需要的是动态的生成,需要请求JSON数据,比如点击了按钮才会显示学生界面{#注意在ajax里面无法使用load static#}

    富文本:pip install django-tinymce
         在站点中使用:首先配置settings文件,再生成迁移文件,再在admin里面注册,再在终端生成用户Ana,但是这种情况下使用的不多,

         在自定义视图中使用:

    celery:
        问题:1.用户发起request,且要等待request返回,但是视图中有些耗时的操作,导致用户可能会等待很长时间才能接受response,这样用户体验很差,       2.网站每隔一段时间需要同步,但是http请求是需要触发的,
        解决:celery
            1.将耗时的操作放到celery中执行
            2.使用celery定时执行
        celery:
            任务:本质是一个Python函数,将耗时操作封装成一个函数
            队列:将要执行的任务放入队列里面
            工人:负责执行队列的任务
            代理brocker:负责调度,在部署环境中使用redis
        安装celery:celery
                    celery-with-redis
                    django-celery

        配置:settings配置
            在应用目录下面穿件task.py文件
            迁移,不要迁移文件
            在工程目录下的project创建celery文件,在__init添加





"""

from django.shortcuts import render
from vote_teacher.models import Subject
from vote_teacher.models import Teacher
from vote_teacher.forms import RegisterForm
import vote_teacher.captcha
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def show_subjects(request):
    """查看所有学科"""
    subjects = Subject.objects.all()
    return render(request, 'subject.html', {'subjects': subjects})


def show_teachers(request):
    """显示指定学科的老师"""
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.get(no=sno)
        teachers = subject.teacher_set.all()
        return render(request, 'teachers.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (KeyError, ValueError, Subject.ObjectDoesNotExist):
        return redirect('/')


def praise_or_criticize(request):
    """好评"""
    try:
        tno = int(request.GET['tno'])
        teacher = Teacher.objects.get(no=tno)
        if request.path.startswith('/praise'):
            teacher.good_count += 1
        else:
            teacher.bad_count += 1
        teacher.save()
        data = {'code': 200, 'hint': '操作成功'}
    except (KeyError, ValueError, Teacher.ObjectDoesNotExist):
        data = {'code': 404, 'hint': '操作失败'}
    return JsonResponse(data)


def register(request):
    page, hint = 'register.html', ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            page = 'login.html'
            hint = '注册成功，请登陆'
        else:
            hint = '请输入有效的注册信息'
    return render(request, page, {'hint': hint})


ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_captcha_text(length=4):
    selected_chars = random.choices(ALL_CHARS, k=length)
    return ''.join(selected_chars)


def get_captcha(request):
    """获得验证码"""
    captcha_text = get_captcha_text()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image, content_type='image/png')


def login(request):
    """登陆"""
    hint = ''
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            
            form = LoginForm(request.POST)
            if form.is_valid():
                #对验证码的正确性进行验证
                captcha_from_user = form.cleaned_data['captcha']
                captcha_from_sess = request.session.get('captcha')
                if captcha_from_sess.lower() != captcha_from_user.lower():
                    hint = '请输入正确的验证码'
                else:
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = User.objects.filter(username=username,
                                               password=password).first()
                if user:
                    request.session['userid'] = user
                    request.session['username'] = user.username
                    return redirect('/')
                else:
                    hint = '用户名或密码错误'
            else:
                hint = '请输入有效的登陆信息'
        else:
            return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    return render(request, 'login.html', {'hint': hint})


def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')


def export_teachers_excel(request):
    # 创建工作簿
    wb = xlwt.Workbook()
    # 添加工作表
    sheet = wb.add_sheet('老师信息表')
    # 查询所有老师的信息（注意：这个地方稍后需要优化）
    queryset = Teacher.objects.all()
    # 向EXCEL表单种写入表头
    colnames = ('姓名', '介绍', '好评数', '差评数', '学科')
    for index, name in enumerate(colnames):
        sheet.write(0, index, name)
    #向单元中写入老师的数据
    props = ('name', 'detail', 'good_count', 'bad_count', 'subject')
    for row, teacher in enumerate(queryset):
        for col, prop in enumerate(props):
            value = getattr(teacher, prop, '')
            if isinstance(value, Subject):
                value = value.name
            sheet.write(row + 1, col, value)
    #保存excel
    buffer = BytesIO()
    wb.save(buffer)
    #将二进制数据写入相应的信息体中并设置MIME类型
    resp = HttpResponse(buffer.getvalue(),
                        content_type='application/vnd.ms-excel')
    #中文文件名需要处理成百分号编码
    filename = quote('老师.xls')
    # 通过响应头告知浏览器下载该文件以及对应的文件名
    resp['content-disposition'] = f'attachment;filename="{filename}"'
    return resp


def get_teachers_data(request):
    queryset = Teacher.objects.all()
    names = [teacher.name for teacher in queryset]
    good = [teacher.good_count for teacher in queryset]
    bad = [teacher.bad_count for teacher in queryset]
    return JsonResponse({'names': names, 'good': good, 'bad': bad})

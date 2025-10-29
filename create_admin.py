import os
import sys
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    # 检查超级用户是否已存在
    if User.objects.filter(username='admin').exists():
        print("超级用户 'admin' 已存在")
        return
    
    # 创建超级用户
    user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    user.save()
    print("超级用户 'admin' 创建成功")

if __name__ == '__main__':
    create_superuser()
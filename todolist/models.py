from django.db import models

class Todo(models.Model):
    # max_length : CharField 和其子类都需要设定一个最大的长度
    title = models.CharField(max_length=255)
    # blank : 允许数据为空白，默认是 False
    description = models.TextField(blank=True)
    # default ：default 值设置了当前属性的默认值，比如这里我们把 completed 的值设置为默认是未完成的 False
    completed = models.BooleanField(default=False)
    # auto_now_add : 只取出我们的 Model 第一次创建时当时的时间戳，作为 DataTimeField 的值
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now ：取当前的时间戳，当当前对象被 saved 的时候，使用最后一次修改的时间戳作为这个 DataTimeField 的值
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        # 先把所有的数据先按照是否完成来开始排序，然后再按照我们最后的更新时间来继续更新
        ordering = ('completed', '-updated_at',)

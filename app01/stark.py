#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import re_path
from django.shortcuts import HttpResponse
from django.urls import reverse
from django import forms
from stark.service.v1 import site,StarkHander,get_choice_text,StarkModelForm,SearchOption
from app01 import models

class DepartModelForm(StarkModelForm):

    xx = forms.CharField()

    class Meta:
        model = models.Depart
        fields = "__all__"

class DepartHandler(StarkHander):

    # # 额外的增加URL
    # def extra_urls(self):
    #     return [
    #         re_path(r'^detail/(\d+)', self.detail_view),
    #     ]
    #
    # def detail_view(self,request,pk):
    #     return HttpResponse('depart详细页面')

    per_page_count = 3

    list_display = [StarkHander.display_checkbox,'id','title',StarkHander.display_edit,StarkHander.display_del]

    has_add_btn = True

    model_form_class = DepartModelForm

    action_list = [StarkHander.action_multi_delete]

site.register(models.Depart,DepartHandler)

class UserInfoModelForm(StarkModelForm):

    class Meta:
        model = models.UserInfo
        fields = ["name","gender","class_ch","age","email","depart"]

class MyOption(SearchOption):

    def get_db_condition(self,request,*args,**kwargs):
        # return {"id__gt":request.GET.get("nid")}
        return {"id__gt":0}

class UserInfoHandler(StarkHander):

    # # 改变URL
    # def get_urls(self):
    #     patterns = [
    #         re_path(r'^list/$',self.changelist_view),
    #         re_path(r'^add/$',self.add_view),
    #     ]
    #     patterns.extend(self.extra_urls())
    #     return patterns
    # 定制页面显示的列

    # def display_gender(self,obj=None,is_header=None):
    #     if is_header:
    #         return "性别"
    #     return obj.get_gender_display()

    list_display = [StarkHander.display_checkbox,'name','age','email','depart',get_choice_text('性别','gender'),get_choice_text('班级','class_ch'),StarkHander.display_edit,StarkHander.display_del]

    per_page_count = 4

    has_add_btn = True

    order_list = ["id"]

    # 姓名中含有关键字或邮箱中含有关键字
    search_list = ["name__contains","email__contains"]

    model_form_class = UserInfoModelForm

    # def save(self,form,is_update=False):

        # form.instance.depart_id = 1
        # form.save()
        # pass

    action_list = [StarkHander.action_multi_delete]

    search_group = [
        SearchOption(
            "gender",
            is_multi=True,
            text_func=lambda field_object: field_object[1] + "666"
                     ),
        SearchOption(
            "class_ch",
        ),
        MyOption(
            "depart",
            text_func=lambda x:x.title
             # db_condition={"id__gt":2}
                     )
    ]

site.register(models.UserInfo,UserInfoHandler)
site.register(models.UserInfo,prev="private")
site.register(models.UserInfo,prev="publish")

class DeployHandler(StarkHander):

    list_display = [StarkHander.display_checkbox,'title',get_choice_text('状态','status'),StarkHander.display_edit,StarkHander.display_del]

    has_add_btn = True

    per_page_count = 1



site.register(models.Deploy,DeployHandler)
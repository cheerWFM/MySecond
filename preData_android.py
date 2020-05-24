# !/usr/bin/env python
# -*- coding:utf-8 -*-

class dataforandroid(object):
    ip = ''
    devices = '6ej4c18629014579'
    pname = 'com.cvte.scorpion.teams'  # 个人安卓端包名
    activity = 'com.cvte.scorpion.teams.mainactivity'  # 个人安卓端activity
    # 发起视频xpath
    createmeeting = '//*[@resource-id="android:id/content"]/android.widget.framelayout[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[2]/android.widget.imageview[1]'
    # 加入视频
    joinmeeting = '//*[@resource-id="android:id/content"]/android.widget.framelayout[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[3]/android.widget.imageview[1]'
    # 预约会议
    reservate = '//*[@resource-id="android:id/content"]/android.widget.framelayout[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[4]/android.widget.imageview[1]'
    # 创建任务
    createtask = '//*[@resource-id="android:id/content"]/android.widget.framelayout[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[5]/android.widget.imageview[1])'
    # 从发起视频邀请界面返回首页
    back = '//*[@resource-id="android:id/content"]/android.widget.framelayout[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]'
    # 离开会议
    leavemeeting = '//*[@resource-id="android:id/content"]/android.widget.framelayout[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[1]/android.view.viewgroup[3]/android.view.viewgroup[5]'
    # 结束会议


class text_element(object):
    # 发起视频的跳过按钮
    jump = '//*[@text="跳过"]'
    # 结束会议
    dismissmeeting = '//*[@text="结束会议"]'

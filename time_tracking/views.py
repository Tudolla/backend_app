from django.shortcuts import render
from .models import Attendance
from datetime import date
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# chi lấy những bản ghi chấm công trong 1 tháng để tối ưu hiệu xuất 
class AttendanceForMonthView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, month, year):
        user = request.user
        start_date = date(year, month, 1)
        
        # xac dinh ngay cuoi cung cua thang
        if month == 12:
            end_date = date(year + 1, 1, 1)
        else: 
            end_date = date(year, month + 1, 1)
        
        # lay du lieu cham cong trong thang
        attendances = Attendance.objects.filter(user = user, date__range=[start_date, end_date])

        attendance_data = []
        for attendace in attendances: 

            # Chi tinh cong khi co mat
            if attendace.status == "Present":
                # tinh thoi gian lam trong 1 ngay
                work_duration_res = attendace.check_out_time - attendace.check_in_time

                work_hours = work_duration_res.total_seconds() / 3600
                if work_hours >= 8:

                    attendance_data.append({
                        "date":attendace.date,
                        "work_hours_res": 1 # di lam du ngay
                    })
                elif 4 <= work_hours < 8:

                    attendance_data.append({
                        "date": attendace.date,
                        "work_hours_res":0.5
                    })



        return Response({"attendance_days": attendance_data})
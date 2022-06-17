from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import User as UserModel




class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    
     #사용자 정보 조회
    def get(self, request):
        user = request.user
        return Response({"message": "사용자 조회 성공!"})
    
    #회원 가입
    def post(self, request):
        usertype = request.POST.get('usertype', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        
        if email == '' or password == '' or usertype == '':
            return Response({"message": "회원 정보를 모두 입력해주세요!"})
        
        exist_user = get_user_model().objects.filter(email=email)
        if exist_user :
            return Response({"message": "이메일이 이미 존재합니다!"})
        
        UserModel.objects.create_user(usertype=usertype, email=email, password=password)
        
        return Response({"message": "회원가입 성공!!"})
    
    #회원 정보 수정
    def put(self, request):
        
        return Response({"message": "회원 정보 수정!!"})
    
    #회원 탈퇴
    def delete(self, request):
        
        return Response({"message": "회원 탈퇴!!"})


class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # 로그인
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "로그인 성공!!"})
    
    #로그아웃
    def delete(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공!"})
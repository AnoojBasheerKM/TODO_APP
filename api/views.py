from django.shortcuts import render,get_object_or_404

# Create your views here.

from rest_framework.views import APIView

from rest_framework import status,serializers

from rest_framework.response import Response

from api.serializers import UserSerializer,TodoSerializer

from rest_framework import authentication,permissions

from task.models import Todo


class UserCreateView(APIView):
    
    serializer_class = UserSerializer
    
    def post(self,request,*args,**kwargs):
        
        serializer_instance = self.serializer_class(data=request.data)

        if serializer_instance.is_valid():
            
            serializer_instance.save()

            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    
class TodoListCreateView(APIView):
    
    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TodoSerializer

    def get(self,request,*args,**kwargs):
        
        qs = Todo.objects.filter(owner=request.user)
        
        if "status" in request.query_params:
            
            search_text = request.query_params.get("status")

            qs = qs.filter(status=search_text)

        serializer_instance = self.serializer_class(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):
        
        serializer_instance = self.serializer_class(data=request.data)

        if serializer_instance.is_valid():
            
            serializer_instance.save(owner=request.user)
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
    
class TodoRetrieveUpdateDeleteView(APIView):
    
    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]
    
    serializer_class = TodoSerializer

    def get(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")

        qs = get_object_or_404(Todo,pk=id)
            
        serialzer_instance = self.serializer_class(qs)

        return Response(data=serialzer_instance.data)
    
    def delete(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")
        
        todo_object =  get_object_or_404(Todo,pk=id) 
        
        if request.user != todo_object.owner:
            
            raise serializers.ValidationError("access Denied ") 

        todo_object.delete()

        return Response(data = {"message":"deleted ok"})
    
    def put(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")        

        todo_object = get_object_or_404(Todo,pk=id)

        if request.user != todo_object.owner:
            
            raise serializers.ValidationError("Access Denied")

        serializer_instance = self.serializer_class(data=request.data,instance=todo_object)

        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)

        


from .models import Student, College
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Helper function 
@csrf_exempt
def student_to_dict(student):
    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "phone": student.phone,
        "college": student.college.name
    }

@csrf_exempt
def college_to_dict(college):
    return {
        "id": college.id,
        "name": college.name,
        "city": college.city
    }

# Create Student
@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Validation
        if not data.get("name"):
            return JsonResponse({"error": "Name is required"}, status=400)

        if not data.get("email"):
            return JsonResponse({"error": "Email is required"}, status=400)

        if not data.get("college_id"):
            return JsonResponse({"error": "College ID is required"}, status=400)

        student = Student.objects.create(
            name=data["name"],
            age=data.get("age"),
            email=data["email"],
            phone=data.get("phone"),
            college_id=data["college_id"]
        )

        return JsonResponse({
            "message": "Student created",
            "id": student.id
        }, status=201)
    

# College API
@csrf_exempt
def create_college(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Validation
        if not data.get("name"):
            return JsonResponse({"error": "Name is required"}, status=400)

        college = College.objects.create(
            name=data["name"],
            city=data.get("city")
        )

        return JsonResponse({
            "message": "College created",
            "id": college.id
        }, status=201)


# Get All Students (Search + pagination)
@csrf_exempt
def get_students(request):
    search = request.GET.get("search")
    page = int(request.GET.get("page", 1))
    limit = int(request.GET.get("limit", 5))

    students = Student.objects.all()

    if search:
        students = students.filter(name__icontains=search)

    start = (page - 1) * limit
    end = start + limit

    data = [student_to_dict(s) for s in students[start:end]]

    return JsonResponse({
        "page": page,
        "count": students.count(),
        "data": data
    })

# Get all colleges
@csrf_exempt
def get_colleges(request):
    colleges = College.objects.all()

    data = [college_to_dict(c) for c in colleges]

    return JsonResponse(data, safe=False, status=200)


# Get Single Student
@csrf_exempt
def get_student(request, id):
    try:
        student = Student.objects.get(id=id)
        return JsonResponse(student_to_dict(student), status=200)

    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)
    

# Get Single College
@csrf_exempt
def get_college(request, id):
    try:
        college = College.objects.get(id=id)
        return JsonResponse(college_to_dict(college), status=200)

    except College.DoesNotExist:
        return JsonResponse({"error": "College not found"}, status=404)

# Update Student
@csrf_exempt
def update_student(request, id):
    if request.method == "PUT":
        try:
            student = Student.objects.get(id=id)
            data = json.loads(request.body)

            student.name = data.get("name", student.name)
            student.age = data.get("age", student.age)
            student.email = data.get("email", student.email)
            student.phone = data.get("phone", student.phone)
            student.save()

            return JsonResponse({"message": "Updated successfully"}, status=200)

        except Student.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

# Update College
@csrf_exempt
def update_college(request, id):
    if request.method == "PUT":
        try:
            college = College.objects.get(id=id)
            data = json.loads(request.body)

            college.name = data.get("name", college.name)
            college.city = data.get("city", college.city)
            college.save()

            return JsonResponse({"message": "Updated successfully"}, status=200)

        except College.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)


# Delete Student
@csrf_exempt
def delete_student(request, id):
    if request.method == "DELETE":
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({"message": "Deleted successfully"}, status=200)

        except Student.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

# Delete College
@csrf_exempt
def delete_college(request, id):
    if request.method == "DELETE":
        try:
            college = College.objects.get(id=id)
            college.delete()

            return JsonResponse({"message": "Deleted successfully"}, status=200)

        except College.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)


# Filter Students
@csrf_exempt
def filter_students(request):
    college_id = request.GET.get("college_id")

    students = Student.objects.filter(college_id=college_id)

    data = [student_to_dict(s) for s in students]

    return JsonResponse(data, safe=False)


# Error Handling
@csrf_exempt
def get_student(request, id):
    try:
        student = Student.objects.get(id=id)

        data = {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "college": student.college.name
        }

        return JsonResponse(data)

    except Student.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
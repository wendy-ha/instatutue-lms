# Instatute Learning Manangement System (MVP)
## VIEW LIVE AT: http://instatutelms.pythonanywhere.com/.
Instatute, a non-profit education provider, is seeking a solution to transform their traditional classroom instruction to an online environment in order to enhance student engagement. However, the company is restrained by two factors: first, its human capital, and second, its internal policies. As a result, Instatute is looking for a technique team to assist them in developing a Learning Management System customised to their unique requirements.


# 1.0 Project Concept Design
## 1.1 Web development technologies
Instatute web application was implemented by employing a wide range of programming languages and software design concepts, which can named a few as table below.

<img width="550" alt="image" src="https://user-images.githubusercontent.com/90888090/189772080-8fa72bad-47be-4972-8c78-36fca8d33ca6.png">

## 1.2 Use case diagram
<img width="600" alt="image" src="https://user-images.githubusercontent.com/90888090/189773413-5a4514d8-8d33-435d-b67e-e176ead8dd18.png">

## 1.3 ERD for Course and Lesson management for Instatute
<img width="600" alt="image" src="https://user-images.githubusercontent.com/90888090/189773553-262d1c9d-d0db-4cc6-bb3c-2869924b62fb.png">

## 1.4 Architecture design with Django
<img width="800" alt="image" src="https://user-images.githubusercontent.com/90888090/189773639-75c97cb1-009b-4724-b466-7acd6d455627.png">


# 2.0 Instatute’s features implementation
## 2.1 Django Administration
I have utilised it as a model-centric interface for managing data in the Course and Lesson models, which were developed in TEP2022/classroom/models.py and TEP2022/lesson/models.py, respectively.

On the other hand, SQLite3 has been chosen as server-side database for the development of Instatute. Hence, the Django admin site could served as a database administration tool that is incredibly beneficial for testing create, read, update, and delete functions in models.

Figure below showned that the Course and Lesson models have been registered and displayed on admin site once logged in.

<img width="550" alt="image" src="https://user-images.githubusercontent.com/90888090/189772522-88e040d3-b8ca-4b86-a61c-c884a7795c64.png">

## 2.2 Managing accessible areas between application’s users
Reflecting explicitly on the Instatute app, after being authenticated and identified as a user of the application through the login process, the user will have access to different resources with different privilege levels depending on whether they are identified as a student or a teacher. Two users, Henry Jackson and Amy Smith, are used as examples to illustrate how to define and restrict access to Instatute's internal resources according to users' roles.

<h3> - For Teacher </h3>
<img width="600" alt="image" src="https://user-images.githubusercontent.com/90888090/189772802-6d6954f9-df87-4187-979f-f72aedfbf489.png">

<h3> - For Student </h3>
<img width="600" alt="image" src="https://user-images.githubusercontent.com/90888090/189772977-c8629b39-64bd-4350-a893-98b692f05b9c.png">

## 2.3 UI
<h3> - For Teacher </h3>
<img width="715" alt="image" src="https://user-images.githubusercontent.com/90888090/189774670-d8819736-7635-436c-9e90-a1f76a35ed09.png">
<img width="715" alt="image" src="https://user-images.githubusercontent.com/90888090/189774933-24fb4eaa-5c47-468f-8248-9e83b462c795.png">

<h3> - For Student </h3>
<img width="957" alt="image" src="https://user-images.githubusercontent.com/90888090/189775368-51656997-ca14-4971-8968-58815d5154df.png">





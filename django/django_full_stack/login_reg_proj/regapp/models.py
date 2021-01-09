from django.db import models
#import regex for email regexn
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        #first and last name validator
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 character"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 character"

        #email validator
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        #check password length
        if len(post_data['password']) < 8:
            errors['password'] = "Password should be at least 8 chars"
        #check password == password confirm
        if (post_data['password'] != post_data['confirm_pass']):
            errors['confirm_pass'] = "Password didn't match."
        
        #check email uniquenes
        user_list = User.objects.filter(email=post_data['email'])
        if(len(user_list)>0):
            errors['email_unique'] = 'This email is already taken.'
        return errors

    def login_validator(self, post_data):
        errors = {}

        #check email format
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        user_list = User.objects.filter(email=post_data['email'])
        #check if email is in the db
        if len(user_list) == 0:
            errors['email_not_found'] = "Email Address not in database!"
        else:
            #check password pw
            if bcrypt.checkpw(
                post_data['password'].encode(), 
                user_list[0].password.encode()
            ) != True:
                errors['password'] = 'Password Invalid'
        return errors
        


class User(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #validation objects
    objects = UserManager()
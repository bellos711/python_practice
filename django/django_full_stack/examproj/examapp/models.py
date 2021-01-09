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

    def wish_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 3:
            errors['title'] = "Wish should be at least 3 characters"
        if len(post_data['desc']) < 1:
            errors['desc'] = "Description can't be empty"
        if len(post_data['desc']) != 0:
            if len(post_data['desc']) < 3:
                errors['desc_not_zero'] = "Description must be at least 3 characters."
            
        return errors
        


class User(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #wish_uploaded
    # liked_wish = models.ManyToManyField('Wish', related_name='users_who_liked')
    #validation objects
    objects = UserManager()

class Wish(models.Model):
    title = models.CharField(max_length=254)
    desc = models.TextField()
    uploaded_by = models.ForeignKey('User', related_name='wish_uploaded', on_delete=models.CASCADE)
    is_granted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users_who_liked = models.ManyToManyField('User', related_name='liked_wish')
    objects = UserManager()
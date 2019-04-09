from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
import datetime

######### CHOICES ##################
class Choices():
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    GRADUATION_PROGRAMME = (
        ('B.Sc.', 'B.Sc.'),
        ('B.Com.', 'B.Com.')
    )
    DEPARTMENT_CHOICES = (
        ('Computer Application', 'Computer Application'),
        ('Information Technology', 'Information Technology'),
    )
    USER_TYPE = (
        ('student','Student'),
        ('faculty','Faculty'),
        ('admin','Admin'), 
        ('guest','Guest'), 
    )
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

class College(models.Model):
    clg_name = models.CharField(_('Name'), max_length=100)
    clg_u_name = models.CharField(_('username'), max_length=100, unique=True)
    desc = models.TextField(_('Description')) # Description
    logo = models.ImageField(_('logo'), upload_to='college/%s/logo/' % clg_u_name, default='college/logo_default.png')
    clg_pic = models.ImageField(_('College Picture'), upload_to='college_list/home_pics/', 
                                default='defaults/college_home_pic.jpeg')
    def __str__(self):
        return self.clg_name
    class Meta:
        # verbose_name = 'College'
        verbose_name_plural = '1. Colleges'

def profile_pic_path(instance, filename):
    return 'profile_pic/{0}/{1}/{2}/{3}'.format(str(instance.college.clg_u_name), str(instance.user_type), str(instance.username), filename)

class User(AbstractUser, Choices):
    def current_year():
        return datetime.date.today().year
    user_type = models.CharField(_('user type'), max_length=30, choices=Choices.USER_TYPE, blank=True, null=True)
    father_name = models.CharField(_("Farther's Name"), max_length=50, blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    graduation_programme = models.CharField(_("Graduation Programme"), max_length=50, choices=Choices.GRADUATION_PROGRAMME, null=True, blank=True)
    department = models.CharField(max_length=50, choices=Choices.DEPARTMENT_CHOICES, null=True, blank=True)
    session = models.IntegerField(_('Session start year'), choices=Choices.YEAR_CHOICES, default=current_year)
    gender = models.CharField(max_length=10, choices=Choices.GENDER_CHOICES, null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    dob = models.DateField(_('date of birth'), null=True, blank=True)

    def upload_path(self, **kwargs):
        return '%s/profile_pics/' % self.user_type
    profile_pic = models.ImageField(_('Profile Picture'), upload_to=profile_pic_path,
                                                          default='defaults/profile_pic.gif')

    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self):
        return self.username
    
    class Meta:
        # verbose_name = 'User'
        verbose_name_plural = '2. Users'

class Exam(models.Model):
    organisor = models.ForeignKey(User, 
                                on_delete=models.CASCADE, 
                                related_name='exam', 
                                limit_choices_to={'user_type': 'faculty'})

    instructions = models.TextField()
    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exam'


########### UNITAL NOTICE BOARD #############
class Notice(models.Model):
    def thirty_day_hence():
        """ Hii """
        return timezone.now() + timezone.timedelta(days=30)

    title = models.CharField(max_length=400)
    body = models.TextField()
    link = models.URLField()
    pub_date = models.DateField(default=timezone.now)
    expire_date = models.DateField(default=thirty_day_hence)

    def __str__(self):
        return str(self.id) + '. ' + self.pub_date.strftime("%d-%b-%Y")
    class Meta:
        # verbose_name = 'Unital Notice'
        verbose_name_plural = '3. Unital Notice'

######### COLLEGE PIC SLIDESHOW ################
def college_pic_path(instance, filename):
    return 'college/{0}/{1}'.format(str(instance.college.id) + '_' + instance.college.clg_u_name, filename)

class CollegePictures(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='pictures')    
    pic = models.ImageField(upload_to=college_pic_path)
    def __str__(self):
        return str(self.id) + ' ' + self.college.clg_u_name
    class Meta:
        verbose_name_plural = '4. College Pictures'

######### COLLEGE NOTICE BOARD #############
class CollegeNotice(Notice):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='notice')
    def __str__(self):
        return str(self.id) + '. ' + self.pub_date.strftime("%d-%b-%Y")
    
    class Meta:
        verbose_name_plural = '5. College Notice Board'



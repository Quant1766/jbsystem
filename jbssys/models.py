from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    "DEFAULT USE storename as username casser"
    is_hide = models.BooleanField("is hide",null=True,blank=True,default=False,)

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.PROTECT)

    "admin|doctor"
    role = models.CharField(
        "role",
        max_length=30,
        null=False,
        default='doctor')

    phone = models.CharField(
        "phone",
        max_length=20,
        blank=True,
        null=True,
        default="")

    default_city = models.CharField(
        "city",
        max_length=50,
        blank=True,
        null=True,
        default='')

    sex = models.CharField(
        "male female",
        max_length=50,
        blank=True,
        null=True,
        default='')

    home_addres = models.CharField(
        "home",
        max_length=100,
        blank=True,
        null=True,
        default='')
    work_addres = models.CharField(
        "work",
        max_length=100,
        blank=True,
        null=True,
        default='')

    telegram = models.CharField(
        "telegram",
        max_length=60,
        blank=True,
        null=True,
        default="")

    user_avatar = models.ImageField(
        upload_to="static/image/avatars/",
        default='/static/image/avatars/doctor_icon.png')  # You need to configure media in settings.py

    def __str__(self):
        return "%s %s" % (self.user.username, self.role)

def gen_aaaannnna(old_id="AAA0000A"):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c1,c2,c3,n1,n2,n3,n4,c4 = tuple(old_id)
    numb = int(''.join((n1,n2,n3,n4)))
    if numb == 9999:
        numb_new = 0


        try:
            c1_i = alphabet.index(c1)

            c1 = alphabet[c1_i+1]
        except:
            c1 = 'A'
            try:
                c2_i = alphabet.index(c2)

                c2 = alphabet[c2_i + 1]
            except:
                c2 = 'A'
                try:
                    c3_i = alphabet.index(c3)

                    c3 = alphabet[c3_i + 1]
                except:
                    c3 = 'A'
                    c4_i = alphabet.index(c4)

                    c4 = alphabet[c4_i + 1]


    else:
        numb_new = numb+1


    new_id = f"{c1}{c2}{c3}{str(numb_new).zfill(4)}{c4}"

    return new_id





class Cancer(models.Model):
    is_hide = models.BooleanField("is hide",null=True,blank=True,default=False,)

    title = models.CharField('title', max_length=20, null=True, blank=True)

class CancerHistory(models.Model):
    cancer = models.ForeignKey(Cancer,related_name="CancerHistory",on_delete=models.PROTECT)
    date_detect = models.DateField("Date detect", default=None, blank=True, null=True)

class ChldPacientDurBreast(models.Model):
    is_hide = models.BooleanField("is hide",null=True,blank=True,default=False,)

    num_child = models.IntegerField("numc child", validators=[
        MaxValueValidator(20),
        MinValueValidator(0)
    ],
        default="0")

    period_months = models.IntegerField("period months", validators=[
        MaxValueValidator(36),
        MinValueValidator(0)
    ],
                                    default="0")


class RelationhipPacient(models.Model):

    is_hide = models.BooleanField("is hide",null=True,blank=True,default=False,)

    relation = models.CharField(max_length=100,
                                  choices=(('father', 'father'),
                                           ('mother', 'mother'),
                                           ('grandmother','grandmother'),
                                           ('grandfather', 'grandfather'),
                                           ('brother', 'brother'),
                                           ('sister', 'sister'),
                                           ('relative', 'relative'),
                                           ('', ''),
                                           ),
                                  default='')

    age_diagnise = models.IntegerField("age diagnise", validators=[
        MaxValueValidator(120),
        MinValueValidator(1)
    ],
        default="1")

    type_cancer = models.ForeignKey(Cancer,on_delete=models.PROTECT, related_name='rel_tcanc')

    position_cancer = models.CharField(max_length=100,
                                  choices=(('one side', 'one side'),
                                           ('both sides', 'both sides'),
                                           ('', ''),
                                           ),
                                  default='')

class Drug(models.Model):
    is_hide = models.BooleanField("is hide",null=True,blank=True,default=False,)

    title = models.CharField('Title', max_length=300, null=True, blank=True)
    name = models.CharField('Name', max_length=300, null=True, blank=True)
    description = models.TextField(
        null=True, blank=True,
        max_length=2500,
        default='')

    routing = models.CharField(max_length=100,
                                  choices=(('Convenience', 'Convenience'),
                                           ('Desired target effect', 'Desired target effect'),
                                               ('Oral','Oral'),
                                           ('Local', 'Local'),

                                           ('Mouth inhalation', 'Mouth inhalation'),
                                           ('Nasal inhalation', 'Nasal inhalation'),
                                           ('Parenteral', 'Parenteral'),
                                           ('Intranasal', 'Intranasal'),
                                           ('Buccal', 'Buccal'),
                                           ('Sublabial administration', 'Sublabial administration'),
                                           ('', ''),
                                           ),
                                  default='')

class MedicalOperation(models.Model):
    title = models.CharField('title operation', max_length=100, blank=True,null=True,default="")
    date_operation = models.DateField("Date operation", default=None, blank=True, null=True)
    num_operation = models.IntegerField("num operation", validators=[
        MaxValueValidator(120),
        MinValueValidator(1)
    ],
                                       default="1")


class Pacient(models.Model):
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=300, blank=True, default='')

    email = models.EmailField('email address', blank=True)

    is_hide = models.BooleanField("is hide", null=True, blank=True, default=False, )

    phone = models.CharField(
        "phone",
        max_length=20,
        blank=True,
        null=True,
        default="")

    date_of_birth = models.DateField("Date of birth", default=None, blank=True, null=True)

    default_city = models.CharField(
        "city",
        max_length=100,
        blank=True,
        null=True,
        default='')

    home_addres = models.CharField(
        "home",
        max_length=100,
        blank=True,
        null=True,
        default='')

    nsh_id = models.CharField('nsh id', max_length=9, blank=True,
                              null=True,
                              default='')

    

class ProfileFormTable(models.Model):
    create_datetime = models.DateTimeField("create datetime",default=None, blank=True, null=True)
    nsh_id_gdisk = models.CharField(
        'nsh id gdisk',
        max_length=25,
        blank=True,
        null=True,
        default=''
    )

    pacient = models.ForeignKey(Pacient,related_name="PacientProfileForm",on_delete=models.PROTECT)


    sex = models.CharField(
        max_length=20,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('', ''),
        ),
        default=''
    )

    datapoint_10 = models.CharField(
        max_length=100,
        choices=(
            ('White', 'White'),
            ('Mixed / Multiple ethnic groups', 'Mixed / Multiple ethnic groups'),
            ('Asian / Asian British','Asian / Asian British'),
            ('Black / African / Caribbean / Black British', 'Black / African / Caribbean / Black British'),
            ('Other ethnic group', 'Other ethnic group'),

            ('', ''),
        ),
        default=''
    )

    metic_sys = models.CharField(
        max_length=20,
        choices=(
            ('IMPERIAL', 'IMPERIAL'),
            ('METRIC', 'METRIC'),
            ('', ''),
        ),
        default=''
    )

    datapoint_12 = models.CharField(max_length=15,
                                   null=True,blank=True,
                                   default='')

    datapoint_13a = models.CharField(max_length=15,
                                    null=True, blank=True,
                                    default='')
    datapoint_13b = models.CharField(max_length=15,
                                     null=True, blank=True,
                                     default='')

    datapoint_14 = models.CharField(max_length=15,
                                     null=True, blank=True,
                                     default='')
    datapoint_15 = models.CharField(max_length=8,
                                     null=True, blank=True,
                                     default='')
    datapoint_16 = models.TextField(
                                    null=True, blank=True,
                                   max_length=3000,
                                   default='')
    datapoint_17 = models.TextField(
                                    null=True, blank=True,
                                   max_length=3000,
                                   default='')

    datapoint_18 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_19 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')
    datapoint_20 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_21 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_22 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_23 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_24 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_25 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_26 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_27 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_28 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_29 = models.ManyToManyField(Drug,related_name="Drug1")


    datapoint_30 = models.ManyToManyField(Drug,related_name="Drug2")


    datapoint_31 = models.ManyToManyField(MedicalOperation,related_name="MedicalOperation1")



    datapoint_32 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_33 = models.DateField("Datapoin 33",default=None,blank=True,null=True)




    datapoint_34 = models.CharField(
        max_length=100,
        choices=(
            ('Never', 'Never'),
            ('1-2 days/week', '1-2 days/week'),
            ('3-4 days/week', '3-4 days/week'),
            ('5+ days/week', '5+ days/week'),
            ('', ''),
        ),
        default=''
    )

    datapoint_35 = models.CharField(
        max_length=50,
        choices=(
            ('I consume a low-fibre diet', 'I consume a low-fibre diet'),
            ('I consume a high-fibre diet', 'I consume a high-fibre diet'),
            ('', ''),
        ),
        default=''
    )

    datapoint_36 = models.CharField(
        max_length=100,
        choices=(
            ('1-6 units', '1-6 units'),
            ('7-14 units', '7-14 units'),
            ('15-24 units', '15-24 units'),
            ('25-48 units', '25-48 units'),
            ('more than 48 units', 'more than 48 units'),

            ('I don’t know', 'I don’t know'),
            ('', 'I don’t know'),
        ),
        default=''
    )

    datapoint_37 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('Ex-smoker', 'Ex-smoker'),
            ('', ''),
        ),
        default=''
    )

    datapoint_38 = models.CharField(max_length=15,
                                     null=True, blank=True,
                                     default='')

    datapoint_39 = models.CharField(max_length=15,
                                     null=True, blank=True,
                                     default='')

    datapoint_40 = models.TextField(
        null=True, blank=True,
        max_length=3000,
        default='')

    datapoint_41 = models.CharField(max_length=15,
                                    null=True, blank=True,
                                    default='')

    datapoint_42 = models.CharField(max_length=15,
                                    null=True, blank=True,
                                    default='')


    datapoint_43 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_44 = models.CharField(max_length=15,
                                    null=True, blank=True,
                                    default='')

    datapoint_45 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_46 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_47 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_48 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_49 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_50 = models.CharField(max_length=15,
                                    null=True, blank=True,
                                    default='')

    datapoint_51 = models.CharField(max_length=15,
                                    null=True, blank=True,
                                    default='')

    datapoint_52 = models.ManyToManyField(ChldPacientDurBreast,related_name='ChldPacientDurBreast1')


    datapoint_53 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_54 = models.CharField(
        max_length=50,
        choices=(
            ('Couple of days', 'Couple of days'),
            ('Couple of weeks', 'Couple of weeks'),
            ('Few weeks', 'Few weeks'),
            ('Couple of months', 'Couple of months'),
            ('Few months', 'Few months'),
            ('A year', 'A year'),
            ('Couple of years', 'Couple of years'),
            ('Many years', 'Many years'),
            ('More than a decade','More than a decade'),
            ('', ''),
        ),
        default=''
    )

    datapoint_55 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_56 = models.CharField(max_length=15,
                                    null=True, blank=True,
                                    default='')

    datapoint_57 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_58 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_59 = models.CharField(
        max_length=50,
        choices=(
            ('Couple of days', 'Couple of days'),
            ('Couple of weeks', 'Couple of weeks'),
            ('Few weeks', 'Few weeks'),
            ('Couple of months', 'Couple of months'),
            ('Few months', 'Few months'),
            ('A year', 'A year'),
            ('Couple of years', 'Couple of years'),
            ('Many years', 'Many years'),
            ('More than a decade','More than a decade'),
            ('', ''),
        ),
        default=''
    )

    datapoint_60 = models.CharField(max_length=15,
                                    null=True, blank=True,
                                    default='')



    datapoint_61 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_62 = models.ManyToManyField(RelationhipPacient,related_name='RelationhipPacient1')

    datapoint_63 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_64 = models.ManyToManyField(RelationhipPacient,related_name='RelationhipPacient2')

    datapoint_65 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_66 = models.ManyToManyField(CancerHistory,related_name='CancerHistory1')

    datapoint_67 = models.CharField(
        max_length=20,
        choices=(
            ('Unknown', 'Unknown'),
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', 'Unknown'),

        ),
        default=''
    )

    datapoint_68 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_69 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_70 = models.CharField(
        max_length=280,
        choices=(
            ('Peutz-Jeghers syndrome (STK11 altered gene)', 'Peutz-Jeghers syndrome (STK11 altered gene)'),
            ('Cowden Syndrome (PTEN altered gene)', 'Cowden Syndrome (PTEN altered gene)'),
            ('Hereditary diffuse gastric (stomach)  cancer (E-Cadheric (CDH11) altered gene)', 'Hereditary diffuse gastric (stomach)  cancer (E-Cadheric (CDH11) altered gene)'),
            ('', ''),

        ),
        default=''
    )


    datapoint_71 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_72 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_73 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_74 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_75 = models.CharField(
        max_length=50,
        choices=(
            ('Help Bathing', 'Help Bathing'),
            ('Help Dressing', 'Help Dressing'),
            ('Help getting in/out of Chair', 'Help getting in/out of Chair'),
            ('Help Walking around house', 'Help Walking around house'),
            ('Help Eating', 'Help Eating'),
            ('Help Grooming', 'Help Grooming'),
            ('Help Using Toilet', 'Help Using Toilet'),
            ('Help up/down Stairs', 'Help up/down Stairs'),
            ('Help lifting 10 lbs', 'Help lifting 10 lbs'),
            ('Help Shopping', 'Help Shopping'),
            ('Help with meal Preparations', 'Help with meal Preparations'),
            ('Help taking Medication', 'Help taking Medication'),
            ('Help with Housework', 'Help with Housework'),
            ('', ''),

        ),
        default=''
    )

    datapoint_76 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_77 = models.CharField(
        max_length=70,
        choices=(
            ('Yes, less than 3 days a week', 'Yes, less than 3 days a week'),
            ('Yes, at least 3 days a week', 'Yes, at least 3 days a week'),
            ('NO', 'NO'),
            ('', 'NO'),

        ),
        default=''
    )

    datapoint_78 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_79 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_80 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_81 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_82 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_83 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_84 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_85 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_86 = models.CharField(
        max_length=10,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),

        ),
        default=''
    )

    datapoint_87 = models.CharField(
        max_length=70,
        choices=(
            ('Lost more than 10 lbs in last year', 'Lost more than 10 lbs in last year'),
            ('Cut down on Usual Activity (in last month)', 'Cut down on Usual Activity (in last month)'),
            ('Stayed in Bed at least half the day due to health (in last month)', 'Stayed in Bed at least half the day due to health (in last month)'),
            ('Feel Everything is an Effort', 'Feel Everything is an Effort'),
            ('Feel Depressed', 'Feel Depressed'),
            ('Feel Happy', 'Feel Happy'),
            ('Feel Lonely', 'Feel Lonely'),
            ('Have Trouble getting going', 'Have Trouble getting going'),
            ('', ''),
        ),
        default=''
    )

    datapoint_88 = models.CharField(
        max_length=20,
        choices=(
            ('Most times', 'Most times'),
            ('Sometimes', 'Sometimes'),
            ('Rarely', 'Rarely'),
            ('', ''),

        ),
        default=''
    )

    datapoint_89 = models.CharField(
        max_length=20,
        choices=(
            ('Most times', 'Most times'),
            ('Sometimes', 'Sometimes'),
            ('Rarely', 'Rarely'),
            ('', ''),

        ),
        default=''
    )

    datapoint_90 = models.CharField(
        max_length=20,
        choices=(
            ('Most times', 'Most times'),
            ('Sometimes', 'Sometimes'),
            ('Rarely', 'Rarely'),
            ('', ''),

        ),
        default=''
    )

    datapoint_91 = models.CharField(
        max_length=20,
        choices=(
            ('Most times', 'Most times'),
            ('Sometimes', 'Sometimes'),
            ('Rarely', 'Rarely'),
            ('', ''),

        ),
        default=''
    )

    datapoint_92 = models.CharField(
        max_length=20,
        choices=(
            ('Most times', 'Most times'),
            ('Sometimes', 'Sometimes'),
            ('Rarely', 'Rarely'),
            ('', ''),

        ),
        default=''
    )

    datapoint_93 = models.CharField(
        max_length=20,
        choices=(
            ('Worse', 'Worse'),
            ('Same', 'Same'),
            ('Better', 'Better'),
            ('', ''),

        ),
        default=''
    )

    datapoint_94 = models.CharField(
        max_length=20,
        choices=(
            ('Poor', 'Poor'),
            ('Fair', 'Fair'),
            ('Good', 'Good'),
            ('Very good', 'Very good'),
            ('Excellent', 'Excellent'),
            ('', ''),

        ),
        default=''
    )

    datapoint_95 = models.TextField("datapoint 95",
                                   max_length=3000,
                                   default='')




class DataFormTable(models.Model):
    "DEFAULT USE storename as username casser"
    create_datetime = models.DateTimeField("create datetime", null=True,blank=True)
    is_hide = models.BooleanField("is hide",null=True,blank=True,default=False)

    pacient = models.ForeignKey(Pacient,related_name="PacientDataForm",on_delete=models.PROTECT)

    profile_data = models.ForeignKey(ProfileFormTable,related_name="PacientDataProfileForm",on_delete=models.PROTECT)

    datapoint_7 = models.TextField("Screener",
                                max_length=3000,
                              default='')

    datapoint_8 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_9 = models.TextField("Datapint99",
                                    max_length=2000,
                                    default='')



    datapoint_10 = models.CharField(max_length=45,
                                  choices=(('Upper - outer peripheral', 'Upper - outer peripheral'),
                                           ('Upper - inner peripheral', 'Upper - inner peripheral'),
                                           ('Lower - inner peripheral', 'Lower - inner peripheral'),
                                           ('Lower - outer peripheral', 'Lower - outer peripheral'),
                                           ('Upper - outer central'   , 'Upper - outer central'   ),
                                           ('Upper - inner central'   , 'Upper - inner central'   ),
                                           ('Lower - inner central'   , 'Lower - inner central'   ),
                                           ('Lower - outer central'   , 'Lower - outer central'   ),
                                           ('Areola'                  , 'Areola'                  ),
                                           ('Nipple'                  , 'Nipple'                  ),
                                           ( ''                       ,  ''                       ),
                                           ),
                                  default='')

    datapoint_11 = models.CharField(max_length=45,
                                    choices=(('Upper - outer peripheral', 'Upper - outer peripheral'),
                                             ('Upper - inner peripheral', 'Upper - inner peripheral'),
                                             ('Lower - inner peripheral', 'Lower - inner peripheral'),
                                             ('Lower - outer peripheral', 'Lower - outer peripheral'),
                                             ('Upper - outer central', 'Upper - outer central'),
                                             ('Upper - inner central', 'Upper - inner central'),
                                             ('Lower - inner central', 'Lower - inner central'),
                                             ('Lower - outer central', 'Lower - outer central'),
                                             ('Areola', 'Areola'),
                                             ('Nipple', 'Nipple'),
                                             ('', ''),
                                             ),
                                  default='')

    datapoint_12 = models.CharField(max_length=15,
                              choices=(('pea'       , 'pea'       ),
                                       ('peanut'    , 'peanut'    ),
                                       ('grape'     , 'grape'     ),
                                       ('walnut'    , 'walnut'    ),
                                       ('lemon'     , 'lemon'     ),
                                       ('egg'       , 'egg'       ),
                                       ('peach'     , 'peach'     ),
                                       ('grapefruit', 'grapefruit'),
                                       (''          , ''          ),
                                       ),
                              default='')



    datapoint_13 = models.CharField(max_length=25,
                              choices=(('Couple of days ago',    'Couple of days ago'),
                                       ('Couple of weeks ago',   'Couple of weeks ago'),
                                       ('Few weeks ago',         'Few weeks ago'),
                                       ('Couple of months ago',  'Couple of months ago'),
                                       ('Few months ago',        'Few months ago'),
                                       ('A year ago',            'A year ago'),
                                       ('Couple of years ago',   'Couple of years ago'),
                                       ('Many years ago',        'Many years ago'),
                                       ('',                      ''),
                                       ),
                              default='')

    datapoint_14 = models.CharField(max_length=25,
                              choices=(('Slowing  growing',        'Slowing  growing'),
                                       ('Rapidly  Growing',        'Rapidly  Growing'),
                                       ('Remained same in size',  'Remained same in size'),
                                       ('Decreased  In Size',      'Decreased  In Size'),
                                       ('',                       ''),
                                       ),
                              default='')

    datapoint_15 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_16 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_16_a = models.CharField(max_length=15,
                              choices=(('1', '1'),
                                       ('2', '2'),
                                       ('3', '3'),
                                       ('4 or more', '4 or more'),
                                       ('',''),
                                       ),
                              default='')

    datapoint_16_b = models.CharField(max_length=15,
                                      choices=(('1', '1'),
                                               ('2', '2'),
                                               ('3', '3'),
                                               ('4 or more', '4 or more'),
                                               ('', ''),
                                               ),
                                      default='')


    datapoint_17 = models.CharField(max_length=25,
                                      choices=(('Soft', 'Soft'),
                                               ('Firm', 'Firm'),
                                               ('Hard', 'Hard'),
                                               ('Dont know', 'Dont know'),
                                               ('', 'Dont know'),
                                               ),
                                      default='')

    datapoint_18 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_19 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_20 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )



    datapoint_21 = models.CharField(max_length=35,
                                      choices=(('less than one month', 'less than one month'),
                                               ('2 - 3 months', '2 - 3 months'),
                                               ('3-6 months', '3-6 months'),
                                               ('6-12 months', '6-12 months'),
                                               ('more than 1 year', 'more than 1 year'),
                                               ('', ''),
                                               ),
                                      default='')

    datapoint_22 = models.CharField(max_length=25,
                                    choices=(('<5% of weight', '<5% of weight'),
                                             ('>5% of weight', '>5% of weight'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_23 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_24 = models.TextField("Datapoint 24",
                                  max_length=3000,
                                  default='')

    datapoint_25 = models.TextField("Datapoint 25",
                                    max_length=3000,
                                    default='')

    datapoint_26 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_27 =  models.TextField("Datapoint 27",
                                    max_length=3000,
                                    default='')

    datapoint_28 = models.TextField("neck groin pos",
                                max_length=2000,
                                default='')


    datapoint_30 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_31 = models.CharField(max_length=25,
                                    choices=(('pea', 'pea'),
                                             ('peanut', 'peanut'),
                                             ('grape', 'grape'),
                                             ('walnut', 'walnut'),
                                             ('lemon', 'lemon'),
                                             ('egg', 'egg'),
                                             ('peach', 'peach'),
                                             ('grapefruit', 'grapefruit'),
                                             ('', ''),
                                             ),
                              default='')

    datapoint_32 = models.CharField(max_length=15,
                                    choices=(('Soft', 'Soft'),
                                             ('Firm', 'Firm'),
                                             ('Hard', 'Hard'),
                                             ('Dont know', 'Dont know'),
                                             ('', 'Dont know'),
                                             ),
                                    default='')

    datapoint_33 = models.CharField(max_length=3,
                                    choices=(('1', '1'),
                                             ('2', '2'),
                                             ('3', '3'),
                                             ('4', '4'),
                                             ('5', '5'),
                                             ('6', '6'),
                                             ('7', '7'),
                                             ('8', '8'),
                                             ('9', '9'),
                                             ('10', '10'),
                                             ('', ''),
                                             ),
                                    default='')
    datapoint_34 = models.CharField(max_length=3,
                                    choices=(('1', '1'),
                                             ('2', '2'),
                                             ('3', '3'),
                                             ('4', '4'),
                                             ('5', '5'),
                                             ('6', '6'),
                                             ('7', '7'),
                                             ('8', '8'),
                                             ('9', '9'),
                                             ('10', '10'),
                                             ('', ''),
                                             ),
                                    default='')


    datapoint_35 = models.CharField(max_length=3,
                                    choices=(('1', '1'),
                                             ('2', '2'),
                                             ('3', '3'),
                                             ('4', '4'),
                                             ('5', '5'),
                                             ('6', '6'),
                                             ('7', '7'),
                                             ('8', '8'),
                                             ('9', '9'),
                                             ('10', '10'),
                                             ('', ''),
                                             ),
                                    default='')
    datapoint_36 = models.CharField(max_length=3,
                                    choices=(('1', '1'),
                                             ('2', '2'),
                                             ('3', '3'),
                                             ('4', '4'),
                                             ('5', '5'),
                                             ('6', '6'),
                                             ('7', '7'),
                                             ('8', '8'),
                                             ('9', '9'),
                                             ('10', '10'),
                                             ('', ''),
                                             ),
                                    default='')
    datapoint_37 = models.CharField(max_length=3,
                                    choices=(('1', '1'),
                                             ('2', '2'),
                                             ('3', '3'),
                                             ('4', '4'),
                                             ('5', '5'),
                                             ('6', '6'),
                                             ('7', '7'),
                                             ('8', '8'),
                                             ('9', '9'),
                                             ('10', '10'),
                                             ('', ''),
                                             ),
                                    default='')
    datapoint_38 = models.CharField(max_length=3,
                                    choices=(('1', '1'),
                                             ('2', '2'),
                                             ('3', '3'),
                                             ('4', '4'),
                                             ('5', '5'),
                                             ('6', '6'),
                                             ('7', '7'),
                                             ('8', '8'),
                                             ('9', '9'),
                                             ('10', '10'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_39 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_40 = models.CharField(max_length=45,
                                    choices=(('Couple of days ago', 'Couple of days ago'),
                                             ('Couple of weeks ago', 'Couple of weeks ago'),
                                             ('Few weeks ago', 'Few weeks ago'),
                                             ('Couple of months ago', 'Couple of months ago'),
                                             ('Few months ago', 'Few months ago'),
                                             ('A year ago', 'A year ago'),
                                             ('Couple of years ago', 'Couple of years ago'),
                                             ('Many years ago', 'Many years ago'),
                                             ('', ''),
                                             ),
                              default='')


    datapoint_41 = models.CharField(max_length=35,
                                    choices=(('Slowing  growing', 'Slowing  growing'),
                                             ('Rapidly  Growing', 'Rapidly  Growing'),
                                             ('remained same in size', 'remained same in size'),
                                             ('Decreased  In Size', 'Decreased  In Size'),
                                             ('', ''),
                                             ),
                              default='')

    datapoint_42 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_43 = models.TextField("Datapint43",
                                      max_length=2000,
                                      default='')

    datapoint_44 = models.TextField("Datapint44",
                                    max_length=2000,
                                    default='')

    datapoint_45 = models.TextField("Datapint45",
                                    max_length=2000,
                                    default='')

    datapoint_46 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_47 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_48 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_49 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_50 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_51 = models.CharField(max_length=45,
                                    choices=(('Couple of days ago', 'Couple of days ago'),
                                             ('Couple of weeks ago', 'Couple of weeks ago'),
                                             ('Few weeks ago', 'Few weeks ago'),
                                             ('Couple of months ago', 'Couple of months ago'),
                                             ('Few months ago', 'Few months ago'),
                                             ('A year ago', 'A year ago'),
                                             ('Couple of years ago', 'Couple of years ago'),
                                             ('Many years ago', 'Many years ago'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_52 = models.CharField(max_length=25,
                                    choices=(('Green', 'Green'),
                                             ('Watery', 'Watery'),
                                             ('White', 'White'),
                                             ('Blood Stained', 'Blood Stained'),
                                             ('Brownish', 'Brownish'),
                                             ('Serous', 'Serous'),
                                             ('Pus', 'Pus'),
                                             ('Yellow', 'Yellow'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_53 = models.TextField("Datapint99",
                                    max_length=2000,
                                    default='')

    datapoint_54 = models.CharField(max_length=25,
                                    choices=(('One spot', 'One spot'),
                                             ('Many spots', 'Many spots'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_55 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_56 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_57 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_58 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_59 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_60 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_61 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )


    datapoint_62 = models.TextField("Datapint62",
                                    max_length=2000,
                                    default='')

    datapoint_63 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_64 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_65 = models.TextField("Datapint65",
                                    max_length=2000,
                                    default='')

    datapoint_66 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_67 = models.CharField(max_length=55,
                                    choices=(('Less than a quarter', 'Less than a quarter'),
                                             ('More than a quarter but less than half', 'More than a quarter but less than half'),
                                             ('More than half of breast', 'More than half of breast'),
                                             ('Whole breast', 'Whole breast'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_68 = models.CharField(max_length=35,
                                    choices=(('Couple of days ago', 'Couple of days ago'),
                                             ('Couple of weeks ago', 'Couple of weeks ago'),
                                             ('Few weeks ago', 'Few weeks ago'),
                                             ('Couple of months ago', 'Couple of months ago'),
                                             ('Few months ago', 'Few months ago'),
                                             ('A year ago', 'A year ago'),
                                             ('Couple of years ago', 'Couple of years ago'),
                                             ('Many years ago', 'Many years ago'),
                                             ('', ''),
                                             ),
                             default='')

    datapoint_69 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_70 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_71 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_72 = models.TextField("Datapint99",
                                    max_length=2000,
                                    default='')

    datapoint_73 = models.CharField(max_length=35,
                                    choices=(('Couple of days ago', 'Couple of days ago'),
                                             ('Couple of weeks ago', 'Couple of weeks ago'),
                                             ('Few weeks ago', 'Few weeks ago'),
                                             ('Couple of months ago', 'Couple of months ago'),
                                             ('Few months ago', 'Few months ago'),
                                             ('A year ago', 'A year ago'),
                                             ('Couple of years ago', 'Couple of years ago'),
                                             ('Many years ago', 'Many years ago'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_74 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_75 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_76 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_77 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_78 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_79 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_80 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_81 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_82 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_83 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_84 = models.TextField("Datapint99",
                                    max_length=2000,
                                    default='')

    datapoint_85 = models.CharField(max_length=25,
                                    choices=(('Couple of days ago', 'Couple of days ago'),
                                             ('Couple of weeks ago', 'Couple of weeks ago'),
                                             ('Few weeks ago', 'Few weeks ago'),
                                             ('Couple of months ago', 'Couple of months ago'),
                                             ('Few months ago', 'Few months ago'),
                                             ('A year ago', 'A year ago'),
                                             ('Couple of years ago', 'Couple of years ago'),
                                             ('Many years ago', 'Many years ago'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_86 = models.CharField(max_length=25,
                                    choices=(('Rapidly progressing', 'Rapidly progressing'),
                                             ('Slowly progressing', 'Slowly progressing'),
                                             ('No change', 'No change'),
                                             ('Getting better', 'Getting better'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_87 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_88 = models.TextField("Datapint88",
                                    max_length=2000,
                                    default='')

    datapoint_89 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_90 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_91 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_92 = models.CharField(max_length=35,
                                    choices=(('Couple of days ago', 'Couple of days ago'),
                                             ('Couple of weeks ago', 'Couple of weeks ago'),
                                             ('Few weeks ago', 'Few weeks ago'),
                                             ('Couple of months ago', 'Couple of months ago'),
                                             ('Few months ago', 'Few months ago'),
                                             ('A year ago', 'A year ago'),
                                             ('Couple of years ago', 'Couple of years ago'),
                                             ('Many years ago', 'Many years ago'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_93 = models.CharField(max_length=35,
                                    choices=(('Rapidly progressing', 'Rapidly progressing'),
                                             ('Slowly progressing', 'Slowly progressing'),
                                             ('No change', 'No change'),
                                             ('Getting better', 'Getting better'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_94 = models.TextField("Datapint99",
                                    max_length=2000,
                                    default='')

    datapoint_95 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_96 = models.TextField("Datapint96",
                                    max_length=2000,
                                    default='')

    datapoint_97 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_98 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_99 = models.TextField("Datapint99",
                                    max_length=2000,
                                    default='')

    datapoint_100 = models.CharField(max_length=45,
                                     choices=(('Upper - outer peripheral', 'Upper - outer peripheral'),
                                              ('Upper - inner peripheral', 'Upper - inner peripheral'),
                                              ('Lower - inner peripheral', 'Lower - inner peripheral'),
                                              ('Lower - outer peripheral', 'Lower - outer peripheral'),
                                              ('Upper - outer central', 'Upper - outer central'),
                                              ('Upper - inner central', 'Upper - inner central'),
                                              ('Lower - inner central', 'Lower - inner central'),
                                              ('Lower - outer central', 'Lower - outer central'),
                                              ('Areola', 'Areola'),
                                              ('Nipple', 'Nipple'),
                                              ('', ''),
                                              ),
                                  default='')

    datapoint_101 = models.CharField(max_length=45,
                                     choices=(('Upper - outer peripheral', 'Upper - outer peripheral'),
                                              ('Upper - inner peripheral', 'Upper - inner peripheral'),
                                              ('Lower - inner peripheral', 'Lower - inner peripheral'),
                                              ('Lower - outer peripheral', 'Lower - outer peripheral'),
                                              ('Upper - outer central', 'Upper - outer central'),
                                              ('Upper - inner central', 'Upper - inner central'),
                                              ('Lower - inner central', 'Lower - inner central'),
                                              ('Lower - outer central', 'Lower - outer central'),
                                              ('Areola', 'Areola'),
                                              ('Nipple', 'Nipple'),
                                              ('', ''),
                                              ),
                                     default='')

    datapoint_102 = models.CharField(max_length=55,
                                     choices=(('Couple of days ago', 'Couple of days ago'),
                                              ('Couple of weeks ago', 'Couple of weeks ago'),
                                              ('Few weeks ago', 'Few weeks ago'),
                                              ('Couple of months ago', 'Couple of months ago'),
                                              ('Few months ago', 'Few months ago'),
                                              ('A year ago', 'A year ago'),
                                              ('Couple of years ago', 'Couple of years ago'),
                                              ('Many years ago', 'Many years ago'),
                                              ('', ''),
                                              ),
                                    default='')

    datapoint_103 = models.TextField("Datapint103",
                                    max_length=2000,
                                    default='')

    datapoint_104 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_105 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_106 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_107 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_108 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_109 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_110 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_111 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_112 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_113 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_114 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_115 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_116 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_117 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_118 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )
    datapoint_119 = models.CharField(
        max_length=100,
        choices=(
            ('YES', 'YES'),
            ('NO', 'NO'),
            ('', ''),
        ),
        default=''
    )

    datapoint_120 = models.CharField("Id in disk", max_length=30, default='')


class DataDictionary(models.Model):
    model_name = models.CharField("Model Name", max_length=50, default='')
    f_code = models.CharField("F Code", max_length=3, default='')
    f_score = models.CharField("F Score", max_length=5, default='',)

    is_hide = models.BooleanField("is hide", null=True, blank=True, default=False, )

    key = models.CharField('Data point', max_length=20, null=True, blank=True,default="")
    value = models.TextField(
        null=True, blank=True,
        max_length=2500,
        default='')
    color = models.CharField('Color', max_length=30, null=True, blank=True,default="")
    model_id = models.CharField('model id', max_length=10, null=True, blank=True,default="")

    link_logic = models.BooleanField("Is logLink",default=False)
    u_score = models.CharField('u score', max_length=3, null=True, blank=True,default="")
    display_distenation =  models.CharField('display distenation', max_length=50, null=True, blank=True,default="")
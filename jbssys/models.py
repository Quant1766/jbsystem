from django.db import models

from django.contrib.auth.models import User



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

class Pacient(models.Model):
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)
    email = models.EmailField('email address', blank=True)

    phone = models.CharField(
        "phone",
        max_length=20,
        blank=True,
        null=True,
        default="")

    date_of_birth = models.DateField("Date of birth",default=None,blank=True,null=True)

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

    nsh_id = models.CharField('nsh id', max_length=9,blank=True,
        null=True,
        default='')



class UserProfile(models.Model):
    "DEFAULT USE storename as username casser"

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


class MasterTable(models.Model):
    "DEFAULT USE storename as username casser"
    create_datetime = models.DateTimeField("Registry DTime", auto_now_add=True)
    updated_datetime = models.DateTimeField("Update DTime", auto_now=True)

    pacient = models.ForeignKey(Pacient,related_name="Pacientmaster",on_delete=models.PROTECT)

    """
    Screnner one or some field
    
    Breast lump
    Lump in axilla or armpit
    Breast pain
    Nipple discharge
    Skin redness of breast
    Retraction of nipple
    Puckering, dimple or indentation of skin
    Breast rash"""

    datapoint_7 = models.TextField("Screener",
                                max_length=1500,
                              default='')

    is_datapoint_8 = models.BooleanField("is Datapint8", null=True,blank=True)

    datapoint_9 = models.CharField(max_length=15,
                                  choices=(('RL', 'Right & left'),
                                           ('R', 'Right'),
                                           ('L', 'Left'),
                                           ('', 'Null'),
                                           ),
                                  default='')



    datapoint_10 = models.CharField(max_length=45,
                                  choices=(('UpOutPir', 'Upper - outer peripheral'),
                                           ('UpInPir', 'Upper - inner peripheral'),
                                           ('LowInPir', 'Lower - inner peripheral'),
                                           ('LowOutPir', 'Lower - outer peripheral'),
                                           ('UpOutCntr', 'Upper - outer central'),
                                           ('UpInCntr', 'Upper - inner central'),
                                           ('LowInCntr', 'Lower - inner central'),
                                           ('LowOutCntr', 'Lower - outer central'),
                                           ('LowOutCntr', 'Areola'),
                                           ('LowOutCntr', 'Nipple'),
                                           ('', 'Null'),
                                           ),
                                  default='')

    datapoint_11 = models.CharField(max_length=45,
                                  choices=(('UpOutPir', 'Upper - outer peripheral'),
                                           ('UpInPir', 'Upper - inner peripheral'),
                                           ('LowInPir', 'Lower - inner peripheral'),
                                           ('LowOutPir', 'Lower - outer peripheral'),
                                           ('UpOutCntr', 'Upper - outer central'),
                                           ('UpInCntr', 'Upper - inner central'),
                                           ('LowInCntr', 'Lower - inner central'),
                                           ('LowOutCntr', 'Lower - outer central'),
                                           ('LowOutCntr', 'Areola'),
                                           ('LowOutCntr', 'Nipple'),
                                           ('', 'Null'),
                                           ),
                                  default='')

    datapoint_12 = models.CharField(max_length=15,
                              choices=(('pea', 'Pea'),
                                       ('peanut', 'Peanut'),
                                       ('grape', 'Grape'),
                                       ('walnut', 'Walnut'),
                                       ('lemon', 'Lemon'),
                                       ('egg', 'Egg'),
                                       ('peach', 'Peach'),
                                       ('grapefruit', 'Grapefruit'),
                                       ('','Null'),
                                       ),
                              default='')



    datapoint_13 = models.CharField(max_length=15,
                              choices=(('couplDay', 'Couple of days ago'),
                                       ('couplWeeks', 'Couple of weeks ago'),
                                       ('fevgWeeks', 'Few weeks ago'),
                                       ('couplMont', 'Couple of months ago'),
                                       ('fevMont', 'Few months ago'),
                                       ('Year', 'A year ago'),
                                       ('couplYear', 'Couple of years ago'),
                                       ('manyYear', 'Many years ago'),
                                       ('','Null'),
                                       ),
                              default='')

    datapoint_14 = models.CharField(max_length=15,
                              choices=(('slowGrow', 'slowing growing'),
                                       ('slowGrow', 'rapidly growing'),
                                       ('remainSize', 'remained same in size'),
                                       ('decrSize', 'decreased in size'),
                                       ('','Null'),
                                       ),
                              default='')

    is_datapoint_15 = models.BooleanField("is Datapint15", null=True,blank=True)

    is_datapoint_16 = models.BooleanField("is Datapint16", null=True, blank=True)

    datapoint_16_a = models.CharField(max_length=15,
                              choices=(('1', '1'),
                                       ('2', '2'),
                                       ('3', '3'),
                                       ('4', '4 or more'),
                                       ('0','Null'),
                                       ),
                              default='')

    datapoint_16_b = models.CharField(max_length=15,
                                      choices=(('1', '1'),
                                               ('2', '2'),
                                               ('3', '3'),
                                               ('4', '4 or more'),
                                               ('0', 'Null'),
                                               ),
                                      default='')


    datapoint_17 = models.CharField(max_length=15,
                                      choices=(('S', 'Soft'),
                                               ('F', 'Firm'),
                                               ('H', 'Hard'),
                                               ('N', 'Dont know'),
                                               ('', 'Dont know'),
                                               ),
                                      default='')

    is_datapoint_18 = models.BooleanField("is Datapint18", null=True, blank=True)
    is_datapoint_19 = models.BooleanField("is Datapint19", null=True, blank=True)
    is_datapoint_20 = models.BooleanField("is Datapint20", null=True, blank=True)



    datapoint_21 = models.CharField(max_length=15,
                                      choices=(('1m', 'less than one month'),
                                               ('2-3m', '2 - 3 months'),
                                               ('3-6m', '3-6 months'),
                                               ('6-12m', '6-12 months'),
                                               ('1y', 'more than 1 year'),
                                               ('', ''),
                                               ),
                                      default='')

    datapoint_22 = models.CharField(max_length=15,
                                    choices=(('<5%', '<5% of weight'),
                                             ('>5%', '>5% of weight'),
                                             ('', ''),
                                             ),
                                    default='')

    is_datapoint_23 = models.BooleanField("is Datapint23", null=True, blank=True)

    datapoint_24 = models.TextField("Datapoint 24",
                                  max_length=2000,
                                  default='')

    datapoint_25 = models.TextField("Datapoint 25",
                                    max_length=2000,
                                    default='')

    is_datapoint_26 = models.BooleanField("is Datapint26", null=True, blank=True)

    datapoint_27 = models.CharField(max_length=35,
                                    choices=(('RLarpit', 'Right & left armpit'),
                                             ('Rarpit', 'Right armpit'),
                                             ('Larpit', 'Left armpit'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_28 = models.TextField("neck groin pos",
                                max_length=2000,
                                default='')

    datapoint_29 = models.TextField("Datapoint 29",
                                max_length=3500,
                                default='')

    is_datapoint_30 = models.BooleanField("is Datapint30", null=True, blank=True)

    datapoint_31 = models.CharField(max_length=15,
                              choices=(('pea', 'Pea'),
                                       ('peanut', 'Peanut'),
                                       ('grape', 'Grape'),
                                       ('walnut', 'Walnut'),
                                       ('lemon', 'Lemon'),
                                       ('egg', 'Egg'),
                                       ('peach', 'Peach'),
                                       ('grapefruit', 'Grapefruit'),
                                       ('','Null'),
                                       ),
                              default='')

    datapoint_32 = models.CharField(max_length=15,
                                    choices=(('S', 'Soft'),
                                             ('F', 'Firm'),
                                             ('H', 'Hard'),
                                             ('N', 'Dont know'),
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

    is_datapoint_39 = models.BooleanField("is Datapint39", null=True, blank=True)


    datapoint_40 = models.CharField(max_length=15,
                              choices=(('couplDay', 'Couple of days ago'),
                                       ('couplWeeks', 'Couple of weeks ago'),
                                       ('fevgWeeks', 'Few weeks ago'),
                                       ('couplMont', 'Couple of months ago'),
                                       ('fevMont', 'Few months ago'),
                                       ('Year', 'A year ago'),
                                       ('couplYear', 'Couple of years ago'),
                                       ('manyYear', 'Many years ago'),
                                       ('','Null'),
                                       ),
                              default='')


    datapoint_41 = models.CharField(max_length=15,
                              choices=(('slowGrow', 'slowing growing'),
                                       ('slowGrow', 'rapidly growing'),
                                       ('remainSize', 'remained same in size'),
                                       ('decrSize', 'decreased in size'),
                                       ('','Null'),
                                       ),
                              default='')

    is_datapoint_42 = models.BooleanField("is Datapint42", null=True, blank=True)

    datapoint_43 = models.TextField("Datapint43",
                                      max_length=2000,
                                      default='')

    datapoint_44 = models.TextField("Datapint44",
                                    max_length=2000,
                                    default='')

    datapoint_45 = models.TextField("Datapint45",
                                    max_length=2000,
                                    default='')

    is_datapoint_46 = models.BooleanField("is Datapint46", null=True, blank=True)

    is_datapoint_47 = models.BooleanField("is Datapint47", null=True, blank=True)

    is_datapoint_48 = models.BooleanField("is Datapint48", null=True, blank=True)

    is_datapoint_49 = models.BooleanField("is Datapint49", null=True, blank=True)

    is_datapoint_50 = models.BooleanField("is Datapint50", null=True, blank=True)

    datapoint_51 = models.CharField(max_length=15,
                                    choices=(('couplDay', 'Couple of days ago'),
                                             ('couplWeeks', 'Couple of weeks ago'),
                                             ('fevgWeeks', 'Few weeks ago'),
                                             ('couplMont', 'Couple of months ago'),
                                             ('fevMont', 'Few months ago'),
                                             ('Year', 'A year ago'),
                                             ('couplYear', 'Couple of years ago'),
                                             ('manyYear', 'Many years ago'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    datapoint_52 = models.CharField(max_length=15,
                                    choices=(('green', 'Green'),
                                             ('watery', 'Watery'),
                                             ('white', 'White'),
                                             ('bloodstained', 'Blood Stained'),
                                             ('brownish', 'Brownish'),
                                             ('serous', 'Serous'),
                                             ('pus', 'Pus'),
                                             ('yellow', 'Yellow'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_53 = models.CharField(max_length=15,
                                  choices=(('RL', 'Right & left'),
                                           ('R', 'Right'),
                                           ('L', 'Left'),
                                           ('', 'Null'),
                                           ),
                                  default='')

    datapoint_54 = models.CharField(max_length=15,
                                    choices=(('onespot', 'One spot'),
                                             ('manyspots', 'Many spots'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    is_datapoint_55 = models.BooleanField("is Datapint55", null=True, blank=True)

    is_datapoint_56 = models.BooleanField("is Datapint56", null=True, blank=True)
    is_datapoint_57 = models.BooleanField("is Datapint57", null=True, blank=True)
    is_datapoint_58 = models.BooleanField("is Datapint58", null=True, blank=True)
    is_datapoint_59 = models.BooleanField("is Datapint59", null=True, blank=True)

    is_datapoint_60 = models.BooleanField("is Datapint60", null=True, blank=True)

    is_datapoint_61 = models.BooleanField("is Datapint61", null=True, blank=True)


    datapoint_62 = models.TextField("Datapint62",
                                    max_length=2000,
                                    default='')

    is_datapoint_63 = models.BooleanField("is Datapint63", null=True, blank=True)

    is_datapoint_64 = models.BooleanField("is Datapint64", null=True, blank=True)

    datapoint_65 = models.CharField(max_length=15,
                                    choices=(('RL', 'Right & left'),
                                             ('R', 'Right'),
                                             ('L', 'Left'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    is_datapoint_66 = models.BooleanField("is Datapint66", null=True, blank=True)

    datapoint_67 = models.CharField(max_length=15,
                                    choices=(('1', 'Less than a quarter'),
                                             ('2', 'More than a quarter but less than half'),
                                             ('3', 'More than half of breast'),
                                             ('4', 'Whole breast'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    datapoint_68 = models.CharField(max_length=15,
                             choices=(('couplDay', 'Couple of days ago'),
                                      ('couplWeeks', 'Couple of weeks ago'),
                                      ('fevgWeeks', 'Few weeks ago'),
                                      ('couplMont', 'Couple of months ago'),
                                      ('fevMont', 'Few months ago'),
                                      ('Year', 'A year ago'),
                                      ('couplYear', 'Couple of years ago'),
                                      ('manyYear', 'Many years ago'),
                                      ('', 'Null'),
                                      ),
                             default='')

    is_datapoint_69 = models.BooleanField("is Datapint69", null=True, blank=True)
    is_datapoint_70 = models.BooleanField("is Datapint70", null=True, blank=True)
    is_datapoint_71 = models.BooleanField("is Datapint71", null=True, blank=True)

    datapoint_72 = models.CharField(max_length=15,
                                    choices=(('RL', 'Right & left'),
                                             ('R', 'Right'),
                                             ('L', 'Left'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    datapoint_73 = models.CharField(max_length=15,
                                    choices=(('couplDay', 'Couple of days ago'),
                                             ('couplWeeks', 'Couple of weeks ago'),
                                             ('fevgWeeks', 'Few weeks ago'),
                                             ('couplMont', 'Couple of months ago'),
                                             ('fevMont', 'Few months ago'),
                                             ('Year', 'A year ago'),
                                             ('couplYear', 'Couple of years ago'),
                                             ('manyYear', 'Many years ago'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    is_datapoint_74 = models.BooleanField("is Datapint74", null=True, blank=True)
    is_datapoint_75 = models.BooleanField("is Datapint75", null=True, blank=True)
    is_datapoint_76 = models.BooleanField("is Datapint76", null=True, blank=True)

    is_datapoint_77 = models.BooleanField("is Datapint77", null=True, blank=True)
    is_datapoint_78 = models.BooleanField("is Datapint78", null=True, blank=True)
    is_datapoint_79 = models.BooleanField("is Datapint79", null=True, blank=True)

    is_datapoint_80 = models.BooleanField("is Datapint80", null=True, blank=True)
    is_datapoint_81 = models.BooleanField("is Datapint81", null=True, blank=True)
    is_datapoint_82 = models.BooleanField("is Datapint82", null=True, blank=True)
    is_datapoint_83 = models.BooleanField("is Datapint83", null=True, blank=True)

    datapoint_84 = models.CharField(max_length=15,
                                    choices=(('RL', 'Right & left'),
                                             ('R', 'Right'),
                                             ('L', 'Left'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    datapoint_85 = models.CharField(max_length=15,
                                    choices=(('couplDay', 'Couple of days ago'),
                                             ('couplWeeks', 'Couple of weeks ago'),
                                             ('fevgWeeks', 'Few weeks ago'),
                                             ('couplMont', 'Couple of months ago'),
                                             ('fevMont', 'Few months ago'),
                                             ('Year', 'A year ago'),
                                             ('couplYear', 'Couple of years ago'),
                                             ('manyYear', 'Many years ago'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    datapoint_86 = models.CharField(max_length=15,
                                    choices=(('1', 'Rapidly progressing'),
                                             ('2', 'Slowly progressing'),
                                             ('3', 'No change'),
                                             ('4', 'Getting better'),
                                             ('', ''),
                                             ),
                                    default='')

    is_datapoint_87 = models.BooleanField("is Datapint87", null=True, blank=True)

    datapoint_88 = models.TextField("Datapint88",
                                    max_length=2000,
                                    default='')

    is_datapoint_89 = models.BooleanField("is Datapint89", null=True, blank=True)

    is_datapoint_90 = models.BooleanField("is Datapint90", null=True, blank=True)

    is_datapoint_91 = models.BooleanField("is Datapint91", null=True, blank=True)

    datapoint_92 = models.CharField(max_length=15,
                                    choices=(('couplDay', 'Couple of days ago'),
                                             ('couplWeeks', 'Couple of weeks ago'),
                                             ('fevgWeeks', 'Few weeks ago'),
                                             ('couplMont', 'Couple of months ago'),
                                             ('fevMont', 'Few months ago'),
                                             ('Year', 'A year ago'),
                                             ('couplYear', 'Couple of years ago'),
                                             ('manyYear', 'Many years ago'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    datapoint_93 = models.CharField(max_length=15,
                                    choices=(('1', 'Rapidly progressing'),
                                             ('2', 'Slowly progressing'),
                                             ('3', 'No change'),
                                             ('4', 'Getting better'),
                                             ('', ''),
                                             ),
                                    default='')

    datapoint_94 = models.CharField(max_length=15,
                                    choices=(('RL', 'Right & left'),
                                             ('R', 'Right'),
                                             ('L', 'Left'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    is_datapoint_95 = models.BooleanField("is Datapint95", null=True, blank=True)

    datapoint_96 = models.TextField("Datapint96",
                                    max_length=2000,
                                    default='')

    is_datapoint_97 = models.BooleanField("is Datapint97", null=True, blank=True)

    is_datapoint_98 = models.BooleanField("is Datapint98", null=True, blank=True)

    datapoint_99 = models.CharField(max_length=15,
                                    choices=(('RL', 'Right & left'),
                                             ('R', 'Right'),
                                             ('L', 'Left'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    datapoint_100 = models.CharField(max_length=45,
                                  choices=(('UpOutPir', 'Upper - outer peripheral'),
                                           ('UpInPir', 'Upper - inner peripheral'),
                                           ('LowInPir', 'Lower - inner peripheral'),
                                           ('LowOutPir', 'Lower - outer peripheral'),
                                           ('UpOutCntr', 'Upper - outer central'),
                                           ('UpInCntr', 'Upper - inner central'),
                                           ('LowInCntr', 'Lower - inner central'),
                                           ('LowOutCntr', 'Lower - outer central'),
                                           ('LowOutCntr', 'Areola'),
                                           ('LowOutCntr', 'Nipple'),
                                           ('', 'Null'),
                                           ),
                                  default='')

    datapoint_101 = models.CharField(max_length=45,
                                     choices=(('UpOutPir', 'Upper - outer peripheral'),
                                              ('UpInPir', 'Upper - inner peripheral'),
                                              ('LowInPir', 'Lower - inner peripheral'),
                                              ('LowOutPir', 'Lower - outer peripheral'),
                                              ('UpOutCntr', 'Upper - outer central'),
                                              ('UpInCntr', 'Upper - inner central'),
                                              ('LowInCntr', 'Lower - inner central'),
                                              ('LowOutCntr', 'Lower - outer central'),
                                              ('LowOutCntr', 'Areola'),
                                              ('LowOutCntr', 'Nipple'),
                                              ('', 'Null'),
                                              ),
                                     default='')

    datapoint_102 = models.CharField(max_length=15,
                                    choices=(('couplDay', 'Couple of days ago'),
                                             ('couplWeeks', 'Couple of weeks ago'),
                                             ('fevgWeeks', 'Few weeks ago'),
                                             ('couplMont', 'Couple of months ago'),
                                             ('fevMont', 'Few months ago'),
                                             ('Year', 'A year ago'),
                                             ('couplYear', 'Couple of years ago'),
                                             ('manyYear', 'Many years ago'),
                                             ('', 'Null'),
                                             ),
                                    default='')

    datapoint_103 = models.TextField("Datapint103",
                                    max_length=2000,
                                    default='')

    is_datapoint_104 = models.BooleanField("is Datapint104", null=True, blank=True)

    is_datapoint_105 = models.BooleanField("is Datapint105", null=True, blank=True)

    is_datapoint_106 = models.BooleanField("is Datapint106", null=True, blank=True)

    is_datapoint_107 = models.BooleanField("is Datapint107", null=True, blank=True)

    is_datapoint_108 = models.BooleanField("is Datapint108", null=True, blank=True)

    is_datapoint_109 = models.BooleanField("is Datapint109", null=True, blank=True)

    is_datapoint_110 = models.BooleanField("is Datapint110", null=True, blank=True)

    is_datapoint_111 = models.BooleanField("is Datapint111", null=True, blank=True)

    is_datapoint_112 = models.BooleanField("is Datapint112", null=True, blank=True)

    is_datapoint_113 = models.BooleanField("is Datapint113", null=True, blank=True)

    is_datapoint_114 = models.BooleanField("is Datapint114", null=True, blank=True)

    is_datapoint_115 = models.BooleanField("is Datapint115", null=True, blank=True)

    is_datapoint_116 = models.BooleanField("is Datapint116", null=True, blank=True)

    is_datapoint_117 = models.BooleanField("is Datapint117", null=True, blank=True)

    is_datapoint_118 = models.BooleanField("is Datapint118", null=True, blank=True)

    is_datapoint_119 = models.BooleanField("is Datapint119", null=True, blank=True)


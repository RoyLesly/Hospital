from django.db import models
from django.db import models

from apps.root.models import CommonStaff
from apps.regis.models import Patient
import datetime
from apps.account.models import Account

from django.db.models.signals import post_save


# ==================== USER FOR WARD ========================================================
class LabUser(models.Model):
    username = models.OneToOneField(Account, unique=True, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.username)


def create_labUser(sender, **kwargs):
    if kwargs['created']:
        print("here")
        created_obj = Account.objects.all().order_by('date_joined').last()
        print(created_obj)
        name = created_obj.username
        if name == 'Laboratory' or name == 'zane' or name == 'admin':
            labUser = LabUser.objects.create(username=created_obj)


post_save.connect(create_labUser, sender=Account)

# ______________________________________________________________________________________________________

# =============  Increment PH number, PH ms, PH ds  (pd = pharmacy dispensary) =======================
def auto_increment_pdn():
    now = datetime.date.today()
    # all_patients = Patient.objects.using('radio_db').all().filter(date_created__year=now.year,
    all_patients = WPatient.objects.all().filter(date_created__year=now.year,
                                                 date_created__month=now.month, ).order_by('un')
    if all_patients.exists():
        lp = all_patients.last()
        if lp.date_created.year == now.year:
            pat_int = int(lp.un[:5])
            new_pat_int = int(pat_int) + 1
            un = str(new_pat_int).zfill(5) + "/" + str(now.year)[2:4]
            return un
    else:
        un = '00001' + "/" + str(now.year)[2:4]
        return un


def auto_increment_pdms():
    now = datetime.date.today()
    # now.month, now.year
    # all_purpose = UPatient.objects.using('radio_db').all().filter(date_created__year=now.year,
    all_purpose = UExam.objects.all().filter(date_created__year=now.year,
                                             date_created__month=now.month, ).order_by("date_created")
    if all_purpose.exists():
        lp = all_purpose.last()
        lp_ms = lp.ms
        lp_date = lp.date_created
        lp_year = lp_date.year
        lp_month = lp_date.month

        if lp_year == now.year:
            if lp_month == now.month:
                new = int(lp_ms) + 1
                ms = str(new).zfill(4)
                return ms
            else:
                ms = '0001'
                return ms
        else:
            ms = '0001'
            return ms
    else:
        ms = '0001'
        return ms


def auto_increment_pdds():
    now = datetime.date.today()
    all_purpose = UExam.objects.all().filter(date_created__year=now.year,
                                             date_created__month=now.month,
                                             date_created__day=now.day).order_by("date_created")
    if all_purpose.exists():
        lp = all_purpose.last()
        if lp.date_created.year == now.year:
            if lp.date_created.month == now.month:
                if lp.date_created.day == now.day:
                    new = int(lp.ds) + 1
                    ds = str(new).zfill(2)
                    return ds
                else:
                    ds = '01'
                    return ds
            else:
                ds = '01'
                return ds
        else:
            ds = '01'
            return ds
    else:
        ds = '01'
        return ds


# -------------------------------------------------------------------------


# ==============  Increment Store number, store ms, store ds  (st = store) =====================
def auto_increment_stn():
    now = datetime.date.today()
    # all_patients = Patient.objects.using('radio_db').all().filter(date_created__year=now.year,
    all_patients = XPatient.objects.all().filter(date_created__year=now.year,
                                                 date_created__month=now.month, ).order_by('xn')
    if all_patients.exists():
        lp = all_patients.last()
        if lp.date_created.year == now.year:
            pat_int = int(lp.xn[:5])
            new_pat_int = int(pat_int) + 1
            xn = str(new_pat_int).zfill(5) + "/" + str(now.year)[2:4]
            return xn
    else:
        xn = '00001' + "/" + str(now.year)[2:4]
        return xn


def auto_increment_stms():
    now = datetime.date.today()
    all_purpose = XExam.objects.all().filter(date_created__year=now.year,
                                             date_created__month=now.month, ).order_by("date_created")
    if all_purpose.exists():
        lp = all_purpose.last()

        if lp.date_created.year == now.year:
            if lp.date_created.month == now.month:
                new = int(lp.ms) + 1
                ms = str(new).zfill(4)
                return ms
            else:
                ms = '0001'
                return ms
        else:
            ms = '0001'
            return ms
    else:
        ms = '0001'
        return ms


def auto_increment_stds():
    now = datetime.date.today()
    all_patients = XExam.objects.all().filter(date_created__year=now.year,
                                              date_created__month=now.month,
                                              date_created__day=now.day).order_by("date_created")
    if all_patients.exists():
        lp = all_patients.last()
        if lp.date_created.year == now.year:
            if lp.date_created.month == now.month:
                if lp.date_created.day == now.day:
                    new = int(lp.ds) + 1
                    ds = str(new).zfill(2)
                    return ds
                else:
                    ds = '01'
                    return ds
            else:
                ds = '01'
                return ds
        else:
            ds = '01'
            return ds
    else:
        ds = '01'
        return ds


# -------------------------------------------------------------------------------------

# ==============  Increment Drug Number =====================================
def auto_increment_ys():
    now = datetime.date.today()
    u_exams = UExam.objects.all().filter(date_created__year=now.year,).order_by('ys')
    if u_exams.exists():
        le =u_exams.last()
        if le.date_created.year == now.year:
            pat_int = int(le.ys[:5])
            new_pat_int = int(pat_int) + 1
            uys = str(new_pat_int).zfill(5) + "/" + str(now.year)[2:4]
            return uys
    else:
        uys = '00001' + "/" + str(now.year)[2:4]
        return uys

# _____________________________________________________________________________________

# ==============  Increment Exam number for X-ray Exams ==========================================
def auto_increment_sys():
    now = datetime.date.today()
    x_exams = XExam.objects.all().filter(date_created__year=now.year).order_by('ys')
    if x_exams.exists():
        le = x_exams.last()
        if le.date_created.year == now.year:
            pat_int = int(le.ys[:5])
            new_pat_int = int(pat_int) + 1
            xys = str(new_pat_int).zfill(5) + "/" + str(now.year)[2:4]
            return xys
    else:
        xys = '00001' + "/" + str(now.year)[2:4]
        return xys

# _____________________________________________________________________________________


# Create your models here.
PURPOSES = (('CONST', 'consultation'), ('RDV', 'rendez-vous'), ('VISIT', 'visit'), ('OTHER', 'other'))
US_EXAM_CHOICES = (('OB', 'OBSTETRICS'),
                   ('ABD/PEL', 'ABD / PEL'),
                   ('PELVIC', 'PELVIC'),
                   ('ABD', 'ABDOMINAL'),
                   ('BREAST', 'BREAST'),
                   ('other', 'OTHER'),
                   ('THYROID', 'THYROID'),
                   ('SCROTAL', 'SCROTAL'),)
WARD_CHOICES = (('OPD', 'OPD'),
                ('MAT', 'Maternity'),
                ('LW', 'Labour / Delivery'),
                ('MW', 'Medical Ward'),
                ('SW', 'Surgical Ward'),
                ('CW', "Childrens' Ward"),
                ('OTHER', 'Other'))
XR_EXAM_CHOICES = (('CXR', 'CXR'),
                   ('Abd XR', 'ABD XR'), ('Pelvis', 'Pelvic'), ('LSS', 'LSS'),
                   ('Skull', 'Skull'), ('Shoulder', 'Shoulder'),
                   ('Humerus', 'Humerus'), ('Fore-Arm', 'Fore-Arm'), ('Hand', 'Hand'), ('Wrist', 'Wrist'),
                   ('Femur', 'Femur'), ('Leg', 'Leg'), ('Foot', 'Foot'), ('Ankle', 'Ankle'),)
RAD_FEES_CHOICES = (('16000', '16000'), ('15000', '15000'), ('14000', '14000'), ('10000', '10000'), ('8000', '8000'),
                    ('7000', '7000'), ('6000', '6000'), ('5000', '5000'), ('3000', '3000'), ('9000', '9000'), ('5500', '5500'),
                    ('9500', '9500'), ('8500', '8500'), ('7500', '7500'), ('6500', '6500'))
DEPTS = (('Laboratory1', 'Laboratory_1'), ('Laboratory2', 'Laboratory_2'))


class LaboDept(models.Model):
    name = models.CharField(max_length=15, unique=True,
                            default='', choices=DEPTS)

    def __str__(self):
        return str(self.name.upper())


class LaboStaff(CommonStaff):
    TITLE_CHOICES = (('PATO', 'Pathologist'),
                    ('LAB Sc.', 'Lab. Scientist'),
                    ('LAB TECH', 'Lab. Technician'),
                    ('As.Tech', 'Assistant Technician'),
                    ('ASS', 'Assistant'),
                    ('OTHER', "Other"))
    title = models.CharField(max_length=15, unique=True,
                            default='', choices=TITLE_CHOICES)

    def __str__(self):
        return str(self.first_name.upper())

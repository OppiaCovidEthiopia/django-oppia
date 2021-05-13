import pytest

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management import call_command
from django.db import IntegrityError

from io import StringIO

from oppia.models import Tracker
from oppia.test import OppiaTestCase

from oppia.models import Award, CertificateTemplate


class GenerateCertificatesTest(OppiaTestCase):
    
    fixtures = ['tests/test_user.json',
                'tests/test_oppia.json',
                'default_gamification_events.json',
                'tests/test_tracker.json',
                'tests/test_permissions.json',
                'default_badges.json',
                'tests/test_course_permissions.json',
                'tests/awards/award-course.json',
                'tests/test_certificatetemplate.json']
    
    @pytest.mark.xfail(reason="works on local, but not on Github workflow")
    def test_create_certificate_new(self):
        
        current_award = Award.objects.all().first()
        self.assertTrue(current_award.certificate_pdf == "")
        
        call_command('generate_certificates', stdout=StringIO())
        
        current_award = Award.objects.all().first()
        self.assertFalse(current_award.certificate_pdf == "")
     
    @pytest.mark.xfail(reason="works on local, but not on Github workflow")   
    def test_create_certificate_all(self):
        
        current_award = Award.objects.all().first()
        self.assertTrue(current_award.certificate_pdf == "")
        
        call_command('generate_certificates', '--allcerts', stdout=StringIO())
        
        current_award = Award.objects.all().first()
        self.assertFalse(current_award.certificate_pdf == "")
        
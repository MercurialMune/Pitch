import unittest
from app.models import Pitch,User


class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username='James', password='potato', email='james@ms.com')
        self.new_pitch = Pitch(pitch_id=12345, pitch_title='Awesome Pitch', pitch_category="weird",pitch_prose='This pitch is the best thing since sliced bread', user=self.user_James)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_id, 12345)
        self.assertEquals(self.new_pitch.pitch_title, 'Awesome Pitch')
        self.assertEquals(self.new_pitch.pitch_category, "weird")
        self.assertEquals(self.new_pitch.pitch_prose, 'This pitch is the best thing since sliced bread')
        self.assertEquals(self.new_pitch.user, self.user_James)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitch(12345)
        self.assertTrue(len(got_pitches) == 1)
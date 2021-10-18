# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : test_patients.py
from app import App

class TestPatientService():

    def setup_class(self):
        self.app=App()

    def teardown_class(self):
        self.app.goto_public_patient().driver.quit()

    def test_xijing_hospital(self):
        self.app.goto_public_patient().xijing_hospital_patient()
        assert self.app.image_contrast("xijing_hospital_patient") > 0.95

    def test_dongguanfuyou_hospital(self):
        self.app.goto_public_patient().dongguanfuyou_hospital_patient()
        assert self.app.image_contrast("dongguanfuyou_hospital_patient") > 0.95

    def test_qingyuan_people_hospital(self):
        self.app.goto_public_patient().qingyuan_people_hospital_patient()
        assert self.app.image_contrast("qingyuan_people_hospital_patient") > 0.95

    def test_guangzhou_panyu_center_hospital(self):
        self.app.goto_public_patient().guangzhou_panyu_center_hospital_patient()
        assert self.app.image_contrast("guangzhou_panyu_center_hospital_patient") > 0.95

    def test_zhengzhou_university_first_hospital(self):
        self.app.goto_public_patient().zhengzhou_university_first_hospital_patient()
        assert self.app.image_contrast("zhengzhou_university_first_hospital_patient") > 0.95

    def test_hunan_zhongyiyao_university_first_hospital(self):
        self.app.goto_public_patient().hunan_zhongyiyao_university_first_hospital_patient()
        assert self.app.image_contrast("hunan_zhongyiyao_university_first_hospital_patient") > 0.95

    def test_beijing_third_hospital(self):
        self.app.goto_public_patient().beijing_third_hospital_patient()
        assert self.app.image_contrast("beijing_third_hospital_patient") > 0.95

    def test_foshan_gaoming_people_hospital(self):
        self.app.goto_public_patient().foshan_gaoming_people_hospital_patient()
        assert self.app.image_contrast("foshan_gaoming_people_hospital_patient") > 0.95

    def test_foshan_second_people_hospital(self):
        self.app.goto_public_patient().foshan_second_people_hospital_patient()
        assert self.app.image_contrast("foshan_second_people_hospital_patient") > 0.95

    def test_guangzhou_huadu_people_hospital(self):
        self.app.goto_public_patient().guangzhou_huadu_people_hospital_patient()
        assert self.app.image_contrast("guangzhou_huadu_people_hospital_patient") > 0.95


class TestExclusiveDocter():
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.goto_public_patient().driver.quit()

    def test_neimenggu_medical_university_hospital(self):
        self.app.goto_public_exclusive().neimenggu_medical_university_hospital_exclusive()
        assert self.app.image_contrast("neimenggu_medical_university_hospital_exclusive") > 0.95

    def test_nanfang_medical_university_hospital(self):
        self.app.goto_public_exclusive().nanfang_medical_university_hospital_exclusive()
        assert self.app.image_contrast("nanfang_medical_university_hospital_exclusive") > 0.95

    def test_deyang_people_hospital(self):
        self.app.goto_public_exclusive().deyang_people_hospital_exclusive()
        assert self.app.image_contrast("deyang_people_hospital_exclusive") > 0.95

    def testxian_gaoxin_hospital(self):
        self.app.goto_public_exclusive().xian_gaoxin_hospital_exclusive()
        assert self.app.image_contrast("xian_gaoxin_hospital_exclusive") > 0.95

    def test_wenzhou_central_hospital(self):
        self.app.goto_public_exclusive().wenzhou_central_hospital_exclusive()
        assert self.app.image_contrast("wenzhou_central_hospital_exclusive") > 0.95

    def test_Chifeng_institute_hospital(self):
        self.app.goto_public_exclusive().Chifeng_institute_hospital_exclusive()
        assert self.app.image_contrast("Chifeng_institute_hospital_exclusive") > 0.95

    def test_wenzhou_medical_university_shiguang_hospital(self):
        self.app.goto_public_exclusive().wenzhou_medical_university_shiguang_hospital_exclusive()
        assert self.app.image_contrast("wenzhou_medical_university_shiguang_hospital_exclusive") > 0.95

    def test_guangzhou_panyu_center_hospital(self):
        self.app.goto_public_exclusive().guangzhou_panyu_center_hospital_exclusive()
        assert self.app.image_contrast("guangzhou_panyu_center_hospital_exclusive") > 0.95

    def test_zigong_first_people_hospital(self):
        self.app.goto_public_exclusive().zigong_first_people_hospital_exclusive()
        assert self.app.image_contrast("zigong_first_people_hospital_exclusive") > 0.95

    def test_nanfang_keji_university_hospital(self):
        self.app.goto_public_exclusive().nanfang_keji_university_hospital_exclusive()
        assert self.app.image_contrast("nanfang_keji_university_hospital_exclusive") > 0.95

    def test_tangdu_hospital(self):
        self.app.goto_public_exclusive().tangdu_hospital_exclusive()
        assert self.app.image_contrast("tangdu_hospital_exclusive") > 0.95

    def test_xijing_hospital(self):
        self.app.goto_public_exclusive().xijing_hospital_exclusive()
        assert self.app.image_contrast("xijing_hospital_exclusive") > 0.95

    def test_liaoning_zhongyiyao_university_hospital(self):
        self.app.goto_public_exclusive().liaoning_zhongyiyao_university_hospital_exclusive()
        assert self.app.image_contrast("liaoning_zhongyiyao_university_hospital_exclusive") > 0.95

    def test_nanjing_oral_hospital(self):
        self.app.goto_public_exclusive().nanjing_oral_hospital_exclusive()
        assert self.app.image_contrast("nanjing_oral_hospital_exclusive") > 0.95

    def test_liuyang_people_hospital(self):
        self.app.goto_public_exclusive().liuyang_people_hospital_exclusive()
        assert self.app.image_contrast("liuyang_people_hospital_exclusive") > 0.95
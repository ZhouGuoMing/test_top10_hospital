# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : patients.py
from  base_page import Base_Page

class Patient_Service(Base_Page):

    def xijing_hospital_patient(self):
        self.parse_action("patient_service.yaml", "xijing_hospital_patient")


    def dongguanfuyou_hospital_patient(self):
        self.parse_action("patient_service.yaml", "dongguanfuyou_hospital_patient")


    def qingyuan_people_hospital_patient(self):
        self.parse_action("patient_service.yaml", "qingyuan_people_hospital_patient")


    def guangzhou_panyu_center_hospital_patient(self):
        self.parse_action("patient_service.yaml", "guangzhou_panyu_center_hospital_patient")


    def zhengzhou_university_first_hospital_patient(self):
        self.parse_action("patient_service.yaml", "zhengzhou_university_first_hospital_patient")


    def hunan_zhongyiyao_university_first_hospital_patient(self):
        self.parse_action("patient_service.yaml", "hunan_zhongyiyao_university_first_hospital_patient")


    def beijing_third_hospital_patient(self):
        self.parse_action("patient_service.yaml", "beijing_third_hospital_patient")


    def foshan_gaoming_people_hospital_patient(self):
        self.parse_action("patient_service.yaml", "foshan_gaoming_people_hospital_patient")


    def foshan_second_people_hospital_patient(self):
        self.parse_action("patient_service.yaml", "foshan_second_people_hospital_patient")


    def guangzhou_huadu_people_hospital_patient(self):
        self.parse_action("patient_service.yaml", "guangzhou_huadu_people_hospital_patient")

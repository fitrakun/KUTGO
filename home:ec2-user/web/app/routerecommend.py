# -*- coding: utf-8 -*-

import csv
import math
import io
import re
from operator import itemgetter


class RouteRecommend:

    def __init__(self):
        self.keyword = ''
        self.chosenKeyword = []
        self.akey = ''
        self.Awing_key = []
        self.bkey = ''
        self.B_Cwing_key = []
        self.kkey = ''
        self.K_key = []
        self.centkey = ''
        self.CentralBuilding = []
        self.caffe = ''
        self.Caffe = []
        self.audito = ''
        self.Auditorium = []
        self.Awing_count=0
        self.B_Cwing_count=0
        self.K_count=0
        self.CentralBuilding_count=0
        self.Caffe_count=0
        self.Auditorium_count=0
        self.KeyWeight = []
        self.name_array1=[]
        self.name_array2=[]
        self.f = ''
        self.writer = ''
        self.temp = ''
    def main_route(self):
        self.keyword = io.open("/home/ec2-user/web/app/keyword.txt", "r", encoding="utf8")

        self.chosenKeyword = self.keyword.readlines()
        for i in range(len(self.chosenKeyword)):
            self.chosenKeyword[i] = self.chosenKeyword[i].strip()

        self.akey = io.open("/home/ec2-user/web/app/awing.txt", "r", encoding="utf8")
        self.Awing_key = self.akey.readlines()
        for j in range(len(self.Awing_key)):
            self.Awing_key[i] = self.Awing_key[i].strip()

        self.bkey = io.open("/home/ec2-user/web/app/bwing.txt", "r", encoding="utf8")
        self.B_Cwing_key = self.bkey.readlines()
        for b in range(len(self.B_Cwing_key)):
            self.B_Cwing_key[b] = self.B_Cwing_key[b].strip()

        self.kkey = io.open("/home/ec2-user/web/app/kkey.txt", "r", encoding="utf8")
        self.K_key = self.kkey.readlines()
        for k in range(len(self.K_key)):
            self.K_key[k] = self.K_key[k].strip()

        self.centkey = io.open("/home/ec2-user/web/app/CentralBuilding.txt", "r", encoding="utf8")
        self.CentralBuilding = self.centkey.readlines()
        for c in range(len(self.CentralBuilding)):
            self.CentralBuilding[c] = self.CentralBuilding[c].strip()

        self.caffe = io.open("/home/ec2-user/web/app/Caffe.txt", "r", encoding="utf8")
        self.Caffe = self.caffe.readlines()
        for ca in range(len(self.Caffe)):
            self.Caffe[ca] = self.Caffe[ca].strip()

        self.audito = io.open("/home/ec2-user/web/app/Auditorium.txt", "r", encoding="utf8")
        self.Auditorium = self.audito.readlines()
        for au in range(len(self.Auditorium)):
            self.Auditorium[au] = self.Auditorium[au].strip()

        for element in self.chosenKeyword:
            if element in self.Awing_key:
                self.Awing_count+=1
            elif element in self.B_Cwing_key:
                self.B_Cwing_count+=1
            elif element in self.CentralBuilding:
                self.CentralBuilding_count+=1
            elif element in self.Caffe:
                self.Caffe_count+=1
            elif element in self.Auditorium:
                self.Auditorium_count+=1
            elif element in self.K_key:
                self.K_count+=1
        self.KeyWeight=[[self.Awing_count,'Awing'], [self.B_Cwing_count, 'B_Cwing'], [self.K_count, 'K'], [self.CentralBuilding_count, 'CentralBuilding'], [self.Caffe_count, 'Caffe'], [self.Auditorium_count, 'Auditorium']]
        self.KeyWeight.reverse()
        self.KeyWeight.sort(key=itemgetter(0))
        self.KeyWeight.reverse()
        self.name_array1=[]
        self.name_array2=[]
        for k in self.KeyWeight:
            self.name_array1.append(k)
    
        for j in self.name_array1:
            self.temp = re.sub(r'[^\w]', '', j[1])
            self.name_array2.append(self.temp)
        self.f = open('/home/ec2-user/web/app/route.csv', 'w')
        self.writer = csv.writer(self.f, lineterminator='\n')
        self.writer.writerow(self.name_array2)
        self.f.close()
        return self.name_array2

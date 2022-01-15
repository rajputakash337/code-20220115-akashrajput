from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response


class CalcViewSet(viewsets.ViewSet):

    def set_data(self, request):
        data = {'users_data': request.data, 'overweight_people_count': 0}

        for i, user_data in enumerate(data['users_data']):

            bmi_cat_health_risk = self.calc_bmi_category_health_risk(
                user_data['WeightKg'], user_data['HeightCm'] / 100)  # divide by hundred to convert cm to m
            user_data.update(bmi_cat_health_risk)

            data['users_data'][i] = user_data

            if bmi_cat_health_risk['BMICategory'] is 'Overweight':
                data['overweight_people_count'] = data['overweight_people_count'] + 1

        return Response(data, status=status.HTTP_202_ACCEPTED)

    @staticmethod
    def calc_bmi_category_health_risk(mass, height):  # mass in KG, height in meter

        bmi = round(mass / (height ** 2), 2)
        bmi_cat_health_risk = {'BMI': bmi}
        if bmi <= 18.4:
            bmi_cat_health_risk['BMICategory'] = "Underweight"
            bmi_cat_health_risk['HealthRisk'] = "Malnutrition risk"

        elif 18.5 <= bmi <= 24.9:
            bmi_cat_health_risk['BMICategory'] = "Normal weight"
            bmi_cat_health_risk['HealthRisk'] = "Low risk"

        elif 25 <= bmi <= 29.9:
            bmi_cat_health_risk['BMICategory'] = "Overweight"
            bmi_cat_health_risk['HealthRisk'] = "Enhanced risk"

        elif 30 <= bmi <= 34.9:
            bmi_cat_health_risk['BMICategory'] = "Moderately obese"
            bmi_cat_health_risk['HealthRisk'] = "Medium risk"

        elif 35 <= bmi <= 39.9:
            bmi_cat_health_risk['BMICategory'] = "Severely obese"
            bmi_cat_health_risk['HealthRisk'] = "High risk"

        elif bmi >= 40:
            bmi_cat_health_risk['BMICategory'] = "Very severely obese"
            bmi_cat_health_risk['HealthRisk'] = "Very high risk"

        return bmi_cat_health_risk

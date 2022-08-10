import datetime
import time
from django.contrib import admin
import csv
import io
import pandas as pd
# Register your models here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.urls import path, reverse
from .models import PoliceCalls, Customer
from django import forms


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class PoliceCallsAdmin(admin.ModelAdmin):
    list_display = ('crime_id', 'original_crime_type_name')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            # print(dataframe)
            start_time = time.time()

            csv_file = request.FILES["csv_upload"]
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            i = 0
            for field in csv_data:
                if i == 0:
                    i += 1
                else:
                    row = field.split(",")
                    if len(row) == 14 or 15:
                        try:
                            created = PoliceCalls.objects.update_or_create(
                                crime_id=row[0],
                                original_crime_type_name=row[1],
                                report_date=row[2],
                                call_date=row[3],
                                offense_date=row[4],
                                call_time=row[5],
                                call_date_time=row[6],
                                disposition=row[7],
                                address=row[8],
                                city=row[9],
                                state=row[10],
                                agency_id=row[11],
                                address_type=row[12],
                                common_location=row[13],
                            )
                        except:
                            pass
            url = reverse('admin:index')
            with open('importing_log.log', 'a+', encoding='utf-8') as file:
                file.write(
                    f'{datetime.datetime.now()} загружено {len(csv_data)} записей | {time.time() - start_time} sec\n')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}

        return render(request, "admin/csv_upload.html", data)


admin.site.register(PoliceCalls, PoliceCallsAdmin)

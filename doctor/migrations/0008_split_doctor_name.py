from django.db import migrations


def split_doctor_names(apps, schema_editor):
    Doctor = apps.get_model('doctor', 'Doctor')
    for doctor in Doctor.objects.all():
        parts = (doctor.name or '').strip().split()
        doctor.first_name = parts[0] if parts else ''
        doctor.last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
        doctor.save()


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_doctor_first_name_doctor_last_name_alter_doctor_name'),
    ]

    operations = [
        migrations.RunPython(split_doctor_names, migrations.RunPython.noop),
    ]

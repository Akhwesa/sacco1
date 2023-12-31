# Generated by Django 4.1.5 on 2023-06-21 08:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claimed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountReference', models.CharField(max_length=50)),
                ('paidAmount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('paymentDate', models.DateField()),
                ('transactionId', models.CharField(max_length=150, unique=True)),
                ('phoneNumber', models.IntegerField()),
                ('fullName', models.CharField(max_length=150)),
                ('invoiceName', models.CharField(max_length=150)),
                ('externalReference', models.CharField(max_length=150)),
                ('status', models.CharField(default='Unclaimed', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountReference', models.CharField(max_length=50)),
                ('paidAmount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('paymentDate', models.DateField()),
                ('transactionId', models.CharField(max_length=150, unique=True)),
                ('phoneNumber', models.IntegerField()),
                ('fullName', models.CharField(max_length=150)),
                ('invoiceName', models.CharField(max_length=150)),
                ('externalReference', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ScannedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='scanned_files/')),
            ],
        ),
        migrations.CreateModel(
            name='shares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharesAmount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('contributor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.member')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanProduct', models.CharField(choices=[('Business Loan', 'Business Loan'), ('Personal Loan', 'Personal Loan'), ('General Loan', 'General Loan'), ('Student Loan', 'Student Loan'), ('Pensioner Loan', 'Pensioner Loan')], max_length=250)),
                ('loanNo', models.IntegerField(blank=True, null=True, unique=True)),
                ('disbursedby', models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Mpesa', 'Mpesa'), ('online Transfer', 'online Transfer')], max_length=150)),
                ('principal', models.IntegerField()),
                ('release_date', models.DateField()),
                ('interestRate', models.CharField(choices=[('Flat Rate', 'Flat Rate'), ('Reducing Balance - Equal Principal', 'Reducing Balance - Equal Principal')], max_length=150)),
                ('loanInterest', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('loanDuration', models.IntegerField()),
                ('durationPer', models.CharField(choices=[('Day', 'Day'), ('month', 'month'), ('week', 'week'), ('year', 'year')], default='year', max_length=50)),
                ('repayment_cycle', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], default='monthly', max_length=10)),
                ('processingFee', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('desc', models.TextField(null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Processing', 'Processing'), ('Defaulted', 'Defaulted'), ('Denied', 'Denied'), ('Write Off', 'Write Off'), ('Debt Review', 'Debt Review'), ('Not Taken Up', 'Not Taken Up')], default='Open', max_length=20)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.member')),
                ('loanFiles', models.ManyToManyField(blank=True, null=True, to='dashboard.scannedfile')),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributionAmount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('insuaranceAmount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('savingAmount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('contributor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.member')),
            ],
        ),
    ]

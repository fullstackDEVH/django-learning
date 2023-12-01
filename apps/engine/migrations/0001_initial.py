# Generated by Django 4.2.7 on 2023-11-29 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PUBLISHED', 'PUBLISHED'), ('FINISHED', 'FINISHED')], default='PUBLISHED', max_length=32)),
                ('contract_term', models.PositiveIntegerField()),
                ('desc', models.TextField()),
                ('max_out', models.PositiveIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('asset', models.CharField(max_length=256)),
                ('period', models.PositiveIntegerField()),
                ('profit_rate', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_role', models.CharField(choices=[('ADMIN', 'ADMIN'), ('SUPER_ADMIN', 'SUPER_ADMIN'), ('USER', 'USER')], default='USER', max_length=32)),
                ('username', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('hashed_password', models.CharField(max_length=256)),
                ('fullname', models.CharField(max_length=256)),
                ('phone_number', models.CharField(max_length=16)),
                ('birthday', models.DateField()),
                ('avatar', models.ImageField(upload_to='User')),
                ('is_active', models.BooleanField(default=False)),
                ('settings', models.JSONField()),
                ('verify_code', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserStaking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_period', models.PositiveIntegerField()),
                ('total_reward', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('STAKED', 'STAKED'), ('DONE', 'DONE')], default='STAKED', max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('staking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.staking')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED'), ('FAILED', 'FAILED')], default='PENDING', max_length=32)),
                ('from_address', models.CharField(max_length=256)),
                ('to_address', models.CharField(max_length=256)),
                ('tx_hash', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.user')),
            ],
        ),
        migrations.AddField(
            model_name='staking',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.user'),
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_staking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.userstaking')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.user')),
            ],
        ),
        migrations.CreateModel(
            name='FinacialTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED'), ('FAILED', 'FAILED')], default='PENDING', max_length=32)),
                ('type_transaction', models.CharField(choices=[('DEPOSIT', 'DEPOSIT'), ('WITHDRAW', 'WITHDRAW')], max_length=32)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('tx_hash', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.user')),
            ],
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.user')),
            ],
        ),
    ]
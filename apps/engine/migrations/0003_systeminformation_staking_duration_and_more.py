# Generated by Django 4.0 on 2023-12-08 18:25

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_remove_user_hashed_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemInformation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('statistical', models.JSONField()),
                ('tier', models.JSONField(default={'config': [{'names': 'TIER 1', 'price': '0.1 USDT', 'supply': 3500000}, {'names': 'TIER 2', 'price': '0.2 USDT', 'supply': 1000000}, {'names': 'TIER 3', 'price': '0.3 USDT', 'supply': 500000}, {'names': 'TIER 4', 'price': '0.4 USDT', 'supply': 0}, {'names': 'TIER 5', 'price': '0.5 USDT', 'supply': 0}, {'names': 'TIER 6', 'price': '0.6 USDT', 'supply': 0}, {'names': 'TIER 7', 'price': '0.7 USDT', 'supply': 0}, {'names': 'TIER 8', 'price': '0.9 USDT', 'supply': 0}], 'default': 0})),
                ('settings', models.JSONField(default={'coin_name': 'VBL', 'deposit': {'coin_deposit_name': 'USDT', 'email_admin_notif_deposit': 'order@velociti.vip', 'min_deposit': '100.0000'}, 'information': {'about_us': '', 'contact_support': 'For any questions, please contact cs@velociti.vip', 'term_of_services': ''}, 'reward': {'binary_reward_percent': '5%', 'refferal_commission_count': '2', 'refferal_reward_percent': '7%'}, 'supply': {'allocate_supply': '5000000', 'lock_supply': '245000000'}, 'swap': {'min_swap_USDT': '50', 'min_swap_token': '50'}, 'transfer': {'min_transfer': '100.0000', 'transfer_USDT_admin_fee': '0', 'transfer_page': 'Open'}, 'withdraw': {'admin_fee_withDraw_percent': '3%', 'dividen_withdraw_USDT_percent': '100%', 'dividen_withdraw_token_percent': '0%', 'email_admin_notif_withdraw': 'order@velociti.vip', 'min_withdraw_USDT': '100.0000'}})),
                ('system_wallets', models.JSONField(default={'BEP20': '0xD6ac90aD39f9DE416977757F252FdfC700D2d93a', 'ERC20': '0xA2c477F593e89d7302cBFadDF4703C0BCCdaa621', 'TRC20': 'TQ29CzvdjA9J9eo9ewtYu3CocgzAXSMoFj'})),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='staking',
            name='duration',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userstaking',
            name='reset_period',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='financialtransactions',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='staking',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='staking',
            name='period',
            field=models.PositiveIntegerField(default=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='system_role',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')], default='USER', max_length=32),
        ),
    ]

class SettingSystem:
    system_wallet = {
        "TRC20": "TQ29CzvdjA9J9eo9ewtYu3CocgzAXSMoFj",
        "BEP20": "0xD6ac90aD39f9DE416977757F252FdfC700D2d93a",
        "ERC20": "0xA2c477F593e89d7302cBFadDF4703C0BCCdaa621",
    }

    tiers = {
        "default": 0,
        "config": [
            {
                "names": "TIER 1",
                "price": "0.1 USDT",
                "supply": 3500000,
            },
            {
                "names": "TIER 2",
                "price": "0.2 USDT",
                "supply": 1000000,
            },
            {
                "names": "TIER 3",
                "price": "0.3 USDT",
                "supply": 500000,
            },
            {
                "names": "TIER 4",
                "price": "0.4 USDT",
                "supply": 0,
            },
            {
                "names": "TIER 5",
                "price": "0.5 USDT",
                "supply": 0,
            },
            {
                "names": "TIER 6",
                "price": "0.6 USDT",
                "supply": 0,
            },
            {
                "names": "TIER 7",
                "price": "0.7 USDT",
                "supply": 0,
            },
            {
                "names": "TIER 8",
                "price": "0.9 USDT",
                "supply": 0,
            },
        ],
    }

    settings = {
        "coin_name": "VBL",
        "deposit": {
            "coin_deposit_name": "USDT",
            "min_deposit": "100.0000",
            "email_admin_notif_deposit": "order@velociti.vip",
        },
        "swap": {
            "min_swap_USDT": "50", 
            "min_swap_token": "50"
        },
        "withdraw": {
            "min_withdraw_USDT" : "100.0000",
            "dividen_withdraw_USDT_percent" : "100%",
            "dividen_withdraw_token_percent" : "0%",
            "email_admin_notif_withdraw": "order@velociti.vip",
            "admin_fee_withDraw_percent": "3%",
        },
        "supply": {
            "lock_supply": "245000000", 
            "allocate_supply": "5000000"
        },
        "reward": {
            "refferal_reward_percent": "7%",
            "refferal_commission_count": "2",
            "binary_reward_percent": "5%",
        },
        "transfer": {
            "min_transfer": "100.0000",
            "transfer_USDT_admin_fee": "0",
            "transfer_page": "Open",
        },
        "information": {
            "contact_support": "For any questions, please contact cs@velociti.vip",
            "about_us": "",
            "term_of_services": "",
        },
    }

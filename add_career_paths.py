#!/usr/bin/env python3
"""
Скрипт для добавления карьерных путей к профессиям
"""

career_paths = {
    "Data Engineer": [
        "Junior Data Engineer (1-2 года)",
        "Data Engineer (2-4 года)",
        "Senior Data Engineer (4-6 лет)",
        "Lead Data Engineer / Principal DE (6-8 лет)",
        "Head of Data Engineering / VP Engineering (8+ лет)"
    ],
    "ML Engineer": [
        "Junior ML Engineer (1-2 года)",
        "ML Engineer (2-4 года)",
        "Senior ML Engineer (4-6 лет)",
        "Lead ML Engineer / Principal MLE (6-8 лет)",
        "Head of ML / VP of AI (8+ лет)"
    ],
    "DevOps инженер": [
        "Junior DevOps Engineer (1-2 года)",
        "DevOps Engineer (2-4 года)",
        "Senior DevOps Engineer (4-6 лет)",
        "Lead DevOps / Platform Engineer (6-8 лет)",
        "Head of Infrastructure / VP Engineering (8+ лет)"
    ],
    "QA Engineer": [
        "Junior QA Engineer (1-2 года)",
        "QA Engineer (2-3 года)",
        "Senior QA Engineer (3-5 лет)",
        "Lead QA / QA Manager (5-7 лет)",
        "Head of QA / Director of Quality (7+ лет)"
    ],
    "UI/UX дизайнер": [
        "Junior UI/UX Designer (1-2 года)",
        "UI/UX Designer (2-4 года)",
        "Senior UI/UX Designer (4-6 лет)",
        "Lead Designer / Design Manager (6-8 лет)",
        "Head of Design / Design Director (8+ лет)"
    ],
    "Product Manager": [
        "Associate Product Manager (1-2 года)",
        "Product Manager (2-4 года)",
        "Senior Product Manager (4-6 лет)",
        "Lead PM / Group PM (6-8 лет)",
        "VP of Product / CPO (8+ лет)"
    ],
    "Scrum Master": [
        "Junior Scrum Master (1-2 года)",
        "Scrum Master (2-4 года)",
        "Senior Scrum Master (4-6 лет)",
        "Agile Coach / Lead SM (6-8 лет)",
        "Head of Agile / Transformation Lead (8+ лет)"
    ],
    "Системный администратор": [
        "Junior System Administrator (1-2 года)",
        "System Administrator (2-4 года)",
        "Senior System Administrator (4-6 лет)",
        "Lead SysAdmin / Infrastructure Manager (6-8 лет)",
        "Head of IT Operations / IT Director (8+ лет)"
    ],
    "Специалист по информационной безопасности": [
        "Junior Security Specialist (1-2 года)",
        "Information Security Specialist (2-4 года)",
        "Senior Security Specialist (4-6 лет)",
        "Lead Security Engineer / Security Manager (6-8 лет)",
        "CISO / Head of Security (8+ лет)"
    ],
    "Security Analyst": [
        "Junior Security Analyst (1-2 года)",
        "Security Analyst (2-3 года)",
        "Senior Security Analyst (3-5 лет)",
        "Lead Security Analyst / SOC Manager (5-7 лет)",
        "Head of Security Operations (7+ лет)"
    ],
    "Cloud архитектор": [
        "Junior Cloud Engineer (1-2 года)",
        "Cloud Engineer (2-4 года)",
        "Senior Cloud Engineer (4-6 лет)",
        "Cloud Architect / Principal Engineer (6-8 лет)",
        "Head of Cloud / VP Infrastructure (8+ лет)"
    ],
    "SRE (Site Reliability Engineer)": [
        "Junior SRE (1-2 года)",
        "SRE (2-4 года)",
        "Senior SRE (4-6 лет)",
        "Principal SRE / SRE Manager (6-8 лет)",
        "Head of Reliability / VP Engineering (8+ лет)"
    ],
    "UX Analyst": [
        "Junior UX Analyst (1-2 года)",
        "UX Analyst (2-3 года)",
        "Senior UX Analyst (3-5 лет)",
        "Lead UX Analyst / UX Manager (5-7 лет)",
        "Head of UX Research (7+ лет)"
    ],
    "Computer Vision инженер": [
        "Junior CV Engineer (1-2 года)",
        "Computer Vision Engineer (2-4 года)",
        "Senior CV Engineer (4-6 лет)",
        "Lead CV Engineer / Principal (6-8 лет)",
        "Head of Computer Vision (8+ лет)"
    ],
    "NLP специалист": [
        "Junior NLP Engineer (1-2 года)",
        "NLP Engineer (2-4 года)",
        "Senior NLP Engineer (4-6 лет)",
        "Lead NLP Engineer / Principal (6-8 лет)",
        "Head of NLP / AI Research (8+ лет)"
    ],
    "Embedded разработчик": [
        "Junior Embedded Developer (1-2 года)",
        "Embedded Developer (2-4 года)",
        "Senior Embedded Developer (4-6 лет)",
        "Lead Embedded Engineer (6-8 лет)",
        "Principal Engineer / Hardware Manager (8+ лет)"
    ],
    "Network Engineer (Cisco/VPN)": [
        "Junior Network Engineer (1-2 года)",
        "Network Engineer (2-4 года)",
        "Senior Network Engineer (4-6 лет)",
        "Lead Network Engineer / Manager (6-8 лет)",
        "Network Architect / Director (8+ лет)"
    ],
    "Selenium тестировщик": [
        "Junior Test Automation Engineer (1-2 года)",
        "Test Automation Engineer (2-3 года)",
        "Senior Test Automation Engineer (3-5 лет)",
        "Lead Automation Engineer (5-7 лет)",
        "Head of Test Automation (7+ лет)"
    ],
    "Apache JMeter специалист": [
        "Junior Performance Tester (1-2 года)",
        "Performance Test Engineer (2-3 года)",
        "Senior Performance Engineer (3-5 лет)",
        "Lead Performance Engineer (5-7 лет)",
        "Head of Performance Testing (7+ лет)"
    ],
    "Firmware разработчик": [
        "Junior Firmware Developer (1-2 года)",
        "Firmware Developer (2-4 года)",
        "Senior Firmware Developer (4-6 лет)",
        "Lead Firmware Engineer (6-8 лет)",
        "Principal Engineer / Manager (8+ лет)"
    ],
    "OT специалист": [
        "Junior OT Specialist (1-2 года)",
        "OT Specialist (2-4 года)",
        "Senior OT Specialist (4-6 лет)",
        "Lead OT Engineer / Manager (6-8 лет)",
        "Head of OT / Industrial IT (8+ лет)"
    ]
}

print("Карьерные пути для добавления в профессии:")
for profession, path in career_paths.items():
    print(f"\n{profession}:")
    for step in path:
        print(f"  - {step}")
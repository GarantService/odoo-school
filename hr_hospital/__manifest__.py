{
    'name': 'hr_hospital',
    'summary': 'Module description',  # Короткий опис для чого цей модуль

    'author': 'GarantService/',
    'website': 'https://gs.com.ua',

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': [
        'base',  # Якщо модуль, не має прямих залежностей, він повінен мати залежність від базового модуля "base".
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menus.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_doctor_views.xml',
        'views/patient_card_views.xml',
        'views/doctor_diagnose_views.xml',
    ],
    'demo': [
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',

}
